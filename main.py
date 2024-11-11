from dotenv import load_dotenv
import os
import re
import streamlit as st
import pandas as pd
from utils import upload_csv, connect_google_sheet, run_web_search, extract_info_from_llm
import re
load_dotenv()
st.title("AI Agent Dashboard")

COUNTER_FILE = './request_count.json'


with st.sidebar:
    st.subheader("Upload CSV or Connect to Google Sheets")
    data_source = st.radio("Choose Data Source", [
                           "Upload CSV", "Google Sheets"])

    if data_source == "Upload CSV":
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file:
            df = upload_csv(uploaded_file)
    elif data_source == "Google Sheets":
        sheet_url = st.text_input("Enter Google Sheets URL")
        if sheet_url:
            df = connect_google_sheet(str(sheet_url))


if 'df' in locals():
    st.write("Data Preview")
    st.dataframe(df.head(8))
    column_name = st.selectbox("Select Main Column", df.columns)
    prompt_template = st.text_input(
        "Enter your prompt (use {entity} as placeholder)",
        placeholder="Get me the email address of {entity}"
    )

    if st.button("Run Extraction"):
        results = []
        count = 0
        for entity in df[column_name].dropna():
            if count > int(os.getenv('MAX_REQUESTS')):
                st.warning(
                    "Daily request limit reached. Download available results.")
                break
            search_query = prompt_template.format(entity=entity)
            search_results = run_web_search(search_query)
            if not search_results:
                st.error(f"No results found for entity: {entity}")
                continue
            extracted_info = extract_info_from_llm(
                search_query, search_results)
            results.append({
                "Entity": entity,
                "Extracted Info":  str(re.findall(r'\[(.*?)\]', extracted_info)) if extracted_info else "No Info found"
            })
            count += 1

        result_df = pd.DataFrame(results)
        st.write("Extraction Results")
        st.dataframe(result_df)
        st.download_button("Download CSV", result_df.to_csv(index=False))
