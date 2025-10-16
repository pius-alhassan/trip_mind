import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(data_path):
    """Loads the raw data from a specified path."""
    return pd.read_csv(data_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Performs initial data cleaning."""
    # e.g., Handle 'No Negative'/'No Positive' in review columns
    # e.g., Convert `Review_Date` to datetime
    # e.g., Extract features from `Tags` (e.g., Leisure trip, Couple, etc.)
    return df

def split_data(df: pd.DataFrame, test_size=0.2, random_state=42):
    """Splitting data into train and test sets."""
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    return train_df, test_df

if __name__ == '__main__':
    # Example usage
    df = load_data('../../data/raw/hotel_data.csv')
    df_clean = clean_data(df)
    train, test = split_data(df_clean)
    train.to_csv('../../dataset/processed_dataset/train.csv', index=False)
    test.to_csv('../../dataset/processed_dataset/test.csv', index=False)