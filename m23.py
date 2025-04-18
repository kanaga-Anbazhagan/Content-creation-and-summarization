from langchain.llms import Groq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Set up the Groq API key (ensure it's set as an environment variable or use the above method)
api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq LLM with the API key
groq_llm = Groq(api_key=api_key)

# Define a prompt for summarization or other tasks
prompt_template = "Summarize the following content: {content}"
prompt = PromptTemplate(input_variables=["content"], template=prompt_template)

# Set up the chain with Groq LLM and prompt
llm_chain = LLMChain(prompt=prompt, llm=groq_llm)

# Example input text
text = "Groq models provide high-performance inference for a wide variety of NLP tasks."

# Get the result by passing the text through the chain
result = llm_chain.run(content=text)

print(result)



