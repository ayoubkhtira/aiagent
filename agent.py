from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_groq import ChatGroq
import datetime
import os

# LLM Gratuit Groq
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

# Tool 1 : Date actuelle
def get_current_date(text):
    return str(datetime.datetime.now())

# Tool 2 : Calculatrice
def calculator(text):
    try:
        return str(eval(text))
    except:
        return "Erreur dans le calcul"

tools = [
    Tool(
        name="DateTool",
        func=get_current_date,
        description="Donne la date actuelle"
    ),
    Tool(
        name="Calculator",
        func=calculator,
        description="Effectue des calculs mathématiques"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(question):
    return agent.run(question)
