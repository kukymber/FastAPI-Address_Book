from schemas import User, PhoneNumber, Email

from database import Base, engine, SessionLocal
from fastapi import FastAPI, status, HTTPException, Depends

from sqlalchemy.orm import Session

import models

#  create the DB
Base.metadata.create_all(engine)

#  Initialize app
app = FastAPI()


# func for work with DB session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
def root():
    return "addressbook"


@app.get("/user/{id}", response_model=User)
def read_user(id: int, session: Session = Depends(get_session)):
    # get the user item. If not found, raise exception and return 404 error
    user_get = session.query(models.User).get(id)

    if not user_get:
        raise HTTPException(status_code=404, detail=f'user with {id} not found')

    return user_get


@app.post('/user', response_model=User, status_code=status.HTTP_201_CREATED)
def created_user(id: int, session: Session = Depends(get_session)):
    session.add(User)
    session.commit()
    return f'created user with {id}'  # !!!


@app.put('/user/{id}', response_model=User)
def update_user(id: int, session: Session = Depends(get_session)):

    # given id the user, which need update
    user_update = session.query(User).get(id)
    # If not found, raise exception and return 404 error
    if not user_update:
        raise HTTPException(status_code=404, detail=f'user with {id} not found')
    return user_update


@app.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, session: Session = Depends(get_session)):

    # given id the user, which need delete
    user_delete = session.query(User).get(id)

    if user_delete:
        session.delete(user_delete)
        session.commit()
        raise HTTPException(status_code=404, detail=f'user with {id} not found')
    return user_delete
