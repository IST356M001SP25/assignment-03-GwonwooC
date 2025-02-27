'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import packaging

st.title("Process One Packages")

pkg_input = st.text_input("Enter package data:")

if pkg_input:
    parsed_data = packaging.parse_packaging(pkg_input)
    total_size = packaging.calc_total_units(parsed_data)
    unit_type = packaging.get_unit(parsed_data)
    
    st.write("### Package Details")
    for entry in parsed_data:
        item_name = list(entry.keys())[0]
        item_count = list(entry.values())[0]
        st.info(f"{item_name} ➡️ {item_count}")
    
    st.success(f"Total Package Size: {total_size} {unit_type}")