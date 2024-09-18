from .prompt import problem_definer_prompt
from .tools import tools

from typing import Literal

from langchain_anthropic import ChatAnthropic
from langgraph.graph import StateGraph, MessagesState

class problem_definer(llm,tools,prompt)
from langchain_core.messages import AIMessage


def agent(message:str):
    llm = ChatOpenAI(model='gpt4-o',temperature=0)
    agent=problem_definer_prompt|llm.bind_tools(tools)
    response = agent.invoke(message)    
    return {"messages": [response]}




