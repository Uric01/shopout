import streamlit as st
import pandas as pd

# Load CSV data
df = pd.read_csv("link_test.csv")

# Add clickable links (replace 'URL' with your column name)
df["Product_Link"] = df['product_link'].apply(
    lambda x: f'<a href="{x}" target="_blank">Google Shopping Link</a>'
)
df = df.drop(columns=['product_link'])

# Add sorting widget
sort_order = st.radio(
    "Sort by number:",
    options=["Ascending", "Descending"],
    index=0
)
ascending = True if sort_order == "Ascending" else False
df_sorted = df.sort_values(by="normal_price", ascending=ascending)

# Wrap the HTML table in a scrollable container
html_table = df_sorted.to_html(escape=False, index=False)
scrollable_html = f"""
<div style="
    max-height: 400px;  /* Adjust height here */
    overflow-y: auto;
    border: 1px solid #e3e3e3;
    border-radius: 5px;
    margin: 10px 0;
">
{html_table}
</div>
"""

# Render the scrollable table
st.markdown(scrollable_html, unsafe_allow_html=True)