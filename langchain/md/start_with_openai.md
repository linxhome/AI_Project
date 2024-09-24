```python
import os
# 设置 OpenAI API 密钥
os.environ["OPENAI_API_KEY"] = "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"


from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
```


```python
llm = ChatOpenAI(model_name="gpt-4o-mini",max_tokens=1024)
messages = [
    HumanMessage(content="给水果店取一个名字"),
]

resp = llm.invoke(messages)
print(resp.content)
```

    当然可以！以下是一些水果店的名字建议：
    
    1. 果香四溢
    2. 水果乐园
    3. 鲜果天地
    4. 果实之家
    5. 甜蜜果坊
    6. 鲜果集
    7. 果趣人生
    8. 自然果语
    9. 果味人生
    10. 绿意果园
    
    希望这些名字能给你一些灵感！如果你有特定的主题或风格需求，也可以告诉我，我可以提供更符合你想法的建议。

