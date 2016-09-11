# import peewee
# from peewee import *
import json
import sys
import re
from collections import OrderedDict





# def mapDept2Abbrev():
#     with open('deptTrans.txt') as f:
#         nameMap = {}
#         for line in f:
#             temp = line.split(' - ')
#             # print(temp)
#             nameMap[temp[0]] = temp[1][:-1]

#     return nameMap

# NAME_MAP = mapDept2Abbrev()

courseNumPattern1 = re.compile(r'\b[0-9]*[0-9A-Z]\b')
# 13AH-BH-CH
courseNumPattern2 = re.compile(r'\b[0-9]+?[A-Z]*\b')

deptPattern = re.compile(r'\b([A-Z][a-z]+)\s?[0-9]+')

multiEmptyLinePattern = re.compile(r'\n[\n|\s]+')

from tika import parser
# text = parser.from_file('pdf/Phys/Physics-BS_2016.pdf')
# text = parser.from_file('pdf/PStat/Statistics-BS-2016.pdf')



numPattern2 = re.compile(r'([0-9]+)[A-Z]?')
def regainCourseNum(courseList):
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
        # print(outList)
    return outList


lst = ['Mathematics','Chemistry','Physics']
# guessDept([1],lst)

def parseLAS(path):

    text = parser.from_file(path)
    # print text.keys()
    text = text['content'].split("MAJOR REGULATIONS")[:-1]

    # print len(text)
    text = text[0].split('PREPARATION FOR THE MAJOR')[1:]
    text = text[0].split('UNITS YET TO COMPLETE')[1:]
    text = "".join(text[0].split('UPPER-DIVISION MAJOR'))
    #text = text[0].encode('utf8').replace('.','')
    deleteDots = re.compile(' \.+ [0-9\-]+')
    #print(re.findall(deleteDots,text))
    text = deleteDots.sub('',text)
    text = text.split('(With consent')[0]
    # print(text)
    deptSet = set(re.findall(deptPattern,text))
    # regexDept = '(' + ".*)|(".join(depts) + '.*)'
    regexDept = '|'.join(deptSet)
    # print(regexDept)

     # deptList = re.findall(r'[A-Z][^\.][a-z]+\s?',text)
    deptList = re.findall(deptPattern,text)

    text = multiEmptyLinePattern.sub('',text)
    textList = text.split('\n')
    #print(textList)
    textList = [' '.join(line.split()[1:]) for line in textList]

    # for ele in textList:
        # print(ele)
    parsedList = []
    for ele in textList:
        parsedList.append(re.split(regexDept,ele))

    # print(parsedList)
    courseNumsDict = OrderedDict()

    lineIndex = -1
    
    courseIndex = 0
    for line in parsedList:
        # print('Line:  ',line)
        for ele in line:
            parsedNum1 = re.findall(courseNumPattern1,ele)
           # parsedNum2 = re.findall(courseNumPattern2,ele)#ele.split('-')
            if parsedNum1 == []:
                parsedNum1 = re.findall(courseNumPattern2,ele)
            #print(parsedNum1)
            parsedNum1 = regainCourseNum(parsedNum1)
            if parsedNum1 != []:
                lineIndex+=1

            #parsedNum1.extend(parsedNum2)
            # for id in parsedNum1:
            #dept = guessDept(parsedNum1,deptSet)
            # dept = guessDept(parsedNum1)
            try:
                # print(parsedNum1)
                # print(deptList[lineIndex]+'    '+ str(lineIndex),end='\n\n')
                for courseNum in parsedNum1:
                    courseNumsDict[courseIndex] = [deptList[lineIndex], courseNum]
                    courseIndex+=1
                # print("newline\n")
            except:
                lineIndex-= 1
                for courseNum in parsedNum1:
                    courseNumsDict[courseIndex] = [deptList[lineIndex], courseNum]
                    courseIndex+=1
        # setOfCourse = set(courseNumsList)
        # print(setOfCourse)
            # if any(courseNumsDict) == True:
            #     print(courseNumsDict)
    #print(courseNumsDict)
    return courseNumsDict
    # for key,value in courseNumsDict.items():
        # print("sub: {} num: {}".format(value,key))


# parseLAS(text)

if (len(sys.argv) != 2):
    print("Error: Invalid Filename, Expecting 1 pdf file")
else:
    courseDict = parseLAS(sys.argv[1])
    print(json.dumps(courseDict,indent=4, separators=(',', ': ')))

    # for key,value in courseDict.items():
        # print("sub: {} num: {}".format(value,key))

# python3 reqGenerator.py pdf/Phys/Physics-BS_2016.pdf > phys.json