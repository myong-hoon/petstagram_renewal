from turtle import forward
from flask import Blueprint, request, render_template, flash, redirect, url_for,jsonify
from flask import current_app as app
from app.controller.DB import sql
# 추가할 모듈이 있다면 추가
 
join= Blueprint('join', __name__, url_prefix='/')

@join.route('/join', methods=['GET','POST'])
def index():
    
  if request.method == 'POST':
      temp = request.form
      print(temp)
      sql.memberInsert(temp)
      return jsonify({'result': 'success','msg':'등록 성공!'})

  elif request.method == 'GET':

    return render_template('/sub/join.html')