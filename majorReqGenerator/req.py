import re
import json
import copy
from collections import OrderedDict
import collections
import os
# This class has two parts: 1. a department name map (self.nameMap) that maps department names to their abbreviations
#                           2. a nested dictionary that allow access to courses by department name and course number
class dept2AbbrevMap:
    def __init__(self):
        with open('deptTrans.txt') as f:
            self.nameMap = {}
            for line in f:
                temp = line.split(' - ')
                self.nameMap[temp[0]] = temp[1][:-1]
        
        self.courseByDeptDict = string2Json('courseByDepartment.json')

    def map2Abrrev(self,deptStr):
        for value in self.nameMap.values():
            if deptStr in value or deptStr.upper() in value:
                print(deptStr)
                return value
        for key in self.nameMap.keys():
            if deptStr in key:
                print(deptStr)
                return self.nameMap[key]
        return "not valid"

    # Given a course [Department,course Number]
    # return whether the course was in the database
    def isValid(self,courseStrList):
        try:
        # print(self.map2Abrrev(courseStrList[0]))
        # print(self.courseByDeptDict[self.map2Abrrev(courseStrList[0])])
            test = self.courseByDeptDict[self.map2Abrrev(courseStrList[0])][str(courseStrList[1]).upper()]
            # print(test)
            return True
        except:
            return False

    # Given a course [Department,course Number]
    # return all information of that course as a dictionary
    def getCourse(self,courseStrList):
        try:
            course = self.courseByDeptDict[self.map2Abrrev(courseStrList[0])][str(courseStrList[1]).upper()]
            return course
        except:
            print('This course is invalid!')
            return None
    # Given a course, return its units
    def getUnits(self,courseStrList):
        units = 0
        try:
            units = self.courseByDeptDict[self.map2Abrrev(courseStrList[0])][str(courseStrList[1]).upper()]["units"]
            print("UNITS:", units)
            return int(units)
        except:
            if type(courseStrList) == collections.OrderedDict and 'course' not in courseStrList.keys():
                # handle course not opened in past three years

                #print('sub:', courseStrList['sub'])
                #print('VALUES', self.courseByDeptDict[courseStrList['sub']].values())
                if courseStrList['number'] not in self.courseByDeptDict[courseStrList['sub']].keys():
                    units = 4
                else:
                    units = self.courseByDeptDict[self.map2Abrrev(courseStrList['sub'])][str(courseStrList['number']).upper()]["units"]
            print('Recieveing: ',courseStrList, 'units: ', units)
            return units
        else:
            print('This course is invalid!',courseStrList)
            return -1
    # change the format of a course to the desired format
    # e.g. math 8 -> MATH 8
    def formatCourse(self,courseStrList):
        if self.isValid(courseStrList):
            lst = [self.map2Abrrev(courseStrList[0]),str(courseStrList[1]).upper()]
            course = OrderedDict()
            # course = {}
            course["sub"] = lst[0]
            course["number"] = lst[1]
            return course
        else:
            print('This course is invalid!',courseStrList[0] + ' ' + courseStrList[1])
            return None


# This is a parser on major requirements. It will create a json file.
# I already convert pdfs to txts in pdf2txt.py, so the parser is playing with strings
# There are 3 rounds of parse in total, each of which convert the data into more concise form
# In round 3, in order to extract the sentence logic (e.g. or, and) from the data,
# I rejoined the list of words, extracted the logic and tokenize the text again.

