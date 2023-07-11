# this split to tokens
import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv
load_dotenv()
openaiApi = os.getenv('OPEN_AI_KEY')

from langchain.text_splitter import TokenTextSplitter
text_splitter = TokenTextSplitter(chunk_size=1, chunk_overlap=0)
text = "foo bar bazzyfoo"
print(text_splitter.split_text(text))