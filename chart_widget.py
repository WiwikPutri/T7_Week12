# ==========================================
# NAMA  : WIWIK PUTRI
# NIM   : F1D02310096
# KELAS : C
# ==========================================

import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0, 0, 0, 0)

    def update_chart(self, df_filtered, category_title, chart_type):
        self.axes.clear()
        
        if df_filtered.empty:
            self.axes.text(0.5, 0.5, f"Tidak ada data untuk {category_title}", 
                           ha='center', va='center', fontsize=12, color='gray')
            self.canvas.draw()
            return

        if chart_type == "Bar Chart (Penjualan per Kota)":
            city_sales = df_filtered.groupby('City', sort=False)['Sales'].sum().reset_index()
            bars = self.axes.bar(city_sales['City'], city_sales['Sales'], color='#2ecc71', edgecolor='#27ae60', width=0.4)
            self.axes.set_title(f"Total Penjualan per Kota\n({category_title})", fontsize=11, fontweight='bold', pad=10)
            self.axes.set_ylabel("Sales (USD)")
            self.axes.grid(axis='y', linestyle='--', alpha=0.5)
            
            for bar in bars:
                yval = bar.get_height()
                self.axes.text(bar.get_x() + bar.get_width()/2, yval + (yval*0.01), f"${yval:,.2f}", ha='center', va='bottom', fontsize=9)

        elif chart_type == "Pie Chart (Tipe Pelanggan)":
            cust_sales = df_filtered.groupby('Customer type', sort=False)['Sales'].sum()
            self.axes.pie(cust_sales, labels=cust_sales.index, autopct='%1.1f%%', 
                          colors=['#3498db', '#f1c40f'], startangle=90, textprops={'fontsize': 10})
            self.axes.set_title(f"Proporsi Penjualan Berdasarkan Tipe Pelanggan\n({category_title})", fontsize=11, fontweight='bold', pad=10)

        elif chart_type == "Line Chart (Tren Penjualan Harian)":
            # Data dijamin sudah bertipe datetime dan urut kronologis dari data_handler
            date_sales = df_filtered.groupby('Date', sort=True)['Sales'].sum().reset_index()
            
            self.axes.plot(date_sales['Date'], date_sales['Sales'], marker='o', 
                           color='#e74c3c', linewidth=2, markersize=4)
            
            self.axes.set_title(f"Tren Penjualan Harian\n({category_title})", fontsize=11, fontweight='bold', pad=10)
            self.axes.set_ylabel("Sales (USD)")
            self.axes.tick_params(axis='x', rotation=30, labelsize=8)
            self.axes.grid(True, linestyle='--', alpha=0.5)

        elif chart_type == "Donut Chart (Distribusi Gender)":
            gender_sales = df_filtered.groupby('Gender', sort=False)['Sales'].sum()
            self.axes.pie(gender_sales, labels=gender_sales.index, autopct='%1.1f%%', 
                          colors=['#e84393', '#0984e3'], startangle=140, textprops={'fontsize': 10},
                          wedgeprops=dict(width=0.4, edgecolor='w'))
            self.axes.set_title(f"Kontribusi Penjualan Berdasarkan Gender\n({category_title})", fontsize=11, fontweight='bold', pad=10)

        self.fig.tight_layout()
        self.canvas.draw()