class MajorReqParser(object):
    def __init__(self,dept,geType,major):
        self.dept = dept
        self.geType = geType
        self.major = major
        self.delList = ['with', 'an', 'average', 'grade', 'of', '~70~','One','course']
        self.dept2AbbrevMap = dept2AbbrevMap()
        self.paranPatt = re.compile(r'\((.*)\)')
        self.noneParanPatt = re.compile(r'(.*)\(.*\)(\w)?')
        self.orPatt = re.compile(r'or',re.I)
        self.andPatt = re.compile(r'and',re.I)
        # pass

    def ParseOneMajor(self,path):
        reqTXT = open(path,'rt').read()
        print(reqTXT)
        combineColons = re.compile(r':\s\n\s')
        reqTXT = combineColons.sub(':\n',reqTXT)
        reqTXT = reqTXT.replace('_','')
        reqTXT = reqTXT.replace(';',',')
        reqTXT = reqTXT.replace(', \n',', ')
        # a = []
        # a.append(reqTXT)
        # print(a)
        

        reqTXT = reqTXT.split('UNITS YET TO COMPLETE')[1]
        reqTXT = reqTXT.split('Elective courses taken')[0]
        reqTXTList = re.split(r'\n',reqTXT)
        print('Before cleaning: ',reqTXT)

        reqList = self.cleaning(reqTXTList,'LAS')
        print(reqList)

        print('First:\n')
        
        shrinkDotsPatt = re.compile(r'[^A-Z]\.+')                           # replace dots with swirl
        replaceStar = re.compile(r'\*')                             # delete stars  


        for j in range(len(reqList)):
            reqList[j] = shrinkDotsPatt.sub('~',reqList[j])
            reqList[j] = replaceStar.sub('',reqList[j])
            reqList[j] = reqList[j].strip()
            # reqList[j] = delParanPatt.sub('',reqList[j])
        # for index in sorted(delIndexList,reverse=True):
        #   del reqTXTList[index]
        # print(self.UDUnits,end="\n\n")


        # for line in reqList:
            # print(line)
        # print('\n\n\n\n')

        # return reqList
        self.reqList = reqList
        self.ParseOneMajor2nd()
        return self.ParseOneMajor3rd()

    def cleaning(self,reqTXTList,LASorCOE='LAS'):
        UDUnitsPatt = re.compile(r'([0-9]+) UD units are required') # delete UD Units requirement
        noNumPatt = re.compile(r'[0-9]+')                           # delete line that lack course numbers
        whiteSpacePatt = re.compile(r'\w+')                         # delete blank lines
        NOTEPatt = re.compile(r'NOTE',re.I)                         # delete line that contain "Note"
        endWith2WhiteSpacePatt = re.compile(r'\s\s$')               # check if valid line
        delParanPatt = re.compile(r'[\(\)]')                        # delete paranthess
        

        delIndexList = []
        for i in range(len(reqTXTList)):
            UDUnits = re.search(UDUnitsPatt,reqTXTList[i])
            noNum = re.search(noNumPatt,reqTXTList[i])
            notBlank = re.search(whiteSpacePatt,reqTXTList[i])
            note = re.search(NOTEPatt,reqTXTList[i])
            validLine = re.search(endWith2WhiteSpacePatt,reqTXTList[i])

            # most of the irrelevant line could be filtered by 'validLine'
            if validLine == None and LASorCOE == 'LAS':
                delIndexList.append(i)
                # print(i,"validLine")
            elif UDUnits != None:
                # self.UDUnits = UDUnits.group()[0:2]
                # print(i,"UD units")
                delIndexList.append(i)
            elif noNum == None:
                # print(i,"noNum")
                delIndexList.append(i)
            elif notBlank == None:
                # print(i,"notblank")
                delIndexList.append(i)
            elif note != None:
                # print(i,"note")
                delIndexList.append(i)
            elif (LASorCOE=='COE'):
                reqTXTList[i] = re.sub(r'\.\s','',reqTXTList[i])

        # for i in delIndexList:
        #   print("DEL: ",i , reqTXTList[i])

        # delete useless lines by index
        # http://stackoverflow.com/questions/18837607/remove-multiple-items-from-list-in-python
        reqList = [v for i, v in enumerate(reqTXTList) if i not in delIndexList]
        return reqList
    
    def ParseOneMajor2nd(self,path=""):
        parsedReqs = []

        courseNumPatt = re.compile(r'[0-9]+[A-Z]+-[A-Z]+-[A-Z]+|[0-9]+[A-Z]+-[A-Z]+')
        for i in range(len(self.reqList)):
            # A. Physic 108
            temp = re.split(r'[A-Z]\.\s+',self.reqList[i])
            if len(temp) != 2:
                self.reqList[i] = temp[0]
            else:
                self.reqList[i] = temp[1]
            self.reqList[i] = self.reqList[i].split()

            # delete some known useless words
            delIndexList = []
            for index in range(len(self.reqList[i])):
                # print(index)
                if self.reqList[i][index] in self.delList:
                    delIndexList.append(index)
                    # print(index)
            oneLine = [v for i, v in enumerate(self.reqList[i]) if i not in delIndexList]

            for j in range(len(oneLine)):
                oneLine[j] = oneLine[j].replace('~','')
                # check if this line contains a course sequence like Math 3A-B
                seqCourses = re.search(courseNumPatt,oneLine[j])
                # 13AH-BH-CH -> 13AH, 13BH, 13CH
                if seqCourses != None:
                    oneLine[j] = recoverCourseNum(seqCourses.group().split('-'))
                # split course sequence like Phys 20-21-22-23-24-25
                if type(oneLine[j]) != list and j != len(oneLine)-1 :
                    oneLine[j] = oneLine[j].split('-')
                # flatten list of list
                if type(oneLine[j]) != list:
                    lst = ['a']
                    lst[0] = oneLine[j]
                    oneLine[j] = lst
            # the actual flatten statement
            oneLine = [item for sublist in oneLine for item in sublist]
            self.reqList[i] = oneLine


        


        print('Second:\n')
        for line in self.reqList:
            print(line)
        print('\n\n\n\n')


    def ParseOneMajor3rd(self):
        print("Third: ")
        reqJoinList = []
        for line in self.reqList:
            reqJoinLine = ""
            for word in line:
                reqJoinLine += (word + ' ')
            reqJoinList.append(reqJoinLine)

        lineDictList = []
        for i in range(len(reqJoinList)):
            lineOfReqList = reqJoinList[i].rsplit(maxsplit=1)
            ordDict = OrderedDict()
            ordDict["course"] = lineOfReqList[0]
            ordDict["units"] = lineOfReqList[1]
            lineDictList.append(ordDict)

        for line in reqJoinList:
            print(line)


        print('\n\n\n\n')
        reqParseList = []
        for lineDict in lineDictList:
            reqOfLine = self.RECParseOneLine(lineDict["course"])
            if reqOfLine[-1] == '':
                reqOfLine = reqOfLine[:-1]
            if len(reqOfLine) == 1:
                reqOfLine = reqOfLine[0]
            # print(reqOfLine, end = "      ")
            # print(lineDict["units"])
            print("\nNEW LINE\n")
            reqParseList.append(reqOfLine)
            # print(reqOfLine)
        print('\n\n\n\n')


        for i in range(len(reqParseList)):
            lineDictList[i]["course"] = reqParseList[i]

        # convert some nested lists into dictionary to match the json output format
        for j in range(len(lineDictList)):
            unitsList = lineDictList[j]["units"].split('-')
            if len(lineDictList[j]["course"]) == 2 and type(lineDictList[j]["course"]) == list and len(lineDictList[j]["course"][0]) > 2 and len(unitsList) == 2:
                for choice in range(2):
                    print("working with ", lineDictList[j]["course"])

                    print("element is type: ", type(lineDictList[j]["course"][0]), " \ncontent:",lineDictList[j]["course"][0], "\n\n")
                    lineDictList[j]["course"][choice] = {
                        "course":lineDictList[j]["course"][choice],
                        "units":self.computeUnits(lineDictList[j]["course"][choice])
                    }

        result = OrderedDict()
        result["major"] = "Physics BS"
        result["geType"] = "LSBS"
        result["ChoiceCourse"]=lineDictList
        
        # print(json.dumps(result, indent=4, separators=(',', ':')))
        return(json.dumps(result, indent=4, separators=(',', ':')))

        print("\n\n\n\n\n")

        # print(lineDictList)
            # print(reqOfLine)
        
        # s = "i love you (or not)."
        # result = re.search(self.paranPatt,s).group()
        # print('result: ',result)


        # for line in self.reqList:
            # print(line)
        print('\n\n\n\n')
    def guessUnits(self,courseDict):
        pass
    def RECParseOneLine(self,text):
        req = []
        print("Rec: ", text)
        subReqList = re.findall(self.paranPatt,text)


        # If this line contain paranthess
        if subReqList != []:
            print("Found paranthess!!!!")
            
            # Create a new string that has been extracted the info in the parathess
            # analyze the new string and combine the info with those course inside paranthess
            if len(subReqList) > 1:
                print('more than one pair of paranthess')
                raise IndexError
            noneParanTextList = re.split(r'\(.*\)',text)

            # need to delete blank element
            noneParanTextList = [text for text in noneParanTextList if text != '']
            print("None Paran: ", noneParanTextList)

            noneParanList = []
            pranReqList = []

            # Recursively parse reqs inside paranthess
            for reqInParan in subReqList:
                print("Inside Paran: ")
                subSub = self.RECParseOneLine(reqInParan)
                pranReqList.append(subSub)
            # Recursively parse reqs outside of parathess
            # and put them in a list
            for reqNoneParan in noneParanTextList:
                noneParanList.append(self.RECParseOneLine(reqNoneParan))
            
            # Now we need to combine none paran with paran
            # assume start with none-paran
            index = 0
            print("\nNone Paran List !\n",noneParanList)
            print("\nParan List !\n",pranReqList)

            while index < len(noneParanList):
                if len(noneParanList) >= 1:
                    print("None Paran item: ", noneParanList[index])
                    # ... or current
                    if noneParanList[index][0] == 'or':
                        try:
                            req.append([noneParanList[index][1], pranReqList[index][0]])
                        except:
                            req.append(noneParanList[index][1])
                    # current or (...)
                    elif noneParanList[index][1] == 'or':
                        try:
                            req.append([ noneParanList[index][0], pranReqList[index][0]])
                        except:
                            print("Error: No more items in the Paranthess")
                            req.append(noneParanList[index][0])
                            contine
                    else:
                        try:
                            # current ()
                            if (pranReqList[index][1] == []):
                                req.append(noneParanList[index][0])
                            # current (...)
                            else:
                                print("Just concatenate: ",noneParanList[index][0], pranReqList[index][0])
                                temp = copy.deepcopy(noneParanList[index][0])
                                temp.append(pranReqList[index][0])
                                # temp.append('')
                                print("deep: ",temp)
                                req.append(temp)
                        except:
                            req.append(noneParanList[index][0])
                index += 1
                print('req: ',req,'\n')

        else:
            req = self.ITERParseOneLine(text)
        return req
        
        # pass
    def ITERParseOneLine(self,text):
        
        tokenized = text.split()
        print("Iter: ", tokenized)
        # deptIndex = 0
        index = 0
        dept = self.dept
        isDept = False
        # print("orig dept",dept)
        courseList = []
        isOrBegin = False

        if text == '':
            return ('EMPTY','')

        # prevent:
        # PSTAT 120A (or W 120A), 120B, 126, 160A 160B
        # [['PSTAT', '120A'], []]
        # if tokenized[0] == ',' :
        #     tokenized[0] = dept
        
        while  index < len(tokenized):
            # avoid paser translate "or" to dept "PORT"
            if tokenized[index] != 'or' and tokenized[index]!='and':
                abbrev = self.dept2AbbrevMap.map2Abrrev(tokenized[index])
                if abbrev != 'not valid':
                    # print(tokenized[index]+"abbrev")
                    dept = abbrev
                    isDept = True
                    # deptIndex = index
            # print(isDept)
            if isDept == False:
                # print('not a dept')
                # if it's a course number, add it to course list
                if re.search(r'[0-9]+[A-Z]?',tokenized[index]) != None:
                    print('It\'s a course', dept, tokenized[index])
                    course = self.dept2AbbrevMap.formatCourse([dept,tokenized[index].strip(',')])
                    print(course)
                    if course != None:
                        courseList.append(course)
                
                elif re.search(self.orPatt, tokenized[index]) != None:
                    print('end with OR')
                    # if it's an "or" at the end of the text,
                    # we should return the parsed courses and a indicator of "or"
                    if index == len(tokenized)-1:
                        return [courseList,'or']
                    # if it's an "or" at the begining
                    elif index == 0:
                        print("begin with OR")
                        isOrBegin = True
                    # if it's an "or" between courses
                    else:
                        print("OR between words")
                        # since in the smallest requirement (where ITERParse is called upon)
                        # 'or' usully appear only once, and only courses in same department was involved
                        # we can take care the difference between
                        # Chemistry 1A-B or 2A-B
                        # Physics 1, 6A or 21
                        # by the following code
                        leftOfOR = 0
                        leftCourseList = []
                        rightOfOR = 0
                        rightCourseList = []
                        newIndex = 0

                        # without this check, PHYS 5L or PHYS 25L will become ({ "course":[[{5L}],[{25L}]], "units": 2}
                        if len(tokenized) > 4:
                        

                            while tokenized[newIndex] != 'or':
                                if len(tokenized) > 0:
                                    # if it's a course number
                                    if re.search(r'\b[A-Z]',tokenized[newIndex]) == None:
                                        leftOfOR += 1
                                        leftCourseList.append(tokenized[newIndex])
                                        print('left',tokenized[newIndex])
                                    newIndex+=1
                            print('or Index ',newIndex)

                            for i in range(newIndex+1,len(tokenized)):
                                rightOfOR += 1
                                rightCourseList.append(tokenized[i])
                                print('right',tokenized[i])

                            print("A-B OR C-D\n")
                            print(leftOfOR,'  ',rightOfOR)
                            if leftOfOR == rightOfOR:
                                print("EQUAL")
                                AB = self.ABORCD(dept,leftCourseList)
                                CD = self.ABORCD(dept,rightCourseList)


                                AB_OR_CD_list = OrderedDict()
                                AB_OR_CD_list["course"] = [AB[0],CD[0]]
                                AB_OR_CD_list["units"] = min(AB[1],CD[1])
                                return [AB_OR_CD_list, '']

                        
                        # A,B,C or D
                        # link the next course with the course before "or"
                        elif re.search(r'[0-9]+[A-Z]?', tokenized[index+1]) != None:
                            # This check doesn't seem necessary
                            course = self.dept2AbbrevMap.formatCourse([dept,tokenized[index+1].strip(',')])
                            if len(courseList) > 1:
                                print(course)
                                if course != None:
                                    courseList[-1] = [courseList[-1], course]
                            # A or B
                            # create a dictionary
                            else:
                                if course != None:
                                    choiceCourse = OrderedDict()
                                    print("Line 454!")
                                    choiceCourse["course"] = [courseList[-1],course]
                                    choiceCourse["units"] = self.dept2AbbrevMap.getUnits(course)
                                    courseList[-1] = choiceCourse
                                else:
                                    pass
                            index += 1
                        else:
                            # the next word is a uselss word or a different dept
                            print("useless: ", tokenized[index])
                        
                # if it's an "and", just ignore it
                elif tokenized[index] == 'and':#re.search(self.andPatt,tokenized[index]):
                    print("encounter AND")
                    pass
                else:
                    print("I don't know: ", tokenized[index])
            index += 1
            isDept = False
            print('After One Word, dept: ',dept,'\n')

        if (len(courseList) == 1):
            courseList = courseList[0]
        print('    parsed: ', [courseList,''] if isOrBegin == False else ['or',courseList], end="\n\n")
        return [courseList,''] if isOrBegin == False else ['or',courseList]
    
    def ABORCD(self,dept,courseNumList):
        result = []
        for num in courseNumList:
            course = OrderedDict()
            course["sub"] = dept
            course["number"] = num
            result.append(course)
        units = 0
        for course in result:
            units += int(self.dept2AbbrevMap.getUnits(course))
        return (result,units)

    def computeUnits(self,courseList):
        print('Computing units!')
        totalUnits = 0
        for course in courseList:
            print(course.values())
            units = self.dept2AbbrevMap.getUnits(list(course.values()))
            if units == -1:
                print("EROOR ON UNITS!!!!")
            else:
                totalUnits += int(units)
        return totalUnits


