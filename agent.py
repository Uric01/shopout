from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from serpapi_tool import get_product_data
from utils import save_df_to_csv

@tool
def shop_out(product_name: str) -> str:
    """Search Google Shopping and save pricing info to CSV."""
    df = get_product_data(product_name)
    path = save_df_to_csv(df)
    return f"Found {len(df)} results. Saved to {path}."

def get_agent():
    llm = ChatOpenAI(temperature=0)
    tools = [shop_out]
    return initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
