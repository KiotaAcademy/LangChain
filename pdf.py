import os
import openai
import sys
sys.path.append('../..')
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
load_dotenv()
openaiApi = os.getenv('OPEN_AI_KEY')

loader = PyPDFLoader('./resources/kipngenokoech.pdf')
pages = loader.load()

print(len(pages))

page = pages[0]

print(page.page_content[0:500])

print(page.metadata)