import streamlit as st
import pandas as pd
from serpapi_tool import get_product_data

st.set_page_config(page_title="Shop Out Tool", layout="centered")
st.title("🛍️ Shop Out - Compare Product Prices")

product = st.text_input("Enter a product to shop out:")

if st.button("Run Shop Out"):
    with st.spinner("Fetching updated data..."):
        df = get_product_data(product)

        if df.empty:
            st.warning("No valid product links found.")
        else:
            df["Google_Shop"] = df["product_link"].apply(
                lambda x: f'<a href="{x}" target="_blank">🔗 View</a>'
            )

            df_display = df.drop(columns=["product_link"])
            df_display = df_display.rename(columns={
                "normal_price": "Normal_Price",
                "promotion_price": "Promotion_Price",
                "title": "Product_Name",
                "source": "Retailer_Name"
            })

            st.markdown(df_display.to_html(escape=False, index=False), unsafe_allow_html=True)

            df.to_csv("shop_out_results.csv", index=False)
            with open("shop_out_results.csv", "rb") as f:
                st.download_button("📥 Download CSV", f, "shop_out_results.csv", "text/csv")
