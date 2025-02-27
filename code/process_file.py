'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
import packaging
from io import StringIO
import json

st.title("Process File of Packages")

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
            total_units = packaging.calc_total_units(parsed_package)
            primary_unit = packaging.get_unit(parsed_package)
            package_list.append(parsed_package)
            st.info(f"{line} ➡️ Total 📦 Size: {total_units} {primary_unit}")
    
    package_count = len(package_list)
    with open(f"./data/{output_json}", "w") as json_file:
        json.dump(package_list, json_file, indent=4)
    
    st.success(f"{package_count} packages saved to {output_json}", icon="💾")