numPattern2 = re.compile(r'([0-9]+)[A-Z]?')
def recoverCourseNum(courseList):
    if courseList == []:
        return []
    # print(courseList)
    outList = courseList[:1]
    for i in range(1,len(courseList)):
        previousNum = re.findall(numPattern2,outList[i-1])
        # print(previousNum)
        currentNum = re.findall(numPattern2,courseList[i])
        # print(currentNum)
        if currentNum == []:
            outList.append(previousNum[0]+courseList[i])
        else:
            outList.append(courseList[i])
        # outList.append('-')
        # print(outList)
    return outList


# helper functions
def string2Json(ifile):
    jsonFile = open(ifile,'rt')
    jsonList = json.loads(jsonFile.read())
    jsonFile.close()
    return jsonList

def makeNewDirIfNecessary(relativePath):
    absPath = WCD + '/' + relativePath
    try: 
        os.makedirs(absPath)
    except OSError:
        if not os.path.isdir(absPath):
            raise
    return

# print(recoverCourseNum(['13AH','BH','CH']))
# print(recoverCourseNum(['3A','B']))


# parser = MajorReqParser('PHYS','LSBS','PHYS')
# # parser = MajorReqParser('MATH')
# # parser.ParseOneMajor('txt/Math/Mathematics-BS-2016.txt')
# parser.ParseOneMajor('txt/Phys/Physics-BS_2016.txt')

