```python
import os
# 设置 OpenAI API 密钥
os.environ["OPENAI_API_KEY"] = "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"

from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
```


```python
loader = TextLoader("./../data/sgyy_abstract.txt")
documents = loader.load()
#print(documents)
```

使用RecursiveCharacterTextSplitter替代CharacterTextSplitter


```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separators=["\n", "。", "，", "？", "！","。"]
)
texts = text_splitter.split_documents(documents)
print(f"分割后的文档数量: {len(texts)}")
```

    分割后的文档数量: 9



```python
embeddings = OpenAIEmbeddings()
#embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/Conan-embedding-v1")
```



```python
docsearch = Chroma.from_documents(texts, embeddings)
```


```python
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
    return_source_documents=True  # 添加此参数
)
```

      llm=OpenAI(),



```python
query = "刘备的兄弟有哪些"
result = qa.invoke({"query": query})  # 使用字典形式传递查询
print(result)
```

    {'query': '刘备的兄弟有哪些', 'result': ' 刘备除了张飞和关羽，还有一个结义兄弟是刘表。', 'source_documents': [Document(metadata={'source': './../data/sgyy_abstract.txt'}, page_content='刘备除了张飞和关羽，还有一个结义兄弟是刘表。'), Document(metadata={'source': './../data/sgyy_abstract.txt'}, page_content='《三国演义》（精校版全本）作者：罗贯中\n \n内容简介'), Document(metadata={'source': './../data/sgyy_abstract.txt'}, page_content='。宋代讲故事的风气盛行，说书成为一种职业，说书人喜欢拿古代人物的故事作为题材来敷演，而陈寿撰、裴松之注的《三国志》里面的人物众多，以多个主人公做线索，事件纷繁，正是撰写故事的最好素材'), Document(metadata={'source': './../data/sgyy_abstract.txt'}, page_content='三国演义》由东汉末年黄巾起义末期开始描写，至西晋初期国家重归统一结束，以魏、蜀、吴三个政治、军事集团之间的形成演变，矛盾斗争为主线，最后由晋统一全国，国家重归统一')]}

