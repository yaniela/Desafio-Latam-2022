import uvicorn
from config import AppConfig

if __name__ == "__main__":
    uvicorn.run(
        app="app.app:app",
        host=AppConfig.APP_HOST,
        port=AppConfig.APP_PORT,
        reload=True if AppConfig.ENV != "production" else False,
        workers=1,
    )