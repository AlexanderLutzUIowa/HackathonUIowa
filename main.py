
from urllib.request import urlopen, urlretrieve
import json


def mapMachine():
    urlBase = "https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=FLPiXUAqjSQsAzY0gBc2YvXYIGwPWbEy"
    stringResultFromNYT = urlopen(urlBase).read().decode('utf8')
    jsonResult = json.loads(stringResultFromNYT)
    print(jsonResult)

mapMachine()
