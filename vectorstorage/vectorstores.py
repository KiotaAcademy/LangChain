import os
import openai
import sys
sys.path.append('../..')
from dotenv import load_dotenv
load_dotenv()
openai_key = os.getenv('OPEN_AI_KEY')

from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
embedding = OpenAIEmbeddings
loaders = [
    PyPDFLoader('../resources/Generative AI.pdf'),
    PyPDFLoader('./resources/kipngenokoech.pdf'),
    PyPDFLoader('./resources/mCT39K3LnP0ACkN5_Qrq8h4105iRriJVC-Save AI models as Jupyter Notebooks transcript_EN.pdf')
]

docs = []
for loader in loaders:
    docs.extend(loader.load())
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
splits = text_splitter.split_documents(docs)
persist_dir = os.path.dirname('/docs/chroma')

vector_store = Chroma.from_documents(
    documents=splits,
    embedding=embedding,
    persist_directory=persist_dir
)
print(vector_store._collection.count())

question = 'The question you are trying to solve'

docs = vector_store.similarity_search(question, k=5)# k standing for number of files tht it wil be returned
