import pandas as pd
import requests
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

api_key = os.environ.get("GROQ_API_KEY")

url = "https://api.x.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {api_key}'
}


def upload_csv(file):
    return pd.read_csv(file)


def connect_google_sheet(sheet_url: str):
    credentials = service_account.Credentials.from_service_account_file(
        './oauth-438319-90e257859786.json')
    service = build('sheets', 'v4', credentials=credentials)
    sheet_id = sheet_url.split("/d/")[1].split("/")[0]
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range="List").execute()
    values = result.get("values", [])

    return pd.DataFrame(values[1:], columns=values[0])


def run_web_search(query):
    serp_api_key = os.getenv("SEARCH_API_KEY")
    if not api_key:
        st.error(
            "API key not found. Please set your SEARCH_API_KEY environment variable.")
        return []
    url = f"https://serpapi.com/search.json?q={query}&api_key={serp_api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("organic_results", [])
    except requests.exceptions.RequestException as e:
        st.error(f'Error during web search: {e}')
        return []


def extract_info_from_llm(search_query, search_result):
    prompt = f"""
    Based on the JSON data provided, identify the information that most directly answers the question. 
    If the question asks for a specific type of data (e.g., email, phone number, location), focus on extracting only that information. 
    Return the relevant answer as a single JSON array of strings, formatted like ["result1", "result2"], without additional context or structure.

    Question: {search_query}

    JSON Data:
    {search_result}
    """
    data = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "grok-beta"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        resp_json = response.json()
        return resp_json['choices'][0]['message']['content']
    # chat_completion1 = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": prompt,
    #         }
    #     ],
    #     model="llama3-8b-8192",
    # )
    # output = chat_completion1.choices[0].message.content

    # refine_prompt = f"""
    # Refine the answer to contain only the most relevant information in response to the question,
    # formatted strictly as a JSON array of strings. Exclude any additional text or context.

    # Question: {search_query}

    # Response: {output}
    # """

    # chat_completion2 = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": refine_prompt,
    #         }
    #     ],
    #     model="llama3-8b-8192",
    # )

    # refined_output = chat_completion2.choices[0].message.content

    # try:
    #     return json.loads(refined_output)
    # except json.JSONDecodeError:
    #     return refined_output.splitlines()
