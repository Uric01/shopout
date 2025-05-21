import streamlit as st
import pandas as pd
from serpapi_tool import get_product_data
from utils import save_df_to_csv

st.set_page_config(page_title="Shop Out Tool", layout="centered")
st.title("🛍️ Shop Out - Compare Product Prices")

product = st.text_input("Enter a product to shop out:")

if st.button("Run Shop Out"):
    with st.spinner("Searching..."):
        # Ensure get_product_data always returns a DataFrame
        df = get_product_data(product)

        if df is None:
            st.error("Failed to fetch data. Please check your API key or network.")
        elif df.empty:
            st.warning("No valid product links found.")
        else:
            save_df_to_csv(df)
            st.success(f"Found {len(df)} valid results.")
            st.dataframe(df)

            with open("shop_out_results.csv", "rb") as f:
                st.download_button(
                    "📥 Download CSV",
                    data=f,
                    file_name="shop_out_results.csv",
                    mime="text/csv"
                )