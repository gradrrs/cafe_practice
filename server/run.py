import uvicorn
from app.db import init_db

if __name__ == "__main__":
    init_db()
    uvicorn.run("app.routes:app", host="127.0.0.1", port=5000, reload=True)