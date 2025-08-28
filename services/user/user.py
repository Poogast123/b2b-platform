from sqlalchemy import Column, Integer, String
from database import Base, engine
from sqlalchemy.orm import Session
from passlib.context import CryptContext

# --------------------------
# Model
# --------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    company = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)


# --------------------------
# Password hashing
# --------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# --------------------------
# Create table & insert demo user
# --------------------------
def create_demo_user():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    db = Session(bind=engine)

    # Check if demo user exists
    if not db.query(User).filter(User.email == "demo@example.com").first():
        demo_user = User(
            name="Demo User",
            email="demo@example.com",
            company="Demo Company",
            hashed_password=pwd_context.hash("demo123")
        )
        db.add(demo_user)
        db.commit()
        print("Demo user created!")

    db.close()


# Run on import
create_demo_user()
