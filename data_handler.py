# ==========================================
# NAMA  : WIWIK PUTRI
# NIM   : F1D02310096
# KELAS : C
# ==========================================

import pandas as pd

class DataHandler:
    def __init__(self, file_path="SuperMarketAnalysis.csv"):
        self.file_path = file_path
        self.df = None
        self.load_data()

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            self.df['Sales'] = pd.to_numeric(self.df['Sales'], errors='coerce')
            self.df['Quantity'] = pd.to_numeric(self.df['Quantity'], errors='coerce')
        except Exception as e:
            print(f"Error saat membaca file: {e}")
            self.df = pd.DataFrame()

    def get_categories(self):
        if self.df.empty:
            return []
        return sorted(self.df['Product line'].dropna().unique().tolist())

    def get_summary_stats(self, category=None):
        filtered_df = self.df
        if category and category != "Semua Kategori":
            filtered_df = self.df[self.df['Product line'] == category]

        total_items = int(filtered_df['Quantity'].sum())
        total_sales = float(filtered_df['Sales'].sum())
        return total_items, total_sales

    def get_filtered_data(self, category=None):
        if category and category != "Semua Kategori":
            return self.df[self.df['Product line'] == category].copy()
        return self.df.copy()