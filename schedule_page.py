from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
    QFrame, QScrollArea, QCalendarWidget, QGroupBox, QDateEdit, 
    QTimeEdit, QLineEdit, QMessageBox, QSizePolicy, QApplication,
    QAbstractSpinBox
)
from PyQt6.QtGui import QTextCharFormat, QFont
from PyQt6.QtCore import Qt, QDate, QTime, pyqtSignal
from datetime import datetime, timedelta
from database import DatabaseHandler
from styles import Styles, COLORS

class TaskCard(QFrame):
    task_updated = pyqtSignal() 
    
    def __init__(self, task_data, db):
        super().__init__()
        self.task_data = task_data
        self.db = db
        self.init_ui()
    
    def init_ui(self):
        self.setObjectName("taskCard")
        self.setFrameShape(QFrame.Shape.Box)
        self.setFixedWidth(550)
        
        self.setStyleSheet(Styles.TASK_CARD_STYLE)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(15, 15, 15, 15)
        
        header_layout = QHBoxLayout()
        
        title_label = QLabel("List To-Do")
        title_label.setObjectName("taskTitle")
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        self.status_label = QLabel(self.task_data['status'])
        if self.task_data['status'] == 'Finished':
            self.status_label.setObjectName("statusFinished")
        else:
            self.status_label.setObjectName("statusNotYet")
        header_layout.addWidget(self.status_label)
        
        layout.addLayout(header_layout)
        
        content_label = QLabel(self.task_data['title'])
        content_label.setObjectName("taskContent")
        content_label.setWordWrap(True)
        layout.addWidget(content_label)
        
        start_time = self.task_data['start_time']
        end_time = self.task_data['end_time']
        time_label = QLabel(f"{start_time} - {end_time}")
        time_label.setObjectName("taskTime")
        layout.addWidget(time_label)
        
        if self.task_data['status'] != 'Finished':
            button_layout = QHBoxLayout()
            
            done_button = QPushButton("Done")
            done_button.setObjectName("doneButton")
            done_button.clicked.connect(self.mark_as_done)
            
            decline_button = QPushButton("Decline")
            decline_button.setObjectName("declineButton")
            decline_button.clicked.connect(self.decline_task)
            
            button_layout.addWidget(done_button)
            button_layout.addWidget(decline_button)
            button_layout.addStretch()
            
            layout.addLayout(button_layout)
    
    def mark_as_done(self):
        if self.db.update_task_status(self.task_data['id'], 'Finished'):
            self.status_label.setText('Finished')
            self.status_label.setObjectName("statusFinished")
            self.status_label.setStyleSheet("") 
            
            for i in range(self.layout().count()):
                item = self.layout().itemAt(i)
                if item and isinstance(item, QHBoxLayout):
                    for j in range(item.count()):
                        widget = item.itemAt(j).widget()
                        if isinstance(widget, QPushButton):
                            widget.hide()
            
            self.task_updated.emit()
            QMessageBox.information(self, "Success", "Task marked as finished!")
        else:
            QMessageBox.warning(self, "Error", "Failed to update task status.")
    
    def decline_task(self):
        reply = QMessageBox.question(self, 'Decline Task',
                                   'Are you sure you want to decline this task?',
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                   QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            if self.db.delete_task(self.task_data['id']):
                self.task_updated.emit()
                QMessageBox.information(self, "Success", "Task declined successfully!")
            else:
                QMessageBox.warning(self, "Error", "Failed to decline task.")

class SchedulePage(QWidget):
    def __init__(self, db: DatabaseHandler):
        super().__init__()
        self.db = db
        self.current_date = QDate.currentDate()
        self.day_buttons = {}
        self.task_cards = []
        self.init_ui()
        self.select_today()
    
    def init_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(20)
        
        left_widget = QWidget()
        left_widget.setFixedWidth(620)
        left_layout = QVBoxLayout(left_widget)
        left_layout.setSpacing(10)
        left_layout.setContentsMargins(10, 0, 10, 0)
        
        title_label = QLabel("To-do List Activity Tracker")
        title_label.setStyleSheet(Styles.SCHEDULE_TITLE_STYLE)
        left_layout.addWidget(title_label)
        
        self.create_day_selector(left_layout)
        
        self.current_day_label = QLabel(f"Today, {self.current_date.toString('MMM d')}")
        self.current_day_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2c3e50;
                margin: 10px 0;
            }
        """)
        left_layout.addWidget(self.current_day_label)
        
        self.task_scroll_area = QScrollArea()
        self.task_scroll_area.setWidgetResizable(True)
        self.task_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.task_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        self.task_container = QWidget()
        self.task_layout = QVBoxLayout(self.task_container)
        self.task_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.task_layout.setSpacing(8)
        
        self.task_scroll_area.setWidget(self.task_container)
        left_layout.addWidget(self.task_scroll_area)
        
        main_layout.addWidget(left_widget)
        
        right_widget = QWidget()
        right_widget.setFixedWidth(420)
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(15)
        
        self.create_calendar(right_layout)
        
        self.create_complete_form(right_layout)
        
        main_layout.addWidget(right_widget)
    
    def create_day_selector(self, parent_layout):
        scroll_area = QScrollArea()
        scroll_area.setFixedHeight(70)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        
        for i in range(14):
            date = QDate.currentDate().addDays(i)

            button = QPushButton()
            button.setObjectName("dayButton")
            button.setCheckable(True)
            button.setFixedSize(70, 50)
            
            day_text = date.toString("dd")
            month_text = date.toString("MMM")
            button.setText(f"{day_text}\n{month_text}")
            
            button.clicked.connect(lambda checked, d=date: self.select_date(d))
            
            button.setStyleSheet(Styles.DAY_BUTTON_STYLE)
            
            layout.addWidget(button)
            self.day_buttons[date] = button
        
        scroll_area.setWidget(container)
        parent_layout.addWidget(scroll_area)
    
    def create_calendar(self, parent_layout):
        self.calendar = QCalendarWidget()
        self.calendar.setFixedSize(420, 280)
        
        fmt = QTextCharFormat()
        fmt.setForeground(Qt.GlobalColor.red)
        self.calendar.setWeekdayTextFormat(Qt.DayOfWeek.Sunday, fmt)
        
        default_fmt = QTextCharFormat()
        self.calendar.setWeekdayTextFormat(Qt.DayOfWeek.Saturday, default_fmt)
        
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendar.clicked.connect(self.select_date)
        self.calendar.setStyleSheet(Styles.CALENDAR_STYLE)
        parent_layout.addWidget(self.calendar)
    
    def create_complete_form(self, parent_layout):
        scroll_area = QScrollArea()
        scroll_area.setFixedSize(420, 360)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)
        
        form_widget = QWidget()
        form_widget.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                margin: 5px;
            }
        """)
        
        form_layout = QVBoxLayout(form_widget)
        form_layout.setContentsMargins(20, 15, 20, 15)
        form_layout.setSpacing(10)
        
        title_label = QLabel("Form To-Do")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: 600;
                color: #343a40;
                text-align: center;
                margin-bottom: 8px;
                background-color: transparent;
                border: none;
            }
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(title_label)
        
        start_date_label = QLabel("Start Date")
        start_date_label.setStyleSheet("""
            QLabel {
                color: #495057; 
                font-size: 13px; 
                font-weight: 500; 
                margin-bottom: 2px;
                background-color: transparent;
                border: none;
            }
        """)
        
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setDate(self.current_date)
        self.start_date_edit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.start_date_edit.dateChanged.connect(self.on_date_changed)
        self.start_date_edit.setStyleSheet("""
            QDateEdit {
                padding: 8px 25px 8px 12px;
                border: 1px solid #ced4da;
                border-radius: 6px;
                font-size: 13px;
                background-color: #ffffff;
                color: #495057;
                min-height: 16px;
            }
            QDateEdit:focus { 
                border-color: #80bdff; 
                background-color: #ffffff;
            }
        """)
        
        form_layout.addWidget(start_date_label)
        form_layout.addWidget(self.start_date_edit)
        
        end_date_label = QLabel("End Date")
        end_date_label.setStyleSheet("""
            QLabel {
                color: #495057; 
                font-size: 13px; 
                font-weight: 500; 
                margin-bottom: 2px;
                background-color: transparent;
                border: none;
            }
        """)
        
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setDate(self.current_date)
        self.end_date_edit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.end_date_edit.setStyleSheet("""
            QDateEdit {
                padding: 8px 25px 8px 12px;
                border: 1px solid #ced4da;
                border-radius: 6px;
                font-size: 13px;
                background-color: #ffffff;
                color: #495057;
                min-height: 16px;
            }
            QDateEdit:focus { 
                border-color: #80bdff; 
                background-color: #ffffff;
            }
        """)
        
        form_layout.addWidget(end_date_label)
        form_layout.addWidget(self.end_date_edit)
        start_time_label = QLabel("Start Time")
        start_time_label.setStyleSheet("""
            QLabel {
                color: #495057; 
                font-size: 13px; 
                font-weight: 500; 
                margin-bottom: 2px;
                background-color: transparent;
                border: none;
            }
        """)
        
        self.start_time_edit = QTimeEdit()
        self.start_time_edit.setTime(QTime.currentTime())
        self.start_time_edit.setDisplayFormat("hh:mm AP")
        self.start_time_edit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.start_time_edit.setStyleSheet("""
            QTimeEdit {
                padding: 8px 25px 8px 12px;
                border: 1px solid #ced4da;
                border-radius: 6px;
                font-size: 13px;
                background-color: #ffffff;
                color: #495057;
                min-height: 16px;
            }
            QTimeEdit:focus { 
                border-color: #80bdff; 
                background-color: #ffffff;
            }
        """)
        
        form_layout.addWidget(start_time_label)
        form_layout.addWidget(self.start_time_edit)
        
        end_time_label = QLabel("End Time")
        end_time_label.setStyleSheet("""
            QLabel {
                color: #495057; 
                font-size: 13px; 
                font-weight: 500; 
                margin-bottom: 2px;
                background-color: transparent;
                border: none;
            }
        """)
        
        self.end_time_edit = QTimeEdit()
        self.end_time_edit.setTime(QTime.currentTime().addSecs(3600))
        self.end_time_edit.setDisplayFormat("hh:mm AP")
        self.end_time_edit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        
        self.end_time_edit.setStyleSheet("""
            QTimeEdit {
                padding: 8px 25px 8px 12px;
                border: 1px solid #ced4da;
                border-radius: 6px;
                font-size: 13px;
                background-color: #ffffff;
                color: #495057;
                min-height: 16px;
            }
            QTimeEdit:focus { 
                border-color: #80bdff; 
                background-color: #ffffff;
            }
        """)
        
        form_layout.addWidget(end_time_label)
        form_layout.addWidget(self.end_time_edit)
        
        activity_label = QLabel("Input Activity")
        activity_label.setStyleSheet("""
            QLabel {
                color: #495057; 
                font-size: 13px; 
                font-weight: 500; 
                margin-bottom: 2px;
                background-color: transparent;
                border: none;
            }
        """)
        
        self.activity_input = QLineEdit()
        self.activity_input.setPlaceholderText("Enter To-Do Activity")
        self.activity_input.returnPressed.connect(self.add_task)
        self.activity_input.setStyleSheet("""
            QLineEdit {
                padding: 8px 12px;
                border: 1px solid #ced4da;
                border-radius: 6px;
                font-size: 13px;
                background-color: #ffffff;
                color: #495057;
                min-height: 16px;
            }
            QLineEdit:focus { 
                border-color: #80bdff; 
                background-color: #ffffff;
            }
            QLineEdit::placeholder { 
                color: #adb5bd; 
            }
        """)
        
        form_layout.addWidget(activity_label)
        form_layout.addWidget(self.activity_input)
        
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.add_task)
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #1e3a8a;
                color: #ffffff;
                border: none;
                padding: 10px 20px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: 600;
                margin-top: 8px;
                min-height: 16px;
            }
            QPushButton:hover {
                background-color: #1e40af;
            }
            QPushButton:pressed {
                background-color: #1d4ed8;
            }
        """)
        form_layout.addWidget(self.submit_button)
        form_layout.addSpacing(20)
        form_container = QWidget()
        container_layout = QVBoxLayout(form_container)
        container_layout.setContentsMargins(10, 10, 10, 30)
        container_layout.addWidget(form_widget)
        scroll_area.setWidget(form_container)
        parent_layout.addWidget(scroll_area)
    
    def select_date(self, date):
        if isinstance(date, bool):
            sender = self.sender()
            for d, btn in self.day_buttons.items():
                if btn == sender:
                    date = d
                    break
        self.current_date = date
        
        for d, btn in self.day_buttons.items():
            btn.setChecked(d == date)
        
        self.calendar.setSelectedDate(date)
        self.start_date_edit.setDate(date)
        self.end_date_edit.setDate(date)
        
        if date == QDate.currentDate():
            self.current_day_label.setText(f"Today, {date.toString('MMM d')}")
        else:
            self.current_day_label.setText(date.toString('dddd, MMM d'))
        self.refresh_tasks()
    
    def select_today(self):
        today = QDate.currentDate()
        self.select_date(today)
    
    def on_date_changed(self, date):
        self.select_date(date)
    
    def add_task(self):
        title = self.activity_input.text().strip()
        start_date = self.start_date_edit.date().toString("yyyy-MM-dd")
        end_date = self.end_date_edit.date().toString("yyyy-MM-dd")
        start_time = self.start_time_edit.time().toString("hh:mm:ss")
        end_time = self.end_time_edit.time().toString("hh:mm:ss")
        
        if not title:
            QMessageBox.warning(self, "Warning", "Please enter an activity before submitting.")
            return
        
        if self.start_date_edit.date() < QDate.currentDate():
            QMessageBox.warning(self, "Invalid Date", "Start date cannot be in the past.")
            return
        
        if self.end_date_edit.date() < self.start_date_edit.date():
            QMessageBox.warning(self, "Invalid Date", "End date cannot be before start date.")
            return
        
        if self.start_time_edit.time() >= self.end_time_edit.time() and start_date == end_date:
            QMessageBox.warning(self, "Invalid Time", "End time must be after start time.")
            return
        
        if self.db.add_task(title, title, start_date, end_date, start_time, end_time):
            QMessageBox.information(self, "Success", "Task added successfully!")
            self.activity_input.clear()
            self.start_time_edit.setTime(QTime.currentTime())
            self.end_time_edit.setTime(QTime.currentTime().addSecs(3600))
            self.refresh_tasks()
        else:
            QMessageBox.warning(self, "Error", "Failed to add task.")
    
    def refresh_tasks(self):
        while self.task_layout.count():
            child = self.task_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        self.task_cards.clear()
        
        # Get tasks for current date
        date_str = self.current_date.toString("yyyy-MM-dd")
        tasks = self.db.get_tasks_by_date(date_str)
        
        # Create task cards
        for task in tasks:
            card = TaskCard(task, self.db)
            card.task_updated.connect(self.refresh_tasks)
            self.task_cards.append(card)
            self.task_layout.addWidget(card)
        
        self.task_layout.addStretch()
    
    def refresh_current_view(self):
        self.refresh_tasks()
    
    def focus_task_input(self):
        self.activity_input.setFocus()
    
    def paste_to_active_input(self, text):
        focused_widget = QApplication.focusWidget()
        
        if isinstance(focused_widget, QLineEdit):
            if focused_widget == self.activity_input:
                focused_widget.setText(text)
                QMessageBox.information(self, "Clipboard", "Text pasted to activity input!")
            else:
                focused_widget.setText(text)
                QMessageBox.information(self, "Clipboard", "Text pasted to input field!")
        else:
            self.activity_input.setFocus()
            self.activity_input.setText(text)
            QMessageBox.information(self, "Clipboard", "Text pasted to activity input!")