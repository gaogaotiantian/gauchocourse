from mako.template import Template
class WebData:
    def __init__(self):
        self.semester = ["summer", "fall", "winter", "spring"]
        self.year = ["freshman", "sophomore", "junior", "senior"]
        self.preNum = 2

if __name__ == "__main__":
    data = WebData()
    myTemp = Template(filename = "./index.html")
    with open("index_pre.html", "w") as fwrite:
        fwrite.write(myTemp.render(data = data))
