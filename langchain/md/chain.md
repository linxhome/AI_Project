```python
import os
# 设置 OpenAI API 密钥
os.environ["OPENAI_API_KEY"] = "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"

from langchain import PromptTemplate,OpenAI,LLMChain
from langchain.memory import ConversationBufferMemory
llm = OpenAI(temperature=0.1)
```


```python
# simple Chain
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good product name for {product}?"
)
## chain的特别之处是每个参数都是component，chain 由一系列的component 组合在一起完成特定的任务,chain 本身也可以作为一个component ，组装成更复杂的调用链
llm_chain = LLMChain(llm=llm,prompt=prompt)
result = llm_chain.run("a kind of thin mobile phone")
print(result)
```

    
    
    "SlenderTech" or "SlimLine"



```python
# Memory Chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain import ConversationChain

# Chain 的第一个特性就是有状态，可以记住会话的历史，是通过 Memory 模块来实现的
memory = ConversationBufferMemory()
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
    The following is a conversation between a human and an AI. The AI is helpful and friendly.please answer the questions with Chinese

    {history}
    Human: {input}
    AI:
    """
)

llm_chain = LLMChain(llm=llm,memory=memory,prompt=prompt)
result = llm_chain.run("窗前明月光的下一句是什么")
print(result)


```

    疑是地上霜。



```python
result = llm_chain.run("who wrote this?")
print(result)
```

    这首诗是由唐代诗人李白写的。



```python


#location chain
template = """你的任务是查到当前城市所在地最著名的一道美食 % USER LOCATION
{user_location}
"""
prompt_template = PromptTemplate(input_variables=["user_location"], template=template)
location_chain = LLMChain(llm=llm, prompt=prompt_template)

# meal_chain
template = """根据前面提到的美食名称，找到这个美食的菜谱 % MEAL
{meal}
"""
prompt_template = PromptTemplate(input_variables=["meal"], template=template)
meal_chain = LLMChain(llm=llm, prompt=prompt_template)

# sequential chain
from langchain.chains import SimpleSequentialChain
overall_chain = SimpleSequentialChain(chains=[location_chain, meal_chain],verbose=True)
review = overall_chain.run("南京")
```

    Error in StdOutCallbackHandler.on_chain_start callback: AttributeError("'NoneType' object has no attribute 'get'")


    [36;1m[1;3m南京的最著名美食是鸭血粉丝汤。这道汤是由鸭血、粉丝、肉片和各种配料熬制而成，口感鲜美，营养丰富。它是南京的传统名吃，被誉为“江南第一汤”。许多游客来到南京必定要品尝这道美食，体验南京的美食文化。[0m
    [33;1m[1;3m以下是鸭血粉丝汤的制作步骤：
    
    材料：
    1. 鸭血 500克
    2. 粉丝 100克
    3. 猪肉 200克
    4. 香菇 50克
    5. 豆腐 100克
    6. 青菜 100克
    7. 葱姜蒜适量
    8. 酱油、盐、料酒、味精适量
    
    步骤：
    1. 将鸭血切成小块，用盐水浸泡30分钟，去除血水。
    2. 将粉丝用温水浸泡20分钟，使其变软。
    3. 将猪肉切成薄片，用料酒、盐、味精腌制10分钟。
    4. 将香菇、豆腐、青菜洗[0m
    
    [1m> Finished chain.[0m

