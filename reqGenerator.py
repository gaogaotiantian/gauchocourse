#!/usr/bin/python

import MySQLdb
import json
import sys

#create database UCSB;
class dbInterface:
	def __init__(self,jsonFile):
		self.courseList = string2Json(jsonFile) 
		pass
		
	def main(self):
		self.dbConnect()
		self.dbCreate()
		
		# disconnect from server
		self.db.close()

	def dbConnect(self):
		# jsonList = string2Json(ifile)
		# Open database connection

		# Please change username and password accordingly
		self.db = MySQLdb.connect("localhost","saber","12345","UCSB")

		# prepare a cursor object using cursor() method
		self.cursor = self.db.cursor()

		# execute SQL query using execute() method.
		self.cursor.execute("SELECT VERSION()")

		# Fetch a single row using fetchone() method.
		data = self.cursor.fetchone()

		print "Database version : %s " % data

		#dbCreate(cursor)

		sql = """INSERT INTO Course(Department,
				ID)
			 VALUES ('Anth', '2')"""
		# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
		#        LAST_NAME, AGE, SEX, INCOME) \
		#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
		#        ('Mac', 'Mohan', 20, 'M', 2000)
		# print sql




		# disconnect from server
		#self.db.close()
		# CREATE USER 'saber'@'localhost' IDENTIFIED BY '12345
		# GRANT ALL PRIVILEGES ON * . * TO 'saber'@'localhost';


		# SET PASSWORD FOR 'saber'@'localhost' = PASSWORD('12345'); 

		# FLUSH PRIVILEGES;
	def dbInsert(self):
		try:
			# Execute the SQL command
			self.cursor.execute(sql)
			# data = cursor.fetchall()
			# Commit your changes in the database
			self.db.commit()
			data = self.cursor.fetchall()
			print data
		except:
			# Rollback in case there is any error
			self.db.rollback()
			#print "Insertion Failed!"
			data = self.cursor.fetchall()
			print data

	def dbCreate(self):
		try:
			# Create table
			sql = """CREATE TABLE Course (
					 Department  CHAR(20) NOT NULL,
					 ID  CHAR(20)   NOT NULL
											)"""

			self.cursor.execute(sql)
			data = self.cursor.fetchall()
			print data
		except:
			print 'table already exist'
			pass
	
def string2Json(ifile):
	jsonStr = open(ifile,'rt').read()
	jsonList = json.loads(jsonStr)
	return jsonList
	#major = jsonList[0]['sub']
	#print major
	# for course in 
	# courseList = []
	#print json.dumps(jsonObj, indent=4, separators=(',', ':')).keys()
	#json.dumps(jsonObj, indent=4, separators=(',', ':'))

# db = dbInterface()
# db.dbConnect()

if (len(sys.argv) != 2):
	print("Error: Invalid Filename")
else:
	db = dbInterface(sys.argv[1])#,sys.argv[2])
	db.main()
