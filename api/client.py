import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/open/invoke", json={"input": {'country': input_text}})
    
    # Print the raw response to debug
    print("OpenAI Response Status Code:", response.status_code)
    print("OpenAI Raw Response:", response.text)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get('output', {}).get('content', "Unexpected response structure: {}".format(data))
        except ValueError:
            return "Error decoding JSON response"
    else:
        return "Request failed with status code {}".format(response.status_code)

def get_gemma_response(input_text):
    response = requests.post("http://localhost:8000/gemma/invoke", json={"input": {'country': input_text}})
    
    # Print the raw response to debug
    print("Gemma Response Status Code:", response.status_code)
    print("Gemma Raw Response:", response.text)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get('output', "Unexpected response structure: {}".format(data))
        except ValueError:
            return "Error decoding JSON response"
    else:
        return "Request failed with status code {}".format(response.status_code)



# Streamlit interface
st.title("Langchain")
input1 = st.text_input("how i can help you")
input2 = st.text_input("Ask anything")

if input1:
    st.write(get_openai_response(input1))

if input2:
    st.write(get_gemma_response(input2))







