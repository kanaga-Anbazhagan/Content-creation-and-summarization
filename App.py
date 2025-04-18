
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from flask import Flask, request, jsonify, send_file
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  




llm=ChatGroq(groq_api_key="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",
             model_name="llama-3.1-8b-instant")  






prompt = ChatPromptTemplate.from_template(
        """
You are a highly skilled and versatile content writer specializing in generating high-quality articles and blogs.
 Your goal is to craft engaging, informative, and well-structured content based on the user's prompts. 
 
  Follow these guidelines:
            1)Understand the Topic: Analyze the user's input topic or description thoroughly to determine the core subject and context.
            2)Tone and Style: Adapt the tone and style to the user's preferences (e.g., professional, conversational, creative, persuasive). Use clear, concise, and impactful language.
            3)Structure: Organize the content logically with appropriate headings, subheadings, bullet points, or lists as needed. Ensure smooth transitions between sections.
            4)Depth: Provide a comprehensive exploration of the topic while avoiding excessive verbosity. Use facts, examples, and relevant data where applicable.
            5)Ethics: Ensure the content is original, non-plagiarized, and free from bias or harmful language.

            output format :
              Deliver a complete article or blog that meets guideliness. 
             
              
              
              
         Here your topic:   {input}.
 """
    )










                                             
def response(topic):
        llm_chain = LLMChain(
                llm=llm,
                prompt=prompt,
                verbose=False)

        response =llm_chain.invoke({"input":topic})
        return response['text']






prompt1 = ChatPromptTemplate.from_template(
        """
You are an advanced AI model specializing in text summarization. 
Your goal is to create concise and accurate summaries while preserving the key information and context of the original text. 
Follow these rules while summarizing:
            1)Ensure the summary is coherent and easy to understand.
            2)Avoid adding any new information or making assumptions.
            3)Remove redundant or repetitive details.
            4)Keep the tone neutral unless instructed otherwise.
            5)If the input text is highly technical, maintain its terminology but make it accessible.
            6)Format the summary in bullet points if the input contains distinct points or sections; otherwise, use paragraph form.
             Here your content:   {input}.
 """
    )






def response_summarization(topic):
        llm_chain = LLMChain(
                llm=llm,
                prompt=prompt1,
                verbose=False)

        response =llm_chain.invoke({"input":topic})
        return response['text']







@app.route('/generate_text', methods=['POST'])
def generate_text():
    try:
        data = request.json
        topic = data.get('prompt')
        if not topic:
            return jsonify({'error': 'No topic provided'}), 400

        text_description = response(topic)
        return jsonify({'generatedContent': text_description})
    except Exception as e:
        return jsonify({'error': str(e)}), 500  
    




@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    try:
        data = request.json
        topic = data.get('content')
        if not topic:
            return jsonify({'error': 'No topic provided'}), 400

        text_description = response_summarization(topic)
        return jsonify({'summary': text_description})
    except Exception as e:
        return jsonify({'error': str(e)}), 500  







if __name__ == '__main__':
    app.run(debug=True)
                        
            
    
 
 


      
