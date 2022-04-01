
from unittest import result
import jwt 
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
from app.controller.DB import sql
from app.controller.token import token

# 추가할 모듈이 있다면 추가
 
main= Blueprint('main', __name__, url_prefix='/')
@main.route('/', methods=['GET'])
def index():
    try:
        result = token.token()
        return render_template('/main/index.html', user_info=result,posts=sql.postSerch())
    except jwt.ExpiredSignatureError:
        return render_template('/main/index.html',user_info='',posts=sql.postSerch())
    except jwt.exceptions.DecodeError:
        return render_template('/main/index.html',user_info='',posts=sql.postSerch())

    

# def home():
# token_receive = request.cookies.get('mytoken')
# try:
#     payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

#     sql = "SELECT * FROM users where username = '%s';"
#     cursor.execute(sql%(payload["id"]))
#     result = cursor.fetchone()

#     return render_template('/main/index.html', user_info=result)

# except jwt.ExpiredSignatureError:
#     return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
# except jwt.exceptions.DecodeError:
#     return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))