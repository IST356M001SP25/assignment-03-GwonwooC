'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st
import packaging
from io import StringIO
import json

st.title("Process Package Files")

if 'summaries' not in st.session_state:
    st.session_state.summaries = []
if 'total_lines' not in st.session_state:
    st.session_state.total_lines = 0
if 'total_files' not in st.session_state:
    st.session_state.total_files = 0

uploaded_file = st.file_uploader("Upload package file:")

if uploaded_file:
    file_name = uploaded_file.name
    output_json = file_name.replace(".txt", ".json")
    package_list = []
    
    file_content = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
    for line in file_content.split("\n"):
        line = line.strip()
        if line:
            parsed_package = packaging.parse_packaging(line)
            package_list.append(parsed_package)
    
    package_count = len(package_list)
    with open(f"./data/{output_json}", "w") as json_file:
        json.dump(package_list, json_file, indent=4)
    
    summary = f"{package_count} packages written to {output_json}"
    st.session_state.summaries.append(summary)
    st.session_state.total_files += 1
    st.session_state.total_lines += package_count
    
    for s in st.session_state.summaries:
        st.info(s, icon="💾")
    
    st.success(f"{st.session_state.total_files} files processed, {st.session_state.total_lines} total lines processed")
