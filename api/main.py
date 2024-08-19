from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI

load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    ChatOpenAI(model="gpt-3.5-turbo"),
    path="/openai"
           )

model=ChatOpenAI()
llm=Ollama(model="gemma2:2b")

prompt1=ChatPromptTemplate.from_template("who is president of the {country}?")
# prompt2=ChatPromptTemplate.from_template("what is the capital of {country}?")
prompt2=ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])


add_routes(
    app,
    prompt2 | llm,
    path="/gemma"
           )

add_routes(
    app,
    prompt1 | model,
    path="/open"
           )


if __name__ == "__main__":

 uvicorn.run(app, host="localhost", port=8000)