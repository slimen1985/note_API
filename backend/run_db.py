import logging.config

from app.core.config import LOGGING_CONFIG
from app.db.session import SessionLocal
from app.db.init_db import init_db_user, init_db_note

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('notes_API')


def init():
    db = SessionLocal()
    init_db_user(db)
    init_db_note(db)


def main():
    logger.info('Run initialization')
    try:
        init()
    except Exception as error:
        logger.error(f"An error during db initialization {error}")
    else:
        logger.info('End initialization')


if __name__ == "__main__":
    main()