from kedro.pipeline import Pipeline,node
from .nodes.preprocess import limit_data_size 
from .nodes.preprocess import rename_columns 
from .nodes.preprocess import clean_data

def dataEng_pipeline():
    return Pipeline(
        [
            node(
                func = limit_data_size,
                inputs = ["yellow_tripData" , "params:limit_size"],
                # input = ["yellow_tripData" , "parametrs"],    parameters["limit_size"]
                outputs="yellow_tripDataLimited",
                # name="limit_data_size"
            ),
             node(
                func = rename_columns,
                inputs = ["yellow_tripDataLimited"],
                # input = ["yellow_tripData" , "parametrs"],    parameters["limit_size"]
                outputs="yellow_tripDataRenamed",
                # name="limit_data_size"
            ),
              node(
                func = clean_data,
                inputs = ["yellow_tripData", "params:maxLat", "params:maxLong"],
                # input = ["yellow_tripData" , "parametrs"],    parameters["limit_size"]
                outputs="yellow_tripDataCleaned",
                # name="limit_data_size"
            ),

        ]
    )