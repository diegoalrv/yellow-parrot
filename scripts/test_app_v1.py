import langchain
from langchain_openai import ChatOpenAI
import json

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
    
    pass

if __name__ == '__main__':
    main()