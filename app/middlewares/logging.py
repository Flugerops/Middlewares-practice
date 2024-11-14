import logging

logger = logging.getLogger("logger")
handler = logging.FileHandler("general.log")
formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logging.basicConfig(level=logging.INFO)
