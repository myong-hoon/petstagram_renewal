import jwt 
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
from app.controller.DB import sql

# 추가할 모듈이 있다면 추가
 
def token():   
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, sql.SECRET_KEY, algorithms=['HS256'])
    result = sql.singIn(payload)
    print(result)
    return result

def userChk(username):   
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, sql.SECRET_KEY, algorithms=['HS256'])
    status = (username == payload["id"])
    print(status)
    return status
