import pandas as pd

def save_df_to_csv(df: pd.DataFrame, filename: str = "shop_out_results.csv") -> str:
    """
    Saves the DataFrame to a CSV file and returns the file path.
    """
    df.to_csv(filename, index=False)
    return filename