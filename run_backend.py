from uvicorn import run as start

from app import app


if __name__ == "__main__":
    start("run_backend:app")
