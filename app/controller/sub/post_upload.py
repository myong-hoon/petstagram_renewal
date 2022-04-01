from datetime import datetime
from flask import Blueprint, request, render_template, flash, redirect, url_for,jsonify
from flask import current_app as app
from jinja2 import Undefined
from app.controller.DB import sql
from app.controller.token import token
import datetime
from werkzeug.utils import secure_filename
from app.controller.token import token
# 추가할 모듈이 있다면 추가
 
post_upload= Blueprint('post_upload', __name__, url_prefix='/')
 
@post_upload.route('/post_upload', methods=['GET','POST'])
def index():

  if request.method == 'POST':
    # print()
    
    user_info=token.token()
    idx=user_info['idx']
    note = request.form['note_give']
    file = request.files["file_give"]
    date=datetime.datetime.now()
    file_name=(str(datetime.datetime.now())+'idx'+str(idx)).replace(' ','')
    file_foot=secure_filename(file.filename)[secure_filename(file.filename).find('.'):len(secure_filename(file.filename))]
    file.save('./app/static/images/photo/post/'+file_name+file_foot)
    post_num=file_name
    temp={
      'num':post_num,
      'idx':idx,
      'note':note,
      'img':'images/photo/post/'+file_name+file_foot,
      'date':date
    }
    sql.postInsert(temp)
    return jsonify({'result': 'success','msg':'등록 성공!'})
  elif request.method == 'GET':
    
    try:
      token.token()
      return render_template('/sub/post_upload.html')
    except:
      return redirect('/')

    

