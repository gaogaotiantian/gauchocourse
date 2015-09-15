import os
import json
import re
import copy
deptData = []
majorList = []
deptList = []
def AddCourse(course):
    exist = False
    for existCourse in deptData:
        if existCourse["CourseTitle"] == course["CourseTitle"]:
            if course["semester"][0] not in existCourse["semester"]:
                existCourse["semester"].append(course["semester"][0])
            existCourse["Major-Limit"] = MajorLimitCombine(existCourse["Major-Limit"], course["Major-Limit"])
            exist = True
    if exist == False:
        deptData.append(course)   

def MajorLimitCombine(limit1, limit2):
    if len(limit1) == 0 or len(limit2) == 0:
        return ""
    else:
        return limit1 + limit2
# This is not compatible with py3
def CmpCourseName(course1, course2):
    wdList1 = course1["CourseTitle"].split()
    wdList2 = course2["CourseTitle"].split()
    if (wdList1[0] != wdList2[0]):
        if wdList1[0] > wdList2[0]:
            return 1
        else:
            return 0
    else:
        pat = re.compile(r"([0-9]*)([a-zA-Z]*)")
        parts1 = re.match(pat, wdList1[-1]).groups()
        parts2 = re.match(pat, wdList2[-1]).groups()
        try:
            if (int(parts1[0]) == int(parts2[0])):
                if (len(parts1) == len(parts2)):
                    if parts1[1] > parts2[1]:
                        return 1
                    else:
                        return -1
                else:
                    return len(parts1) - len(parts2)
            else: 
                return int(parts1[0]) - int(parts2[0])
        except:
            print "We got an error when parsing course title:"
            print course1["CourseTitle"]
            print course2["CourseTitle"]
            return 0
def AddFileData(filename):
    semester = None
    if filename[-6] == '1':
        semester = "winter"
    elif filename[-6] == '2':
        semester = "spring"
    elif filename[-6] == '3':
        semester = "summer"
    elif filename[-6] == '4':
        semester = "fall"
    with open(filename) as f:
        fileData = json.load(f)
        for data in fileData:
            data["semester"] = [semester]
            data["CourseTitle"] = " ".join(data["CourseTitle"].split())
            AddCourse(data)

def GetFormat(course, idNum, geCourses):
    ret = {}
    ret["label"] = course["CourseTitle"] + " " + course["Full Title"]
    ret["semester"] = course["semester"]
    ret["id"] = str(idNum)
    ret["sub"] = (" ").join(course["CourseTitle"].split()[:-1])
    ret["number"] = course["CourseTitle"].split()[-1]
    ret["levellimit"] = course["Level-Limit"]
    ret["prereq"] = course["PreRequisite"]

    # Major Limit, only apply when major-limit-pass is empty because 
    # otherwise it's just pass limit
    ret["majorlimit"] = []
    if len(course["Major-Limit-Pass"]) == 0:
        for major in majorList:
            if re.search(r"\b{0}\b".format(major), course["Major-Limit"]) is not None:
                ret["majorlimit"].append(major)

    # Units
    # if units is like 1.0-4.0, we consider it as 0
    if '-' in course["Units"]:
        ret["units"] = "0"
    else:
        ret["units"] = str(int(float(course["Units"])))

    # GE Area
    # Iterate through all geCourses and find match
    # We need exact match to avoid ANTH 2 == ANTH 20
    # We need to add GE Area back to the label after getting all of them
    ret["gearea"] = []
    MajorArea = []
    MinorArea = []
    for area in geCourses:
        for course in geCourses[area]:
            courseName = course.split("-")[0].strip()
            if (" ").join([ret["sub"], ret["number"]]) == courseName:
                if area in ["B", "C", "D", "E", "F", "G"]:
                    MajorArea.append(area)
                else:
                    MinorArea.append(area)

    retGroup = []
    if len(MajorArea) == 0:
        for minArea in MinorArea:
            ret["gearea"].append(minArea)
        retGroup.append(ret)

    for area in MajorArea:
        temp = copy.deepcopy(ret)
        temp["gearea"].append(area)
        for minArea in MinorArea:
            temp["gearea"].append(minArea)
        retGroup.append(temp)
    

    
    for ele in retGroup:
        if len(ele["gearea"]) > 0:
            ele["label"] += " | Area " + ", ".join(ele["gearea"])

    # return this dictList
    return retGroup

if __name__ == "__main__":
    # Read in GE Areas
    ge_folder = "./gearea/"
    geCourses = {}
    for subdir, dirs, files in os.walk(ge_folder):
        for gefile in files:
            with open(ge_folder + gefile) as f:
                # strip ".txt" for key
                geCourses[gefile[:-4]] = f.read().splitlines()
    with open("./majorList.txt") as fmajor:
        majorList = fmajor.read().splitlines()
    with open("./depts.txt") as fdept:
        allDeptData = []
        formattedData = []
        deptList = fdept.read().splitlines()
        for dept in deptList:
            print "Grabbing data from: " + dept
            json_folder = "./json_raw_data/"
            for subdir, dirs, files in os.walk(json_folder):
                for f in files:
                    if f.startswith(dept) and f[len(dept)] == '_' and "2015" in f:
#                       print "Reading File: " + f
                        AddFileData(json_folder + f)
                        
            deptData.sort(cmp=CmpCourseName)
            allDeptData += deptData
            deptData = []
        idNum = 0 
        for course in allDeptData:
            for data in GetFormat(course, idNum, geCourses):
                formattedData.append(data)
                idNum += 1
        with open("allCourses.json", "w") as fout:
            fout.write(json.dumps(formattedData, indent=4, separators=(',', ':')))

