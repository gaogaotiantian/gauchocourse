import re

f = open("course_html.txt","r")
html = f.read()
f.close()
f = open("expr.txt","r")
expr = f.read()
expr = re.compile(expr)
f.close()
matched = re.findall(expr,html)
expr2 = "value=\".*\""


res = []
for string in matched:
        sl = re.findall(expr2,string)
        if sl==0:
            print("no value this line")
            continue
        else:
            s = sl[0]
            s = s[len('value="'):-1]
            res.append(s)


f = open("subjects_and_quaters.txt","w+")
for item in res:
    f.write(item)
f.close()
    
