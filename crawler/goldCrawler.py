import re
import requests
import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import sys


headers={
	#'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	#'Accept-Encoding':'gzip, deflate, br',
	#'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
	#'Cache-Control':'max-age=0',
	#'Connection':'keep-alive',
	#'Content-Length':'1238',
	#'Content-Type':'application/x-www-form-urlencoded',
	#'Cookie':'instructor=false; enrollcode=false; restrictions=false; prerequisites=false; ARRAffinity_my.sa.ucsb.edu_gold=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; ARRAffinity_my.sa.ucsb.edu_bulletins=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ARRAffinity_my.sa.ucsb.edu=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ASP.NET_SessionId=ao0g4hhmtlesymcoufy4emlu; ARRAffinity_my.sa.ucsb.edu_public=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; _gat=1; GOLDCookie=GOLDCookie; GOLD=9D02EAF2648BB0A014CEEF4E5CE008A461570ACE8A6ACBD9A67E484F42DB42EAC780AB490C538DC482A05E775CA8E186198A285D89CD97400DE617D0E095C381C6C36E1BEFD4C99A3CC0AB2F25A8B5DDE53275B92A659FFBB4EFD862A9AC464F157801CA47C60C631C2A3CAD0A3D2C81788E0EE327A7407E0883B2227A4C49748D26C699BFF87DF978D9A3D8B30414976BF60FB0F5C862E8FE714248B61214CD; _ga=GA1.2.315646158.1471969562',
	#'Host':'my.sa.ucsb.edu',
	#'Origin':'https://my.sa.ucsb.edu',
	#'Referer':'https://my.sa.ucsb.edu/gold/Login.aspx',
	#'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

data = {
	'__LASTFOCUS':'',
	'__VIEWSTATE':'/wEPDwUKMjA3NzgzODY0OA9kFgJmD2QWAgIHD2QWAgIDD2QWDgIBDxYCHgRUZXh0BTc8bGluayByZWw9c3R5bGVzaGVldCBocmVmPSJTdHlsZXMuY3NzIiB0eXBlPSJ0ZXh0L2NzcyI+ZAIDDw8WAh4HVmlzaWJsZWhkZAIEDw9kFgIeDGF1dG9jb21wbGV0ZQUDb2ZmZAIFDw9kFgIfAgUDb2ZmZAIHD2QWAmYPZBYEAgEPDxYCHwFoZGQCBw8WAh8BaGQCCA8PFgIeC05hdmlnYXRlVXJsBS0vL215LnNhLnVjc2IuZWR1L1Blcm1QaW5SZXNldC9Gb3Jnb3RQZXJtLmFzcHhkZAIJDw8WAh8DBS8vL215LnNhLnVjc2IuZWR1L1Blcm1QaW5SZXNldC9QZXJtUGluUmVzZXQuYXNweGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBR1jdGwwMCRwYWdlQ29udGVudCRsb2dpbkJ1dHRvbgUqY3RsMDAkcGFnZUNvbnRlbnQkUGVybVBpbkxvZ2luJGxvZ2luQnV0dG9uDC6OlbzK6/cctnHk3sej8bxmhXo0rNjNCWErIw2EbAI=',
	#'__VIEWSTATEGENERATOR':'00732C32',
	'__EVENTTARGET':'',
	'__EVENTARGUMENT':'',
	'__EVENTVALIDATION':'/wEdAAfmGS0z6nIxsitOtZIFr7Z1FPojxflIGl2QR/+/4M+LrK6wLDfR+5jffPpLqn7oL3ttZruIm/YRHYjEOQyILgzL2Nu6XIik3f0iXq7Wqnb39/ZNiE/A9ySfq7gBhQx160NmmrEFpfb3YUvL+k7EbVnKRmxlXL+8IKdF1sVp2ea8DS+4mKJd3qLsz+LbLdoUzeQ=',
	'ctl00$pageContent$loginButton.x':'79',
	'ctl00$pageContent$loginButton.y':'14',
	'ctl00$pageContent$PermPinLogin$userNameText':'',
	'ctl00$pageContent$PermPinLogin$passwordText':''
}

host = "my.sa.ucsb.edu"
login_url='https://my.sa.ucsb.edu/gold/Login.aspx'
home_url='https://my.sa.ucsb.edu/gold/Home.aspx'



def getCourseHistoryFromGOLD(username,password):
	sess=requests.session()
	response = sess.get(login_url,headers=headers)
	hiddenVal = get_hiddenvalue(response.text)

	# print hiddenVal
	data['__VIEWSTATE'] = hiddenVal[0]
	data['__EVENTVALIDATION'] = hiddenVal[1]
	data['ctl00$pageContent$userNameText']= username
	data['ctl00$pageContent$passwordText'] = password
	# login
	response = sess.post(login_url,headers=headers, data=data)
	# print response.headers#.decode('utf8')
	# print response.headers
	grades_url = 'https://my.sa.ucsb.edu/gold/StudentGrades.aspx'
	# headers['']
	#login_data = urllib.urlencode()#{'username' : username, 'j_password' : password})

	#resp = opener.open('http://www.example.com/hiddenpage.php')

	#print cj

	#hiddenVal = get_hiddenvalue(response.text)

	grade_data = data

	del grade_data['ctl00$pageContent$userNameText']
	del grade_data['ctl00$pageContent$passwordText']
	del grade_data['ctl00$pageContent$loginButton.x']
	del grade_data['ctl00$pageContent$loginButton.y']
	del grade_data['ctl00$pageContent$PermPinLogin$userNameText']
	del grade_data['ctl00$pageContent$PermPinLogin$passwordText']

	headers['Referer'] = home_url

	# print headers
	# print 
	# print
	# print grade_data
	# print
	# print
	#response = sess.get(grades_url,headers=headers,data = grade_data)
	#print response.text
	#hiddenVal = get_hiddenvalue(response.text)
	#grade_data['__VIEWSTATE'] = hiddenVal[0]
	#grade_data['__EVENTVALIDATION'] = hiddenVal[1]


	response = sess.post(grades_url,headers=headers, data=grade_data)

	VIEWSTATE = re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', response.text,re.I)
	VIEWSTATEGENERATOR = re.findall(r'<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />', response.text,re.I)
	#print VIEWSTATEGENERATOR

	# headers['__VIEWSTATEGENERATOR'] = VIEWSTATEGENERATOR[0]
	headers['Referer'] = grades_url
	headers['Host']='my.sa.ucsb.edu'
	grade_data['__EVENTTARGET'] = 'ctl00$pageContent$quarterDropDown'
	grade_data['ctl00$pageContent$quarterDropDown'] = 'ALL'
	grade_data['__VIEWSTATE'] = VIEWSTATE[0]

	response = sess.post(grades_url,headers=headers, data=grade_data)
	# print response.headers
	#hiddenval = get_hiddenvalue(response.text)
	#print hiddenVal
	#reponse = sess.post(grades_url,headers)

	rawGradesByQuarter = response.text
	print parseHistory(rawGradesByQuarter)
	return


# import re

def parseHistory(html):
	#history = open(ifile,"r").read()
	#print history
	#print re.findall(r'<table id(.*?)<td>', history, re.M)
	soup = BeautifulSoup(html,"lxml")
	courseTextList = []
	for ele in soup.find_all(class_="datatable"):
		courseTextList.append(ele)

	courseByQuarter = []

	# raw = re.findall(r'width="225"(.*?)-',str(courseTextList[0]))
	# print raw[0]
	# print re.sub(' +',' ',raw[0])[5:]
	for i in range(len(courseTextList)):
		rawCourseOneQuarter = re.findall(r'width="225"(.*?)-',str(courseTextList[i]))
		if rawCourseOneQuarter == []:
			pass
		else:
			courseThisQuarter = []
			for course in rawCourseOneQuarter:
				courseThisQuarter.append(re.sub(' +',' ',course)[5:])#[17:])
			courseByQuarter.append(courseThisQuarter)

	return courseByQuarter

	#print len(courseTextList)
	# for courseIndex in range(len(courseTextList):
	# 	courseTextList[courseIndex]#.find_all(class_="")
	#print re.findall(r'<table cellspacing="0" class="datatable" id="pageContent_quarterGrid_gradesByQuarter_(.*?)</td>\n</tr>\n</table>\n</td>\n</tr>\n<tr>\n<td>', soup)
	#print soup
# ="pageContent_quarterGrid_gradesByQuarter
#parseHistory('out.html')


def get_hiddenvalue(html):
    VIEWSTATE =re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', html,re.I)
    EVENTVALIDATION =re.findall(r'input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />', html,re.I)
    return VIEWSTATE[0],EVENTVALIDATION[0]

if (len(sys.argv) != 3):
	print("Error: Invalid Filename, Expecting username and password")
else:
	getCourseHistoryFromGOLD(sys.argv[1],sys.argv[2])

















#print re.findall(r'<table id="pageContent_quarterGrid_gradesByQuarter(.*?)"/>"', rawGradesByQuarter, re.I)




# # import requests
# import ssl
# import http.client
# import urllib.request
# import urllib.parse
# #import urllib.parse
# import gzip
# import requests
# from lxml import html
# # headers = {
# #     'Referer':'https://my.sa.ucsb.edu/gold/Logout.aspx',
# #     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
# #     'Cookie':'instructor=false; enrollcode=false; restrictions=false; prerequisites=false; ARRAffinity_my.sa.ucsb.edu_gold=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; ARRAffinity_my.sa.ucsb.edu_bulletins=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ARRAffinity_my.sa.ucsb.edu=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ASP.NET_SessionId=ao0g4hhmtlesymcoufy4emlu; ARRAffinity_my.sa.ucsb.edu_public=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; GOLDCookie=GOLDCookie; GOLD=701834A1B62F516DB19D9F2019BCC031900953C6921FD3E51F2F2D3F9C47D3C504291E7415F8CB212033C3C040B693DAFE946909CD9D848A15460E3192C9AB56DC10BEF08FAE489CD323107718DD931260C5F1BE40754800C984665D36D52DDBEB54C1FCD08AF661A25B1215C05B49F6686585175876F7B01219D127E565A544F39B5254885DFC0CC1FA09CB98179159E62A077A2344263008DB0C3A6AB2AB3F; _gat=1; _ga=GA1.2.315646158.1471969562'
# # }
# # url='https://my.sa.ucsb.edu/gold/Login.aspx'
# # print(requests.get(url=url,headers=headers).text)



# sess=requests.session()
# result = sess.get(login_url)



# headers = {
#     'Referer':'https://my.sa.ucsb.edu/gold/Login.aspx',
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
#     'Cookie':'instructor=false; enrollcode=false; restrictions=false; prerequisites=false; ARRAffinity_my.sa.ucsb.edu_gold=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; ARRAffinity_my.sa.ucsb.edu_bulletins=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ARRAffinity_my.sa.ucsb.edu=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ASP.NET_SessionId=ao0g4hhmtlesymcoufy4emlu; ARRAffinity_my.sa.ucsb.edu_public=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; GOLDCookie=GOLDCookie; GOLD=701834A1B62F516DB19D9F2019BCC031900953C6921FD3E51F2F2D3F9C47D3C504291E7415F8CB212033C3C040B693DAFE946909CD9D848A15460E3192C9AB56DC10BEF08FAE489CD323107718DD931260C5F1BE40754800C984665D36D52DDBEB54C1FCD08AF661A25B1215C05B49F6686585175876F7B01219D127E565A544F39B5254885DFC0CC1FA09CB98179159E62A077A2344263008DB0C3A6AB2AB3F; _gat=1; _ga=GA1.2.315646158.1471969562'
# }

# #data = urllib.parse.urlencode(values)
# result = sess.post(url=login_url,data=values,headers=headers)
# print(sess.get(url=home_url,headers=headers).text)
#req = urllib.request.Request(url,data.encode('UTF-8'),headers)
#response = urllib.request.urlopen(req)
#print(response.read())


#print(client.getresponse())
# client.request("POST",url,data,headers)
# response = client.getresponse()
# raw_codes = response.read()
# html = gzip.decompress(raw_codes)
# html = html.decode("utf-8")

# print(html)

#req = sess.post(url=url,headers=headers,data=data)
#print(req.text)
# try to get cookie
#s=requests.session()
#s.get('https://my.sa.ucsb.edu/gold/Logout.aspx')

#r=s.get(url=url,headers=headers)
#print(r.json()['respose'])
#coding=utf-8
# import requests
# headers={
#     'Cookie':'sagree=true; selected_nc=ch; JSESSIONID=1BC521B3AC3AA3A548A40B93DD3D12EA',
#     'Referer':'http://www.simsimi.com/talk.htm?lc=ch',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1485.0 Safari/537.36'
#     }
# msg="lol"
# url ='http://www.simsimi.com/func/req?msg=%s&lc=ch'%msg
# r=requests.get(url=url,headers=headers)
# print r.json()['response']

# 'Cookie':'instructor=false; enrollcode=false; restrictions=false; prerequisites=false; ARRAffinity_my.sa.ucsb.edu_gold=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; ARRAffinity_my.sa.ucsb.edu_bulletins=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ARRAffinity_my.sa.ucsb.edu=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ASP.NET_SessionId=ao0g4hhmtlesymcoufy4emlu; ARRAffinity_my.sa.ucsb.edu_public=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; GOLDCookie=GOLDCookie; GOLD=701834A1B62F516DB19D9F2019BCC031900953C6921FD3E51F2F2D3F9C47D3C504291E7415F8CB212033C3C040B693DAFE946909CD9D848A15460E3192C9AB56DC10BEF08FAE489CD323107718DD931260C5F1BE40754800C984665D36D52DDBEB54C1FCD08AF661A25B1215C05B49F6686585175876F7B01219D127E565A544F39B5254885DFC0CC1FA09CB98179159E62A077A2344263008DB0C3A6AB2AB3F; _gat=1; _ga=GA1.2.315646158.1471969562'
#import urllib, urllib2, cookielib



# headers={
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
# 'Cache-Control':'max-age=0',
# 'Connection':'keep-alive',
# 'Content-Length':'1238',
# 'Content-Type':'application/x-www-form-urlencoded',
# 'Cookie':'instructor=false; enrollcode=false; restrictions=false; prerequisites=false; ARRAffinity_my.sa.ucsb.edu_gold=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; ARRAffinity_my.sa.ucsb.edu_bulletins=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ARRAffinity_my.sa.ucsb.edu=e6a176fe5c411eaa4113d69b47118138f317ef9a40aea74d0501a313e8815fc8; ASP.NET_SessionId=ao0g4hhmtlesymcoufy4emlu; ARRAffinity_my.sa.ucsb.edu_public=808a8a15a4d8ae50e1724b76589ebdbad90cf5166124de5fa0c1c500e95f66fe; _gat=1; GOLDCookie=GOLDCookie; GOLD=9D02EAF2648BB0A014CEEF4E5CE008A461570ACE8A6ACBD9A67E484F42DB42EAC780AB490C538DC482A05E775CA8E186198A285D89CD97400DE617D0E095C381C6C36E1BEFD4C99A3CC0AB2F25A8B5DDE53275B92A659FFBB4EFD862A9AC464F157801CA47C60C631C2A3CAD0A3D2C81788E0EE327A7407E0883B2227A4C49748D26C699BFF87DF978D9A3D8B30414976BF60FB0F5C862E8FE714248B61214CD; _ga=GA1.2.315646158.1471969562',
# 'Host':'my.sa.ucsb.edu',
# 'Origin':'https://my.sa.ucsb.edu',
# 'Referer':'https://my.sa.ucsb.edu/gold/Login.aspx',
# 'Upgrade-Insecure-Requests':'1',
# 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }


# import requests
# import cookielib

# sess = requests.session()

# cookie=cookielib.CookieJar()
# request = sess.get(login_url,cookies=cookie)
# print request.text
# print cookie

# import urllib, urllib2, cookielib
# import httplib
# httplib.HTTPConnection.debuglevel = 1
# #client = http.client.HTTPSConnection(host)
# #client.connect()
# request = urllib2.Request(login_url)
# opener = urllib2.build_opener()
# feeddata = opener.open(request).read()
# print feeddata
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# login_data = urllib.urlencode(data)
# #print headers.items()
# opener.add_headers = headers.items()
# opener.open(login_url,login_data)
# resp = opener.open(login_url)
# print resp.read()













# data = urllib.parse.urlencode(data)
# print(type(data))
# request = urllib.request.Request(login_url,data.encode("utf-8"),headers)
# response = urllib.request.urlopen(request)

# print (response)
#client.request("POST",login_url,data,headers)
#print (client)
# response = client.getresponse()
# raw_codes=res.read()
# html = gzip.decompress(raw_codes)
# html=html.decod("utf-8")
