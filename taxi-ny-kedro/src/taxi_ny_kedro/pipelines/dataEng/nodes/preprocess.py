from kedro.pipeline import node

# Preparing the first "node"
def return_greeting():
    return "Hello"
#defining the node that will return
return_greeting_node = node(func=return_greeting, inputs=None, outputs="my_salutation")