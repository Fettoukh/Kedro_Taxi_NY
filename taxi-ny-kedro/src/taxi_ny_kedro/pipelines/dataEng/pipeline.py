import from nodes/preprocess import return_greeting_node

#importing the library
from kedro.pipeline import Pipeline
# Assigning "nodes" to "pipeline"
pipeline = Pipeline([return_greeting_node, join_statements_node])