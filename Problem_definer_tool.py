from langgraph.prebuilt import ToolNode

@tool
def ask(message:str) -> str:
    """
    If you are not clear about the user's issue, you can use this tool to ask questions to the user. such as if the user's response is ambiguous, you can use this tool to make further inquiries.
    If you think you fully understand the customer's product issue, describe your understanding of the problem in simple language to the user.

   Args:
   message:The message you want to ask

   Returns:
   User's explanation of the product issue
    """
    print(message,"\n")
    print("请输入你的回答：")
    reply= input()
    return {'ask':reply}


@tool
def write(message: str):
    """
    Once the user confirms that you have correctly understood the issue with their product, you can use this tool to write the  user problem feedback document and send it to other employees.
    Args:
   message:the message you need to write and send
    """
    return {"write"：message}

tools=[ask,write]
tool=ToolNode(tools)



