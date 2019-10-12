
from urllib.request import urlopen, urlretrieve
import json


def mapMachine():
    urlBase = "https://api.nytimes.com/svc/archive/v1/2018/1.json?api-key=FLPiXUAqjSQsAzY0gBc2YvXYIGwPWbEy"
    stringResultFromNYT = urlopen(urlBase).read().decode('utf8')
    jsonResult = json.loads(stringResultFromNYT)
    resultSize = jsonResult["response"]["meta"]["hits"]
    i = 0
    titles = []
    words = {}
    while i < resultSize:
        titles.append(jsonResult["response"]["docs"][i]["headline"]["print_headline"])
        i = i + 1

    for title in titles:
        if title not in ["None", " ", None]:
            for word in title.split():
                if word not in ["a"]:
                    if word in words:
                        words[word] = words[word] + 1
                    else:
                        words[word] = 1
    print(words)






#def testFile(input):
    #fileStream = open("text.txt", encoding='utf-8')
    #fileStream.write("hello")


mapMachine()
