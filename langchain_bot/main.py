
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import google.generativeai as genai


load_dotenv()
# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
# print(os.getenv("GOOGLE_API_KEY"))
# print(os.getenv("OPENAI_API_KEY"))

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.3)
# llm=ChatOpenAI(api_key=os.getenv("openai_api_key"), model="gpt-3.5-turbo",temperature=0.3)
# print(llm.invoke("who is the president of the United States?"))
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])


# stremlit

st.title("Langchain")
input=st.text_input("Enter text")

output_parser = StrOutputParser()

#  llm


chain = prompt | llm | output_parser
output = chain.invoke({"input":input})


if input:
    st.write(output)


