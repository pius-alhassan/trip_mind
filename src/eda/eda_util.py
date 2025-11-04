"""
eda_setup.py — common EDA setup for the Trip Mind project.
Handles imports, visualization settings, and dataset loading.
"""

import os
import warnings

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Suppress warnings ---
warnings.filterwarnings("ignore")

# --- Visualization setup ---
plt.style.use("seaborn-v0_8")
sns.set_palette("husl")
plt.rcParams["figure.figsize"] = (12, 8)


def load_data(path: str = None):
    """
    Loading of the Hotel Reviews dataset from the given or default path.

    Args:
        path (str): Optional. Custom path to CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    if path is None:
        # Default path (relative to project root)
        path = os.path.join(
            os.path.dirname(__file__), 
            "dataset", 
            "raw_dataset", 
            "Hotel_Reviews.csv"
        )

    try:
        df = pd.read_csv(path)
        print("✅ Data loaded successfully!")
        return df
    except FileNotFoundError:
        print(f"❌ File not found at: {path}")
        raise
