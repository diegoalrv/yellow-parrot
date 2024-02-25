import langchain
import json

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

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
    question = """A que se dedica la empresa 'Eliza'?"""

    print('Sin info extra')
    print()
    print(llm.invoke(question))
    print()
    print()
    print('Con info extra')
    print()

    loader = WebBaseLoader("https://elizadeco.cl/pages/nuestra-empresa")
    docs = loader.load()

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)
    
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)
    
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    response = retrieval_chain.invoke({"input": question})
    print(response["answer"])
    

    pass

if __name__ == '__main__':
    main()