def save_df_to_csv(df, filename="shop_out_results.csv"):
    df.to_csv(filename, index=False)
    return filename