# # parser.ParseOneMajor('txt/Chem/Chemistry-BS_2016.txt')
# # parser.ParseOneMajor('txt/Math/Financial-Math-Stat-BS-2016.txt')

# parser.ParseOneMajor2nd()
# parser.ParseOneMajor3rd()

# parser.dept2AbbrevMap.getUnits(['PHYS','25L'])

# a = OrderedDict()
# a["sub"] = "MATH"
# a["number"] = "3A"
# print(list(a.values()))
# print(parser.ITERParseOneLine('Physics 20 21 22 23 24 25 or '))
# print(parser.ITERParseOneLine('or 13AH 13BH 13CH'))
# print(parser.ITERParseOneLine('Physics 127BL, 128BL, 142L, 143L, 144L, 145L, 199'))
# print(parser.ITERParseOneLine('Physics 104 or 105B'))
# print(parser.ITERParseOneLine('5L or 25L'))
# print(parser.ITERParseOneLine('CHEM 1A 1B or 2A 2B'))

WCD = os.getcwd()

deptNamePatt = re.compile(r'(.*)[-_]BF?[AS]')
for dept in os.listdir('txt'):
    for major in os.listdir('txt/'+dept):
        txtPath = 'txt/'+ dept + '/'+ major
        # fileName = txtPath.rsplit('-',maxsplit=1)
        fileName = re.findall(deptNamePatt,txtPath)
        # getType = txt
        # txtDir = 'txt/' + dept
        # txtPath = 'txt' + pdfPath[3:-4] + '.txt'
        if 'Minor' not in txtPath and re.search(r'BS',txtPath) != None and dept != 'Earth' :
            if fileName == []:
                pass
                # print("Original: ",txtPath)
            else:
                # parser.ParseOneMajor()
                
                major = fileName[0][4+len(dept)+1:]
                parser = MajorReqParser(dept,'LSBS',major)
                parsedTXTDir = 'parsed/' + fileName[0][4:]
                parsedTXTPath = parsedTXTDir + 'BS' + '.json'
                # print(major,'   ',parsedTXTDir,'    ')
                makeNewDirIfNecessary(parsedTXTDir)
                parsedTXT = open(parsedTXTPath,'wt')
                try:
                    JSON = parser.ParseOneMajor(txtPath)
                    parsedTXT.write(JSON)
                except:
                    print(major)
                parsedTXT.close()
                # print(parsedTXTDir)
                # print(fileName)


        # makeNewDirIfNecessary(txtDir)
        # newTXT = open(txtPath,'wt')
        # newTXT.write(parser.from_file(pdfPath)['content'])
        # newTXT.close()



