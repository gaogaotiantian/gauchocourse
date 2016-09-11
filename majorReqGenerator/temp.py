db = SqliteDatabase('course.db')

# class Course(Model):
#     Department = CharField()
#     Number = DateField()
#     JsonID = IntegerField()

#     #is_relative = BooleanField()

#     class Meta:
#         database = db # This model uses the "people.db" database.

# db.connect()

# try:
#     db.create_tables([Course])
# except:
#     pass



# try:
#     for course in courseList:
#         newCourse = Course(Department = course['sub'], Number = course['number'], JsonID = course['id'])
#         newCourse.save()
# except:
#     pass

    # course['majorlimit']
    # course['levellimit']

    # course['semester']
    # course['gearea']
    # course['units']
    # course['label']




def string2Json(ifile):
    jsonStr = open(ifile,'rt').read()
    jsonList = json.loads(jsonStr)
    return jsonList



# courseList = string2Json('../courseData.json')



# convert 13AH-BH-CH in to ['13AH', '13BH', '13CH']
# numPattern = re.compile(r'([0-9]+)[A-Za-z]+')
# def regainCourseNum(courseList,index=1):
#     lst = courseList
#     indx = index
#     for j in range(index,len(lst)):
#         # print('aaa')
#         for i in range(index-1,-1,-1):
#             try:
#                 num = re.match(numPattern,lst[i]).group()
#                 lst[j] = num + lst[j]
#                 break
#                 print(num)
#             except:
#                 continue
#     return lst





# a = ['13AH','BH','CH']
# print(regainCourseNum(a))
# def createDeptList(deptSet):
#     deptList = list(deptSet)
#     keys = NAME_MAP.keys()
#     outList = []
#     for dept in deptList:
#         try:
#             outList.append(NAME_MAP[dept])
#         except:
#             for key in keys:
#                 if dept in key:
#                     outList.append(NAME_MAP[key])
#     print(outList)

# def guessDept(deptSet, numList):
#     deptList = list(deptSet)
#     deptIndex = 0
#     for dept in deptList:

# def checkDept(dept,numList):
#     for course in Course.select().where(Course.Department == dept):
#         for num in numList:
#             if course.Number != num:
#                 return False
#     return True
            
#             #print("{} {}".format(course.Department,course.Number),end='           ')
