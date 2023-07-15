##### tl;dr:

This application is a PoC for automating the patient checkout process, especially the doctors report. We try to achieve this, by using the medical data of patients and summarizing it with Large Language Models (such as GPT-4).

___

##### usage:
- go to the "search field" and search for a patient by ID or a name  
- select the patient by patiend ID and click on "show details"
- on the next page, check the data you want to summarize to a report and click "write report"  
- wait for the AI to create a Doctors Report based on given Documents.

___
 
##### architecture and technicallities (for the nerds):

To achieve our goal, we combine several technicals solutions:
* we leverage pinecone, a vector database, to store the patient data as vector embeddings; 
* we use medAlpacca, a to medical Q&A finetuned LLM in the 7b version, to generate text; 
* we use langchain to tie together the embeddings with the AI text generation. 
* as UI for our PoC we used streamlit.
___


 