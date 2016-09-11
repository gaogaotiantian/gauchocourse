import sys
import json
from collections import OrderedDict

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
            # print(deptStr)
            if deptStr in value or deptStr.upper() in value:
                return value
        for key in self.nameMap.keys():
            if deptStr in key:
                return self.nameMap[key]
        raise IndexError

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


class terminalInterface:
    def __init__(self,jsonPath):

        # self.allCourseList = string2Json('../courseData.json')
        # print(self.allCourseList.keys())

        self.dept2AbbrevMap = dept2AbbrevMap()
        
        courseDictRaw = self.json2OrderedDict(jsonPath)
        self.courseDict = OrderedDict()

        # delete invalid courses found by parser
        newIndex = 0
        for key,value in courseDictRaw.items():
            dept = self.dept2AbbrevMap.map2Abrrev(value[0])
            course = [dept, value[1]]
            # print(course)
            if self.dept2AbbrevMap.isValid(course):
                self.courseDict[newIndex] = course
                newIndex+=1
        self.parseCourseLength = newIndex

        # print(self.courseDict)
        # self.prettyPrint()
        
    # print courses founded by parser
    # print in three columns
    def prettyPrint(self):
        print('The parser find the following courses from the pdf/json file:\n')
        outStrList = []
        for key,value in self.courseDict.items():
            oneCourse = '{}. {} {}'.format(key,value[0],value[1])
            outStrList.append(oneCourse)
        # print(outStrList)
        numOfColumns = 3
        # self.parseCourseLength = len(outStrList)
        print(self.parseCourseLength)
        numOfRows = self.parseCourseLength // numOfColumns
        courseIndex = 0
        # print(numOfRows)
        for row in range(numOfRows):
            # try:
            print('{:<25}{:<25}{:<25}'.format(outStrList[courseIndex],outStrList[courseIndex+1],outStrList[courseIndex+2]))
            courseIndex += numOfColumns
        if self.parseCourseLength % numOfColumns != 0:
            for i in range(numOfRows * numOfColumns,self.parseCourseLength):
                print('{:<25}'.format(outStrList[i]), end='')
            print('\n')

        return

    def getUsefulIndices(self):
        print('Please enter the indices of course you want to add to this field. Note that the index start from 0.')
        inStr = ''
        indexSet = set()
        while(inStr!='end'):
            try:
                inStr = input()
                if inStr == 'end':
                    # print('breaking!!')
                    continue
                index = int(inStr)
                # print("??")
                if index >= self.parseCourseLength or index < 0:
                    raise IndexError
                indexSet.add(index)
                    # print("!!")
            except:
                print('The index you entered is not valid. It should be a integer less than or equal to '+str(self.parseCourseLength-1) + '.')
        
        print('This field now contain the follwoing course:')
        outList = sorted(list(indexSet))
        # print(outStr)
        outList = self.index2CourseList(outList)
        # print('OUT!!!',outList)
        print(outList)
        return outList

    def getElectiveFields(self):
        inStr = ''
        electiveIndexMatrix = []
        while (inStr != 'end'):
            try:
                inStr = input('Please enter the number of elective fields: (you should enter an integer)\n')

                numOfElectiveFields = int(inStr)
                
                for i in range(numOfElectiveFields):
                    electiveIndexList = getUsefulIndices()
                    # electiveIndexList = addMoreCourse(electiveIndexList)
                    electiveIndexMatrix.append(electiveIndexList[:])

                self.electiveIndexMatrix = electiveIndexMatrix
                return

            except:
                print('You should enter an integer. Alternatively, you could type "end" to skip elective course entry.')
        



    def addMoreCourse(self,listOfCourse):
        inStr = ''
        print('Now you can add courses that were not discovered by the parse.\n For example, type "Math 117" and press enter will add Math 117 into currrent field.\n')
        while (inStr!='end'):
            try:
                inStr = input()
                if inStr == 'end':
                    continue
                course = inStr.rsplit(maxsplit=1)
                print(course)
                # if type(eval(course[1])) != 
            except:
                print('Invalid Syntax. Please try "Math 117"\n')

    def index2CourseList(self,indexList):
        courseList = []
        for index in indexList:
            course = [self.dept2AbbrevMap.map2Abrrev(self.courseDict[index][0]),self.courseDict[index][1]]
            if self.dept2AbbrevMap.isValid(course):
                courseList.append(course)
            else:
                # print(index," invalid")
                continue
        return courseList

    def run(self):
        # while 1:

            # print('Please enter the path of major requirement pdf:    e.g. ../pdf/Phys/Physics-BS_2016.pdf')
            # path = input('Please enter the path of major requirement pdf:    e.g. ./pdf/Phys/Physics-BS_2016.pdf\n')
            # print(path)
        # path='pdf/Phys/Physics-BS_2016.pdf'

        # requiredIndexList = []
        self.prettyPrint()
        try:
            self.requiredIndexList = self.getUsefulIndices()[:]
        except:
            self.requiredIndexList = []
            print('This major has no required course? I think it\'s impossible')
        self.requiredIndexList = self.addMoreCourse(requiredIndexList)

        self.electiveIndexMatrix = self.getElectiveFields()

        print(self.requiredIndexList)

        print(self.electiveIndexMatrix)


    def json2OrderedDict(self,jsonPath):
        reqDict = string2Json(jsonPath)
        reqOrderdDict = OrderedDict(sorted(reqDict.items(), key = lambda x: int(x[0])))
        reqOrderdDict = OrderedDict((int(key),value) for key, value in reqOrderdDict.items())
        return reqOrderdDict


# helper functions
def string2Json(ifile):
    jsonFile = open(ifile,'rt')
    jsonList = json.loads(jsonFile.read())
    jsonFile.close()
    return jsonList

# This function shouldn't be call during data entry
# It will modify courseByDepartment.json
# courseData.json is a list of dictiionaries
# this function converts it to a dictionary of dictonary
# where courses were seperated by department
# inside each department, courses can be accessed by number
def courseByDepartment(self):
    allCourseList = string2Json('../courseData.json')

    courseByDeptDict = OrderedDict() # Deptment name -> courses in that dept
    # deptCourses = OrderedDict()  # courseNum -> courseData
    for i in range(len(allCourseList)):
        try:
            courseByDeptDict[allCourseList[i]['sub']][allCourseList[i]['number']] = allCourseList[i]
        except:
            courseByDeptDict[allCourseList[i]['sub']] = OrderedDict()
            courseByDeptDict[allCourseList[i]['sub']][allCourseList[i]['number']] = allCourseList[i]
    # num = 0
    # for dept in courseByDeptDict.values():
    #     for course in dept.keys():
    #         num+=1
        # print(dept)
    # print(num)
    print(json.dumps(courseByDeptDict,indent=4, separators=(',', ': ')))

if (len(sys.argv) != 2):
    print("Error: Invalid Filename, Expecting 1 json file")
else:
    # courseByDepartment()
    interface = terminalInterface(sys.argv[1])
    # interface.addMoreCourse([90])
    # interface.index2CourseList([0,2,3,5,8,33])
    # interface.dept2AbbrevMap.isValid(['ANTH',2])
    # deptMap = dept2AbbrevMap()
    # deptMap.courseByDepartment()
    # print(deptMap.isValid(['MATH','1']))
    # print(interface.allCourseList[0])
    interface.run()

# python3 terminalInterface.py phys_parsed.json > out.json