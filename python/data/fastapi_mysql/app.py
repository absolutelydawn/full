from fastapi import FastAPI
from pydantic import BaseModel
from database import db_conn
from models import St_info, St_grade

app = FastAPI()

db = db_conn()
session = db.sessionmaker()

@app.get('/')
async def health_check():
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)

@app.get('/stinfo')
async def select_st_info():
    result = session.query(St_info)
    return result.all()

@app.get('/st_grade')
async def select_st_grade():
    result = session.query(St_grade)
    return result.all()

@app.get('/getuser')
async def getuser(id=None, name=None):
    if (id is None) and (name is None):
        return "학번 또는 이름으로 검색하세요"
    else:
        if name is None:
            result = session.query(St_info).filter(St_info.ST_ID == id).all()
        elif id is None:
            result = session.query(St_info).filter(St_info.NAME == name).all()
        else:
            result = session.query(St_info).filter(St_info.ST_ID == id, St_info.NAME == name).all()
    return result

@app.get('/useradd')
async def useradd(id=None, name=None, dept=None):
    if (id and name and dept) is None:
        return "학번, 이름, 학과명을 입력하세요"
    else:
        user = St_info(ST_ID=id, NAME=name, DEPT=dept)
        session.add(user)
        session.commit()
        result = session.query(St_info).all()
        return result

@app.get('/userupdate')
async def updateadd(id=None, name=None, dept=None):
    if id is not None:
        return "학번을 입력하세요"
    else:
        user = session.query(St_info).filter(St_info.ST_ID == id).first()
        user.NANE = name
        user.DEPT = dept
        session.add(user)
        session.commit()
        result = session.query(St_info).filter(St_info.ST_ID == id).all()
    return result

@app.get('/userdel')
async def userdel(id=None):
    if id is not None:
        session.query(St_info).filter(St_info.ST_ID == id).delete()
        session.commit()
        result = session.query(St_info).all()
    return