from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq






prompt = ChatPromptTemplate.from_template(
        """
  {input}.
 """
    )


llm=ChatGroq(groq_api_key="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", 
             model_name="llama-3.1-8b-instant")  #llama3-groq-70b-8192-tool-use-preview
                                                 #llama-3.1-8b-instant
def response(topic):
        llm_chain = LLMChain(
                llm=llm,
                prompt=prompt,
                verbose=False)

        response =llm_chain.invoke({"input":topic})
        return response['text']



for i in range (100):
    topic = input(" enter you text")
    print(response(topic))



 