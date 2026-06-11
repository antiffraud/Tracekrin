import csv
import os
from datetime import datetime
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
    QTableWidget, QTableWidgetItem, QMessageBox, QFileDialog,
    QHeaderView, QFrame, QTextEdit, QGroupBox, QApplication
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
from database import DatabaseHandler
from styles import Styles, COLORS

class ExportPage(QWidget):
    def __init__(self, db: DatabaseHandler):
        super().__init__()
        self.db = db
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)  
        main_layout.setSpacing(10) 
        
        title_label = QLabel("Export Data")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 10px;
            }
        """)
        main_layout.addWidget(title_label)
        
        self.create_export_section(main_layout)
        
        self.create_data_preview(main_layout)
    
    def create_export_section(self, parent_layout):
        export_frame = QFrame()
        export_frame.setObjectName("exportSection")
        export_frame.setMinimumHeight(180)
        export_frame.setMaximumHeight(200)
        
        background_image_path = "assets/Frame 182.png"
        if os.path.exists(background_image_path):
            export_frame.setStyleSheet(f"""
                QFrame#exportSection {{
                    background-image: url({background_image_path.replace(os.sep, '/')});
                    background-repeat: no-repeat;
                    background-position: center;
                    border-radius: 16px;
                    border: 2px solid #dee2e6;
                }}
            """)
            export_layout = QVBoxLayout(export_frame)
            export_layout.setContentsMargins(0, 0, 0, 20)
            export_layout.addStretch()
            
        else:
            export_frame.setStyleSheet("""
                QFrame#exportSection {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                                stop:0 #e3f2fd, stop:1 #bbdefb);
                    border-radius: 16px;
                    border: 2px solid #dee2e6;
                }
            """)
            
            export_layout = QVBoxLayout(export_frame)
            export_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            export_layout.setSpacing(10)
            export_layout.setContentsMargins(20, 15, 20, 15)
            
        button_image_path = "assets/Standard.png"
        if os.path.exists(button_image_path):
            export_button = QPushButton()
            export_button.setFixedSize(150, 40)
            export_button.setStyleSheet(f"""
                QPushButton {{
                    background-image: url({button_image_path.replace(os.sep, '/')});
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
                    border-radius: 12px;
                    color: transparent;
                }}
                QPushButton:hover {{
                    background-color: rgba(0, 0, 0, 0.1);
                    border: none;
                }}
                QPushButton:pressed {{
                    background-color: rgba(0, 0, 0, 0.2);
                    border: none;
                }}
            """)
        else:
            export_button = QPushButton("✓ Let's Do it!")
            export_button.setFixedSize(150, 40)
            export_button.setStyleSheet("""
                QPushButton {
                    background-color: #28a745;
                    color: #ffffff;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 12px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #218838;
                }
                QPushButton:pressed {
                    background-color: #1e7e34;
                }
            """)
        
        export_button.clicked.connect(self.export_to_csv)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(export_button)
        button_layout.addStretch()
        export_layout.addLayout(button_layout)
        
        parent_layout.addWidget(export_frame)
    
    def create_data_preview(self, parent_layout):
        preview_group = QGroupBox()
        preview_layout = QVBoxLayout(preview_group)
        preview_layout.setSpacing(2) 
        
        preview_heading = QLabel("Data Preview")
        preview_heading.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 0px;
                padding: 2px 0;
            }
        """)
        preview_layout.addWidget(preview_heading)
        
        info_label = QLabel("Preview of data that will be exported:")
        info_label.setStyleSheet("""
            color: #6c757d; 
            font-size: 12px; 
            margin-bottom: 3px; 
            margin-top: 0px;
            padding: 0px;
        """)
        preview_layout.addWidget(info_label)
        
        self.preview_table = QTableWidget()
        self.preview_table.setColumnCount(7)
        
        headers = ["Date", "Activity", "Start Time", "End Time", "Duration", "Status", "Created"]
        self.preview_table.setHorizontalHeaderLabels(headers)
        
        self.preview_table.verticalHeader().setVisible(True)
        self.preview_table.verticalHeader().setDefaultSectionSize(30) 
        
        header = self.preview_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # Date
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)           # Activity
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)  # Start Time
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # End Time
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # Duration
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)  # Status
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)  # Created
        
        self.preview_table.setAlternatingRowColors(True)
        self.preview_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.preview_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.preview_table.setMaximumHeight(220)  
        self.preview_table.setMinimumHeight(220)
        
        self.preview_table.setStyleSheet("""
            QTableWidget {
                gridline-color: #dee2e6;
                background-color: #ffffff;
                alternate-background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                font-size: 12pt;
            }
            QTableWidget::item {
                padding: 8px 6px;
                border-bottom: 1px solid #dee2e6;
                font-size: 12pt;
            }
            QTableWidget::item:selected {
                background-color: #0E2C75;
                color: white;
            }
            QTableWidget QHeaderView { 
                background-color: #e9ecef;
                font-size: 12pt;
            }
            QTableWidget QHeaderView::section { 
                background-color: #e9ecef;
                color: #495057;
                padding: 10px 8px; 
                border: 1px solid #dee2e6; 
                font-weight: bold;
                font-size: 12pt;
                min-height: 30px;
                text-align: center;
            }
            QTableWidget QHeaderView::section:hover {
                background-color: #dee2e6;
            }
            QTableWidget QHeaderView::section:pressed {
                background-color: #ced4da;
            }
            QTableWidget QHeaderView[orientation="1"]::section {
                background-color: #e9ecef;
                color: #495057;
                border: 1px solid #dee2e6;
                font-size: 12pt;
                font-weight: bold;
                text-align: center;
                padding: 5px;
                min-width: 35px;
            }
            QTableWidget QTableCornerButton::section {
                background-color: #e9ecef;
                border: 1px solid #dee2e6;
            }
        """)
        
        preview_layout.addWidget(self.preview_table)
        
        self.stats_label = QLabel()
        self.stats_label.setStyleSheet("color: #495057; font-size: 11px; margin-top: 3px;")
        preview_layout.addWidget(self.stats_label)
        
        preview_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding-top: 8px;
                margin-top: 3px;
                background-color: #ffffff;
            }
        """)
        
        parent_layout.addWidget(preview_group)
    
    def load_export_data(self):
        try:
            tasks = self.db.get_all_tasks()
            if tasks is None:
                tasks = []
            self.populate_preview_table(tasks)
        except Exception as e:
            print(f"Error loading export data: {e}")
            self.populate_preview_table([])
            if hasattr(self, 'stats_label'):
                self.stats_label.setText("Error loading data")
    
    def populate_preview_table(self, tasks):
        if not tasks:
            tasks = []
            
        self.preview_table.setRowCount(len(tasks))
        
        for row, task in enumerate(tasks):
            try:                
                # Date
                date_item = QTableWidgetItem(str(task.get('start_date', 'N/A')))
                date_item.setFont(QFont("Arial", 12))  
                self.preview_table.setItem(row, 0, date_item)
                
                # Activity
                activity_item = QTableWidgetItem(str(task.get('title', 'N/A')))
                activity_item.setFont(QFont("Arial", 12))
                self.preview_table.setItem(row, 1, activity_item)
                
                # Start Time
                start_time = QTableWidgetItem(str(task.get('start_time', 'N/A')))
                start_time.setFont(QFont("Arial", 12))
                self.preview_table.setItem(row, 2, start_time)
                
                # End Time
                end_time = QTableWidgetItem(str(task.get('end_time', 'N/A')))
                end_time.setFont(QFont("Arial", 12))
                self.preview_table.setItem(row, 3, end_time)
                
                # Duration 
                duration = self.calculate_duration(
                    task.get('start_time', '00:00:00'), 
                    task.get('end_time', '00:00:00')
                )
                duration_item = QTableWidgetItem(duration)
                duration_item.setFont(QFont("Arial", 12))
                self.preview_table.setItem(row, 4, duration_item)
                
                # Status
                status_text = task.get('status', 'Not Yet')
                status_item = QTableWidgetItem(status_text)
                status_item.setFont(QFont("Arial", 12))
                if status_text == 'Finished':
                    status_item.setBackground(QColor(212, 237, 218))  # Light green
                else:
                    status_item.setBackground(QColor(248, 215, 218))  # Light pink
                self.preview_table.setItem(row, 5, status_item)
                
                created_item = QTableWidgetItem(str(task.get('created_at', 'N/A')))
                created_item.setFont(QFont("Arial", 12))
                self.preview_table.setItem(row, 6, created_item)
                
            except Exception as e:
                print(f"Error populating row {row}: {e}")
                for col in range(7):
                    if not self.preview_table.item(row, col):
                        error_item = QTableWidgetItem("Error")
                        error_item.setFont(QFont("Arial", 12))
                        self.preview_table.setItem(row, col, error_item)
        
        total_tasks = len(tasks)
        completed_tasks = len([t for t in tasks if t.get('status') == 'Finished'])
        pending_tasks = total_tasks - completed_tasks
        
        if hasattr(self, 'stats_label'):
            self.stats_label.setText(
                f"Total: {total_tasks} tasks | Completed: {completed_tasks} | Pending: {pending_tasks}"
            )
    
    def calculate_duration(self, start_time, end_time):
        try:
            start = datetime.strptime(start_time, "%H:%M:%S")
            end = datetime.strptime(end_time, "%H:%M:%S")
            
            if end < start:
                end = end.replace(day=start.day + 1)
            
            duration = end - start
            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60
            
            return f"{hours}h {minutes}m"
        except:
            return "N/A"
    
    def export_to_csv(self):
        try:
            tasks = self.db.get_all_tasks()
            
            if not tasks:
                QMessageBox.information(self, "No Data", "No activities to export.")
                return
            
            filename, _ = QFileDialog.getSaveFileName(
                self, 'Export to CSV', 
                f'trackerin_activities_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
                'CSV Files (*.csv)'
            )
            
            if filename:
                try:
                    with open(filename, 'w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        
                        headers = ['Date', 'Activity', 'Description', 'Start Time', 'End Time', 
                                 'Duration', 'Status', 'Created At']
                        writer.writerow(headers)
                        
                        for task in tasks:
                            try:
                                duration = self.calculate_duration(
                                    task.get('start_time', '00:00:00'), 
                                    task.get('end_time', '00:00:00')
                                )
                                row = [
                                    task.get('start_date', 'N/A'),
                                    task.get('title', 'N/A'),
                                    task.get('description', 'N/A'),
                                    task.get('start_time', 'N/A'),
                                    task.get('end_time', 'N/A'),
                                    duration,
                                    task.get('status', 'N/A'),
                                    task.get('created_at', 'N/A')
                                ]
                                writer.writerow(row)
                            except Exception as e:
                                print(f"Error writing task row: {e}")
                                writer.writerow(['Error', 'Error', 'Error', 'Error', 'Error', 'Error', 'Error', 'Error'])
                    
                    QMessageBox.information(
                        self, "Success! 🎉", 
                        f"Data exported successfully!\n\nFile: {os.path.basename(filename)}\nLocation: {os.path.dirname(filename)}\nTotal records: {len(tasks)}"
                    )
                    
                except Exception as e:
                    QMessageBox.critical(self, "Export Error", f"Failed to write CSV file:\n{str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Export Error", f"Failed to export data:\n{str(e)}")
    
    def refresh_data(self):
        try:
            self.load_export_data()
        except Exception as e:
            print(f"Error refreshing export data: {e}")
            if hasattr(self, 'stats_label'):
                self.stats_label.setText("Error refreshing data")