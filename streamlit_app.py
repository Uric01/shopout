import streamlit as st
import pandas as pd
from serpapi_tool import get_product_data
from utils import save_df_to_csv

st.set_page_config(page_title="Shop Out Tool", layout="centered")
st.title("🛍️ Shop Out - Compare Product Prices")

# 1️⃣ Use session_state to remember the product query and DataFrame
if "product_name" not in st.session_state:
    st.session_state.product_name = ""
if "results_df" not in st.session_state:
    st.session_state.results_df = pd.DataFrame()

# 2️⃣ Text input bound to session_state
st.session_state.product_name = st.text_input(
    "Enter a product to shop out:",
    value=st.session_state.product_name,
    key="input_box"
)

# 3️⃣ Run search and store results in session_state
if st.button("Run Shop Out"):
    with st.spinner("Fetching live data..."):
        df = get_product_data(st.session_state.product_name)
        st.session_state.results_df = df.copy()
        save_df_to_csv(df)

# 4️⃣ If we have results in state, display them and show download
df = st.session_state.results_df
if not df.empty:
    st.success(f"Found {len(df)} valid results.")
    
    # Build clickable link column
    df_display = df.copy()
    df_display["Google_Shop"] = df_display["product_link"].apply(
        lambda x: f'<a href="{x}" target="_blank">Click Me</a>'
    )
    df_display = (
        df_display
        .drop(columns=['product_link'])
        .rename(columns={
            'title': 'Product_Name',
            'normal_price': 'Normal_Price',
            'promotion_price': 'Promotion_Price',
            'source': 'Retailer_Name'
        })
    )
    
    st.markdown(
        df_display.to_html(escape=False, index=False),
        unsafe_allow_html=True
    )

    # Download button (won't clear session_state)
    with open("shop_out_results.csv", "rb") as f:
        st.download_button(
            "📥 Download CSV",
            data=f,
            file_name="shop_out_results.csv",
            mime="text/csv"
        )
