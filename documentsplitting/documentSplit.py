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
r_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
c_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

text = 'abcdefghijklmnopqrstuvwxyz'
textExtra = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXabc'
text_with_spaces = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '
print(r_splitter.split_text(text))
print(r_splitter.split_text(textExtra))
print(r_splitter.split_text(text_with_spaces))


## chuck size is the number of characters in the chubks when splitted
## chunk overlap is the number of characters in the previous chunk that is going to overlap into the next chunk
