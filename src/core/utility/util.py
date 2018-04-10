import itertools
import re
import pymysql

from settings.GetSettings import Database


def isAscii(text):
    return all(ord(char) < 128 for char in text)

def dictToList(dict):
    return list(dict.keys())

def readTextFile(fileName):
    with open(fileName) as f:
        result = f.readlines()

    result = [x.strip() for x in result]
    for x in result:
        x.strip()
        if("#" in x):
            result.remove(x)
    return list(filter(None, result));

def writeTextFile(fileName, ext, data):
    configFile = open(fileName+ext, "w")
    configFile.write(data)
    configFile.close()

def findBetween(str, delimeter):
    result = ""
    start = str.index(delimeter)
    end = str.index(delimeter, start+1)

    for i in range(start+1, end):
        result += str[i]
    return result

def removeNonAlphaNum(text):
    regex = re.compile('[^a-zA-Z0-9\-\/]')
    return regex.sub(' ', text)

def find(src, target, all):
    result=[]
    lines = src.split('\n')
    for line in lines:
        if (target in line):
            result.append(removeNonAlphaNum(line).strip())
            if(not all):
                return removeNonAlphaNum(line.replace(target, "")).strip()

    return result

def executeSql(sql, args):
    try:
        db = Database()
        conn = pymysql.connect(
            host=db.getHost(), user=db.getUname(), passwd=db.getPwd(), db=db.getDb())
        cursor = conn.cursor()

        in_p = ', '.join(itertools.repeat('%s', len(args)))
        sql = sql % in_p
        cursor.execute(sql, args)
        conn.commit()

    except Exception as e:
        print("Error connecting to the database: " + str(e))
        if not cursor is None:
            cursor.close()
        if not conn is None:
            conn.close()
        return "Error"