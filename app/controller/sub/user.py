
from unittest import result
import jwt 
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
from app.controller.DB import sql
from app.controller.main import index as main
from app.controller.token import token
# 추가할 모듈이 있다면 추가
 
user= Blueprint('user', __name__, url_prefix='/')

@user.route('/user/<username>', methods=['GET'])
def index(username):
    try:
        result = token.token()
        status=token.userChk(result['id'])
        return render_template('/sub/user.html', user_info=result,posts=sql.postSerch(),status=status)
    except jwt.ExpiredSignatureError:

        return render_template('/sub/user.html',user_info='',posts=sql.postSerch(),status='')
    except jwt.exceptions.DecodeError:

        return render_template('/sub/user.html',user_info='',posts=sql.postSerch(),status='')

    
# @app.route('/user/<username>')
# def user(username):
#     # 각 사용자의 프로필과 글을 모아볼 수 있는 공간
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         status = (username == payload["id"])  # 내 프로필이면 True, 다른 사람 프로필 페이지면 False

#         sql = "SELECT * FROM users where username = '%s';"
#         cursor.execute(sql%(username))
#         result = cursor.fetchone()

#         return render_template('user.html', user_info=result, status=status)
#     except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
#         return redirect(url_for("home"))
