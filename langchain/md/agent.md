```python
import os
# 设置 OpenAI API 密钥
os.environ["OPENAI_API_KEY"] = "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"
```

定义一个tool，以及对它的参数描述


```python
from langchain.agents import tool
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent

# tools
@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

tools = [get_word_length]
```

创建一个agent，并把tools 包含进去


```python
from langchain.agents import AgentType

llm = ChatOpenAI(temperature=0)
agent = initialize_agent(tools,llm, agent=AgentType.OPENAI_FUNCTIONS)
result = agent.run("how many letters in the word 'Internationalization'?")
print(result)

```

    The word "Internationalization" has 20 letters.

