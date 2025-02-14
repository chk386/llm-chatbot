from fastapi import FastAPI
from api.v1.router import api_router

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="", port=8000, reload=True)
