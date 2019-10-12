
from urllib.request import urlopen, urlretrieve



def mapMachine():
    urlBase = "https://api.nytimes.com/svc/archive/v1/2019/1.json?FLPiXUAqjSQsAzY0gBc2YvXYIGwPWbEy=yourkey"
    stringResultFromGoogle = urlopen(urlBase).read().decode('utf8')

mapMachine()
