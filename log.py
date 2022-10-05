import logging 
import sys
logging.basicConfig(level=logging.DEBUG, filename="text.log", filemode="w", format="%(asctime)s - %(funcName)s - %(levelname)s - %(message)s")
logging.debug("AAA")
logging.info("BBB")
logging.warning("CCC")
logging.error("DDD")
logging.critical("EEE")

logger = logging.getLogger("main")
formatter = logging.Formatter("%(asctime)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler(filename="deneme.log", mode="w")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler(sys.stdout)

stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

logger.info("asdasdkad")
logger.debug("fffff")