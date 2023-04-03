from fastapi import FastAPI
from app.core.config import Settings

from app.core.config import LOGGING_CONFIG
import logging.config

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("notes_api")


def start_application(config: Settings):
    application = FastAPI(
        debug=True,
        title=config.PROJECT_NAME,
        version=config.PROJECT_VERSION,
        description="notes"
    )
    return application


settings = Settings()

app = start_application(settings)


@app.get("/")
async def root():
    logger.debug("Start application")
    return {"message": "Hello FastAPI"}