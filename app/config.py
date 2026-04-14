import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def get_database_uri():
    database_url = os.environ.get("DATABASE_URL")
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    if database_url:
        return database_url

    return f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"


def get_upload_folder():
    upload_folder = os.environ.get(
        "UPLOAD_FOLDER",
        os.path.join(BASE_DIR, "app", "static", "uploads"),
    )

    if not os.path.isabs(upload_folder):
        upload_folder = os.path.join(BASE_DIR, upload_folder)

    return os.path.abspath(upload_folder)


class Config(object):
    """Base config object."""

    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "Som3$ec5etK*y")
    UPLOAD_FOLDER = get_upload_folder()
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
