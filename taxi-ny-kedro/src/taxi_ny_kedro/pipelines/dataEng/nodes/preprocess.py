from kedro.pipeline import node
import logging

logger = logging.getLogger(__name__) 

def limit_data_size(data ,limit_size):
    print("node Started !!!")
    if limit_size is None:
        logger.warning("No limit size provided !")
        return data
    return data.head(limit_size)