import peewee
from peewee import *
import json
import sys

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
# 	newCourse = Course(Department = course['sub'], Number = course['number'], JsonID = course['id'])
# 	newCourse.save()
	# course['majorlimit']
	# course['levellimit']

	# course['semester']
	# course['gearea']
	# course['units']
	# course['label']
for course in Course.select().where(Course.Department=='ANTH'):
	print("{} {}".format(course.Department,course.Number),end='           ')
	#sleep(1)
# from datetime import date
# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
# uncle_bob.save() # bob is now stored in the database

# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
# grandma.name = 'Grandma L.'
# grandma.save()  # Update grandma's name in the database.



