from modules.core import settings
broker_url = f"redis://{settings.QUEUE_HOST}:{settings.QUEUE_PORT}/{settings.QUEUE_DB}"
result_backend = f"redis://{settings.QUEUE_HOST}:{settings.QUEUE_PORT}/{settings.QUEUE_DB}"
