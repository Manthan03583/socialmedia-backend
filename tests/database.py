from fastapi.testclient import TestClient
from app.database import Base, get_db
from app.main import app
from app import schema
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
import pytest
from alembic import command

sqlalchemy_database_url = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"
engine = create_engine(sqlalchemy_database_url)

TestingSessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def session():
    Base.metadata.drop_all(bind = engine)
    Base.metadata.create_all(bind = engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    # Base.metadata.drop_all(bind = engine)
    # Base.metadata.create_all(bind = engine)

    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    # command.upgrade("head")
    # yield TestClient(app)
    # command.downgrade("base")