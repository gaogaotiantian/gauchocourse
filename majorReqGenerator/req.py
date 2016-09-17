import re
import json

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

    # change the format of a course to the desired format
    # e.g. math 8 -> MATH 8
    def formatCourse(self,courseStrList):
        if self.isValid(courseStrList):
            return [self.map2Abrrev(courseStrList[0]),str(courseStrList[1]).upper()]
        else:
            print('This course is invalid!')
            return None

class MajorReqParser(object):
	def __init__(self):
	    self.delList = ['with', 'an', 'average', 'grade', 'of', '~70~','One','course']
	    self.dept2AbbrevMap = dept2AbbrevMap()
	    self.paranPatt = re.compile(r'\((.*)\)')
	    self.noneParanPatt = re.compile(r'(.*)\(.*\)(\w)?')
	    self.orPatt = re.compile(r'or',re.I)
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
		print(reqTXT)
		UDUnitsPatt = re.compile(r'([0-9]+) UD units are required') # delete UD Units requirement
		noNumPatt = re.compile(r'[0-9]+')							# delete line that lack course numbers
		whiteSpacePatt = re.compile(r'\w+')							# delete blank lines
		shrinkDotsPatt = re.compile(r'[^A-Z]\.+')							# replace dots with swirl
		NOTEPatt = re.compile(r'NOTE',re.I)							# delete line that contain "Note"
		replaceStar = re.compile(r'\*')
		endWith2WhiteSpacePatt = re.compile(r'\s\s$')
		delParanPatt = re.compile(r'[\(\)]')
		

		delIndexList = []
		for i in range(len(reqTXTList)):
			UDUnits = re.search(UDUnitsPatt,reqTXTList[i])
			noNum = re.search(noNumPatt,reqTXTList[i])
			notBlank = re.search(whiteSpacePatt,reqTXTList[i])
			note = re.search(NOTEPatt,reqTXTList[i])
			validLine = re.search(endWith2WhiteSpacePatt,reqTXTList[i])

			# most of the irrelevant line could be filtered by 'validLine'
			if validLine == None:
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

		# for i in delIndexList:
		# 	print("DEL: ",i , reqTXTList[i])

		# http://stackoverflow.com/questions/18837607/remove-multiple-items-from-list-in-python
		reqList = [v for i, v in enumerate(reqTXTList) if i not in delIndexList]
		print(reqList)

		print('First:\n')
		
		for j in range(len(reqList)):
			reqList[j] = shrinkDotsPatt.sub('~',reqList[j])
			reqList[j] = replaceStar.sub('',reqList[j])
			reqList[j] = reqList[j].strip()
			# reqList[j] = delParanPatt.sub('',reqList[j])
		# for index in sorted(delIndexList,reverse=True):
		# 	del reqTXTList[index]
		# print(self.UDUnits,end="\n\n")


		for line in reqList:
			print(line)
		print('\n\n\n\n')
		# return reqList
		self.reqList = reqList


	def ParseOneMajor2nd(self,path=""):
		parsedReqs = []

		courseNumPatt = re.compile(r'[0-9]+[A-Z]+-[A-Z]+-[A-Z]+|[0-9]+[A-Z]+-[A-Z]+')
		for i in range(len(self.reqList)):
			temp = re.split(r'[A-Z]\.\s+',self.reqList[i])
			if len(temp) != 2:
				self.reqList[i] = temp[0]
			else:
				self.reqList[i] = temp[1]
			self.reqList[i] = self.reqList[i].split()

			delIndexList = []
			for index in range(len(self.reqList[i])):
				# print(index)
				if self.reqList[i][index] in self.delList:
					delIndexList.append(index)
					# print(index)
			oneLine = [v for i, v in enumerate(self.reqList[i]) if i not in delIndexList]
			for j in range(len(oneLine)):
				oneLine[j] = oneLine[j].replace('~','')
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
		# for ithLine in range(len(self.reqList)):
		# 	lineOfReq = []
		# 	for jthWord in range(len(self.reqList[ithLine])):
		# 		majorIndex = 0
		# 		major = ''
		# 		abbrev = self.dept2AbbrevMap.map2Abrrev(self.reqList[ithLine][jthWord])
		# 		# if it's a department name
		# 		if abbrev!= 'not valid':
		# 			major = word
		# 			majorIndex = jthWord
		# 		# then if it's a course number
		# 		elif type(self.reqList[ithLine][jthWord][0]) == int:
		# 			lineOfReq.append([major,self.reqList[ithLine][jthWord][0]])
		# 		# it might be a word like "units", "following", "or"
		# 		else:
		# 			pass
		reqJoinList = []
		for line in self.reqList:
			reqJoinLine = ""
			for word in line:
				reqJoinLine += (word + ' ')
			reqJoinList.append(reqJoinLine)

		lineDictList = []
		for i in range(len(reqJoinList)):
			lineOfReqList = reqJoinList[i].rsplit(maxsplit=1)
			lineDictList.append({"course": lineOfReqList[0], "units": lineOfReqList[1]})

		for line in reqJoinList:
			print(line)


		print('\n\n\n\n')

		for lineDict in lineDictList:
			reqOfLine = self.RECParseOneLine(lineDict["course"])
			# print(reqOfLine)
		
		# s = "i love you (or not)."
		# result = re.search(self.paranPatt,s).group()
		# print('result: ',result)


		# for line in self.reqList:
			# print(line)
		print('\n\n\n\n')

	def RECParseOneLine(self,text):
		req = []
		print("Rec: ", text)
		subReqList = re.findall(self.paranPatt,text)


		# .group()
		if subReqList != []:
			print("Found paranthess!!!!")
			
			# Create a new string that has been extracted the info in the parathess
			# analyze the new string and combine the info with those course inside paranthess
			if len(subReqList) > 1:
				print('more than one pair of paranthess')
				raise IndexError
			noneParanText = re.sub(r'\(.*\)','',text)
			print("None Paran: ", noneParanText)

			noneParanList = []
			subSubReqList = []
			for reqInParan in subReqList:

				subSub = self.RECParseOneLine(reqInParan)
				# if subSub != None:
				subSubReqList.append(subSub)
			req.append(subSubReqList)
		else:
			req.append(self.ITERParseOneLine(text))
		return req
		
		# pass
	def ITERParseOneLine(self,text):
		print("Iter: ")

		return text

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
        # print(outList)
    return outList


