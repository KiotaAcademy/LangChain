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

> sources of your own data

1. Accessing:
   1. websites
   2. Databases
   3. Youtube
   4. arXiv

> formats of your own data

2. Data Types
   1. PDF
   2. HTML
   3. JSON
   4. word, Powerpoint

it should return a list of documents. each page returned is a document. A document contains text(`page_content`) and `metadata`

the neccessity of document letters is to take all this different sources of information in different data type formats and load them into a standardized data format that our models can work with.

#### DOCUMENT LOADERS

they can be used to load documents from unstructured and structured data sources like:

1. unstructured
   1. youtube
   2. wikipedia
   3. twitter
   4. arXiv
   5. jupyter
   6. figma
   7. github
   8. word
   9. notion
   10. powerpoint
   11. whatsapp
   12. slack
   13. telegram among others
2. structured data types
   1. datasets
   2. openweather
   3. excel
   4. Airbyte
   5. stripe
   6. APify
   7. azure among others

