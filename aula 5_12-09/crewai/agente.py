### Sistemas de multi-agentes de inteligencias artificiais

# Biblioteca
from crewai_tools import tool
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

# Modelo LLM - Llama3 70B
llm = ChatGroq(temperature=0.7,
               groq_api_key='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',
               model_name='llama3-70b-8192')

# Ferramentas - Busca na internet com DuckDuckGo
@tool('DuckDuckGoSearchRun')
def search_tool(search_query: str):
  ''' Search the web for infotmation on a given topic'''
  return DuckDuckGoSearchRun().run(search_query)

# Topico do blog
topic = "Queimadas no Mato Grosso no Brasil"

# Agentes
researcher = Agent(
    role = "Senior Researcher",
    goal = f"Investigue noticias em alta sobre {topic}.",
    backstory = "You are an innovative researher who follows the latest news",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

writer = Agent(
    role = "Top Writer",
    goal = f"Escreva um conteudo engajador sobre {topic}. ",
    backstory = "You are an expert blogger who writes interesting articles.",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

# Tarefas
research_task = Task(
    description = f"Investigue as ultimas noticias sobre {topic}.",
    expected_output = "A comprehensive 4 paragraphs long report on the latest news trends.",
    tools = [search_tool],
    agent = researcher,
)

write_task = Task(
    description = f"Escreva um artigo engajador sobre {topic} que foca nas ultimas noticias.",
    expected_output = f"A comprehensive 4 paragraphs blog on {topic} in markdown format.",
    tools = [search_tool],
    agent = researcher,
    output_file = "news.md"
)

# Orquestrador
crew = Crew(
    agents=[researcher, writer],
    tasks = [research_task, write_task]
)

result = crew.kickoff(
    inputs = {"topic": topic}
)
