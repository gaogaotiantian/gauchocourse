import os
import re
COEPatt = re.compile(r'engr|ece',re.I)





class COEMajorReqParser():
    def __init__(self,txtPath):
        WCD = os.getcwd()
        txt = open(WCD+'/'+txtPath,'rt')
        # for line in txt:
        #   print(line)
        self.txt = txt.read()
        # lst = []
        # lst.append(self.txt)
        # print(lst)
        self.parsedTXT = self.txt
        txt.close()
        self.parser1st()
        pass

    def parser1st(self):
        geUselessPatt = re.compile(r'UNIVERSITY REQUIREMENTS.*General Education and Free Electives taken:',re.S)
        self.parsedTXT = self.parsedTXT.split('Courses required for the major')[0]
        self.parsedTXT = re.sub(geUselessPatt,'',self.parsedTXT)
        self.parsedTXT = self.parsedTXT.strip()
        self.required = self.parsedTXT.split('Major Field Electives')[0].split('\n')
        self.elective = self.parsedTXT.split('Major Field Electives')[1]
        noNumPatt = re.compile(r'[0-9]+')                           # delete line that lack course numbers

        # print(re.search(geUselessPatt,self.parsedTXT).group())
        # for part in self.elective:
        #     print(part)
        print(self.elective)
        print(self.required)
            # for line in part:
            #     print(line)
            #     line = re.sub(noNumPatt,'',line)
        # print(self.parsedTXT)
        # for line in self.parsedTXT:
        #     print(line)
        # print(self.parsedTXT)

# for dept in os.listdir('txt'):
#     for major in os.listdir('txt/'+ dept):
#         txtPath = 'txt/'+ dept + '/'+ major
#         # fileName = txtPath.rsplit('-',maxsplit=1)
#         # fileName = re.findall(deptNamePatt,txtPath)
#         # getType = txt
#         # txtDir = 'txt/' + dept
#         # txtPath = 'txt' + pdfPath[3:-4] + '.txt'
#         if re.search(COEPatt,txtPath) != None:
#           print(txtPath)
            # COEMajorReqParser(txtPath)        


# COEMajorReqParser('txt/ece/ece.txt')
COEMajorReqParser('txt/compsci-engr/compsci-engr.txt')