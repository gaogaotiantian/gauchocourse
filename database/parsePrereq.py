import json
import re

courseData = []
deptName = []
deptNamePattern = r""
class RuleParser:
    def __init__(self):
        self.keyWdList = []
        self.keyWdPat = [
            ["NUM", r"\b[0-9]+?[A-Z]*\b", 0],
            ["DEPT", deptNamePattern, 0],
            ["OR", r"\bor\b|,", 0],
            ["AND", r"\band\b", re.I],
            ["CONCUR", r"\bconcur", re.I],
            ["MUST", r"\bmust\b", re.I]
        ]
    def GenCourseInfo(self):
        courseList = []
        curDept = None
        curNum  = None
        curAdded = True
        concur = False
        must = False
        concurData = "n"
        singleCourse = []
        for keyWd in self.keyWdList:
            if keyWd[1] == "DEPT":
                curDept = keyWd[2]
            elif keyWd[1] == "NUM" and curDept != None:
                curNum = keyWd[2]
                curAdded = False
            elif keyWd[1] == "OR" and curDept != None and curNum != None:
                if curAdded == False:
                    singleCourse.append([curDept, curNum])
                    curAdded = True
            elif keyWd[1] == "AND" and curDept != None and curNum != None:
                if curAdded == False:
                    singleCourse.append([curDept, curNum])  
                if singleCourse != []:
                    courseList.append(singleCourse)
                    singleCourse = []
            elif keyWd[1] == "CONCUR":
                concur = True
            elif keyWd[1] == "MUST":
                must = True
        # After iterating keyword, we may need to append the last one
        # to courseList
        if concur:
            if must:
                concurData = 'm'
            else:
                concurData = 'y'

        if curAdded == False:
            singleCourse.append([curDept, curNum])   
        if singleCourse != []:
            courseList.append(singleCourse)
        for singleCourse in courseList:
            for req in singleCourse:
                req.append(concurData)
        return courseList

    def ParseStr(self, ruleStr):
        for pat in self.keyWdPat:
            keyWdIter = re.finditer(pat[1], ruleStr, pat[2])
            for m in keyWdIter:
                self.keyWdList.append([m.start(), pat[0], m.group(0)])
        self.keyWdList.sort(key = lambda wdList:wdList[0])
        courseList = self.GenCourseInfo()
        return courseList 

def NormPrereq(prereq):
    ret = prereq
    for dept in deptName:
        if dept[0] in ret:
            ret = ret.replace(dept[0], dept[1])
    return ret
def ParseRuleList(ruleList):
    ret = []
    for rule in ruleList:
        parser = RuleParser()
        parsedRule = parser.ParseStr(rule)
        if len(parsedRule) > 0:
            for r in parsedRule:
                ret.append(r)
    return ret
        
def ParsePrereqStr(prereq):
    afterNormPrereq = NormPrereq(prereq)
    delimiters = r"\.|;"
    ruleList = re.split(delimiters, afterNormPrereq)
    return ParseRuleList(ruleList)

def GetID(sub, num):
    idList = []
    for course in courseData:
        if course["sub"] == sub and course["number"] == num:
            idList.append(course["id"])
    return idList
if __name__ == "__main__":
    courseFile = "allCourses.json"
    deptTransFile = "deptTrans.txt"
    parsedCourseData = []
    with open(courseFile) as f:
        courseData = json.load(f)

    with open(deptTransFile) as f:
        depttemp = f.read().splitlines()
        for dept in depttemp:
            deptName.append(dept.split(" - "))

    shortNameList = [name[1] for name in deptName]
    deptNamePattern = r"\b" + r"\b|\b".join(shortNameList) + r"\b"
    for i in range(len(courseData)):
        parsedPrereq = []
        for req in ParsePrereqStr(courseData[i]["prereq"]):
            oneReq = []
            for course in req:
                idList = GetID(course[0], course[1])
                if len(idList) == 0:
                    del course
                else:
                    for oneid in idList:
                        reqDict = {}
                        reqDict["id"] = oneid
                        reqDict["concur"] = course[2]
                        oneReq.append(reqDict)
            parsedPrereq.append(oneReq)
        courseData[i]["prereq"] = parsedPrereq
    with open("courseData.json", "w") as fwrite:
        fwrite.write(json.dumps(courseData, indent=4, separators=(',', ':')))
