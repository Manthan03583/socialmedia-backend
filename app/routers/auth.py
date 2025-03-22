from fastapi import APIRouter, status, Depends, Response, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schema, models, utils, oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schema.Token)
def login(user_credentional: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):

    # OAuth2PasswordRequestForm
    # {
    #     username
    #     password
    # }
    user = db.query(models.User).filter(models.User.email == user_credentional.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utils.verify(user_credentional.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create token
    # return token

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}