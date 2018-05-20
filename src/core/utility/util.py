import io
import re
import bs4
import time
import pymysql
import execnet
import itertools
from ftplib import FTP
import netifaces as ni
from pathlib import Path
from urllib.request import urlopen
from settings.GetSettings import Database, FtpServer, Server


def isAscii(text):
    return all(ord(char) < 128 for char in text)

def dictToKeyList(dict):
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
    return regex.sub(' ', text).strip()

def find(src, target, all):
    result=[]
    lines = src.split('\n')
    for line in lines:
        if (target in line):
            if(not all):
                return removeNonAlphaNum(line.replace(target, "")).strip()

            result.append(' '.join(removeNonAlphaNum(line).strip().split()))

    return str(result)

#Execute command on the SQL server
def executeSql(sql, args):
    try:
        db = Database()

        conn = pymysql.connect(
            host=db.getHost(), user=db.getUname(), passwd=db.getPwd(), db=db.getDb())
        cursor = conn.cursor()

        in_p = ', '.join(itertools.repeat('%s', len(args)))
        if len(args) > 0:
            sql = sql % in_p
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)

        results = cursor.fetchone()

        conn.commit()

        return results

    except Exception as e:
        print("Error connecting to the database: " + str(e))
        if not cursor is None:
            cursor.close()
        if not conn is None:
            conn.close()
        return "Error"

def getAllSql(sql, values):
    try:
        db = Database()
        conn = pymysql.connect(
            host=db.getHost(), user=db.getUname(), passwd=db.getPwd(), db=db.getDb())
        cursor = conn.cursor()

        if not values:
            cursor.execute("SELECT * from " + sql)
        else:
            statement = "SELECT "
            for val in values:
                statement += val + ", "
            #Trim extra comma
            statement = statement[:-2] + " from " + sql
            cursor.execute(statement)

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
    fullName = path + fileName

    ftp.storbinary('STOR ' + fileName, io.BytesIO(file.encode('utf-8')))
    ftp.quit()

    ftpWait = 0
    fileAvail = False
    ftpConnection = FtpServer()
    ftp = FTP(ftpConnection.getHost())
    ftp.login(ftpConnection.getUname(), ftpConnection.getPwd())
    ftp.cwd(path)

    while not fileAvail and ftpWait < 10:
        ftpWait += 1
        time.sleep(1)

        if fileName in ftp.nlst():
            return True

    return False

def replaceTabsWithSpaces(string):
    return string.replace("\t", "  ")

def getLatestOS(model):

    url = 'https://kb.juniper.net/InfoCenter/index?page=content&id=KB21476&actp=METADATA'
    output_directory = "tmp"
    webPage = urlopen(url)
    parsedHtml = bs4.BeautifulSoup(webPage, 'lxml')

    #Search for the recommended OS in the list file
    found = False
    lines = parsedHtml.findAll('tr')
    for line in lines:
        txtVal = ''.join(line.findAll(text=True))
        if model in txtVal:
            return txtVal.replace(" ", "").split()[2]

    return False

#https://stackoverflow.com/questions/27863832/calling-python-2-script-from-python-3
def callPy(Version, Module, Function, ArgumentList):
    try:
        gw = execnet.makegateway("popen//python=python%s" % Version)
        channel = gw.remote_exec("""
            from %s import %s as the_function
            channel.send(the_function(*channel.receive()))
        """ % (Module, Function))
        channel.send(ArgumentList)
        return channel.receive()
    except:
        print("Unable to execute the Python script.")
        return False

def outputTrim(string, command):
    return string.replace(command, "").replace("asdn>", "").strip()

#Get the server IP
def isExecOnServer():
    try:
        server = Server()
        uplink = server.getUplink()
        ni.ifaddresses(uplink)
        address = ni.ifaddresses(uplink)[ni.AF_INET][0]['addr']
        if server.getAddress()==address:
            return True
        else:
            return False
    except:
        return False