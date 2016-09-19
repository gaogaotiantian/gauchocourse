from tika import parser
# text = parser.from_file('pdf/Phys/Physics-BS_2016.pdf')

import os

WCD = os.getcwd()

def makeNewDirIfNecessary(relativePath):
	absPath = WCD + '/' + relativePath
	try: 
	    os.makedirs(absPath)
	except OSError:
	    if not os.path.isdir(absPath):
	        raise
	return

for dept in os.listdir('pdf'):
    for major in os.listdir('pdf/'+dept):
    	pdfPath = 'pdf/'+ dept + '/'+ major
    	txtDir = 'txt/' + dept
    	txtPath = 'txt' + pdfPath[3:-4] + '.txt'
    	print(txtPath)
    	makeNewDirIfNecessary(txtDir)
    	newTXT = open(txtPath,'wt')
    	newTXT.write(parser.from_file(pdfPath)['content'])
    	newTXT.close()

# python pdf2txt.py