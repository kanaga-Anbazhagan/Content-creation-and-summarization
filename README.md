
---

# AI Content Manager and Summarization Service

This project is an AI-powered content management and summarization service built with **LangChain**, **Groq API**, and **Flask**. The service enables users to generate high-quality articles or blogs based on a given topic and to summarize existing content efficiently. The backend is designed using Flask to provide a RESTful API that communicates with the Groq-based LLM (Large Language Model) for content generation and summarization tasks.

---

## Features

1. **Content Generation**: Generates high-quality content or articles based on a provided topic.  
2. **Content Summarization**: Summarizes existing content, making it concise and easy to understand while retaining the key information.  
3. **RESTful API**: Uses Flask to create an API for interacting with content generation and summarization functionalities.  
4. **Groq Integration**: Leverages the Groq API to interact with the LLaMA language model for generating and summarizing content.

---

## Technologies Used

- **LangChain**: For managing prompt-based chains and working with templates.  
- **Groq API**: To access the LLaMA language model for text generation and summarization.  
- **Flask**: Lightweight web framework for building the REST API.  
- **Flask-CORS**: Enables Cross-Origin Resource Sharing for frontend-backend communication.  
- **Python**: Primary programming language for backend development.

---

## API Endpoints

### 1. `/generate_text` [POST]  
Generates content based on a given topic.

#### Request Body:
```json
{
  "prompt": "Your topic description here."
}
```

#### Response:
```json
{
  "generated_text": "Generated content based on the provided topic."
}
```

---

### 2. `/summarize_text` [POST]  
Summarizes the given content.

#### Request Body:
```json
{
  "text": "Long content that needs to be summarized."
}
```

#### Response:
```json
{
  "summary": "Summarized version of the input content."
}
```

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgments

- **LangChain** – For managing language model interactions effectively.  
- **Groq API** – For enabling fast and powerful LLM capabilities.  
- **Flask** – For building a scalable RESTful backend.  
- **Flask-CORS** – For smooth integration with frontend services.

---

