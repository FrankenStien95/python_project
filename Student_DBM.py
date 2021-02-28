import pymysql as p 
from flask import *

def getConnection():
    db = p.connect(host = "localhost", user = "root", password = "", database = "pyproj")
    return db
print(getConnection())

def insertData(t):
    db = getConnection()
    cr = db.cursor()
    sql = "insert into studentss(rollno,name,contactno,email,college,address,password) value(%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

    
def selectAllDataByID(id):
    db = getConnection()
    cr = db.cursor()
    sql = "select * from studentss where id = %s"
    cr.execute(sql,id)
    Student_list = cr.fetchall()
    # for i in Student_list:
    #     print(i)
    db.commit()
    db.close()
    return Student_list[0]

def selectAllData():
    db = getConnection()
    cr = db.cursor()
    sql = "select * from studentss"
    cr.execute(sql)
    Student_list = cr.fetchall()
    # for i in Student_list:
    #     print(i)
    db.commit()
    db.close()
    return Student_list


def delete(t):
    db = getConnection()
    cr = db.cursor()
    sql = "delete from studentss where id = %s"
    cr.execute(sql,t)
    db.commit()
    db.close()

def updateData(t):
    db = getConnection()
    cr = db.cursor()
    sql = "update studentss set rollno=%s, name=%s, contactno=%s, email=%s,  college=%s, address=%s, password=%s where id=%s"
    cr.execute(sql,t)
    db.commit()
    db.close()
