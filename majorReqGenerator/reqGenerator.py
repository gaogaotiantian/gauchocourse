import peewee
from peewee import *
import json
import sys
import re

db = SqliteDatabase('course.db')

def string2Json(ifile):
    jsonStr = open(ifile,'rt').read()
    jsonList = json.loads(jsonStr)
    return jsonList

class Course(Model):
    Department = CharField()
    Number = DateField()
    JsonID = IntegerField()

    #is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

# class Pet(Model):
#     owner = ForeignKeyField(Person, related_name='pets')
#     name = CharField()
#     animal_type = CharField()

#     class Meta:
#         database = db # this model uses the "people.db" database

db.connect()

try:
    db.create_tables([Course])
except:
    pass

from time import sleep
courseList = string2Json('../courseData.json')
# for course in courseList:
#   newCourse = Course(Department = course['sub'], Number = course['number'], JsonID = course['id'])
#   newCourse.save()
    # course['majorlimit']
    # course['levellimit']

    # course['semester']
    # course['gearea']
    # course['units']
    # course['label']
#for course in Course.select().where(Course.Department=='ANTH'):
    #print("{} {}".format(course.Department,course.Number),end='           ')
    #sleep(1)

# courseNumPattern = re.compile(r'(^\W\w+) [...]')

# courseNumPattern = re.compile(r'\S\s+ (...) ') # get units
# courseNumPattern = re.compile(r'\W\w+ (.*)')
# courseNumPattern = re.compile(r'[A-Z]\w+\s(.*)')


# Physics 20-21-22-23-24-25
# courseNumPattern1 = re.compile(r'[\s|-]([0-9]\w+)')#[\s|-]')
# courseNumPattern1 = re.compile(r'[0-9]+[a-zA-Z]?[^\.]')#[\s|-]')
# courseNumPattern1 = re.compile(r'[\s|-]([0-9]+[a-zA-Z]+?)')
courseNumPattern1 = re.compile(r'\b[0-9]*[0-9A-Z]\b')
# 13AH-BH-CH
courseNumPattern2 = re.compile(r'\b[0-9]+?[A-Z]*\b')

courseNumPattern3 = re.compile(r'\s[0-9]+[^.]\s')
multiEmptyLinePattern = re.compile(r'\n[\n|\s]+')
from tika import parser
text = parser.from_file('pdf/Phys/Physics-BS_2016.pdf')
# text = parser.from_file('pdf/PStat/Statistics-BS-2016.pdf')


# convert 13AH-BH-CH in to ['13AH', '13BH', '13CH']
numPattern = re.compile(r'[0-9]+')
def regainCourseNum(lst,index=1):
    indx = index
    for j in range(index,len(lst)):
        print('aaa')
        for i in range(index-1,-1,-1):
            try:
                num = re.match(numPattern,lst[i]).group()
                lst[j] = num + lst[j]
                break
                print(num)
            except:
                continue
    return lst

# a = ['13AH','BH','CH']
# print(regainCourseNum(a))

def parseLAS(text):
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
    # text = text.strip('')
    # text = text.split('\n')/
    # remove empty lines
    text = multiEmptyLinePattern.sub('',text)
    textList = text.split('\n')
    print(textList)
    textList = [' '.join(line.split()[1:]) for line in textList]
    reqList = [req.split(' or ') for req in textList]
    #text = text.split('UNITS YET TO COMPLETE')[1]
    #text = text.split('UPPER-DIVISION MAJOR')
    #lower = text[0]
    #upper = text[1]
    #text = text[0].split()
    # print len(text)
    #print(lower)
    #text = re.split('from|following',text)
    #takeEveryCourse = text 
    #selectFromCourses =
    # for line in textList:
        # print(line)
    # print(textList)

    print()
    # print(reqList)
    for req in reqList:
        print(req)
    numOfReq = 0
    for req in reqList:
        for ele in req:
            parsedNum1 = re.findall(courseNumPattern1,ele)
            parsedNum2 = re.findall(courseNumPattern2,ele)#ele.split('-')
            # parsedNum1.extend(parsedNum2)
            # for id in parsedNum1:

            courseNumsList = parsedNum1
            #setOfCourse = set(courseNumsList)
            # print(setOfCourse)
            print(courseNumsList)
            print(parsedNum2)
            #for c in setOfCourse:
            #  print(c)
    # a.append(text)
    # print(a)
    # out = re.findall(courseNumPattern,text)
    # for ele in out:
    #   print(ele)
    #print(upper)

parseLAS(text)