# helper functions
def string2Json(ifile):
    jsonFile = open(ifile,'rt')
    jsonList = json.loads(jsonFile.read())
    jsonFile.close()
    return jsonList


# print(recoverCourseNum(['13AH','BH','CH']))
# print(recoverCourseNum(['3A','B']))


parser = MajorReqParser()
# parser.ParseOneMajor('txt/Math/Mathematics-BS-2016.txt')
# parser.ParseOneMajor('txt/Phys/Physics-BS_2016.txt')
# parser.ParseOneMajor('txt/Chem/Chemistry-BS_2016.txt')
parser.ParseOneMajor('txt/Math/Financial-Math-Stat-BS-2016.txt')
parser.ParseOneMajor2nd()
parser.ParseOneMajor3rd()
# for dept in os.listdir('pdf'):
#     for major in os.listdir('pdf/'+dept):
#     	pdfPath = 'pdf/'+ dept + '/'+ major
#     	txtDir = 'txt/' + dept
#     	txtPath = 'txt' + pdfPath[3:-4] + '.txt'
#     	print(txtPath)
#     	makeNewDirIfNecessary(txtDir)
#     	newTXT = open(txtPath,'wt')
#     	newTXT.write(parser.from_file(pdfPath)['content'])
#     	newTXT.close()





# python3 req.py
		