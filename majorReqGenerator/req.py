import re
class MajorReqParser(object):
	def __init__(self):
		pass

	def ParseOneMajor(self,path):
		reqTXT = open(path,'rt').read()
		reqTXT = reqTXT.split('UNITS YET TO COMPLETE')[1]
		reqTXT = reqTXT.split('Elective courses taken')[0]
		reqTXTList = re.split(r'\n',reqTXT)

		UDUnitsPatt = re.compile(r'([0-9]+) UD units are required') # delete UD Units requirement
		noNumPatt = re.compile(r'[0-9]+')							# delete line that lack course numbers
		whiteSpacePatt = re.compile(r'\w+')							# delete blank lines
		shrinkDotsPatt = re.compile(r'\.+')							# replace dots with swirl
		NOTEPatt = re.compile(r'NOTE',re.I)							# delete line that contain "Note"
		replaceStar = re.compile(r'\*')

		delIndexList = []
		for i in range(len(reqTXTList)):
			UDUnits = re.search(UDUnitsPatt,reqTXTList[i])
			noNum = re.search(noNumPatt,reqTXTList[i])
			notBlank = re.search(whiteSpacePatt,reqTXTList[i])
			note = re.search(NOTEPatt,reqTXTList[i])

			if UDUnits != None:
				# self.UDUnits = UDUnits.group()[0:2]
				delIndexList.append(i)
			if noNum == None:
				# print(reqTXTList[i])
				delIndexList.append(i)
			# if notBlank == None:
			# 	# print(i)
			# 	delIndexList.append(i)
			if note != None:
				# print(i)
				delIndexList.append(i)



		# http://stackoverflow.com/questions/18837607/remove-multiple-items-from-list-in-python
		reqList = [v for i, v in enumerate(reqTXTList) if i not in delIndexList]

		for j in range(len(reqList)):
			reqList[j] = shrinkDotsPatt.sub('~',reqList[j])
			reqList[j] = replaceStar.sub('',reqList[j])
		# for index in sorted(delIndexList,reverse=True):
		# 	del reqTXTList[index]
		# print(self.UDUnits,end="\n\n")


		for line in reqList:
			print(line)
		print('\n\n\n\n')
		return reqList


















parser = MajorReqParser()
# print(parser.ParseOneMajor('txt/Math/Mathematics-BS-2016.txt'))
print(parser.ParseOneMajor('txt/Phys/Physics-BS_2016.txt'))

# python3 req.py
		