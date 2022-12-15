import os
from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from jose import JWTError, jwt

from app.schemas import User, Item
from app.models import User, Item
from app.database import Sessionlocal, engine, Base

from fastapi_sqlalchemy import DBSessionMiddleware, db

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

