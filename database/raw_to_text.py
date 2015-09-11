# -*- coding: utf-8 -*-
import re
import json
import os

class RegexContainer:
    def __init__(self):
        self.contHead = ""
        self.contTail = ""
        self.tdids    = []
        self.subs     = []
        self.subNum   = 0
    def AddContainHead(self, contHead):
        self.contHead = contHead
    def AddContainTail(self, contTail):
        self.contTail = contTail
    def AddTdId(self, tdid):
        self.tdids.append(tdid);
    def AddSub(self, sub):
        self.subs.append(sub)
    def GetRegex(self):
        regstr = self.contHead + r".*?"
        for sub in self.subs:
            if (sub[0] == "subject") :
                regstr += sub[1]
                regstr += r'.*?<span.*?>(.*?)</span>.*?'
            elif (sub[0] == "tdid") :
                regstr += sub[1]
                regstr += r'.*?>(.*?)<.*?'
        regstr += self.contTail
        reg = re.compile(regstr, re.MULTILINE | re.DOTALL)
        return reg
                    
def ReadPage(pageFolder, pageName):
    pageData = []
    try:
        f = open(pageFolder + pageName)
    except:
        print "file does not exist: " + pageFolder + pageName
        exit(1);
    rawHtml = f.read()
    regCont = RegexContainer()
    regCont.AddContainHead(r'class="CourseInfoRow"')
    regCont.AddSub(("tdid", "CourseTitle"))
    regCont.AddSub(("subject", "Full Title"))
    regCont.AddSub(("subject", "PreRequisite"))
    regCont.AddSub(("subject", "Units"))
    regCont.AddSub(("subject", "Level-Limit"))
    regCont.AddSub(("subject", "Major-Limit-Pass"))
    regCont.AddSub(("subject", "Major-Limit"))
    regCont.AddContainTail(r'</tr>')
    prog = regCont.GetRegex()
    it = prog.finditer(rawHtml)
    lastData = None
    for match in it:
        subNum = 1
        courseData = {}
        for sub in regCont.subs:
            courseData[sub[1]] = " ".join(match.group(subNum).split())
            subNum += 1
        if lastData is None or courseData["CourseTitle"] != lastData["CourseTitle"]:
            pageData.append(courseData)
            lastData = courseData
    f.close()
    try:
        filename = pageName.split(".")[0] + ".json"
        f = open("./json_raw_data/" + filename, "w")
    except:
        print "error when open file to write!"
        exit(1);
    f.write(json.dumps(pageData, indent = 4, separators=(',', ':'), encoding = "latin-1", ensure_ascii=False).encode("utf-8"))
    f.close()
def ReadAll(folderPath):
    for subdir, dirs, files in os.walk(folderPath):
        for f in files:
            print f
            ReadPage(folderPath, f)
if __name__ == "__main__":
    ReadAll("../raw_data/")
#ReadPage("../raw_data/", "FR_20134.html")
