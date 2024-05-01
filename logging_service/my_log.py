from utils.logging_util import init_logger

logger = init_logger()

logger.setLevel(10)

logger.debug("debug")

logger.info("info")

logger.warning("warning")

logger.error("error")

logger.fatal("fatal")