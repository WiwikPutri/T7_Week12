# ==========================================
# NAMA  : WIWIK PUTRI
# NIM   : F1D02310096
# KELAS : C
# ==========================================

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, 
                             QTableWidgetItem, QComboBox, QLabel, QGroupBox, QHeaderView)
from PySide6.QtCore import Qt
from data_handler import DataHandler
from chart_widget import ChartWidget

class SupermarketDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.data_manager = DataHandler()
        self.init_ui()
        self.populate_filters()
        self.refresh_dashboard()

    def init_ui(self):
        main_layout = QHBoxLayout(self)
        
        table_group = QGroupBox("Data Transaksi Supermarket")
        table_layout = QVBoxLayout(table_group)
        
        self.table = QTableWidget()
        headers = ["Invoice ID", "Branch", "City", "Customer Type", "Product Line", "Quantity", "Sales"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setAlternatingRowColors(True)
        
        table_layout.addWidget(self.table)
        main_layout.addWidget(table_group, stretch=6)

        right_panel = QVBoxLayout()
        
        filter_data_group = QGroupBox("Filter Data")
        filter_data_layout = QHBoxLayout(filter_data_group)
        filter_data_layout.addWidget(QLabel("Pilih Lini Produk:"))
        self.combo_filter_data = QComboBox()
        self.combo_filter_data.currentTextChanged.connect(self.refresh_dashboard)
        filter_data_layout.addWidget(self.combo_filter_data)
        right_panel.addWidget(filter_data_group)
        
        filter_chart_group = QGroupBox("Filter Tampilan Grafik")
        filter_chart_layout = QHBoxLayout(filter_chart_group)
        filter_chart_layout.addWidget(QLabel("Pilih Jenis Chart:"))
        self.combo_filter_chart = QComboBox()
        self.combo_filter_chart.currentTextChanged.connect(self.refresh_dashboard)
        filter_chart_layout.addWidget(self.combo_filter_chart)
        right_panel.addWidget(filter_chart_group)
        
        kpi_group = QGroupBox("Ringkasan Performa Data")
        kpi_layout = QHBoxLayout(kpi_group)
        
        self.lbl_total_items = QLabel("Total Kuantitas: 0 unit")
        self.lbl_total_sales = QLabel("Total Penjualan: $0.00")
        self.lbl_total_items.setStyleSheet("font-weight: bold; font-size: 12px; color: #34495e;")
        self.lbl_total_sales.setStyleSheet("font-weight: bold; font-size: 12px; color: #27ae60;")
        
        kpi_layout.addWidget(self.lbl_total_items)
        kpi_layout.addWidget(self.lbl_total_sales)
        right_panel.addWidget(kpi_group)
        
        self.chart = ChartWidget()
        right_panel.addWidget(self.chart, stretch=1)
        
        main_layout.addLayout(right_panel, stretch=4)

    def populate_filters(self):
        self.combo_filter_data.addItem("Semua Kategori")
        categories = self.data_manager.get_categories()
        self.combo_filter_data.addItems(categories)
        
        self.combo_filter_chart.addItems([
            "Bar Chart (Penjualan per Kota)",
            "Pie Chart (Tipe Pelanggan)",
            "Line Chart (Tren Penjualan Harian)",
            "Donut Chart (Distribusi Gender)"
        ])

    def refresh_dashboard(self):
        selected_category = self.combo_filter_data.currentText()
        selected_chart = self.combo_filter_chart.currentText()
        
        if not selected_chart:
            return
            
        df_filtered = self.data_manager.get_filtered_data(selected_category)
        
        items, sales = self.data_manager.get_summary_stats(selected_category)
        self.lbl_total_items.setText(f"Total Kuantitas: {items} unit")
        self.lbl_total_sales.setText(f"Total Penjualan: ${sales:,.2f}")
        
        self.chart.update_chart(df_filtered, selected_category, selected_chart)
        
        self.table.setRowCount(0)
        for target_row_idx, (_, row_data) in enumerate(df_filtered.iterrows()):
            self.table.insertRow(target_row_idx)
            
            display_cols = [
                row_data['Invoice ID'], row_data['Branch'], row_data['City'], 
                row_data['Customer type'], row_data['Product line'], 
                str(row_data['Quantity']), f"${row_data['Sales']:.2f}"
            ]
            
            for col_idx, value in enumerate(display_cols):
                item = QTableWidgetItem(str(value))
                if col_idx in [5, 6]:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.table.setItem(target_row_idx, col_idx, item)