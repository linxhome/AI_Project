import langchain
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.embeddings import HuggingFaceEmbeddings

loader = TextLoader("data/sgyy_abstract.txt")
documents = loader.load()
#print(documents)

# 使用RecursiveCharacterTextSplitter替代CharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separators=["\n", "。", "，", "？", "！","。"]
)

texts = text_splitter.split_documents(documents)
print(f"分割后的文档数量: {len(texts)}")

embeddings = OpenAIEmbeddings()
#embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/Conan-embedding-v1")

docsearch = Chroma.from_documents(texts, embeddings)

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
    return_source_documents=True  # 添加此参数
)

query = "刘备的兄弟有哪些"
result = qa({"query": query})  # 使用字典形式传递查询

print("回答：")
print(result["result"])
print("\n相关的搜索 chunks：")
for doc in result["source_documents"]:
    print(f"Chunk: {doc.page_content}")
    print("-" * 50)

