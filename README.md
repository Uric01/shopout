
# 🛍️ Shop Out - Compare Product Prices

A simple Streamlit-powered web tool that helps you **search and compare prices** of products across various online retailers using **SerpAPI**.

---

## 🔍 Features

- 🔎 Search for a product using a keyword (e.g., "Samsung TV 55 inch")
- 📦 Get product name, normal price, promo price, and source
- 🌐 Clickable Google Shopping links for quick access
- 📥 Download search results as a CSV file
- 🧼 Clean and interactive web interface

---

## 🧱 Tech Stack

- [Streamlit](https://streamlit.io/)
- [SerpAPI](https://serpapi.com/)
- [Pandas](https://pandas.pydata.org/)

---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-username/shop-out-tool.git
cd shop-out-tool
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set your SerpAPI key**

Create a `.env` file in the root folder and add:

```env
SERPAPI_API_KEY=your_serpapi_key
```

4. **Run the app**

```bash
streamlit run your_script.py
```

---

## 🧪 How It Works

1. User enters a product name.
2. The app queries SerpAPI to retrieve shopping results.
3. Results are cleaned and formatted into a table.
4. Each result includes product name, retailer, pricing, and a link.
5. Optionally, results can be downloaded as a CSV.

---

## 📁 Output

- `shop_out_results.csv`: A CSV file containing product details and links.

---

## 📄 License

MIT License. open for use and extension.
