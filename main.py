
from urllib.request import urlopen, urlretrieve
import json


def mapMachine():
    urlBase = "https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=FLPiXUAqjSQsAzY0gBc2YvXYIGwPWbEy"
    stringResultFromNYT = urlopen(urlBase).read().decode('utf8')
    jsonResult = json.loads(stringResultFromNYT)
    with open("data_file.json", "w") as write_file:
        json.dump(jsonResult, write_file)
    print(jsonResult)


#def testFile(input):
    #fileStream = open("text.txt", encoding='utf-8')
    #fileStream.write("hello")


mapMachine()
