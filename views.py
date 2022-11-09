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


@app.post('/user', response_model=User, status_code=status.HTTP_201_CREATED)
def created_user(id: int, session: Session = Depends(get_session)):
    session.add(User)
    session.commit()
    return f'created user with {id}'


@app.get("/user/{id}", response_model=User)
def read_user(id: int, session: Session = Depends(get_session)):
    # get the user item. If not found, raise exception and return 404 error
    user_get = session.query(models.User).get(id)

    if not user_get:
        raise HTTPException(status_code=404, detail=f'user with {id} not found')

    return user_get


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


"""User's phone number"""


@app.post('/phone_number', response_model=PhoneNumber, status_code=status.HTTP_201_CREATED)
def created_user(id: int, session: Session = Depends(get_session)):
    session.add(PhoneNumber)
    session.commit()

    return f'created phone_number with {id}'


@app.get('/phone_number/{id}', response_model=PhoneNumber)
def read_phone_number(id: int, session: Session = Depends(get_session)):
    phone_num_get = session.query(models.PhoneNumber).get(id)

    if not phone_num_get:
        raise HTTPException(status_code=404, detail=f'phone_number with {id} not found')

    return phone_num_get


@app.put('/phone_number/{id}', response_model=PhoneNumber)
def update_user(id: int, session: Session = Depends(get_session)):
    phone_num_update = session.query(PhoneNumber).get(id)

    if not phone_num_update:
        raise HTTPException(status_code=404, detail=f'phone_number with {id} not found')
    return phone_num_update


@app.delete('/phone_number/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, session: Session = Depends(get_session)):
    phone_num_delete = session.query(PhoneNumber).get(id)

    if phone_num_delete:
        session.delete(phone_num_delete)
        session.commit()
        raise HTTPException(status_code=404, detail=f'phone_number with {id} not found')
    return phone_num_delete


"""User's Email"""


@app.post('/email', response_model=Email, status_code=status.HTTP_201_CREATED)
def created_user(id: int, session: Session = Depends(get_session)):
    session.add(Email)
    session.commit()
    return f'Created email with {id}'


@app.get('/email/{id}', response_model=Email)
def read_phone_number(id: int, session: Session = Depends(get_session)):
    email_get = session.query(models.Email).get(id)

    if not email_get:
        raise HTTPException(status_code=404, detail=f'Email with {id} not found')

    return email_get


@app.put('/email/{id}', response_model=PhoneNumber)
def update_user(id: int, session: Session = Depends(get_session)):
    email_update = session.query(Email).get(id)

    if not email_update:
        raise HTTPException(status_code=404, detail=f'Email with {id} not found')
    return email_update


@app.delete('/email/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, session: Session = Depends(get_session)):
    email_delete = session.query(Email).get(id)

    if email_delete:
        session.delete(email_delete)
        session.commit()
        raise HTTPException(status_code=404, detail=f'Email with {id} not found')
    return email_delete
