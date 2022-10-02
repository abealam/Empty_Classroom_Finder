from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import mysql.connector
import datetime
import bisect
from collections import defaultdict

#Khai's section
class Room:
    def __init__(self, roomNum, availUntil=-1, availIn=-1):
        self.roomNum = roomNum
        self.availUntil = availUntil
        self.availIn = availIn

    def __str__(self):
        h1, m1 = self.availIn // 60, self.availIn % 60
        h2, m2 = self.availUntil // 60, self.availUntil % 60
        if self.availIn > 0:
            tmp = convertTime(h1, m1)
            s = tmp[0:2] + ":" + tmp[2:]
            return "Room " + self.roomNum + " available in: " + s
        else:
            tmp = convertTime(h2, m2)
            s = tmp[0:2] + ':' + tmp[2:]
            return "Room " + self.roomNum + " available until: " + s


def convertTime(h, m):
    print("ConvertTime executed")
    hour, minute = "",""
    if h < 10:
        hour = '0' + str(h)
    else:
        hour = str(h)
    if m < 10:
        minute = '0' + str(m)
    else:
        minute = str(m)
    return hour + minute

def index(response):
    db = mysql.connector.connect (
    host = "remotemysql.com",
    database = "Q03Tg9475z",
    user = "Q03Tg9475z",
    password = "IjP1ddd6bm"
    )
    cursor = db.cursor(buffered=True)


    query1 = "SELECT * FROM testBuildings"
    cursor.execute(query1)

    #db.commit()

    allBuildings = []
    for buildingID, buildingName in cursor.fetchall():
        tmp = buildingName.split()
        allBuildings.append("".join(tmp))

    todayDay = datetime.datetime.today().weekday() - 2
    todayHour = datetime.datetime.today().hour
    todayMin = datetime.datetime.today().minute
    hourFormat = convertTime(todayHour, todayMin)

    query2 = "SELECT * FROM testRooms WHERE day = %s ORDER BY start"
    cursor.execute(query2, (todayDay,))
   #db.commit()

    extraContext = {}
    allRooms = {}
    roomsToBuilding = defaultdict(str)


    for roomID, buildingID, roomNum, d, startTime, endTime in cursor.fetchall():
        buildingName = allBuildings[buildingID-1]
        print("ROOMID Works")
        if roomNum not in allRooms:
            allRooms[roomNum] = [] 
        #Assuming all start,end are ordered sets
        allRooms[roomNum].append(int(startTime))
        allRooms[roomNum].append(int(endTime))     

        if buildingName not in extraContext:
            extraContext[buildingName] = []
            
        roomsToBuilding[roomNum] = buildingName
        #for the moment, do the computation of time here

    #roomsObj = []
    for roomNum in allRooms:
        curHour = int(hourFormat)
        indx = bisect.bisect_left(allRooms[roomNum], curHour)
        availIn, availUntil = -1, -1
        if indx & 1:
            availIn = allRooms[roomNum][indx] - curHour
            
        else:
            #Assume classrooms are available until 10pm only
            if indx == len(allRooms[roomNum]):
                availUntil = 2200 - curHour
            else:
                availUntil = allRooms[roomNum][indx] - curHour

        curRoom = Room(roomNum, availUntil, availIn)
        #roomsObj.append(curRoom)
        print(curRoom)
        buildingName = roomsToBuilding[roomNum]
        extraContext[buildingName].append(curRoom)

    #render()
    print(extraContext)


    return render(response, "base.html", {'extraContext':extraContext} )

def v1(response):
    return render(response, "home.html", {})
