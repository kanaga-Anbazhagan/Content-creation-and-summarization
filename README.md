    # AI Content Manager and Summarization Service

This project is an AI-powered content management and summarization service built with LangChain, Groq API, and Flask. The service enables users to generate high-quality articles or blogs based on a given topic and to summarize existing content efficiently. The backend is designed using Flask to provide a RESTful API that communicates with the Groq-based LLM (Large Language Model) for content generation and summarization tasks.

## Features
1. **Content Generation**: The service generates high-quality content or articles based on a provided topic.
2. **Content Summarization**: The service summarizes existing content, making it concise and easy to understand while retaining the key information.
3. **RESTful API**: The project uses Flask to create an API that allows users to interact with the content generation and summarization functionalities.
4. **Groq Integration**: Utilizes the Groq API to interact with the LLaMA language model to generate and summarize content.

## Technologies Used
- **LangChain**: For working with templates and managing prompt-based chains.
- **Groq API**: For using the LLaMA language model to generate and summarize content.
- **Flask**: A lightweight web framework for building the API and managing HTTP requests.
- **Flask-CORS**: For enabling Cross-Origin Resource Sharing (CORS), allowing the frontend to communicate with the backend.
- **Python**: Programming language used for the backend implementation.

## API Endpoints

### 1. `/generate_text` [POST]
Generates content based on a given topic.

#### Request Body:
```json
{
  "prompt": "Your topic description here."
}

## License
This project is licensed under the MIT License.

## Acknowledgments
- **LangChain**: A powerful library for working with language models and managing prompt chains.
- **Groq API**: Used for leveraging the LLaMA language model for content generation and summarization tasks.
- **Flask**: A lightweight web framework for building the backend API.
- **Flask-CORS**: Helps in enabling CORS for smooth communication between frontend and backend.
