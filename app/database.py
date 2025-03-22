from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# database_url = "postgresql://<username>:<password>@<ip-address/hostname>/<database_name>"

sqlalchemy_database_url = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(sqlalchemy_database_url)

SessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:

#     try:
#         conn = psycopg2.connect(host="localhost", database='fastapi', user='postgres', password='Rosalin@1975', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database Connection Successfull!')
#         break
#     except Exception as error:
#         print("Database connection failed")
#         print("Error: ", error)
#         time.sleep(4)

    