import ssl
import http.client
import urllib.parse
import gzip
import time
def string2headers(s):
    pos = 0
    res = "{"
    while(pos<len(s)):
        foo = "\""
        while(s[pos]!=":"):
            if s[pos]!=' ':
                foo+=s[pos]
            pos+=1
        foo+="\""
        res+=foo+":"
        pos+=1
        foo = "\""
        while(pos<len(s) and s[pos]!="\n"):
            if s[pos]!=' ':
                foo+=s[pos]
            pos+=1
        foo+="\""
        res+=foo
        pos+=1
        if pos!=len(s):
            res+=",\n"
    res+= "}"
    return res


##################################################
header_text = open("headers.txt").read()
headers = eval(string2headers(header_text))
body_text = open("body.txt").read()
body = eval(string2headers(body_text))
course_key = "ctl00$pageContent$courseList"
quarter_key = "ctl00$pageContent$quarterList"
host = "my.sa.ucsb.edu"
url = "/Public/curriculum/courseSearch.aspx"

####################################################
#reading course and quarters
courses = []
quarters = []
f = open("courses.txt","r")
for line in f:
    courses.append(line)
    if courses[-1][-1] == "\n":
        courses[-1] = courses[-1][:-1]
f.close()
f = open("quarters.txt","r")
for line in f:
    quarters.append(line)
    if quarters[-1][-1]=="\n":
        quarters[-1] = quarters[-1][:-1]
f.close()


##################################################

def single_page(course,quarter):
    while(1):
        try:
            client = http.client.HTTPSConnection(host)
            client.connect()
            '''
            client.request("GET",url)
            res = client.getresponse()
            '''
            

            ############################
            body[quarter_key] = quarter
            body[course_key] = course
            #print(body)
            data = urllib.parse.urlencode(body)
            client.request("POST",url,data,headers)
            res = client.getresponse()
            #print(res.getheaders())
            raw_codes = res.read()
            html = gzip.decompress(raw_codes)
            html = html.decode("utf-8")
            ##################################
            filepath = "./raw_data/"+course+"_"+quarter+".html"
            f = open(filepath,"w+")
            f.write(html)
            f.close()
            client.close()
            time.sleep(0.1)
            break
            ###############################

            
        except:
            print(raw_codes)
            print("error when reading this page!!!skipping!")
            break

def run():
    for quarter in quarters:
        for course in courses:
            print()
            print("course=",course)
            print("quarter=",quarter)
            print()
            single_page(course,quarter)


single_page("EEMB","20153")










client = http.client.HTTPSConnection(host)
client.connect()
client.request("GET",url)
res = client.getresponse()







