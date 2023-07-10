# loading the environment and preparing it
import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv
load_dotenv()
openaiApi = os.getenv('OPEN_AI_KEY')

## importing text splitters
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
chunk_size = 27
chunk_overlap = 4
r_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap, separators=["\n\n", "\n", " ", ""])
c_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator=' ')

text = 'abcdefghijklmnopqrstuvwxyz'
textExtra = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXabc'
text_with_spaces = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '

some_text = """When writing documents, writers will use document structure to group content. \
This can convey to the reader, which idea's are related. For example, closely related ideas \
are in sentances. Similar ideas are in paragraphs. Paragraphs form a document. \n\n  \
Paragraphs are often delimited with a carriage return or two carriage returns. \
Carriage returns are the "backslash n" you see embedded in this string. \
Sentences have a period at the end, but also, have a space.\
and words are separated by space."""
print(r_splitter.split_text(text))
print(r_splitter.split_text(textExtra))
print(r_splitter.split_text(text_with_spaces))
print(c_splitter.split_text(text_with_spaces))
print(len(some_text))
print(c_splitter.split_text(some_text))
print(r_splitter.split_text(some_text))


## chuck size is the number of characters in the chubks when splitted
## chunk overlap is the number of characters in the previous chunk that is going to overlap into the next chunk
