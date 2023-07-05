import os
import openai
import sys

from langchain.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://www.linkedin.com/feed/")
docs = loader.load()
print(docs[0].page_content[:500])