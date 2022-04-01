from flask import Blueprint, request, render_template, flash, redirect, url_for,jsonify,flash
from flask import current_app as app
import jwt
from datetime import datetime, timedelta
from app.controller.DB import sql
# 추가할 모듈이 있다면 추가
 
login= Blueprint('login', __name__, url_prefix='/')
 
@login.route('/login', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
      
      temp = request.form
      id = temp['id']
      pw = temp['password']
      if(sql.memberSerch(id,pw) == True):
        payload = {
          'id': id,
          'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
          }
        token = jwt.encode(payload, sql.SECRET_KEY, algorithm='HS256')
        print("맞음")
        return jsonify({'result': 'success', 'token': token})
      
      else:
        print("틀림")
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})
        


  elif request.method == 'GET':

    return render_template('/sub/login.html')



# def sign_in():
# # 로그인
#   username_receive = request.form['username_give']
#   password_receive = request.form['password_give']
#   

#   if loginResultCount == 1:
#       payload = {
#       'id': username_receive,
#       'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
#       }
#       token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

#       return jsonify({'result': 'success', 'token': token})
#   # 찾지 못하면
#   else:
#       return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})