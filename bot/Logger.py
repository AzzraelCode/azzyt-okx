import logging

def setup_logger():
    """
    Использую logging
    чтобы при деплое легко переключить сохранение логов в файл
    :return:
    """
    fmt = logging.Formatter(fmt="%(asctime)s %(levelname).3s | %(message)s", datefmt="%m/%d %H:%M:%S")
    cons = logging.StreamHandler()
    cons.setFormatter(fmt)
    logger = logging.getLogger('azzraelcode-yt')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(cons)
    return logger
