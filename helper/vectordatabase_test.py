
#import chromadb


#client = chromadb.Client()

#collection = client.create_collection("sample_collection")

# Add docs to the collection. Can also update and delete. Row-based API coming soon!
#collection.add(
#    documents=["This is document1", "This is document2"], # we embed for you, or bring your own
#    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on arbitrary metadata!
#    ids=["doc1", "doc2"], # must be unique for each doc 
#)

#results = collection.query(
#    query_texts=["This is a query document"],
#    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
#)


# get items from a collection
#collection.get("sample_collection", "123456789")

import pinecone
from getpass import getpass
from langchain.embeddings.openai import OpenAIEmbeddings

from tqdm.auto import tqdm
from uuid import uuid4


# # ########################### Pincone connection

# API key in console at app.pinecone.io
YOUR_API_KEY = getpass("Pinecone API Key: ")

# find ENV (cloud region) next to API key in console
YOUR_ENV = input("Pinecone environment: ")

index_name = 'aidocrep' # 'langchain-retrieval-agent'
pinecone.init(
    api_key=YOUR_API_KEY,
    environment=YOUR_ENV
)

if index_name not in pinecone.list_indexes():
    # we create a new index
    pinecone.create_index(
        name=index_name,
        metric='dotproduct',
        dimension=1536  # 1536 dim of text-embedding-ada-002
    )



############ create embeddings via open AI ada 002

OPENAI_API_KEY = getpass("OpenAI API Key: ")  # platform.openai.com
model_name = 'text-embedding-ada-002'

embed = OpenAIEmbeddings(
    model=model_name,
    openai_api_key=OPENAI_API_KEY
)

# ## ### indexing

batch_size = 100

texts = []
metadatas = []

for i in tqdm(range(0, len(data), batch_size)):
    # get end of batch
    i_end = min(len(data), i+batch_size)
    batch = data.iloc[i:i_end]
    # first get metadata fields for this record
    metadatas = [{
        'title': record['title'],
        'text': record['context']
    } for j, record in batch.iterrows()]
    # get the list of contexts / documents
    documents = batch['context']
    # create document embeddings
    embeds = embed.embed_documents(documents)
    # get IDs
    ids = batch['id']
    # add everything to pinecone
    index.upsert(vectors=zip(ids, embeds, metadatas))
