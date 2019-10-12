
from urllib.request import urlopen, urlretrieve
import json
import time


def mapMachine(year, month, key):
    urlBase = "https://api.nytimes.com/svc/archive/v1/" + year + "/" + month + ".json?api-key=" + key
    stringResultFromNYT = urlopen(urlBase).read().decode('utf8')
    jsonResult = json.loads(stringResultFromNYT)
    resultSize = jsonResult["response"]["meta"]["hits"]
    i = 0
    titles = []
    words = {}
    words_to_ignore = ["his", "was", "a.", "c.", "i", "n.", "first", "plan", "set", "miss", "‐‐", "city","—", "n" , "has", "not", "that", "a", " ", "the", "and", "on", "title", "new", "of", "with", "for", "to", "in", "at", "by", "is", "will", "be", "says", "know", "no", "as", "from", "", "are", "york", "here", "he", "but", "up", "two", "2", "mrs", "u.", "s." , "mrs.", "3", "1", "4", "--", "an", "|", "6", "7", "8", ]
    with open("data_file.json", "w") as write_file:
        json.dump(jsonResult, write_file)
    while i < resultSize:
        #print(i)
        if ("main") in jsonResult["response"]["docs"][i]["headline"]:
            titles.append(jsonResult["response"]["docs"][i]["headline"]["main"])
        i = i + 1

    for title in titles:
        if title not in ["None", " ", None]:
            for word in title.split():
                word = word.lower().strip(");:{-}[]()!@'#$%^&*?/,<>")
                if word not in words_to_ignore:
                    if word in words:
                        words[word] = words[word] + 1
                    else:
                        words[word] = 1
    sortedWords = sorted(words.items(), key=lambda x: x[1], reverse=True)
    print(sortedWords)
    print(sortedWords[0])

def dataGetter(year, month, iterations = 25, jump_size = 1):
    i = 0
    key1 = "FLPiXUAqjSQsAzY0gBc2YvXYIGwPWbEy"
    key2 = "kkTOXQGned4gaefoipGgrVnQjclgdhPp"
    key3 = "lXFbtGN6XLAQw8AGvVTMNZ205PmIrxk1"

    keys = [key1, key2, key3]
    while i < iterations:
        mapMachine(str(i), "1", str(keys[i % 3]))
        time.sleep(.0001)
        year = year + month//12
        month = month + jump_size
        month = month % 12
        i = i + 1








#def testFile(input):
    #fileStream = open("text.txt", encoding='utf-8')
    #fileStream.write("hello")


test()
