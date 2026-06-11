COLORS = {
    'primary': '#0E2C75',       
    'primary_light': '#0E2C75', 
    'secondary': '#f8f9fa',      
    'accent': '#17a2b8',       
    'success': '#28a745',     
    'warning': '#ffc107',        
    'danger': '#dc3545',        
    'light': '#f8f9fa',         
    'dark': '#495057',           
    'white': '#ffffff',
    'text_primary': '#2c3e50',
    'text_secondary': '#6c757d',
    'border': '#dee2e6',
    'finished_bg': '#d4edda',    
    'not_yet_bg': '#f8d7da',    
}

class Styles:
    MAIN_WINDOW_STYLE = """
        QMainWindow {
            background-color: #f8f9fa;
        }
    """
    
    GENERAL_WIDGET_STYLE = """
        QWidget {
            background-color: #ffffff;
            color: #2c3e50;
        }
    """
    
    HEADER_STYLE = """
        QWidget#headerWidget {
            background-color: #ffffff;
            border-bottom: 1px solid #dee2e6;
        }
        
        QLabel#logoLabel {
            font-size: 28px;
            font-weight: bold;
            color: #2c3e50;
            padding: 10px;
        }
        
        QPushButton#navButton {
            background-color: transparent;
            border: none;
            color: #6c757d;
            font-size: 16px;
            font-weight: 500;
            padding: 12px 20px;
            margin: 5px;
            border-radius: 8px;
            min-width: 100px;
        }
        
        QPushButton#navButton:hover {
            background-color: #f8f9fa;
            color: #2c3e50;
        }
        
        QPushButton#navButton:checked {
            background-color: #0E2C75;
            color: #ffffff;
        }
        
        QLabel#profilePic {
            background-color: #0E2C75;
            color: #ffffff;
            border-radius: 20px;
            font-size: 20px;
        }
        
        QLabel#userLabel {
            color: #2c3e50;
            font-size: 12px;
            margin-left: 10px;
        }
    """
    
    TAB_WIDGET_STYLE = """
        QTabWidget::pane {
            border: 1px solid #dee2e6;
            background-color: #ffffff;
        }
        QTabBar::tab {
            background-color: #e9ecef;
            color: #495057;
            padding: 8px 16px;
            margin-right: 2px;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
        }
        QTabBar::tab:selected {
            background-color: #ffffff;
            color: #2c3e50;
            border-bottom: 2px solid #0E2C75;
        }
    """
    
    SCHEDULE_TITLE_STYLE = """
        QLabel {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 20px;
        }
    """
    
    DAY_BUTTON_STYLE = """
        QPushButton#dayButton {
            background-color: #f8f9fa;
            color: #6c757d;
            border: 1px solid #dee2e6;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
            min-width: 70px;
            min-height: 50px;
            margin: 2px;
        }
        
        QPushButton#dayButton:hover {
            background-color: #e9ecef;
            border-color: #0E2C75;
        }
        
        QPushButton#dayButton:checked {
            background-color: #0E2C75;
            color: #ffffff;
            border-color: #0E2C75;
        }
    """
    
    CALENDAR_STYLE = """
        QCalendarWidget {
            background-color: #0E2C75;
            color: #0B235E;
            border-radius: 12px;
            font-size: 14px;
        }
        
        QCalendarWidget QMenu {
            background-color: #0E2C75;
            color: #ffffff;
            border: 1px solid #0268d5;
        }
        
        QCalendarWidget QSpinBox {
            background-color: #0E2C75;
            color: #ffffff;
            border: none;
            padding: 2px;
        }
        
        QCalendarWidget QAbstractItemView {
            background-color: #0E2C75;
            color: #ffffff;
            selection-background-color: #0268d5;
            outline: none;
        }
    """
    
    TASK_CARD_STYLE = """
        QFrame#taskCard {
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 15px;
            padding: 15px;
            margin: 8px 0;
        }
        
        QLabel#taskTitle {
            font-size: 16px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 5px;
        }
        
        QLabel#taskContent {
            font-size: 13px;
            color: #495057;
            background-color: #f8f9fa;
            padding: 8px;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            margin: 4px 0;
        }
        
        QLabel#taskTime {
            font-size: 12px;
            color: #6c757d;
            background-color: #f8f9fa;
            padding: 6px;
            border: 1px solid #dee2e6;
            border-radius: 8px;
        }
        
        QLabel#statusFinished {
            background-color: #d4edda;
            color: #155724;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
        }
        
        QLabel#statusNotYet {
            background-color: #f8d7da;
            color: #721c24;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
        }
        
        QPushButton#doneButton {
            background-color: #28a745;
            color: #ffffff;
            border: none;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 500;
            margin-right: 5px;
        }
        
        QPushButton#doneButton:hover {
            background-color: #218838;
        }
        
        QPushButton#declineButton {
            background-color: #dc3545;
            color: #ffffff;
            border: none;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 500;
        }
        
        QPushButton#declineButton:hover {
            background-color: #c82333;
        }
    """
    FORM_WIDGET_STYLE = """
        QGroupBox {
            border: 2px solid #dee2e6;
            border-radius: 12px;
            background-color: #ffffff;
            margin-top: 20px;
            padding-top: 20px;
            font-size: 16px;
            font-weight: bold;
            color: #2c3e50;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            left: 15px;
            top: -10px;
            padding: 5px 10px;
            background-color: #ffffff;
            color: #2c3e50;
            font-size: 18px;
            font-weight: bold;
            border-radius: 4px;
        }
        
        QLabel {
            color: #2c3e50;
            font-size: 14px;
            font-weight: 500;
            padding: 2px 0;
        }
    """
    
    # Fixed LINE_EDIT_STYLE with proper QComboBox syntax
    LINE_EDIT_STYLE = """
        QLineEdit, QDateEdit, QTimeEdit {
            padding: 10px 15px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 14px;
            background-color: #ffffff;
            min-height: 20px;
            color: #2c3e50;
        }
        QLineEdit:focus, QDateEdit:focus, QTimeEdit:focus {
            border-color: #0E2C75;
            outline: none;
            background-color: #ffffff;
        }
        QLineEdit::placeholder {
            color: #6c757d;
            font-style: italic;
        }
        QComboBox {
            padding: 10px 15px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 14px;
            background-color: #ffffff;
            min-height: 20px;
            color: #2c3e50;
            padding-right: 30px;
        }
        QComboBox:focus {
            border-color: #0E2C75;
            outline: none;
            background-color: #ffffff;
        }
        QComboBox::drop-down {
            border: none;
            width: 25px;
            background-color: transparent;
            border-left: 1px solid #dee2e6;
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
        }
        QComboBox::down-arrow {
            width: 0;
            height: 0;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-top: 10px solid #2c3e50;
            margin-right: 8px;
        }
        QComboBox::drop-down:hover {
            background-color: #f8f9fa;
        }
        QComboBox QAbstractItemView {
            border: 2px solid #0E2C75;
            background-color: #ffffff;
            selection-background-color: #0E2C75;
            selection-color: #ffffff;
            border-radius: 4px;
        }
    """
    
    SAVE_BUTTON_STYLE = """
        QPushButton {
            background-color: #0E2C75;
            color: #ffffff;
            border: 2px solid #0E2C75;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 500;
            min-width: 120px;
            min-height: 20px;
        }
        QPushButton:hover {
            background-color: #0E2C75;
            border-color: #0E2C75;
        }
        QPushButton:pressed {
            background-color: #004085;
            border-color: #004085;
        }
    """
    
    TABLE_STYLE = """
        QTableWidget {
            gridline-color: #dee2e6;
            background-color: #ffffff;
            alternate-background-color: #f8f9fa;
            border: none;
            font-size: 12pt;
        }
        QTableWidget::item {
            padding: 10px 8px;
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
            padding: 12px 15px; 
            border: 1px solid #dee2e6; 
            font-weight: bold;
            font-size: 12pt;
            min-height: 40px;
            text-align: center;
        }
        QTableWidget QHeaderView::section:hover {
            background-color: #dee2e6;
        }
        QTableWidget QHeaderView::section:pressed {
            background-color: #ced4da;
        }
        QTableWidget QTableCornerButton::section {
            background-color: #e9ecef;
            border: 1px solid #dee2e6;
        }
    """
    
    TABLE_CONTAINER_STYLE = """
        QWidget {
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            margin: 10px;
        }
    """

    TABLE_TITLE_STYLE = "font-weight: bold; font-size: 16px; color: #2c3e50; margin-bottom: 10px;"
    
    DELETE_BUTTON_STYLE = """
        QPushButton {
            background-color: #dc3545;
            color: white;
            border: 2px solid #dc3545;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: bold;
            font-size: 12px;
            min-width: 60px;
            text-align: center;
        }
        QPushButton:hover { 
            background-color: #c82333; 
            border-color: #c82333;
        }
        QPushButton:pressed { 
            background-color: #bd2130; 
            border-color: #bd2130;
        }
    """
    
    EXPORT_SECTION_STYLE = """
        QFrame#exportSection {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                        stop:0 #e3f2fd, stop:1 #bbdefb);
            border-radius: 16px;
            padding: 30px 20px;
            margin: 20px 10px;
            min-height: 140px;
        }
        
        QLabel {
            color: #2c3e50;
            font-weight: bold;
        }
    """
    
    EXPORT_BUTTON_STYLE = """
        QPushButton {
            background-color: #28a745;
            color: #ffffff;
            border: 2px solid #28a745;
            padding: 15px 30px;
            border-radius: 12px;
            font-size: 18px;
            font-weight: bold;
            margin-top: 20px;
            min-width: 200px;
        }
        QPushButton:hover {
            background-color: #218838;
            border-color: #218838;
        }
        QPushButton:pressed {
            background-color: #1e7e34;
            border-color: #1e7e34;
        }
    """
    
    SEARCH_INPUT_STYLE = """
        QLineEdit#searchBox {
            background-color: #ffffff;
            border: 2px solid #dee2e6;
            border-radius: 20px;
            padding: 10px 15px;
            font-size: 14px;
            color: #2c3e50;
            min-width: 300px;
        }
        QLineEdit#searchBox:focus {
            border-color: #0E2C75;
        }
        QLineEdit#searchBox::placeholder {
            color: #6c757d;
            font-style: italic;
        }
    """
    
    CLEAR_SEARCH_BUTTON_STYLE = """
        QPushButton {
            background-color: #6c757d;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 12px;
        }
        QPushButton:hover { background-color: #5a6268; }
    """
    
    DOCK_WIDGET_STYLE = """
        QDockWidget {
            background-color: #ffffff;
            border: 2px solid #dee2e6;
            border-radius: 10px;
            font-size: 14px;
        }
        
        QDockWidget::title {
            background-color: #f8f9fa;
            color: #2c3e50;
            padding: 12px;
            font-weight: bold;
            font-size: 16px;
            border-bottom: 2px solid #dee2e6;
        }
        
        QWidget {
            background-color: #ffffff;
            color: #2c3e50;
        }
        
        QLineEdit, QComboBox {
            border: 2px solid #dee2e6;
            border-radius: 6px;
            padding: 8px 12px;
            background-color: #ffffff;
            font-size: 14px;
        }
        
        QLineEdit:focus, QComboBox:focus {
            border-color: #0E2C75;
        }
        
        QPushButton {
            border: 2px solid #0E2C75;
            background-color: #0E2C75;
            color: #ffffff;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 500;
        }
        
        QPushButton:hover {
            background-color: #0E2C75;
            border-color: #0E2C75;
        }
    """
    
    DOCK_TITLE_STYLE = "font-weight: bold; font-size: 14px; color: #2c3e50; margin-bottom: 8px; padding: 2px 0;"
    PROFILE_CARD_STYLE = """
        QWidget {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            margin: 10px;
        }
    """
    
    STATUS_BAR_STYLE = """
        QStatusBar {
            background-color: #0E2C75;
            color: #ffffff;
            border: none;
            padding: 5px 15px;
            font-size: 12px;
            max-height: 25px;
            min-height: 25px;
        }
        QStatusBar::item {
            border: none;
            margin: 0px;
            padding: 0px;
        }
        QStatusBar QLabel {
            color: #ffffff;
            font-size: 12px;
            margin: 0px;
            padding: 2px 5px;
        }
    """
    
    STUDENT_INFO_STATUS_STYLE = """
        font-weight: bold; 
        color: #ffffff; 
        padding: 2px 10px;
        margin: 0px;
        font-size: 12px;
        background-color: transparent;
    """
    
    MESSAGE_BOX_STYLE = f"""
        QMessageBox {{
            background-color: {COLORS['white']};
            color: {COLORS['text_primary']};
        }}
        QMessageBox QPushButton {{
            background-color: {COLORS['primary']};
            color: {COLORS['white']};
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            min-width: 80px;
        }}
        QMessageBox QPushButton:hover {{
            background-color: {COLORS['primary_light']};
        }}
    """

def get_complete_stylesheet():
    return (
        Styles.MAIN_WINDOW_STYLE +
        Styles.GENERAL_WIDGET_STYLE +
        Styles.HEADER_STYLE +
        Styles.TAB_WIDGET_STYLE +
        Styles.SCHEDULE_TITLE_STYLE +
        Styles.DAY_BUTTON_STYLE +
        Styles.CALENDAR_STYLE +
        Styles.TASK_CARD_STYLE +
        Styles.FORM_WIDGET_STYLE +
        Styles.LINE_EDIT_STYLE +
        Styles.SAVE_BUTTON_STYLE +
        Styles.TABLE_STYLE +
        Styles.EXPORT_SECTION_STYLE +
        Styles.EXPORT_BUTTON_STYLE +
        Styles.SEARCH_INPUT_STYLE +
        Styles.DOCK_WIDGET_STYLE +
        Styles.STATUS_BAR_STYLE +
        Styles.MESSAGE_BOX_STYLE
    )