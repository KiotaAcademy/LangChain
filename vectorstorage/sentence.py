import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv
load_dotenv()
openai_key = os.getenv('OPEN_API_KEY')


from langchain.embeddings.openai import OpenAIEmbeddings
embedding = OpenAIEmbeddings()
sentence = 'I like Chelsea football club'
sentence2 = 'Christian Pulisic is a player for chelsea football club'
sentence3 = 'chelsea is in london'
sentence4 = 'london is in united Kingdom'

embedding1 = embedding.embed_query(sentence)
embedding2 = embedding.embed_query(sentence2)
embedding3 = embedding.embed_query(sentence3)
embedding4 = embedding.embed_query(sentence4)

import numpy as np

print(np.dot(embedding1, embedding2))
print(np.dot(embedding1, embedding3))
print(np.dot(embedding1, embedding4))

