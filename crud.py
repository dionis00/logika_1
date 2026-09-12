from schemas import UserBase
from models import User

def create_user(db, user: UserBase):
    db.user = User(username=user.username, email=user.email)
    db.add(db.user)
    db.commit()
    db.refresh(db.user)
    return db.user

def get_user(db, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db):
    return db.query(User).all()