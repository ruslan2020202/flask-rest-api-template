from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


def execute_data(query: str):
    result = db.session.execute(text(query))
    return result.fetchall()


class Base:
    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()


class UsersModel(db.Model, Base):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self) -> str:
        return f'id {self.id} username {self.username} email {self.email} password {self.password}'

    @classmethod
    def find_by_email(cls, email: str) -> 'UsersModel':
        return cls.query.filter_by(email=email).first()
