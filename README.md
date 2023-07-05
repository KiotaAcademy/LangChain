# LangChain

LLMs

LangChain is an open source framework for builind LLMs applications - large language models like chatGPT

## LANGCHAIN MODULAR COMPONENTS

1. Prompts
2. Models
3. Indexes
4. Chains
5. Agents

## LANGCHAIN with your Own Data

to create a 'chatGPT' with your own data you first have to figure out how to send/upload your data to the server/or to the model.

### Retrieval Augmented Generation

here LLMs retrieves contextual documents from an external dataset as part of its execution.

this is useful if you want to ask a specific question about or concerning specific documents.

so you need to load your data to a format LLM can understand

#### DOCUMENTAT LOADING

document loaders deals with the specifics of accessing and converting data.

1. Accessing:
   1. websites
   2. Databases
   3. Youtube
   4. arXiv
2. Data Types
   1. PDF
   2. HTML
   3. JSON
   4. word, Powerpoint

it should return a list of documents. each page returned is a document. A document contains text(`page_content`) and `metadata`
