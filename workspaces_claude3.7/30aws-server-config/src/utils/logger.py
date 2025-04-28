import logging

def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler and set level
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    return logger

# Example usage:
# logger = setup_logger('aws_server_config')
# logger.info('Logger is set up and ready to use.')