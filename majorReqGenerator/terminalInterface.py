import sys
import json
from collections import OrderedDict

class dept2AbbrevMap:
    def __init__(self):
        with open('deptTrans.txt') as f:
            self.nameMap = {}
            for line in f:
                temp = line.split(' - ')
                # print(temp)
                self.nameMap[temp[0]] = temp[1][:-1]
            # print('sfsdafas')
            # print(self.nameMap.keys())
    def map2Abrrev(deptStr):
        for key in self.nameMap.keys():
            if deptStr in key:
                return key
    # def getCourse()

    # courseData.json is a list of dictiionaries
    # this function converts it to a dictionary of dictonary
    # where courses were seperated by department
    # inside each department, courses can be accessed by number
    def courseDataByDepartment(self):
        self.allCourseList = string2Json('../courseData.json')
        currentDept = self.allCourseList[0]['sub']
        # for dept in self.nameMap.values():
        courseByDeptDict = OrderedDict() # Deptment name -> courses in that dept
        deptCourses = OrderedDict()  # courseNum -> courseData
        for i in range(len(self.allCourseList)):
            if (self.allCourseList[i]['sub'] != currentDept):
                courseByDeptDict[currentDept] = OrderedDict(deptCourses)
                deptCourses = OrderedDict(self.allCourseList[i])
                currentDept = self.allCourseList[i]['sub']
            else:
                deptCourses[self.allCourseList[i]['number']] = self.allCourseList[i]
        print(json.dumps(courseByDeptDict,indent=4, separators=(',', ': ')))

class terminalInterface:
    def __init__(self,jsonPath):

        # key is a integer looks like index
        # value is a list [department, coureseNum]
        self.allCourseList = string2Json('../courseData.json')
        # print(self.allCourseList.keys())

        self.dept2AbbrevMap = dept2AbbrevMap()
        self.dept2AbbrevMap.courseDataByDepartment()
        self.courseDict = self.json2OrderedDict(jsonPath)
        # self.prettyPrint()
        

    def prettyPrint(self):
        outStrList = []
        for key,value in self.courseDict.items():
            oneCourse = '{}. {} {}'.format(key,value[0],value[1])
            outStrList.append(oneCourse)
        # print(outStrList)
        numOfColumns = 3
        self.parseCourseLength = len(outStrList)
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

    def getUsefulIndices(self,listLength):
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
                if index > listLength-1:
                    raise IndexError
                indexSet.add(index)
                    # print("!!")
            except:
                print('The index you entered is not valid. It should be a integer less than or equal to '+str(listLength-1) + '.')
        
        print('This field now contain the follwoing course:')
        outList = sorted(list(indexSet))
        print(outList)
        return outList

    def getElectiveFields(self,listLength):
        inStr = ''
        electiveIndexMatrix = []
        while (inStr != 'end'):
            try:
                inStr = input('Please enter the number of elective fields: (you should enter an integer)\n')

                numOfElectiveFields = int(inStr)
                
                for i in range(numOfElectiveFields):
                    electiveIndexList = getUsefulIndices(listLength)
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
                course[1] = int(course[1])
                # if type(eval(course[1])) != 
            except:
                print('Invalid Syntax. Please try "Math 117"\n')

    def run(self,path):
        # while 1:

            # print('Please enter the path of major requirement pdf:    e.g. ../pdf/Phys/Physics-BS_2016.pdf')
            # path = input('Please enter the path of major requirement pdf:    e.g. ./pdf/Phys/Physics-BS_2016.pdf\n')
            # print(path)
        # path='pdf/Phys/Physics-BS_2016.pdf'
        print('The parser find the following courses from the pdf/json file:\n')

        # requiredIndexList = []
        
        
        requiredIndexList = self.getUsefulIndices(self.parseCourseLength)[:]
        self.requiredIndexList = self.addMoreCourse(requiredIndexList)

        self.electiveIndexMatrix = self.getElectiveFields(self.parseCourseLength)

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



if (len(sys.argv) != 2):
    print("Error: Invalid Filename, Expecting 1 json file")
else:
    interface = terminalInterface(sys.argv[1])
    # print(interface.allCourseList[0])
    # interface.run()