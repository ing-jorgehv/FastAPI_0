from fastapi import FastAPI
from Controllers.api_controller import router as api_router


def create_app():
    app = FastAPI()
    app.include_router(api_router)
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
