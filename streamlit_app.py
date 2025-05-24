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
        #df = pd.read_csv("link_test.csv")
        df = get_product_data(product)

        if df is None:
            st.error("Failed to fetch data. Please check your API key or network.")
        elif df.empty:
            st.warning("No valid product links found.")
        else:
            save_df_to_csv(df)
            st.success(f"Found {len(df)} valid results.")
            #st.dataframe(df.to_html(escape=False, index=False))
            df["Google_Shop"] = df['product_link'].apply(
                lambda x: f'<a href="{x}" target="_blank" style="text-decoration: none;">Click Me</a>'
                )
            df = df.drop(columns=['product_link'])
            df = df.rename(columns={'normal_price': 'Normal_Price', 'title': 'Product_Name', 'source': 'Retailer_Name','promotion_price': 'Promotion_Price'})
            st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

            with open("shop_out_results.csv", "rb") as f:
                st.download_button(
                    "📥 Download CSV",
                    data=f,
                    file_name="shop_out_results.csv",
                    mime="text/csv"
                )
                
                

