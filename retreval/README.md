# RETRIEVAL

when a query comes in, you want to retrieve the most relevant splits for it.

methods to do this retrival include:

1. Semantic similarity research
2. Maximum marginal relevance (MMR)
3. LLM Aided Retrievals ()
4. compression

## Maximum Marginal Relevance (MMR)

### Algorithm

1. query the vector store
2. choose the fetch_k most similar responses
3. within those responses chose the k most diverse

## LLM Aided Retrievals

there are several cases where the query applied to the DB is more than just the question asked

so essentially what this does is to convert the user question intoa query

i.e `what are some movies about space released in 2020?` our retrieval mechanism will construct a query:
`movies("year", 2020)`

it is passed through a query parser

so the filter will be `movies("year", 2020` and the search term will be `space`

## Compression

it is used to pull out only the most relevant information from the database.

it shrinks the responses to relevant information only - the most important information
