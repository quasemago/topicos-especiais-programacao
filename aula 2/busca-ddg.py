from langchain_community.tools import DuckDuckGoSearchRun

ddg_search = DuckDuckGoSearchRun()
result = ddg_search.run("Noticias Venezuela")
print(result)
