import getpass
import os
from reward_desginer import problem_definer,problem_definer_tool,probelm_definer_router

from pydantic import BaseModel



        
def _set_if_undefined(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"Please provide your {var}:")






if __name__=='__main__':

_set_if_undefined("OPENAI_API_KEY")#sk-proj-VPRUUxuRnsbqpI8pkRKbT3BlbkFJuvUF2awsJ9rYlBbeKRJy

def user_problem(ask:string):
    if ask==None
        print("请输入你的问题:")
        reply=inupt()
    else:    
        print(ask)
        reply = input(在此处回复:)
    return reply


# Either agent can decide to end
workflow = StateGraph(AgentState)  
workflow.add_node("problem",user_problem)
workflow.add_node("problem_definer",problem_definer.agent)
workflow.add_node("problem_definer_tool)", problem_definer_tool.tool)

workflow.set_entry_point("problem")
workflow.add_adge("problem","problem_definer")
workflow.add_edge("problem_definer","problem_definer_tool")
workflow.add_conditional_edge("problem_definer_tool",problem_definer_router.should_continue,)


