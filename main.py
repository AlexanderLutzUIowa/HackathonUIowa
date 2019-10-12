
from urllib.request import urlopen, urlretrieve
import json


def mapMachine():
    urlBase = "https://api.nytimes.com/svc/archive/v1/2016/1.json?api-key=FLPiXUAqjSQsAzY0gBc2YvXYIGwPWbEy"
    stringResultFromNYT = urlopen(urlBase).read().decode('utf8')
    jsonResult = json.loads(stringResultFromNYT)
    with open("data_file.json", "w") as write_file:
        json.dump(jsonResult, write_file)
    resultSize = jsonResult["response"]["meta"]["hits"]
    i = 0
    titles = []
    words = {}
    words_to_ignore = ["a"]
    with open("data_file.json", "w") as write_file:
        json.dump(jsonResult, write_file)
    while i < resultSize:
        print(i)
        if ("print_headline") in jsonResult["response"]["docs"][i]["headline"]:
            titles.append(jsonResult["response"]["docs"][i]["headline"]["print_headline"])
        i = i+1
    print(i)


    print("result size is ", resultSize)

    for title in titles:
        if title not in ["None", " ", None]:
            for word in title.split():
                word = word.lower()
                word1 = word.strip("?!'()-:")
                if word1 not in words_to_ignore:
                    if word1 in words:
                        words[word1] = words[word1] + 1
                    else:
                        words[word1] = 1

    sortedWords = sorted(words.items(), key=lambda x: x[1], reverse=True)
    print(sortedWords)
    print(sortedWords[0])







#def testFile(input):
    #fileStream = open("text.txt", encoding='utf-8')
    #fileStream.write("hello")


mapMachine()
