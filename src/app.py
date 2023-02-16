import os

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        os.getenv("DATABASE_URL"),
        isolation_level="REPEATABLE READ",
    )
)


@app.route("/health")
def status():
    return {"message": "success"}, 200
