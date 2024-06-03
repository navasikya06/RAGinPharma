# RAGinPharma

This project is part of an attempt to create a solution for the Medical Affairs team in a pharmaceutical company. The team has to regularly create summaries of academic papers to send out to the business and also to doctors they are visiting. This tool can help save them a lot of time in the process of generating these summaries.

In order to realize this use case of document intelligence/document chatbot, we explored a few models and approaches, and share them below.

This repo contains of the following elements:
- A DistilBERT Question Answering model finetuning and evaluation notebook. For the purpose of document intelligence, we started by training and evaluating a QA model, and see if that can generate answers to our questions about a document (HuggingFace has a set of models for Document QA which we thought would be a good start). However, the QA model turns out to only be able to find pieces of information in the context and output it in a certain format. It's not very useful to extract and summarize information out of a document, as we show in the last part of the notebook.
- A RAG implementation and evaluation notebook. Moving on from the QA model, we found the Retrieval Augmented Generation (RAG) architecture that could help give context to a question before the model generates its answer. This notebook can be run on Google Colab, GPU or CPU, using Gemma, and includes a RAG dataset to evaluate ouput, Lanchain document loading, Hugging Face Embedding, and FAISS for context search. We find that this architecture and the text generation model Gemma is a lot better at extracting insights from document.
- A Streamlit RAG implementation: to run locally, using Gemma from ollama. User can upload document, determine the number of similar context pieces to include, and get answers to their questions about the document.

A few things to note:
- You need to get an Access Token on Hugging Face and agree to the conditions of use for Gemma, in order to run the notebook.
- To use bitsandbytes quantization, a Nvidia GPU is required.
- For using the local streamlit app, go into the 'streamlit' folder:
  + Install dependencies with pip install -r requirements.txt
  + Run with streamlit run app/app.py

!image /image.png

![image](image.png)

