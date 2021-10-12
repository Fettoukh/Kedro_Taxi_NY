from kedro.pipeline import Pipeline,node
from .nodes.preprocess import limit_data_size 

def dataEng_pipeline():
    return Pipeline(
        [
            node(
                func = limit_data_size,
                inputs = ["yellow_tripData" , "params:limit_size"],
                # input = ["yellow_tripData" , "parametrs"],    parameters["limit_size"]
                outputs="yellow_tripDataLimited",
                # name="limit_data_size"
            )
        ]
    )