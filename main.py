import os
from langchain_experimental.graph_transformers.diffbot import DiffbotGraphTransformer
from langchain_community.document_loaders import WikipediaLoader
from langchain_community.graphs import FalkorDBGraph
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import FalkorDBQAChain

# Create a DiffbotGraphTransformer instance
diffbot_api_key = os.environ.get("DIFFBOT_API_KEY")
diffbot_nlp = DiffbotGraphTransformer(diffbot_api_key=diffbot_api_key)

# Load documents from Wikipedia
query = "Washington"
raw_documents = WikipediaLoader(query=query).load()
graph_documents = diffbot_nlp.convert_to_graph_documents(raw_documents)

# Add documents to FalkorDB
graph = FalkorDBGraph("falkordb")
graph.add_graph_documents(graph_documents)
graph.refresh_schema()

# Create Google Generative AI LLM Instance
model_name = "models/text-bison-001"
llm = GoogleGenerativeAI(model_name=model_name)

# Create a Langchain instance
chain = FalkorDBQAChain.from_llm(graph=graph, llm=llm, verbose=True)

# Run the chain
chain.run("Which organization is in Washington?")