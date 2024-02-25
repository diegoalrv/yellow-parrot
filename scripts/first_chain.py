import langchain
import json

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    print(langchain.__version__)
    # credentials_path
    file_path = '/app/credentials/openia_api_key.json'

    # Read JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)  # Load data as dictionary

    # Extract API_KEY to variable
    openai_api_key = data['API_KEY']

    llm = ChatOpenAI(openai_api_key=openai_api_key)

    print(llm.invoke("how can langsmith help with testing?"))
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class technical documentation writer."),
        ("user", "{input}")
    ])

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    invoke = chain.invoke({"input": "how can langsmith help with testing?"})
    print(invoke)
    pass

if __name__ == '__main__':
    main()