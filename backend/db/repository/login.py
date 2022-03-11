from db.models.users import User
from sqlalchemy import or_
from sqlalchemy.orm import Session


def get_user(username: str, db: Session):
    user = (
        db.query(User)
        .filter(or_(User.username == username, User.email == username))
        .first()
    )
    return user
