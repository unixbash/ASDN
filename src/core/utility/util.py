import io
import re
import itertools
import pymysql
from ftplib import FTP
from settings.GetSettings import Database, FtpServer


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
    regex = re.compile('[^a-zA-Z0-9\-\/\.]')
    return regex.sub(' ', text)

def find(src, target, all):
    result=[]
    lines = src.split('\n')
    for line in lines:
        if (target in line):
            if(not all):
                return removeNonAlphaNum(line.replace(target, "")).strip()

            result.append(' '.join(removeNonAlphaNum(line).strip().split()))

    return result

def executeSql(sql, args):
    try:
        db = Database()
        conn = pymysql.connect(
            host=db.getHost(), user=db.getUname(), passwd=db.getPwd(), db=db.getDb())
        cursor = conn.cursor()

        in_p = ', '.join(itertools.repeat('%s', len(args)))
        if len(args) > 0:
            sql = sql % in_p
        response = cursor.execute(sql, args)
        results = cursor.fetchall()
        conn.commit()

        return results

    except Exception as e:
        print("Error connecting to the database: " + str(e))
        if not cursor is None:
            cursor.close()
        if not conn is None:
            conn.close()
        return "Error"

def uploadFile(file, fileName, path):
    # Log into FTP
    ftpConnection = FtpServer()
    ftp = FTP(ftpConnection.getHost())
    ftp.login(ftpConnection.getUname(), ftpConnection.getPwd())
    ftp.cwd(path)

    ftp.storbinary('STOR ' + fileName, io.BytesIO(file.encode('utf-8')))
    ftp.quit()

def replaceTabs(string):
    return string.replace("\t", "  ")