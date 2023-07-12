import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
embedding = OpenAIEmbeddings()
load_dotenv()

openai_key = os.getenv('OPEN_API_KEY')
texts = [
    """The Amanita phalloides has a large and imposing epigeous (aboveground) fruiting body (basidiocarp).""",
    """A mushroom with a large fruiting body is the Amanita phalloides. Some varieties are all-white.""",
    """A. phalloides, a.k.a Death Cap, is one of the most poisonous of all known mushrooms.""",
]

smallDb = Chroma.from_texts(texts, embedding=embedding)
question = "Tell me about all-white mushrooms with large fruiting bodies"
print(smallDb.similarity_search(question, k=2))
print(smallDb.max_marginal_relevance_search(question, k=2, fetch_k=3))