import streamlit as st
from serpapi_tool import get_product_data
from utils import save_df_to_csv

st.set_page_config(page_title="Shop Out Tool", layout="centered")

st.title("🛍️ Shop Out - Compare Product Prices")

product = st.text_input("Enter a product to shop out:")

if st.button("Run Shop Out"):
    with st.spinner("Searching..."):
        df = get_product_data(product)
        if df.empty:
            st.warning("No valid product links found.")
        else:
            save_df_to_csv(df)
            st.success(f"Found {len(df)} valid results.")
            st.dataframe(df)

            with open("shop_out_results.csv", "rb") as f:
                st.download_button("📥 Download CSV", f, file_name="shop_out_results.csv", mime="text/csv")
