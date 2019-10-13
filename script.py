import json
import glob
from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf


#You can convert many xml files
def utility():
    for f in glob.glob('*.xml'):
        n = str.split(f, ".")[-2]
        with open(f, "r") as i:
            j = bf.data(fromstring(i.read()))
            with open(n + ".json","w+") as newFile:
                json.dump(j, newFile, ensure_ascii=False)


if __name__ == "__main__":
    utility()
    print('Done!')