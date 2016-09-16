from tika import parser
# text = parser.from_file('pdf/Phys/Physics-BS_2016.pdf')


import os
for dept in os.listdir('pdf'):
    # callthecommandhere(blablahbla, filename, foo)
    print(dept,"\n")
    for major in os.listdir('pdf/'+dept):
    	print(major)