message={"wi":"nian"}
def should_continue(message):
    key=list(message.keys())[0]
    if key =='write':
        return "__end__"
    else:
        return "problem_desginer"
