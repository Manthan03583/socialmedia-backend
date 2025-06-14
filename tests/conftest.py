import pytest
from alembic import command
from app import schema
from fastapi.testclient import TestClient
from app.database import Base, get_db
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.oauth2 import create_access_token
from app import models

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

@pytest.fixture
def test_user2(client):
    user_data = {"email" : "hello12@gmail.com",
                 "password" : "password123"
                }
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user

@pytest.fixture
def test_user(client):
    user_data = {"email" : "hello123@gmail.com",
                 "password" : "password123"
                }
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{
        "title": "first title",
        "content": "first content",
        "owner_id": test_user["id"] 
    },
    {
        "title": "2nd title",
        "content": "2nd content",
        "owner_id": test_user["id"]
    },
    {
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user["id"]
    },
    {
        "title": "4th title",
        "content": "4th content",
        "owner_id": test_user2["id"]
    }]

    def create_post_model(post):
        return models.Post(**post)
    
    posts_map = map(create_post_model, posts_data)
    posts = list(posts_map)

    session.add_all(posts)

    # session.add_all([
    #     models.Post(title="first title", content="first content", owner_id= test_user["id"]),
    #     models.Post(title= "2nd title", content= "2nd content", owner_id= test_user["id"]),
    #     models.Post(title= "3rd title", content= "3rd content", owner_id= test_user["id"]),
    # ])

    session.commit()

    posts = session.query(models.Post).all()

    return posts