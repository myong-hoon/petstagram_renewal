from flask import Flask
# 추가할 모듈이 있다면 추가
 
app= Flask(__name__)
 
# app 정상 실행

# 파일 이름이 index.py이므로
from app.controller.main.index import main as main
from app.controller.sub.join import join as join
from app.controller.sub.login import login as login
from app.controller.sub.post_upload import post_upload as post_upload
from app.controller.sub.user import user as user
# 위에서 추가한 파일을 연동해주는 역할
app.register_blueprint(main)# as main으로 설정해주었으므로
app.register_blueprint(join)
app.register_blueprint(login)
app.register_blueprint(post_upload)
app.register_blueprint(user)

# #app TEST 실행

# from app.test.test import test as test
# app.register_blueprint(test)
