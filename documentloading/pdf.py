import os
import openai
import sys
sys.path.append('../..')
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=150,
    length_function=len
)
load_dotenv()
openaiApi = os.getenv('OPEN_AI_KEY')

loader = PyPDFLoader('./resources/kipngenokoech.pdf')
pages = loader.load()

docs = text_splitter.split_documents(pages)

print(len(pages), ':', len(docs))

page = pages[0]

print(page.page_content[0:500])

print(page.metadata)