# AI Agent Project

## Overview
This application works like an AI Agent that reads through a dataset (CSV or Google Sheets) and performs a web search to retrieve specific information for each entity in a chosen column. The AI parses the web results based on the user's query and formats the extracted data in a structured output using the language model. The project includes building a simple dashboard where users can upload a file, define search queries, and view/download the results.

## Setup Instructions
1. Clone the Repository
   ``` 
   git clone 
   ```
2. Create a virtual env
   ``` python
   python -m venv venv
   ```
3. Load the virtual env
4. Install the dependencies
    ```python
    pip install -r requirements.txt
    ```
5. create a .env file and add your own api keys and request limit
   ```.env
   SEARCH_API_KEY = 
    GROQ_API_KEY = 
    MAX_REQUESTS = 10
   ```
