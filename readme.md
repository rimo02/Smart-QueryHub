# AI Agent Project

## Overview
This application serves as an AI-powered agent that reads data from either a CSV file or Google Sheets, then performs a web search to gather specific information for each entity listed in a chosen column. The outputs are then passed to a language model - Grok(xAI) to answer the relevant question. The project includes a simple dashboard that enables users to upload a file, define search queries, and view or download the final results.

## Features
- File Upload and Google Sheets Integration: Users can upload a CSV file or connect to a Google Sheet, select a main column (e.g., company names), and preview the data.
- Custom Query Input: A text box for users to specify a query with placeholders, like “Get me the email address of {company}, or show me offic e locations of {entity}” where each entity is dynamically inserted.
- Automated Web Search: For each entity, the agent performs a web search to gather relevant results, utilizing SerpAPI.
- LLM-Based Parsing: The application sends search results to an LLM( **Grok**), which extracts the required information (e.g., email, address).
- Data Display and Download: Display extracted data in a table format, and download the results as a CSV or write them directly to Google Sheets.

## Setup Instructions

1. Clone the Repository
   ```bash
   git clone https://github.com/rimo02/BreakoutAI.tech-Assignment.git
   ```

2. Create a Virtual Environment
   ```bash
   python -m venv venv
   ```

3. Activate the Virtual Environment
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Set Up Environment Variables
   - Create a `.env` file in the root directory.
   - Add the following details:
     ```plaintext
     SEARCH_API_KEY=<Your serp  API Key>
     GROQ_API_KEY=<Your LLM API Key>
     MAX_REQUESTS=10  # Set request limit to handle rate limiting. This represents the maximum value of requests you can make to the agent before getting the desired output.
     ```
 6. Go to [Google Cloud Console](https://console.cloud.google.com).
   - Create a new project and navigae to API and Services
   -  Search for Google Sheets API and click enable to enable it.
   -  Go to API & Services > Credentials. Click Create Credentials and select Service account. Fill Service account details. For role select Editor > Done
   -  Go to Credentials > Add Key > Create New Key. Select JSON as the key type.
   -  Download  it in the same directory of the project.

## Usage Guide
1. Running the Application
   ```bash
   streamlit run app.py
   ```

2. Using the Dashboard
   - Upload a CSV or connect to Google Sheets by entering credentials.
   - Choose the primary column with entities (e.g., companies) for information retrieval.
   - Enter a custom query with placeholders, like “Get the address of {company}.”
   - View the extracted information, and download it as a CSV or update Google Sheets.

## API Keys and Environment Variables
Add the required API keys for web search (e.g., SerpAPI, ScraperAPI) and the LLM (e.g., Groq or OpenAI). These should be stored securely in the `.env` file as shown above.

## Optional Features
This project includes:
- Advanced Query Templates: Extract multiple fields in a single prompt, e.g., “Get the email and address for {company}.”

## Loom Video Walkthrough
For a quick overview, check out the [video walkthrough](https://www.loom.com/share/2ba192aa81d849369b8df693fc91f9a8?sid=942791d2-3bd1-47b7-a8c6-be3dbdcfbe21) of the project.
