import hashlib
import jwt
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
from markupsafe import re
from app.module import dbModule
from app.controller.sub import tag_split
mysql= Blueprint('sql', __name__, url_prefix='/')
SECRET_KEY = 'myoung'
 

def memberInsert(temp):
    db_class= dbModule.Database()
    pw = temp['password']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    sql     = "INSERT INTO petstagram.member(id,pw,name,img,status) \
                VALUES('%s','%s','%s','%s','0')"% (temp['id'],pw_hash,temp['name'],'images/photo/admin/default.png')
    db_class.execute(sql)
    print("??")
    db_class.commit()

    pass

def memberSerch(id, pw):
    db_class= dbModule.Database()
    sql = "SELECT id, pw FROM member"
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    loginResult = db_class.executeAll(sql)
    loginResultCount = loginResult.count({'id': id, 'pw': pw_hash})
    if(loginResultCount==1):
        result = True
    else:
        result = False
    return result

@mysql.route('/signIn', methods=['POST'])
def singIn(payload):
    db_class= dbModule.Database()
    sql = "SELECT * FROM member where id = '%s';"
    result = db_class.executeOne(sql%(payload["id"]))
    del result['pw']

    return result

def postInsert(temp):
    db_class= dbModule.Database()
    post_id=temp['num']
    date=temp['date']
    sql     = "INSERT INTO petstagram.post(num,idx,note,date,img) \
                VALUES('%s','%s','%s','%s','%s')"% (post_id,temp['idx'],temp['note'],date,temp['img'])
    db_class.execute(sql)
    db_class.commit()
    tag=tag_split.tag_split(temp['note'])
    print(tag)
    for i in tag:
        print(i)
        sql2     = "INSERT INTO petstagram.post_tag(post_id,tag,date) \
                    VALUES('%s','%s','%s')"% (post_id,i,date)
        db_class.execute(sql2)
        db_class.commit()
    
    pass

def postSerch():
    db_class= dbModule.Database()
    sql = "SELECT p.*,m.id FROM post AS p JOIN member AS m ON p.idx = m.idx WHERE p.idx"
    result = db_class.executeAll(sql)
    return result

     


# # SELECT 함수 예제
# @test.route('/select', methods=['GET'])
# def select():
#     db_class= dbModule.Database()
 
#     sql     = "SELECT idx, test \
#                 FROM testDB.testTable"
#     row     = db_class.executeAll(sql)
 
#     print(row)
 
#     return render_template('/test/test.html',
#                             result=None,
#                             resultData=row[0],
#                             resultUPDATE=None)
 
 
 
# # UPDATE 함수 예제
# @test.route('/update', methods=['GET'])
# def update():
#     db_class= dbModule.Database()
 
#     sql     = "UPDATE testDB.testTable \
#                 SET test='%s' \
#                 WHERE test='testData'"% ('update_Data')
#     db_class.execute(sql)   
#     db_class.commit()
 
#     sql     = "SELECT idx, test \
#                 FROM testDB.testTable"
#     row     = db_class.executeAll(sql)
 
#     return render_template('/test/test.html',
#                             result=None,
#                             resultData=None,
#                             resultUPDATE=row[0])
