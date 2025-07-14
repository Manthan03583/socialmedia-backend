# FastAPI Social Media API

A modern, full-featured REST API built with FastAPI that provides social media functionality including user authentication, posts, and voting system.

## 🚀 Features

- **User Authentication**: JWT-based authentication with secure password hashing
- **Post Management**: Create, read, update, and delete posts
- **Voting System**: Users can vote on posts
- **Database Integration**: PostgreSQL with SQLAlchemy ORM
- **Database Migrations**: Alembic for schema management
- **Docker Support**: Containerized development and production environments
- **CORS Support**: Cross-origin resource sharing enabled
- **Environment Configuration**: Secure configuration management

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (PyJWT)
- **Password Hashing**: bcrypt
- **Database Migrations**: Alembic
- **Containerization**: Docker & Docker Compose
- **Server**: Gunicorn with Uvicorn
- **Reverse Proxy**: Nginx (production)

## 📋 Prerequisites

- Python 3.8+
- Docker and Docker Compose
- PostgreSQL (if running locally)

## 🚀 Quick Start

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fast-api
   ```

2. **Start the development environment**
   ```bash
   docker-compose -f docker-compose-dev.yml up --build
   ```

   This will:
   - Start a PostgreSQL database
   - Run database migrations
   - Start the FastAPI server on `http://localhost:8000`

3. **Access the API**
   - API Documentation: `http://localhost:8000/docs`
   - Alternative Documentation: `http://localhost:8000/redoc`

### Local Development

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_HOSTNAME=localhost
   DATABASE_PORT=5432
   DATABASE_PASSWORD=your_password
   DATABASE_NAME=fastapi
   DATABASE_USERNAME=postgres
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

4. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

5. **Start the server**
   ```bash
   uvicorn app.main:app --reload
   ```

## 📚 API Endpoints

### Authentication
- `POST /login` - User login
- `POST /register` - User registration

### Users
- `GET /users` - Get all users
- `GET /users/{id}` - Get user by ID
- `POST /users` - Create new user

### Posts
- `GET /posts` - Get all posts
- `GET /posts/{id}` - Get post by ID
- `POST /posts` - Create new post
- `PUT /posts/{id}` - Update post
- `DELETE /posts/{id}` - Delete post

### Votes
- `POST /vote` - Vote on a post

## 🗄️ Database Schema

### Users Table
- `id` (Primary Key)
- `email` (Unique)
- `password` (Hashed)
- `created_at`
- `phone_number`

### Posts Table
- `id` (Primary Key)
- `title`
- `content`
- `published`
- `created_at`
- `owner_id` (Foreign Key to Users)

### Votes Table
- `user_id` (Composite Primary Key)
- `post_id` (Composite Primary Key)

## 🐳 Docker Configuration

### Development
```bash
docker-compose -f docker-compose-dev.yml up --build
```

### Production
```bash
docker-compose -f docker-compose-prod.yml up --build
```

## 🧪 Testing

Run tests using pytest:
```bash
pytest
```

## 📁 Project Structure

```
fast-api/
├── alembic/                 # Database migrations
├── app/
│   ├── routers/            # API route handlers
│   │   ├── auth.py        # Authentication routes
│   │   ├── post.py        # Post management routes
│   │   ├── user.py        # User management routes
│   │   └── votes.py       # Voting routes
│   ├── __init__.py
│   ├── calculations.py
│   ├── config.py          # Configuration settings
│   ├── database.py        # Database connection
│   ├── main.py           # FastAPI application
│   ├── models.py         # SQLAlchemy models
│   ├── oauth2.py         # JWT authentication
│   ├── schema.py         # Pydantic schemas
│   └── utils.py          # Utility functions
├── tests/                 # Test files
├── docker-compose-dev.yml # Development Docker setup
├── docker-compose-prod.yml # Production Docker setup
├── Dockerfile            # Docker image configuration
├── requirements.txt      # Python dependencies
└── start-dev.sh         # Development startup script
```

## 🔧 Configuration

The application uses environment variables for configuration. Key variables include:

- `DATABASE_HOSTNAME`: Database host
- `DATABASE_PORT`: Database port
- `DATABASE_PASSWORD`: Database password
- `DATABASE_NAME`: Database name
- `DATABASE_USERNAME`: Database username
- `SECRET_KEY`: JWT secret key
- `ALGORITHM`: JWT algorithm
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time

## 🔒 Security Features

- Password hashing with bcrypt
- JWT token-based authentication
- CORS middleware for cross-origin requests
- SQL injection protection through SQLAlchemy
- Environment variable configuration

## 📝 Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions, please open an issue in the repository. 