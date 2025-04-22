import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'  # SQLite database file in the project folder
    SQLALCHEMY_TRACK_MODIFICATIONS = False