# print(parser.ITERParseOneLine('Physics 1 2 3 4 5 70'))

# for dept in os.listdir('pdf'):
#     for major in os.listdir('pdf/'+dept):
#       pdfPath = 'pdf/'+ dept + '/'+ major
#       txtDir = 'txt/' + dept
#       txtPath = 'txt' + pdfPath[3:-4] + '.txt'
#       print(txtPath)
#       makeNewDirIfNecessary(txtDir)
#       newTXT = open(txtPath,'wt')
#       newTXT.write(parser.from_file(pdfPath)['content'])
#       newTXT.close()
'''
class COEMajorReqParser(MajorReqParser):
    def __init__(self,txtPath,dept):
        MajorReqParser.__init__(self,'ECE','COE','ECE')
        WCD = os.getcwd()
        txt = open(WCD+'/'+txtPath,'rt')
        self.dept = dept
        # for line in txt:
        #   print(line)
        self.txt = txt.read()
        # lst = []
        # lst.append(self.txt)
        # print(lst)
        self.parsedTXT = self.txt
        txt.close()
        self.parser1st()
        

    def parser1st(self):
        geUselessPatt = re.compile(r'UNIVERSITY REQUIREMENTS.*General Education and Free Electives taken:',re.S)
        courseNumPatt = re.compile(r'[A-Z]+\s[0-9]+.*\s')
        self.parsedTXT = self.parsedTXT.split('Courses required for the major')[0]
        self.parsedTXT = re.sub(geUselessPatt,'',self.parsedTXT)
        self.parsedTXT = self.parsedTXT.strip()
        
        # general data cleanning, removing empty lines and lines without course numbers/ units
        self.parsedTXT = '\n'.join(self.cleaning(self.parsedTXT.split('\n'),'COE')).strip()

        if (self.dept =='CMPSC'):
            self.parsedTXT = self.parsedTXT.split('1CMPSC 111')[0].strip()

        print(self.parsedTXT)
        # ECE
        if len(self.parsedTXT.split('Major Field Electives')) == 1:
            eceCleanPatt = re.compile(r'[0-9]{2}  •  mAjor reqUiremenTS.*PREPARATION FOR THE MAJOR  ',re.S)
            self.required = self.parsedTXT.split('Must include at least 2 sequences, one of which must be an ')[0]
            self.required = re.sub(eceCleanPatt,'',self.required).split('\n')
            print('\n\n\n\n\n\n')
            for i in range(len(self.required)):
                try:
                    # print(re.findall(courseNumPatt,self.required[i]))
                    self.required[i] = self.required[i].strip()
                    self.required[i] = self.required[i].replace(',','')
                    self.ITERParseOneLine(self.required[i])
                except:
                    pass
                    # print('No course at : ',line)
            self.elective = self.parsedTXT.split('Must include at least 2 sequences, one of which must be an ')[1].split('\n')
        # CS
        else:
            self.required = self.parsedTXT.split('Major Field Electives')[0]
            self.required = re.sub(r'  UPPER DIVISION MAJOR   ','',self.required)
            self.required = re.sub(r'[0-9]{2}  •  mAjor reqUiremenTS\n  PREPARATION FOR THE MAJOR  ','',self.required).split('\n')
            self.elective = self.parsedTXT.replace('(selected from the following list (at least 8 units must be CMPSC courses))','')
            
            self.elective = self.elective.split('Major Field Electives')[1].split('\n')
        # noNumPatt = re.compile(r'[0-9]+')                           # delete line that lack course numbers

        # print(re.search(geUselessPatt,self.parsedTXT).group())
        print('\n\n\n\n\n\n\n\n')
        # for part in self.elective:
        #     print(part)
        print(self.elective)
        print('\n\n\n\n')
        print(self.required)
        # for line in self.required:
        #     print(self.RECParseOneLine(line))

        # print(self.elective)
        # print(self.required)
    def COECleaning(self):
        pass
COEMajorReqParser('txt/compsci-engr/compsci-engr.txt','CMPSC')
print('\n\n\n\n\n\n\n')
COEMajorReqParser('txt/ece/ece.txt','ECE')

'''

# python3 req.py > test.txt
