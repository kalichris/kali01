import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedLayout,\
    QStackedWidget, QHBoxLayout, QTextEdit, QCheckBox, QMessageBox, QLabel, QComboBox, QMessageBox, QDesktopWidget,\
    QGroupBox, QPlainTextEdit, QScrollBar, QScrollArea, QSlider, QSpinBox, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsItem, QSizePolicy, QFileDialog, QLineEdit, QFrame, QListWidget, QDesktopWidget, QDialog
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QColor, QContextMenuEvent, QTextCursor
from PyQt5.QtCore import Qt, QSize, QObject, QFile, QTextStream, QDateTime, pyqtSlot, pyqtSignal, QMetaObject, Q_ARG,QThread,QTimer,QMutex,QRunnable,QThreadPool
from PyQt5 import QtWidgets, uic
import time
import datetime
import sqlite3
import platform
import os
import facebook
from threading import *

class localTools():
    def mybutton(name, tooltip, style_button, height_button,icon_img,x,y,x1=0,y1=0,x2=0,y2=0,x3=0,y3=0,x4=0,y4=0,posstion=None,mv_x=0,mv_y=0,w=None,bg_set=None):
        
        icon_style="""
                QLabel{
                   background-color:#323643;
                   color:white;
                   font-size:20px;
               }QLabel:hover{
                    color:#2777ff;
                }
                """
        label_style="""
            QLabel{
                background-color:#23252e;
                border-radius:1px;
            """


        if len(icon_img)==0:
            button_name = QPushButton(name,posstion)
            button_name.setStyleSheet(style_button)
        else:
            button_name = QPushButton(posstion)
            button_name.setStyleSheet(style_button)
        if w == None :
            button_name.setFixedHeight(height_button)
        else:
             button_name.setFixedSize(w,height_button)
        button_name.setToolTip(tooltip)
        button_name.move(mv_x,mv_y)
        
        if not len(icon_img)==0:
            button_name.setIcon(QIcon(icon_img))
            button_name.setIconSize(QSize(x,y))
        else:
            pass
        if len(name) == 0:
            pass 
        elif len(name)>1 and len(icon_img) >0:
            bg_label=QLabel(name,button_name)
            bg_label.setObjectName("Name")
            button_name.setObjectName(name)
            bg_label.move(x1,y1)
            if bg_set == None :
                bg_label.setStyleSheet(icon_style)
            else :
                bg_label.setStyleSheet(bg_set)
        label_sty=QLabel(button_name)
        label_sty.move(x2,y2)
        label_sty.setFixedSize(x3,y3)
        label_sty.setStyleSheet(label_style)
        
        if button_name.underMouse():
            label_sty.setStyleSheet(" background-color:#2777ff; border-radius:1px;")
        else :
            label_sty.setStyleSheet("background-color:#23252e; border-radius:1px;")
        return button_name

    def paintEvent(self, event):
        painter = QPainter(self)
        brush = QBrush(QColor(255, 0, 0))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(50, 50, 50, 50)


class DataBasesSqlite():
    def CreateData(self, path_db):
        db = sqlite3.connect(path_db)
        db.execute('''CREATE TABLE USER
                                       (id INTEGER PRIMARY KEY,
                                        NAME TEXT,
                                        API TEXT,
                                        EMAIL TEXT, 
                                        PAASSD TEXT);''')
        db.execute('''CREATE TABLE POST
                                       (id INTEGER PRIMARY KEY,
                                        POST_TXT TEXT,
                                        FILE BOLD,);''')
        db.execute('''CREATE TABLE CreateAccount
                                       (id INTEGER PRIMARY KEY,
                                        api TEXT,
                                        PASSWD INTEGER,);''')

    def check_databases_def(self):
        type_sys = platform.system()
        if type_sys == "Linux":
            if os.path.isdir("/var/lib/TheKingMarketing"):
                if os.path.isfile("/var/lib/ChrisStore/TheKingMarketing.db"):
                    pass
                else:
                    path_db = "/var/lib/ChrisStore/TheKingMarketing.db"
                    DataBasesSqlite.CreateData(path)
            else:
                os.mkdir("/var/lib/TheKingMarketing")
                path_db = "/var/lib/ChrisStore/TheKingMarketing.db"
                DataBasesSqlite.CreateData(path)
        elif type_sys == "Window":
            if os.path.isdir("C:\ProgramData\TheKingMarketing\ "):
                if os.path.isfile("C:\ProgramData\TheKingMarketing\TheKingMarketing.db"):
                    pass
                else:
                    path_db = "C:\ProgramData\TheKingMarketing\TheKingMarketing.db"
                    DataBasesSqlite.CreateData(path_db)
            else:
                os.mkdir("C:\ProgramData\TheKingMarketing\ ")
                path_db = "C:\ProgramData\TheKingMarketing\TheKingMarketing.db"
                DataBasesSqlite.CreateData(path_db)


class MainWindow(QMainWindow):
    def __init__(self, stacked_layout):
        super().__init__()
        style_button = """
            QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:25px;
                background-color : #323643;
                top:2px;
                text-align:left;
                padding-left :5px;
                padding-bottom:5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:25px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """
        icon_style="""
                QLabel{
                    background-color:#eeeeec;
                    border-top:1px solid black;
                    border-bottom:1px solid black;
                    
                }QLabel:hover,QPushButton:hover{
                    border:none;
                    border-bottom:2px solid #2777ff;
                }
                """
        size_icon = QSize(25, 25)

        self.setWindowTitle("Main Window")
        self.setStyleSheet('background-color : #23252e;')
        screen_size = QDesktopWidget().screenGeometry(-1)
        x = (screen_size.width() - self.frameSize().width()) / 2
        y = (screen_size.height() - self.frameSize().height()) / 2
        self.setGeometry(int(x), int(y), 300, 550)
        self.setMaximumSize(301, 551)
        self.setMinimumSize(300, 550)

        layout = QVBoxLayout()
        
        self.button_fb = localTools.mybutton("Facebook","Facebook Tools", style_button, 50,"icon/fb.png",65,60,100,10,75,5,4,40,40,50)
        
        self.button_inst= localTools.mybutton("Instagram","Instagram Tools", style_button, 50,"icon/isnt.png",65,60,100,10,75,5,4,40,40,50)

        self.button_tik = localTools.mybutton("Tiktok","Tiktok Tools", style_button, 50,"icon/tik.png",65,60,100,10,75,5,4,40,40,50)
        
        self.button_snap = localTools.mybutton("Snapchat","Snapchat Tools", style_button, 50,"icon/snap.png",65,60,100,10,75,5,4,40,40,50)
        
        self.button_tw = localTools.mybutton("Twitter", "Twitter Tools", style_button, 50,"icon/titt.png",65,60,100,10,75,5,4,40,50,40)
        
        self.button_wb = localTools.mybutton("WhatsApp", "WhatsApp Tools", style_button, 50,"icon/waths1.png",65,60,100,10,75,5,4,40,40,50)
        
        self.button_setting = localTools.mybutton("Setting", "Setting app", style_button, 50,"icon/sett.png",65,60,100,10,75,5,4,40,40,50)
        
        self.button_exit = localTools.mybutton("Exit","close Application", style_button, 50,"icon/logout.png",65,60,100,10,75,5,4,40,40,50)

        layout.addWidget(self.button_fb)
        layout.addWidget(self.button_inst)
        layout.addWidget(self.button_tik)
        layout.addWidget(self.button_snap)
        layout.addWidget(self.button_tw)
        layout.addWidget(self.button_wb)
        layout.addWidget(self.button_setting)
        layout.addWidget(self.button_exit)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.button_fb.clicked.connect(self.open_fb_window)
        self.button_inst.clicked.connect(self.open_inst_window)
        self.button_snap.clicked.connect(self.open_snap_window)
        self.button_tik.clicked.connect(self.open_tik_window)
        self.button_tw.clicked.connect(self.open_tw_window)
        self.button_wb.clicked.connect(self.open_wb_window)
        self.button_exit.clicked.connect(self.button_exit_def)

    def open_fb_window(self):
        stacked_layout.setCurrentWidget(fb_main)

    def open_inst_window(self):
        stacked_layout.setCurrentWidget(inst_main)

    def open_tik_window(self):
        stacked_layout.setCurrentWidget(tik_main)

    def open_snap_window(self):
        stacked_layout.setCurrentWidget(snap_main)

    def open_tw_window(self):
        stacked_layout.setCurrentWidget(tw_main)

    def open_wb_window(self):
        stacked_layout.setCurrentWidget(wb_main)

    class exit_sure(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Main Window")
            self.setStyleSheet('background-color : #23252e;')
            screen_size = QDesktopWidget().screenGeometry(-1)
            x = (screen_size.width() - self.frameSize().width()) / 2
            y = (screen_size.height() - self.frameSize().height()) / 2
            self.setGeometry(int(x-80), int(y)+180, 550, 120)
            self.setMaximumSize(550, 120)
            self.setMinimumSize(550, 120)
            style_button = """
            QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:20px;
                background-color : #323643;
                top:2px;
                text-align:left;
                padding-left :5px;
                padding-bottom:5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:20px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """
            
            lable_style = """
                    QLabel{
                        color : white;
                        font-size: 20px;
                    }
                    """
            icon_style="""
                QLabel{
                    background-color:white;
                    border-top:1px solid black;
                    border-bottom:1px solid black;
                    
                }QLabel:hover,QPushButton:hover{
                    border:none;
                    border-bottom:2px solid #2777ff;
                }
                    """
            image_style="""
                QLabel{
                    background-color:white;
                    border-radius:25;
                    }
                    """
            self.mass = QLabel("Do you really want out? ", self)
            self.mass.setStyleSheet(lable_style)
            self.mass.setFixedWidth(600)
            self.mass.move(80, 15)
            
            self.imgae_label=QLabel(self)
            self.imgae_label_1=QLabel(self.imgae_label)
            self.imgae_label.move(20,10)
            self.img_exit=QPixmap("icon/warning.png").scaled(35,35)
            self.imgae_label_1.setPixmap(self.img_exit)
            self.imgae_label_1.move(8,7)
            self.imgae_label.setStyleSheet(image_style)
            self.imgae_label.setFixedSize(50,50)
            
            self.button_back = localTools.mybutton("Back", "Back Main Window", style_button, 40,"icon/back.png",45,40,70,5,50,2,3,35,30,40,self,int(self.width()-300),75,140)
             
            self.button_exi = localTools.mybutton("Exit", "Close Application", style_button, 40,"icon/logout.png",45,40,70,5,50,2,3,35,30,40,self,int(self.width()-150),75,140)
                 
            self.button_back.clicked.connect(self.back_def)
            self.button_exi.clicked.connect(self.button_exit)

        def back_def(self):
            self.reject()

        def button_exit(self):
            sys.exit()

    def button_exit_def(self):
        self.exit_sure().exec_()


class SecondWindow(QMainWindow):
    def __init__(self, stacked_layout):
        super().__init__()

    class Fb_main(QMainWindow):
        def __init__(self, stacked_layout):
            super().__init__()
            style_button = """
            QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:25px;
                background-color : #323643;
                top:2px;
                text-align:left;
                padding-left :5px;
                padding-bottom:5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:25px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """

            self.setWindowTitle("Facebook Tools ")
            screen_size = QDesktopWidget().screenGeometry(-1)
            x = (screen_size.width() - self.frameSize().width()) / 2
            y = (screen_size.height() - self.frameSize().height()) / 2
            self.setGeometry(int(x), int(y), 300, 300)
            self.setStyleSheet('background-color : #23252e;')
            self.setMinimumSize(300, 300)
            self.setMaximumSize(301, 301)

            size_icon = QSize(25, 25)
            button_post = localTools.mybutton("Post","Post an unlimited number of posts in groups", style_button, 50,"icon/fb.png",65,60,130,10,75,5,4,40,40,50)
            button_bot = localTools.mybutton("Bot","The automatic reply bot to the messages and posts", style_button, 50,"icon/bot.png",65,60,130,10,75,5,4,40,40,50)
            button_profile = localTools.mybutton("Profile",  "Your profile", style_button, 50,"icon/user.png",65,60,130,10,75,5,4,40,40,50)
            button_back = localTools.mybutton("Back", "Back Main Window", style_button, 50,"icon/back.png",65,60,130,10,75,5,4,40,40,50)

            layout = QVBoxLayout()
            layout.addWidget(button_post)
            layout.addWidget(button_bot)
            layout.addWidget(button_profile)
            layout.addWidget(button_back)
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            button_post.clicked.connect(self.go_post_main)
            button_profile.clicked.connect(self.go_profile_fb_main)
            button_back.clicked.connect(self.go_back_main)

        def go_post_main(self):
            stacked_layout.setCurrentWidget(post_fb_main)

        def go_profile_fb_main(self):
            stacked_layout.setCurrentWidget(profile_fb)

        def go_back_main(self):
            stacked_layout.setCurrentWidget(window)

    class INST_main (QMainWindow):
        def __init__(self, stacked_layout):
            super().__init__()
            self.setWindowTitle("Instagram Tools")
            screen_size = QDesktopWidget().screenGeometry(-1)
            x = (screen_size.width() - self.frameSize().width()) / 2
            y = (screen_size.height() - self.frameSize().height()) / 2
            self.setGeometry(int(x), int(y), 300, 300)
            self.setStyleSheet('background-color : #23252e;')
            self.setMinimumSize(300, 300)
            self.setMaximumSize(301, 301)
            style_button = """
            QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:25px;
                background-color : #323643;
                top:2px;
                text-align:left;
                padding-left :5px;
                padding-bottom:5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:25px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """

            button_back = localTools.mybutton("Back","Back Main Window", style_button, 50,"icon/back.png",65,60,130,10,75,5,4,40,40,50)

            layout = QVBoxLayout()
            layout.addWidget(button_back)
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            button_back.clicked.connect(self.go_back_main)

        def go_back_main(self):
            stacked_layout.setCurrentWidget(window)

    class TIK_main (QMainWindow):
        def __init__(self, stacked_layout):
            super().__init__()
            self.setWindowTitle("Tiktok Tools")
            screen_size = QDesktopWidget().screenGeometry(-1)
            x = (screen_size.width() - self.frameSize().width()) / 2
            y = (screen_size.height() - self.frameSize().height()) / 2
            self.setGeometry(int(x), int(y), 300, 300)
            self.setStyleSheet('background-color : #23252e;')
            self.setMinimumSize(300, 300)
            self.setMaximumSize(301, 301)
            style_button = """
            QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:25px;
                background-color : #323643;
                top:2px;
                text-align:left;
                padding-left :5px;
                padding-bottom:5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:25px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """

            button_back =localTools.mybutton("Back","Back Main Window", style_button, 50,"icon/back.png",65,60,130,10,75,5,4,40,40,50)
            
            layout = QVBoxLayout()
            layout.addWidget(button_back)
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            button_back.clicked.connect(self.go_back_main)

        def go_back_main(self):
            stacked_layout.setCurrentWidget(window)

    class SNAP_main (QMainWindow):
        def __init__(self, stacked_layout):
            super().__init__()
            self.setWindowTitle("Snapchat Tools")
            screen_size = QDesktopWidget().screenGeometry(-1)
            x = (screen_size.width() - self.frameSize().width()) / 2
            y = (screen_size.height() - self.frameSize().height()) / 2
            self.setGeometry(int(x), int(y), 300, 300)
            self.setStyleSheet('background-color : #23252e;')
            self.setMinimumSize(300, 300)
            self.setMaximumSize(301, 301)
            style_button = """
            QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:25px;
                background-color : #323643;
                top:2px;
                text-align:left;
                padding-left :5px;
                padding-bottom:5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:25px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """
            
            button_back = localTools.mybutton("Back","Back Main Window", style_button, 50,"icon/back.png",65,60,130,10,75,5,4,40,40,50)
            
            layout = QVBoxLayout()
            layout.addWidget(button_back)
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            button_back.clicked.connect(self.go_back_main)

        def go_back_main(self):
            stacked_layout.setCurrentWidget(window)

    class TW_main (QMainWindow):
        def __init__(self, stacked_layout):
            super().__init__()
            self.setWindowTitle("Twitter Tools")
            screen_size = QDesktopWidget().screenGeometry(-1)
            x = (screen_size.width() - self.frameSize().width()) / 2
            y = (screen_size.height() - self.frameSize().height()) / 2
            self.setGeometry(int(x), int(y), 300, 300)
            self.setStyleSheet('background-color : #23252e;')
            self.setMinimumSize(300, 300)
            self.setMaximumSize(301, 301)
            style_button = """
            QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:25px;
                background-color : #323643;
                top:2px;
                text-align:left;
                padding-left :5px;
                padding-bottom:5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:25px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """
            
            button_back = localTools.mybutton("Back","Back Main Window", style_button, 50,"icon/back.png",65,60,130,10,75,5,4,40,50,40)
            
            layout = QVBoxLayout()
            layout.addWidget(button_back)
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            button_back.clicked.connect(self.go_back_main)

        def go_back_main(self):
            stacked_layout.setCurrentWidget(window)

    class WB_main (QMainWindow):
        def __init__(self, stacked_layout):
            super().__init__()
            self.setWindowTitle("WhatsApp Tools")
            screen_size = QDesktopWidget().screenGeometry(-1)
            x = (screen_size.width() - self.frameSize().width()) / 2
            y = (screen_size.height() - self.frameSize().height()) / 2
            self.setGeometry(int(x), int(y), 300, 300)
            self.setStyleSheet('background-color : #23252e;')
            self.setMinimumSize(300, 300)
            self.setMaximumSize(301, 301)
            style_button = """
            QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:25px;
                background-color : #323643;
                top:2px;
                text-align:left;
                padding-left :5px;
                padding-bottom:5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:25px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """

            button_back = localTools.mybutton("Back","Back Main Window", style_button, 50,"icon/back.png",65,60,130,10,75,5,4,40,40,50)
            
            layout = QVBoxLayout()
            layout.addWidget(button_back)
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            button_back.clicked.connect(self.go_back_main)

        def go_back_main(self):
            stacked_layout.setCurrentWidget(window)

class third_window(QMainWindow, QObject):
    def __init__(self, stacked_layout):
        super().__init__()

    class T_Fb_main(QMainWindow):
        def __init__(self, stacked_layout):
            super().__init__()

        class MyLabel(QLabel):
            def __init__(self, parent=None):
                super().__init__(parent)

            def paintEvent(self, event):
                super().paintEvent(event)
                painter = QPainter(self)
                painter.setRenderHint(QPainter.Antialiasing)
                painter.setPen(QPen(QColor("#1b1d24"), 5, Qt.SolidLine))
                center_x = self.width()/2
                center_y = self.height()/2
                radius = 73
                painter.drawEllipse(int(center_x - radius), int(center_y - radius), radius * 2, radius * 2)

        class T_Post(QMainWindow):
            def __init__(self, stacked_layout):
                super().__init__()
                self.setWindowTitle("Facebook Post")
                screen_size = QDesktopWidget().screenGeometry(-1)
                x = (screen_size.width() - self.frameSize().width()) / 2
                y = (screen_size.height() - self.frameSize().height()) / 2
                self.setGeometry(int(x), int(y-150), 630, 800)
                self.setStyleSheet('background-color : #23252e;')
                self.setMinimumSize(630, 800)
                self.setMaximumSize(631, 801)

            def remove_item(self):
                for x in QtWidgets:
                    x.deleteLater()

            def showEvent(self, event):
                self.remove_item

                scroll_style = """
                    QScrollBar:vertical {
                        border: none;
                        background:#292c37 ;
                        width: 18px;
                        margin: 0px 0px 0px 0px;
                    }QScrollBar::handle:vertical {
                        background: #1b1d24;
                        min-height: 20px;
                    }QScrollBar::add-line:vertical {
                        border: none;
                        background: #1d66e2;
                        height: 20px;
                        subcontrol-position: bottom;
                        subcontrol-origin: margin;
                    }QScrollBar::sub-line:vertical {
                        border: none;
                        background: #1d66e2;
                        height: 20px;
                        subcontrol-position: top;
                        subcontrol-origin: margin;
                    }QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                        background: none;
                    }QScrollArea::up-arrows{
                        background:red;
                        }
                     """

                self.scroll_area = QScrollArea(self)
                self.scroll_area.setWidgetResizable(True)
                self.setCentralWidget(self.scroll_area)
                self.main_group = QGroupBox(self)
                self.main_group.setFixedSize(self.width(), 1490)
                self.scroll_area.setWidget(self.main_group)
                self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.scroll_area.setStyleSheet(scroll_style)
                self.scroll_area.setFrameShape(QFrame.NoFrame)
                self.scroll_area.verticalScrollBar().setStyleSheet(scroll_style)

                lable_style = """
                    QLabel{
                        color : white;
                        font-size: 30px;
                    }
                    """
                style_button = """
            QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:7px;
                background-color : #323643;
                text-align:left;
                padding-left :3px;
                padding-bottom:2.5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:7px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """
                style_button_cn = """
                   QPushButton{
                        color : white;
                        border: 1.1px solid black;
                        border-radius:7px;
                        background-color : #323643;
                        text-align:center;
                        font-size:18px;
                        padding-left:2.5px;
                        padding-right:2.5px;
                    }QPushButton:hover{
                        border:none;
                        border-radius:7px;
                        border:2px solid #2777ff;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                    """
                input_style = """
                    QTextEdit{
                        border-radius: 5px;
                        border: 1.5px solid #0d0e11;
                        background-color:#292c37;
                        color:#c8c2bb;
                        padding-right:5px;
                        padding-left:5px;
                    }QTextEdit:focus{
                        background-color:#1b1d24;
                        border-color:#1d66e2;
                        color:white;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                    """
                self.check_input_access_style = """
                    QCheckBox{
                        border-radius:4px;
                        background-color:#292c37;
                        border: 1.5px solid #0d0e11;
                        color:white;
                    }QCheckBox::indicator{
                        width:30px;
                        height:30px;
                    }QCheckBox:hover{
                        background-color:#1b1d24;
                        border: 1.5px solid #1d66e2 ;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                    """
                self.check_input_file_style = """
                    QCheckBox{
                        border-radius:5px;
                        background-color:#292c37;
                        border: 1.5px solid #0d0e11;
                        color:white;
                    }QCheckBox::indicator{
                        width:35px;
                        height:30px;
                    }QCheckBox:hover{
                        background-color:#1b1d24;
                        border: 1.5px solid #1d66e2 ;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                        }
                        """
                accon_label_style = """
                    QLabel{
                        color: white;
                        font-size:20px;
                    }
                    """
                div_groups_style = """
                    QGroupBox{
                        border-radius:5px;
                        border: 1.5px solid #1d66e2;
                        background-color:#1b1d24;
                        color:white;
                    }QGroupBox:hover{
                        border: 2px solid white;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                    """
                range_label_style = """
                    QLabel{
                        color:white;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                """
                label_log_style = """
                    QLabel{
                        font-size:18px;
                        color:white;
                    }
                """
                self.spin_style = """
                    QSpinBox{
                        border-radius:5px;
                        border: 1.5px solid #1d66e2;
                        background-color:#1b1d24;
                        padding-right:3px;
                        padding-left:3px;
                        color:white;
                    }QSpinBox:hover{
                        color:white;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }QSpinBox:focus{
                        background-color:#1b1d24;
                        border-color:#1d66e2;
                        color:white;
                    }QSpinBox::up-arrow {
                            color: white;
                    } 
                    """
                self.disable_spin ="""
                    QSpinBox{
                        border-radius:5px;
                        border: 1px solid #0d0e11;
                        background-color:#292c37;
                        padding-right:3px;
                        padding-left:3px;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                    """
                self.check_spin_style = """
                    QCheckBox{
                        border-radius:4px;
                        background-color:#292c37;
                        border: 1.5px solid #0d0e11;
                        color:white;
                    }QCheckBox::indicator{
                        width:31px;
                        height:31px;
                    }QCheckBox:hover{
                        background-color:#1b1d24;
                        border: 1.5px solid #1d66e2 ;
                    }QCheckBox:after{
                        background-color:#1b1d24;
                        border: 1.5px solid #1d66e2 ;
                        }
                    QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                    """
                self.checked_style_spin="""
                    QCheckBox{
                        color:white;
                        background-color:#1b1d24;
                        border: 1.5px solid #1d66e2;
                        border-radius:4px;
                    }QCheckBox::indicator{
                        width:31px;
                        height:31px;
                        }
                    """
                self.checked_style_access="""
                    QCheckBox{
                        color:white;
                        background-color:#1b1d24;
                        border: 1.5px solid #1d66e2;
                        border-radius:4px;
                    }QCheckBox::indicator{
                        width:30px;
                        height:30px;
                        }
                    """
                self.checked_style_file="""
                    QCheckBox{
                        color:white;
                        background-color:#1b1d24;
                        border: 1.5px solid #1d66e2;
                        border-radius:4px;
                    }QCheckBox::indicator{
                        width:35px;
                        height:30px;
                        }
                    """
                log_style = """
                    QPlainTextEdit{
                        border-radius:5px;
                        border: 1.5px solid #1d66e2;
                        background-color:#1b1d24;
                        color:white;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                    """
                self.input_file_style = """
                    QLineEdit{
                        border-radius: 5px;
                        border: 1.5px solid #0d0e11;
                        background-color:#292c37;
                        color:#c8c2bb;
                        font-size:14px;
                        padding-right:5px;
                        padding-left:5px;
                        font-size:20px;
                    }QLineEdit:hover{
                        border
                    }
                    QLineEdit:focus{
                        background-color:#1b1d24;
                        border-color:#1d66e2;
                        color:white;
                    }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                  """

                choose_accont_style = """
                    QComboBox{
                        color:white;
                        background-color:#323643;
                        border:1px solid black;
                        border-radius:5px;
                        }QComboBox:hover{
                            background:#1b1d24;
                        }QToolTip{
                        background-color : #292c37;
                        color:white;
                        padding:5px;
                    }
                    """
                lable_info_style = """
                    QLabel{
                        color : white;
                        font-size: 15px;
                        background-color:#1b1d24;
                    }
                    """
                lable_addr_style = """
                    QLabel{
                        color : white;
                        font-size: 20px;
                        background-color:#1b1d24;
                        }
                     """
                sty_button="""
                         QPushButton{
                            border:none;
                            background-color : #23252e;
                        }QPushButton:hover{
                            border:none;
                            background-color: #323643;
                            border-bottom:2px solid #2777ff;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                            }
                    """""
                size_icon = QSize(25, 25)
                
                main_lable = QLabel("Facebook Post", self.main_group)
                main_lable.setStyleSheet(lable_style)
                main_lable.setWordWrap(True)
                main_lable.setFixedWidth(self.width())
                main_lable.move(215, 20)

                accon_label = QLabel("Select your Account", self.main_group)
                accon_label.setStyleSheet(accon_label_style)
                accon_label.setFixedWidth(self.width())
                accon_label.move(20, 70)

                self.choose_accont = QComboBox(self.main_group)
                self.choose_accont.move(19, 100)
                self.choose_accont.setStyleSheet("background:red")
                self.choose_accont.setFixedSize(315, 35)
                self.choose_accont.setToolTip("chosse account which will be post")
                self.choose_accont.setStyleSheet(choose_accont_style)

                try:
                    self.conn_sql = sqlite3.connect("test.db")
                    self.ex_sql = self.conn_sql.cursor()
                    self.ex_sql.execute('SELECT NAME FROM ADD_USER')
                    self.name_button_clic = None
                    rows = self.ex_sql.fetchall()
                    names = []
                    for row in rows:
                        x = 0
                        self.name = row[x]
                        x += 1
                        if self.name is not None and len(self.name) > 1:
                            names.append(self.name)
                            self.choose_accont.addItem(self.name)
                except Exception as e:
                    QMessageBox.warning(self, "error", str(e))
                print(str(names[0]))
                access_label = QLabel("Enter Your Access Token", self.main_group)
                access_label.setStyleSheet(accon_label_style)
                access_label.setFixedWidth(self.width())
                access_label.move(20, 140)
                
                self.button_check_access=localTools.mybutton("Check","click to check access token",style_button,35,"icon/view-refresh.svg",40,35,50,3,40,1,3,33,20,35,self.main_group,int(self.width()-155),135,120)
                self.button_check_access.setDisabled(True)
                
                self.input_api_fb = QLineEdit(self.main_group)
                self.input_api_fb.setFixedSize(540, 35)
                self.input_api_fb.setStyleSheet(self.input_file_style)
                self.input_api_fb.setPlaceholderText("Enter Your Access Token")
                self.input_api_fb.move(19, 175)
                self.input_api_fb.setDisabled(True)
                self.input_api_fb.setToolTip("A fast alternative to registering in your new account for posting by access token , if you want to enable it click check box")

                self.check_input_access = QCheckBox(self.main_group)
                self.check_input_access.move(self.width()-70, 175)
                self.check_input_access.setStyleSheet(self.check_input_access_style)
                self.check_input_access.setFixedSize(35, 35)
                self.check_input_access.stateChanged.connect(self.chack_input_access_def)

                self.conn_sql = sqlite3.connect("test.db")
                self.ex_sql = self.conn_sql.cursor()
                self.ex_sql.execute('SELECT * FROM ADD_USER WHERE NAME = ?', (self.choose_accont.currentText(),))

                rows_n = self.ex_sql.fetchall()
                self.ccess_token = rows_n[0][2]
                self.id_page = rows_n[0][5]

                self.group_info = QGroupBox(self.main_group)
                self.group_info.setFixedSize(575, 175)
                self.group_info.setStyleSheet(div_groups_style)
                self.group_info.move(19, 220)

                self.lable_info_app_id = QLabel("App Id : %s " % (rows_n[0][0]), self.group_info)
                self.lable_info_app_id.setStyleSheet(lable_info_style)
                self.lable_info_app_id.setFixedWidth(300)
                self.lable_info_app_id.move(20, 20)

                self.lable_info_pro_id = QLabel("Account Id : %s " % (rows_n[0][5]), self.group_info)
                self.lable_info_pro_id.setStyleSheet(lable_info_style)
                self.lable_info_pro_id.setFixedWidth(250)
                self.lable_info_pro_id.move(290, 20)

                self.lable_info_app_name = QLabel("App Name : %s" % (rows_n[0][6]), self.group_info)
                self.lable_info_app_name.setStyleSheet(lable_info_style)
                self.lable_info_app_name.setFixedWidth(300)
                self.lable_info_app_name.move(20, 50)

                self.lable_info_name = QLabel("Account Name %s" % (rows_n[0][3]), self.group_info)
                self.lable_info_name.setStyleSheet(lable_info_style)
                self.lable_info_name.move(290, 50)
                self.lable_info_name.setFixedWidth(250)

                self.app_isset = datetime.datetime.fromtimestamp(rows_n[0][7])
                self.label_app_isset = QLabel("Issued at : %s" % (self.app_isset), self.group_info)
                self.label_app_isset.setStyleSheet(lable_info_style)
                self.label_app_isset.move(20, 80)
                self.label_app_isset.setFixedWidth(300)
                
                self.app_end = datetime.datetime.fromtimestamp(rows_n[0][8])
                self.label_app_end = QLabel("Expires at : %s" % (self.app_end), self.group_info)
                self.label_app_end.setStyleSheet(lable_info_style)
                self.label_app_end.move(290, 80)
                self.label_app_end.setFixedWidth(280)
                
                self.get_time_1 = datetime.datetime.strptime(str(self.app_isset), "%Y-%m-%d %H:%M:%S").timestamp()
                self.get_time_2 = datetime.datetime.strptime(str(self.app_end), "%Y-%m-%d %H:%M:%S").timestamp()
                self.total = self.get_time_2-self.get_time_1
                self.res = datetime.timedelta(seconds=int(self.total))
                self.label_time = QLabel("Expiration date : %s" % (self.res), self.group_info)
                self.label_time.setStyleSheet(lable_info_style)
                self.label_time.move(20, 110)
                self.label_time.setFixedWidth(350)
                self.get_time_1_1 = datetime.datetime.now().timestamp()

                self.get_time_1_2 = datetime.datetime.strptime(str(self.app_end), "%Y-%m-%d %H:%M:%S").timestamp()
                self.total_1 = self.get_time_1_2-self.get_time_1_1
                self.res_1 = datetime.timedelta(seconds=int(self.total_1))
                self.label_time_1 = QLabel("Time remaining : %s" % (self.res_1), self.group_info)
                self.label_time_1.setStyleSheet(lable_info_style)
                self.label_time_1.setFixedWidth(350)
                self.label_time_1.move(20, 140)

                self.input_post = QTextEdit(self.main_group)
                self.input_post.setFixedSize(self.width()-55, 150)
                self.input_post.setStyleSheet(input_style)
                self.input_post.setPlaceholderText("Enter Text Post")
                self.input_post.setToolTip("Enter your text you want to post on Facebook")
                self.input_post.move(19, 405)
                
                self.input_file = QLineEdit(self.main_group)
                self.input_file.setFixedSize(self.width()-140, 35)
                self.input_file.setStyleSheet(self.input_file_style)
                self.input_file.setPlaceholderText("add file to post (image , video)")
                self.input_file.move(19, 563)
                
                self.input_file.setDisabled(True)
                self.input_file.setToolTip("add file to post , if you want add file click check box to right and click button add file or write full path file in input ")
                
                self.button_choose_file = localTools.mybutton("","click to add file with file manager",sty_button,35,"icon/document-open.svg",x=35,y=35,mv_x=int(self.width()-115),mv_y=563,posstion=self.main_group,w=35)
                
                self.button_choose_file.setDisabled(True)
                
                self.check_input_file = QCheckBox(self.main_group)
                self.check_input_file.move(self.width()-75, 563)
                self.check_input_file.setStyleSheet(self.check_input_file_style)
                self.check_input_file.setFixedSize(40, 35)
                self.check_input_file.stateChanged.connect(self.chack_input_file_def)
                self.check_input_file.setToolTip("click to enable add file")

                groups_label = QLabel("Select the group you want to post", self.main_group)
                groups_label.setFixedWidth(self.width())
                groups_label.setStyleSheet(accon_label_style)
                groups_label.move(20, 605)

                self.scroll_groups = QScrollArea()
                self.scroll_groups.setWidgetResizable(True)
                self.scroll_groups.setFixedSize(545, 220)
                self.groups_widget = QWidget()
                self.groups_layout = QVBoxLayout()

                self.groups_widget.setLayout(self.groups_layout)
                self.scroll_groups.setWidget(self.groups_widget)
                self.scroll_groups.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.scroll_groups.setStyleSheet(scroll_style)
                self.scroll_groups.setFrameShape(QFrame.NoFrame)
                self.scroll_groups.verticalScrollBar().setStyleSheet(scroll_style)

                self.div_groups = QGroupBox(self.main_group)
                self.div_groups.setStyleSheet(div_groups_style)
                self.div_groups.move(20, 645)
                self.div_groups.setFixedSize(573, 250)
                self.div_groups.setToolTip("select groups in your account")
                self.groups_box_layout = QVBoxLayout()
                self.groups_box_layout.addWidget(self.scroll_groups)
                self.div_groups.setLayout(self.groups_box_layout)
                
                self.button_reload = localTools.mybutton("Refresh","reload groups in account",style_button,35,"icon/view-refresh.svg",40,35,50,3,40,1,3,33,30,40,self.main_group,int(self.width()-175),605,138)
               
                div_groups_button_con = QGroupBox(self.main_group)
                div_groups_button_con.setStyleSheet(div_groups_style)
                div_groups_button_con.move(19, 905)
                div_groups_button_con.setFixedSize(573, 60)
                div_groups_button_con.setParent(self.main_group)
                div_groups_button_con.setToolTip("button control")
                
                self.button_select_all = localTools.mybutton("Select All","Select All groups",style_button_cn,35,"",0,0,posstion=div_groups_button_con,mv_x=int(self.width()-166),mv_y=13,w=94)
                self.button_select_all.setDisabled(True)
                
                self.button_un_select_all = localTools.mybutton("UnSelect All","UnSelect All groups",style_button_cn,35,"",0,0,posstion=div_groups_button_con,mv_x=int(self.width()-300),mv_y=13,w=118)
                self.button_un_select_all.setDisabled(True)
                
                self.button_sh_unselect = localTools.mybutton("Show UnSelect","show group unselect",style_button_cn,35,"",0,0,posstion=div_groups_button_con,mv_x=int(155),mv_y=13,w=152)
                self.button_sh_unselect.setDisabled(True)
                
                self.button_sh_select = localTools.mybutton("Show Select","show group select",style_button_cn,35,"",0,0,posstion=div_groups_button_con,mv_x=int(15),mv_y=13,w=120)
                self.button_sh_select.setDisabled(True)

                div_groups_range = QGroupBox(self.main_group)
                div_groups_range.setStyleSheet(div_groups_style)
                div_groups_range.move(19, 980)
                div_groups_range.setFixedSize(573, 70)
                div_groups_range.setParent(self.main_group)
                div_groups_range.setToolTip("advanced setting ")

                time_sleep_label = QLabel("Timee Sleep", self.main_group)
                time_sleep_label.move(35, 970)
                time_sleep_label.setStyleSheet(range_label_style)

                self.time_spin = QSpinBox(div_groups_range)
                self.time_spin.move(15, 20)
                self.time_spin.setFixedSize(100, 35)
                self.time_spin.setStyleSheet(self.disable_spin)
                self.time_spin.setDisabled(True)
                self.time_spin.setToolTip("The time between post each post and the other ")

                self.check_time_sleep = QCheckBox(div_groups_range)
                self.check_time_sleep.move(120, 20)
                self.check_time_sleep.setFixedSize(35, 35)
                self.check_time_sleep.setStyleSheet(self.check_spin_style)
                self.check_time_sleep.stateChanged.connect(self.chack_time_sleep_def)
                self.check_time_sleep.setToolTip("Enable Time Sleep")

                range_post_label = QLabel("Total Post", self.main_group)
                range_post_label.move(237, 970)
                range_post_label.setStyleSheet(range_label_style)

                self.check_range_post = QCheckBox(div_groups_range)
                self.check_range_post.move(320, 20)
                self.check_range_post.setFixedSize(35, 35)
                self.check_range_post.setStyleSheet(self.check_spin_style)
                self.check_range_post.stateChanged.connect(self.chack_range_post_def)
                self.check_range_post.setToolTip("Enable total Posts to be posted ")

                self.range_post_spin = QSpinBox(div_groups_range)
                self.range_post_spin.move(215, 20)
                self.range_post_spin.setFixedSize(100, 35)
                self.range_post_spin.setStyleSheet(self.disable_spin)
                self.range_post_spin.setMinimum(1)
                self.range_post_spin.setMaximum(200)
                self.range_post_spin.setDisabled(True)
                self.range_post_spin.setToolTip("The number of post in one group ")

                range_post_in_group_label = QLabel("Post in Group", self.main_group)
                range_post_in_group_label.move(436, 970)
                range_post_in_group_label.setStyleSheet(range_label_style)

                self.check_range_post_in_group = QCheckBox(div_groups_range)
                self.check_range_post_in_group.move(520, 20)
                self.check_range_post_in_group.setFixedSize(35, 35)
                self.check_range_post_in_group.setStyleSheet(self.check_spin_style)
                self.check_range_post_in_group.setToolTip("enable Post in Group")
                self.check_range_post_in_group.stateChanged.connect(self.chack_range_post__in_group_def)

                self.range_post_in_group_spin = QSpinBox(div_groups_range)
                self.range_post_in_group_spin.move(415, 20)
                self.range_post_in_group_spin.setFixedSize(100, 35)
                self.range_post_in_group_spin.setStyleSheet(self.disable_spin)
                self.range_post_in_group_spin.setMinimum(1)
                self.range_post_in_group_spin.setMaximum(100)
                self.range_post_in_group_spin.setDisabled(True)
                self.range_post_in_group_spin.setToolTip("The number of post in one group ")

                div_groups_button = QGroupBox(self.main_group)
                div_groups_button.setStyleSheet(div_groups_style)
                div_groups_button.move(19, 1060)
                div_groups_button.setFixedSize(573, 60)
                div_groups_button.setParent(self.main_group)
                div_groups_button.setToolTip("button control")
                
                self.button_start = localTools.mybutton("Start","Start Post",style_button_cn,35,"",0,0,posstion=div_groups_button,mv_x=int(self.width()-166),mv_y=13,w=93)
                
                self.button_stop = localTools.mybutton("Stop","stop or end  Post",style_button_cn,35,"",0,0,posstion=div_groups_button,mv_x=int(self.width()-300),mv_y=13,w=118)
                
                self.button_break = localTools.mybutton("Pause","break post or pause post",style_button_cn,35,"",0,0,posstion=div_groups_button,mv_x=int(156),mv_y=13,w=150)
                 
                self.button_continue = localTools.mybutton("Continue","continue post",style_button_cn,35,"",0,0,posstion=div_groups_button,mv_x=int(15),mv_y=13,w=120)
                
                log_label = QLabel("Log Massage ", self.main_group)
                log_label.setStyleSheet(label_log_style)
                log_label.move(20, 1130)
                
                self.button_clear_log=localTools.mybutton("Clear","clear log",style_button,35,"icon/edit-paste-style.svg",40,35,60,3,45,1,3,33,20,35,self.main_group,int(self.width()-180),1130,140)
                
                self.log = QPlainTextEdit(self.main_group)
                self.log.setReadOnly(True)
                self.log.setFixedSize(570, 260)
                self.log.setStyleSheet(log_style)
                self.log.move(20, 1170)

                log_scroll = QScrollArea(self.main_group)
                log_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                log_scroll.move(20, 1170)
                log_scroll.setFixedSize(573, 264)
                log_scroll.setWidgetResizable(True)
                log_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                log_scroll.setWidget(self.log)
                log_scroll.verticalScrollBar().setStyleSheet(scroll_style)
                
                self.button_back=localTools.mybutton("Back","Back Facebook Tools",style_button,35,"icon/back.png",40,35,60,3,45,1,3,33,20,35,self.main_group,int(self.width()-330),1445,140)
                
                self.button_export=localTools.mybutton("Export","Export log to file log",style_button,35,"icon/export.png",40,35,60,3,45,1,3,33,20,35,self.main_group,int(self.width()-180),1445,140)
                
                self.xstat=None
                self.choose_accont.currentTextChanged.connect(self.button_choose_account_def)
                self.button_check_access.clicked.connect(self.button_check_access_def)
                self.button_choose_file.clicked.connect(self.button_choose_file_def)
                self.button_reload.clicked.connect(self.button_refresh_groups_def)
                self.button_select_all.clicked.connect(self.button_select_all_def)
                self.button_un_select_all.clicked.connect(self.button_un_select_all_def)
                self.button_sh_select.clicked.connect(self.popup_show_select_def)
                self.button_sh_unselect.clicked.connect(self.popup_dishow_select_def)
                self.button_start.clicked.connect(self.start_post_def)
                self.button_stop.clicked.connect(self.stop_posting)
                self.button_break.clicked.connect(self.pasue_posting)
                self.button_continue.clicked.connect(self.continue_posting)
                self.button_clear_log.clicked.connect(self.clear_log_def)
                self.button_export.clicked.connect(self.export_file_fb_def)
                self.button_back.clicked.connect(self.go_back_main)
                
                self.running=True
                self.paused=False
                
            def clear_log_def(self):
                self.log.clear()
            
            class startPost(QThread):
                def __init__(self):
                    super().__init__()
                    self.running=True
                    self.paused=False
                    self.input_postit=post_fb_main.input_post
                    self.input_fileit=post_fb_main.input_file
                    self.logit=post_fb_main.log 
                    self.button_startit=post_fb_main.button_start
                    self.err=[]
                    if len(self.input_postit.toPlainText()) > 5:
                        self.post_text=self.input_postit.toPlainText()
                    elif not len(self.input_postit.toPlainText()) > 5:
                        self.err.append("text_post_err")
                        QMessageBox.warning(self,"Warning","<p style='color :yellow;'>Warning:</p><p>Please enter post text</p>")
                    if self.input_fileit.isEnabled():
                        if len(self.input_fileit.text()) > 1:
                            self.file_upload_post=self.input_fileit.text()
                        elif len(self.input_fileit.text()) < 1:
                            self.err.append("file_null_err")
                            QMessageBox.warning(self,"Warning","<p style='color :yellow;'>Warning:</p><p>Please enter your file by button or write full path</p>")
                def run(self):
                    if len(self.err) == 0:
                        x=0
                        while x<= 200 and self.running:
                            self.button_startit.setEnabled(False)
                            if not self.paused:
                                self.logit.insertPlainText("test"+str(x)+"\n")
                                x+=1
                            time.sleep(1)
                            self.button_startit.setEnabled(True)
                def stopit(self):
                    self.button_stopit=post_fb_main.button_stop
                    self.button_startit.setEnabled(True)
                    self.button_stopit.setEnabled(False)
                    self.running=False
                    
                def pauseit(self):
                    self.button_breakit=post_fb_main.button_break
                    self.button_breakit.setEnabled(False)
                    self.paused=True
                    
                def continueit(self):
                    self.button_continueit=post_fb_main.button_continue
                    self.button_continueit.setEnabled(False)
                    self.button_breakit.setEnabled(True)
                    self.paused=False
                    
            def start_post_def(self):
                self.name=self.sender().text()
                # self.th=Thread(target=self.startPost)
                # self.button_start.setEnabled(False)
                # self.button_stop.setEnabled(True)
                # self.running=True
                # self.paused=False
                self.th=self.startPost()
                self.th.start()
                
            def stop_posting(self):
#                 self.button_start.setEnabled(True)
#                 self.running=False
#                 self.button_stop.setDisabled(True)
                  self.startPost().stopit()
            def pasue_posting(self):
#                 self.button_break.setEnabled(False)
#                 self.paused=True
                  self.startPost().pauseit()
            def continue_posting(self):
#                 self.button_break.setEnabled(True)
#                 self.paused=False
                  self.startPost().stopit()
            
            
            def update_check_def(self):
                list_check_update=self.show_select_group(QDialog).list_check_up
                list_uncheck_update=self.show_select_group(QDialog).list_uncheck_up
                #get_check=self.div_groups
                
                get_checkbox_groups = self.div_groups.findChildren(QCheckBox)
                for check in get_checkbox_groups:
                    for tex in list_check_update:
                        if check.text() == tex:
                            check.setChecked(True)
                for check in get_checkbox_groups:
                    for tex in list_uncheck_update:
                        if check.text() == tex:
                            check.setChecked(False)
                            
            class show_select_group(QDialog):
                def __init__(self, check=None, stat_sh=None):
                    super().__init__()
                    self.send=pyqtSignal(str,str)
                    self.setWindowTitle("Show group select")
                    screen_size = QDesktopWidget().screenGeometry(-1)
                    x = (screen_size.width() - self.frameSize().width()) / 2
                    y = (screen_size.height() - self.frameSize().height()) / 2
                    self.setGeometry(int(x+55), int(y), 530, 580)
                    self.setStyleSheet('background-color : #23252e;')
                    lable_style = """
                    QLabel{
                        color : white;
                        font-size: 20px;
                    }
                    """
                    style_button = """
                        QPushButton{
                                color : white;
                                background-color : #292c37;
                                text-align:center;
                                font-size:20px;
                            }QPushButton:hover{
                                background-color:#1b1d24;
                            }QToolTip{
                                background-color : #292c37;
                                color:white;
                                padding:5px;
                            }
                            """
                    scroll_style = """
                        QScrollBar:vertical {
                            border: none;
                            background:#292c37 ;
                            width: 18px;
                            margin: 0px 0px 0px 0px;
                        }QScrollBar::handle:vertical {
                            background: #1b1d24;
                            min-height: 20px;
                        }QScrollBar::add-line:vertical {
                            border: none;
                            background: #1d66e2;
                            height: 20px;
                            subcontrol-position: bottom;
                            subcontrol-origin: margin;
                        }QScrollBar::sub-line:vertical {
                            border: none;
                            background: #1d66e2;
                            height: 20px;
                            subcontrol-position: top;
                            subcontrol-origin: margin;
                        }QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                            background: none;
                        }QScrollArea::up-arrows{background:red;}
                        """
                    div_groups_style = """
                        QGroupBox{
                            border-radius:5px;
                            border: 1.5px solid #1d66e2;
                            background-color:#1b1d24;
                            color:white;
                        }QGroupBox:hover{
                            border: 2px solid white;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                        }
                        """
                    self.style_check = """
                        QCheckBox{
                            border-radius:20px;
                            font-size:16px;
                            border: 1.5px solid #1b1d24;
                            border-radius:8px;
                            color:white;
                            padding : 5px;
                            background-color:#1b1d24;
                            width:100%;
                        }QCheckBox::indicator{
                            width:15px;
                            height:15px;
                            border: 3px solid #282b36;
                            border-radius:10px;
                        }QCheckBox::indicator:checked{
                            border: 3px solid #282b36;
                            background-color:#1d66e2;
                            border-radius:10px;
                        }QCheckBox:hover{
                            background-color:#1b1d24;
                            border: 1.5px solid #1d66e2 ;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                        }QCheckBox::pressed{
                            background-color :#1d66e2 ;
                        }
                        """

                    self.label_title = QLabel("show elect", self)
                    self.label_title.move(200, 10)
                    self.label_title.setStyleSheet(lable_style)

                    self.scroll_groups_up = QScrollArea()
                    self.scroll_groups_up.setWidgetResizable(True)
                    self.scroll_groups_up.setFixedSize(445, 420)
                    self.groups_widget_up = QWidget()
                    self.groups_layout_up = QVBoxLayout()

                    self.groups_widget_up.setLayout(self.groups_layout_up)
                    self.scroll_groups_up.setWidget(self.groups_widget_up)

                    self.scroll_groups_up.setStyleSheet(scroll_style)
                    self.scroll_groups_up.setFrameShape(QFrame.NoFrame)
                    self.scroll_groups_up.verticalScrollBar().setStyleSheet(scroll_style)
                    self.scroll_groups_up.horizontalScrollBar().setStyleSheet(scroll_style)
                    self.div_groups_up = QGroupBox(self)
                    self.div_groups_up.setStyleSheet(div_groups_style)
                    self.div_groups_up.move(20, 40)
                    self.div_groups_up.setFixedSize(473, 450)
                    self.div_groups_up.setToolTip("select groups in your account")
                    self.groups_box_layout_up = QVBoxLayout()
                    self.groups_box_layout_up.addWidget(self.scroll_groups_up)
                    self.div_groups_up.setLayout(self.groups_box_layout_up)

                    self.get_checkbox_groups_up = check

                    self.button_ok = QPushButton("ok", self)
                    self.button_ok.move(410, 510)
                    self.button_ok.setToolTip("save change and close ")
                    self.button_ok.setStyleSheet(style_button)
                    self.button_ok.setFixedHeight(35)

                    self.button_cli = QPushButton("cancel", self)
                    self.button_cli.move(310, 510)
                    self.button_cli.setToolTip("close without save ")
                    self.button_cli.setStyleSheet(style_button)
                    self.button_cli.setFixedHeight(35)

                    self.button_ok.clicked.connect(self.save_def)
                    self.button_cli.clicked.connect(self.ok_def)
                    self.list_check_up=[]
                    self.list_uncheck_up=[]
                    if stat_sh == "show":
                        self.show_up()
                    elif stat_sh == "dishow":
                        self.dishow_up()
                    else:
                        QMessageBox.warning(self, "Error", "try again")

                def show_up(self):
                    for checkbox in self.get_checkbox_groups_up:

                        checkbox_add = QCheckBox(checkbox)
                        checkbox_add.setStyleSheet(self.style_check)
                        checkbox_add.setFixedHeight(35)
                        self.groups_layout_up.addWidget(checkbox_add)
                        checkbox_add.setChecked(True)

                def dishow_up(self):
                    self.label_title.setText("show unselect")
                    for checkbox in self.get_checkbox_groups_up:
                        checkbox_add = QCheckBox(checkbox)
                        checkbox_add.setStyleSheet(self.style_check)
                        checkbox_add.setFixedHeight(35)
                        self.groups_layout_up.addWidget(checkbox_add)
                        checkbox_add.setChecked(False)

                def save_def(self):
                    
                    for check_up in self.div_groups_up.findChildren(QCheckBox):
                        if check_up.isChecked():
                            self.list_check_up.append(check_up.text())
                        else:
                            self.list_uncheck_up.append(check_up.text())
                    #self.send.emit(list_check_up,list_uncheck_up)
                    #self.send.connect(third_window.T_Fb_main.T_Post.update_check_def)
                    third_window.T_Fb_main.T_Post(stacked_layout).update_check_def
                    self.close()
                    

                def ok_def(self):
                    self.reject()

            def popup_show_select_def(self):
                get_checkbox_groups = self.div_groups.findChildren(QCheckBox)
                list_check = []
                for checked in get_checkbox_groups:
                    if checked.isChecked():
                        list_check.append(checked.text())

                self.show_select_group(list_check, "show").exec_()

            def popup_dishow_select_def(self):
                get_checkbox_groups = self.div_groups.findChildren(QCheckBox)
                list_check = []
                for checked in get_checkbox_groups:
                    if not checked.isChecked():
                        list_check.append(checked.text())
                self.show_select_group(list_check, "dishow").exec_()

            def button_un_select_all_def(self):
                num = 0
                get_checkbox_groups = self.div_groups.findChildren(QCheckBox)
                for check_group in get_checkbox_groups:
                    if check_group.isChecked():
                        check_group.setChecked(False)
                        num += 1
                QMessageBox.information(self, "Info", "%s groups have been successfully deleted" % (num))

            def button_select_all_def(self):
                num = 0
                get_checkbox_groups = self.div_groups.findChildren(QCheckBox)
                for check_group in get_checkbox_groups:
                    if not check_group.isChecked():
                        num += 1
                        check_group.setChecked(True)
                QMessageBox.information(self, "Info", "%s groups have been successfully identified" % (num))
            def button_check_access_def(self):
                th=Thread(target=self.button_check_access_def_th)
                th.start()
                
            def button_check_access_def_th(self):
                if len(self.input_api_fb.text()) < 5 :
                    QMessageBox.warning(self,"Warning","<p style='color :yellow;'>Warning:</p><p>lease enter access token</p>")
                elif not len(self.input_api_fb.text()) < 5:
                    try:
                        access_token = self.input_api_fb.text()
                        self.graph = facebook.GraphAPI(access_token=access_token)
                        self.profile = self.graph.get_object('me')
                        self.button_refresh_groups_def(access_token)
                        self.lable_info_app_id.setText("App Id : None")
                        self.lable_info_app_name.setText("App Name : None")
                        self.lable_info_pro_id.setText("Account Id : %s" % (self.profile['id']))
                        self.lable_info_name.setText("Account Name : %s" % (self.profile['name']))
                        self.label_app_end.setText("Expires It : None")
                        self.label_app_isset.setText("Issued It : None")
                        self.label_time.setText("Expiration Date : None")
                        self.label_time_1.setText("Time Remaining : None")
                        QMessageBox.information(self, "Success", "<font color='green'>Success :</font> <br><font color='white'>Account registration successful</font>")
                        
                    except:
                        QMessageBox.warning(self, "Error", "Check access token ")
                            
            def button_choose_account_def(self, text):
                self.conn_sql = sqlite3.connect("test.db")
                self.ex_sql = self.conn_sql.cursor()
                self.ex_sql.execute('SELECT * FROM ADD_USER WHERE NAME = ?', (text,))
                rows_n = self.ex_sql.fetchall()
                self.lable_info_app_id.setText("App Id : %s" % (rows_n[0][0]))
                self.lable_info_app_name.setText("App Name : %s" % (rows_n[0][6]))
                self.lable_info_pro_id.setText("Account Id : %s" % (rows_n[0][5]))
                self.lable_info_name.setText("Account Name : %s" % (rows_n[0][3]))
                self.app_isset = datetime.datetime.fromtimestamp(rows_n[0][7])

                self.app_end = datetime.datetime.fromtimestamp(rows_n[0][8])
                self.label_app_isset.setText("Issued It : %s" % (self.app_isset))

                self.label_app_end.setText("Expires It : %s" % (self.app_end))
                self.get_time_1 = datetime.datetime.strptime(str(self.app_isset), "%Y-%m-%d %H:%M:%S").timestamp()
                self.get_time_2 = datetime.datetime.strptime(str(self.app_end), "%Y-%m-%d %H:%M:%S").timestamp()
                self.total = self.get_time_2-self.get_time_1
                self.res = datetime.timedelta(seconds=int(self.total))
                self.label_time.setText("Expiration Date : %s" % (self.res))

                self.get_time_1_1 = datetime.datetime.now().timestamp()
                self.get_time_1_2 = datetime.datetime.strptime(str(self.app_end), "%Y-%m-%d %H:%M:%S").timestamp()
                self.total_1 = self.get_time_1_2-self.get_time_1_1
                self.res_1 = datetime.timedelta(seconds=int(self.total_1))
                self.label_time_1.setText("Time Remaining : %s" % (self.res_1))
            @pyqtSlot()
            def button_refresh_groups_def(self):
                th=Thread(target=self.button_refresh_groups_def_th)
                th.start()
            @pyqtSlot()
            def button_refresh_groups_def_th(self):
                try:
                    if not self.input_api_fb.isEnabled():
                        self.conn_sql = sqlite3.connect("test.db")
                        self.ex_sql = self.conn_sql.cursor()
                        self.ex_sql.execute('SELECT * FROM ADD_USER WHERE NAME = ?', (self.choose_accont.currentText(),))
                        rows_n = self.ex_sql.fetchall()
                        self.access_token = rows_n[0][2]

                        self.graph = facebook.GraphAPI(access_token=self.access_token)
                        self.profile = self.graph.get_object('me')
                        page_id = self.profile['id']

                        # print(page_id,self.access_token)
                    elif self.input_api_fb.isEnabled():
                        self.access_token = self.input_api_fb.text()
                        self.graph = facebook.GraphAPI(access_token=self.access_token)
                        self.profile = self.graph.get_object('me')
                        page_id = self.profile['id']
                    else:
                        QMessageBox.warning(self, "Error", "try latter")
                    style_check = """
                         QCheckBox{
                            border-radius:20px;
                            font-size:16px;
                            border: 1.5px solid #1b1d24;
                            border-radius:8px;
                            color:white;
                            padding : 5px;
                            background-color:#1b1d24;
                            width:100%;
                        }QCheckBox::indicator{
                            width:15px;
                            height:15px;
                            border: 3px solid #282b36;
                            border-radius:10px;
                        }QCheckBox::indicator:checked{
                             border: 3px solid #282b36;
                             background-color:#1d66e2;
                             border-radius:10px;
                        }QCheckBox:hover{
                            background-color:#1b1d24;
                            border: 1.5px solid #1d66e2 ;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                        }QCheckBox::pressed{
                            background-color :#1d66e2 ;
                        }
                        """
                    try:
                        graph = facebook.GraphAPI(self.access_token)
                        groups = graph.get_connections(page_id, 'groups')['data']

                        for group in groups:
                            sel = QCheckBox(group['name'])

                            sel.setStyleSheet(style_check)
                            sel.setFixedHeight(35)
                            self.groups_layout.addWidget(sel)
                        self.button_select_all.setDisabled(False)
                        self.button_un_select_all.setDisabled(False)
                        self.button_sh_select.setDisabled(False)
                        self.button_sh_unselect.setDisabled(False)
                    except Exception as e:
                        QMessageBox.warning(self, "Error", "Check access token %s" % (str(e)))
                except :
                    QMessageBox.warning(self, "Error", "Check internet" )
            def button_choose_file_def(self):
                file_paths, _ = QFileDialog.getOpenFileNames(None, "Choose files", "", "image  (*.jpeg *.png *.jpg );;video (*.mp4)")
                self.input_file.setText(", ".join(file_paths))

            def export_file_fb_def(self):
                date_fb = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
                file_name_fb = "KingMarketing-"+str(date_fb)+".log"
                file_path, _ = QFileDialog.getSaveFileName(self, "Save Log File As", file_name_fb, "Log Files (*.log)")
                if file_path:
                    file = QFile(file_path)
                    if file.open(QFile.WriteOnly | QFile.Text):
                        out = QTextStream(file)
                        text = self.log.toPlainText()
                        out << text
                        file.close()

            def go_back_main(self):
                stacked_layout.setCurrentWidget(fb_main)

            def chack_input_file_def(self, state):
                if state:
                    self.check_input_file.setStyleSheet(self.checked_style_file)
                    self.button_choose_file.setDisabled(False)
                    self.input_file.setDisabled(False)
                    self.input_file.setStyleSheet(self.input_file_style)
                else:
                    self.check_input_file.setStyleSheet(self.check_input_file_style)
                    self.button_choose_file.setDisabled(True)
                    self.input_file.setDisabled(True)

            def chack_input_access_def(self, state):
                if state:
                    self.check_input_access.setStyleSheet(self.checked_style_access)
                    self.input_api_fb.setDisabled(False)
                    self.button_check_access.setDisabled(False)
                    self.choose_accont.setDisabled(True)
                else:
                    self.check_input_access.setStyleSheet(self.check_input_access_style)
                    self.input_api_fb.setDisabled(True)
                    self.button_check_access.setDisabled(True)
                    self.choose_accont.setDisabled(False)

            def chack_time_sleep_def(self, state):
                if state:
                    self.check_time_sleep.setStyleSheet(self.checked_style_spin)
                    self.time_spin.setDisabled(False)
                    self.time_spin.setStyleSheet(self.spin_style)
                else:
                    self.check_time_sleep.setStyleSheet(self.check_spin_style)
                    self.time_spin.setStyleSheet(self.disable_spin)
                    self.time_spin.setDisabled(True)

            def chack_range_post_def(self, state):
                if state:
                    self.check_range_post.setStyleSheet(self.checked_style_spin)
                    self.range_post_spin.setStyleSheet(self.spin_style)
                    self.range_post_spin.setDisabled(False)
                else:
                    self.check_range_post.setStyleSheet(self.check_spin_style)
                    self.range_post_spin.setStyleSheet(self.disable_spin)
                    self.range_post_spin.setDisabled(True)

            def chack_range_post__in_group_def(self, state):
                if state:
                    self.check_range_post_in_group.setStyleSheet(self.checked_style_spin)
                    self.range_post_in_group_spin.setStyleSheet(self.spin_style)
                    self.range_post_in_group_spin.setDisabled(False)
                else:
                    self.check_range_post_in_group.setStyleSheet(self.check_spin_style)
                    self.range_post_in_group_spin.setStyleSheet(self.disable_spin)
                    self.range_post_in_group_spin.setDisabled(True)

        class T_profile_fb_main(QMainWindow, QObject):

            def __init__(self, stacked_layout, parent=None):
                super().__init__(parent)
                self.setWindowTitle("Facebook Profile")
                screen_size = QDesktopWidget().screenGeometry(-1)
                x = (screen_size.width() - self.frameSize().width()) / 2
                y = (screen_size.height() - self.frameSize().height()) / 2
                self.setGeometry(int(x), int(y), 300, 300)
                self.setStyleSheet('background-color : #292c37;')
                self.setMinimumSize(300, 300)
                self.setMaximumSize(301, 300)
                self.layout = QVBoxLayout()

            def remove_item(self):
                for button in self.findChildren(QtWidgets.QPushButton):
                    self.layout.removeWidget(button)
                    button.deleteLater()

            def showEvent(self, event):

                self.remove_item()

                scroll_style = """
                    QScrollBar:vertical {
                        border: none;
                        background:#292c37 ;
                        width: 18px;
                        margin: 0px 0px 0px 0px;
                    }QScrollBar::handle:vertical {
                        background: #1b1d24;
                        min-height: 20px;
                    }QScrollBar::add-line:vertical {
                        border: none;
                        background: #1d66e2;
                        height: 20px;
                        subcontrol-position: bottom;
                        subcontrol-origin: margin;
                    }QScrollBar::sub-line:vertical {
                        border: none;
                        background: #1d66e2;
                        height: 20px;
                        subcontrol-position: top;
                        subcontrol-origin: margin;
                    }QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                        background: none;
                    }QScrollArea::up-arrows{
                         background:red;
                    }
                """
                self.layout = QVBoxLayout()
                self.main_group = QWidget()
                self.main_group.setLayout(self.layout)
                self.repaint()
                self.scroll_area = QScrollArea(self)
                self.scroll_area.setWidgetResizable(True)
                self.scroll_area.setWidget(self.main_group)
                self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.scroll_area.setStyleSheet(scroll_style)
                self.scroll_area.setFrameShape(QFrame.NoFrame)
                self.scroll_area.verticalScrollBar().setStyleSheet(scroll_style)
                self.layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)
                self.setCentralWidget(self.scroll_area)

                size_icon = QSize(25, 25)
                lable_style = """
                    QLabel{
                        color : white;
                        font-size: 30px;
                    }
                    """
                self.style_button = """
                QPushButton{
                color : white;
                border: 1.1px solid black;
                border-radius:25px;
                background-color : #323643;
                text-align:left;
                padding-left :3px;
                padding-bottom:2.5px;
                font-size:20px;
                text-decoration: none;
            }QPushButton:hover,QLabel:Name{
                border:none;
                border-radius:25px;
                border:2px solid #2777ff;
            }QToolTip{
                background-color : #292c37;
                color:white;
                padding:5px;
            }
            """
                input_style = """
                    QTextEdit{
                        border-radius: 5px;
                        border: 2px solid black;
                        background-color:;
                        color:#c8c2bb;
                        padding-right:5px;
                        padding-left:5px;
                    }QTextEdit:hover{
                        background-color:#191a20;
                        color:white;
                        border-color:white;
                    }
                """
                self.button_add_account = localTools.mybutton("add Account","add new account", self.style_button, 50,"icon/add_cc.png",65,60,100,10,75,2,3,50,40,50)
                
                self.button_back = localTools.mybutton("Back","back to facebook tools", self.style_button, 50,"icon/back.png",65,60,100,10,75,2,3,50,40,50)
               
                self.layout.addWidget(self.button_add_account)

                self.conn_sql = sqlite3.connect("test.db")
                self.ex_sql = self.conn_sql.cursor()
                self.ex_sql.execute('SELECT NAME FROM ADD_USER')
                self.name_button_clic = None
                rows = self.ex_sql.fetchall()
                self.buttons = []
                for row in rows:
                    x = 0
                    self.name = row[x]
                    x += 1
                    if self.name is not None and len(self.name) > 1:
                        add_button = localTools.mybutton(self.name,"account : %s"%(self.name), self.style_button, 50,"icon/user.png",65,60,100,10,75,2,3,50,40,50)

                        self.layout.addWidget(add_button)
                        add_button.clicked.connect(self.edit_profile_fb_def)
                        self.buttons.append(add_button)

                self.layout.addWidget(self.button_back)

                self.button_add_account.clicked.connect(self.go_add_account_fb)
                self.button_back.clicked.connect(self.go_back_main)

            def edit_profile_fb_def(self):
                name_button_clic = self.sender().objectName()
                edit_profile_fb = third_window.T_Fb_main.T_profile_fb_main.Edite_profile_fb_class(stacked_layout, name_button_clic)
                stacked_layout.addWidget(edit_profile_fb)
                stacked_layout.setCurrentWidget(edit_profile_fb)

            def go_add_account_fb(self):
                stacked_layout.setCurrentWidget(add_account_fb)
            
            def go_back_main(self):
                stacked_layout.setCurrentWidget(fb_main)

            class Edite_profile_fb_class(QMainWindow):
                def __init__(self, stacked_layout, name):
                    super().__init__()

                    self.setWindowTitle("Edite Profile Facebook")
                    screen_size = QDesktopWidget().screenGeometry(-1)
                    x = (screen_size.width() - self.frameSize().width()) / 2
                    y = (screen_size.height() - self.frameSize().height()) / 2
                    self.setGeometry(int(x), int(y-100), 600, 670)
                    self.setStyleSheet('background-color : #23252e;')
                    self.setMinimumSize(600, 670)
                    self.setMaximumSize(601, 670)
                    lable_style = """
                        QLabel{
                            color : white;
                            font-size: 30px;
                        }
                        """
                    lable_info_style = """
                        QLabel{
                            color : white;
                            font-size: 15px;
                            background-color:#1b1d24;
                        }
                        """
                    lable_addr_style = """
                        QLabel{
                            color : white;
                            font-size: 20px;
                            background-color:#1b1d24;
                        }
                        """
                    style_button = """
                        QPushButton{
                            color : white;
                            border: 1.1px solid black;
                            border-radius:9px;
                            background-color : #323643;
                            
                            text-align:center;
                            font-size:20px;
                        }QPushButton:hover{
                            border:none;
                            border-radius:9px;
                            border:2px solid #2777ff;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                        }
                    """
                    style_button_cn = """
                        QPushButton{
                            color : white;
                            border: 1.1px solid black;
                            border-radius:9px;
                            background-color : #323643;
                            padding-left:3px;
                            text-align:left;
                            font-size:20px;
                        }QPushButton:hover{
                            border:none;
                            border-radius:9px;
                            border:2px solid #2777ff;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                        }
                    """
                    sty_button="""
                         QPushButton{
                            border:none;
                            background-color : #1b1d24;
                        }QPushButton:hover{
                            border:none;
                            background-color: #292c37;
                            border-bottom:2px solid #2777ff;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                            }
                    """
                    input_style = """
                        QTextEdit{
                            border-radius: 5px;
                            border: 2px solid black;
                            background-color:;
                            color:#c8c2bb;
                            padding-right:5px;
                            padding-left:5px;
                        }QTextEdit:hover{
                            background-color:#191a20;
                            color:white;
                            background-color : #292c37;
                            border-color:white;
                        }
                    """
                    div_groups_style = """
                        QGroupBox{
                            border-radius:5px;
                            border: 1.5px solid #1d66e2;
                            background-color:#1b1d24;
                            color:white;
                        }QGroupBox:hover{
                            border: 2px solid white;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                        }
                    """
                    self.input_style = """
                        QLineEdit{
                            border-radius: 5px;
                            border: 1px solid #0d0e11;
                            background-color:#292c37;
                            color:#c8c2bb;
                            padding-right:5px;
                            padding-left:5px;
                            font-size:20px;
                        }QLineEdit:hover{
                            border
                        }QLineEdit:focus{
                            background-color:#1b1d24;
                            border-color:#1d66e2;
                            color:white;
                        }
                    """
                    self.check_edit_style = """
                        QCheckBox{
                            border-radius:5px;
                            background-color:#292c37;
                            border: 1.5px solid #0d0e11;
                            color:white;
                        }QCheckBox::indicator{
                            width:40px;
                            height:35px;
                        }QCheckBox:hover{
                            background-color:#1b1d24;
                            border: 1.5px solid #1d66e2 ;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                        }
                        """
                    self.main_group = QGroupBox(self)
                    self.main_group.setFixedSize(self.width(), self.height())

                    size_icon = QSize(25, 25)
                    try:
                        self.name = name
                        self.conn_sql = sqlite3.connect("test.db")
                        self.ex_sql = self.conn_sql.cursor()

                        self.ex_sql.execute('SELECT * FROM ADD_USER WHERE NAME=?', (self.name,))
                        self.rows = self.ex_sql.fetchone()

                        self.label_name = QLabel("Facebook Profile", self)
                        self.label_name.setStyleSheet(lable_style)
                        self.label_name.move(200, 15)
                        self.label_name.setFixedSize(300, 40)

                        self.group_label_info = QGroupBox(self)
                        self.group_label_info.setStyleSheet(div_groups_style)
                        self.group_label_info.setFixedSize(560, 50)
                        self.group_label_info.move(20, 80)

                        self.lable_info = QLabel("get Info Your Account", self.group_label_info)
                        self.lable_info.setStyleSheet(lable_addr_style)
                        self.lable_info.setFixedWidth(250)
                        self.lable_info.move(20, 10)
                        
                        self.button_get_info = localTools.mybutton("Get Info","refresh your information account",style_button,35,"",0,0,posstion=self.group_label_info,mv_x=int(self.width()-155),mv_y=7,w=100) 

                        self.group_info = QGroupBox(self)
                        self.group_info.setFixedSize(560, 175)
                        self.group_info.setStyleSheet(div_groups_style)
                        self.group_info.move(19, 140)

                        self.lable_info_app_id = QLabel("App Id : %s " % (self.rows[0]), self.group_info)
                        self.lable_info_app_id.setStyleSheet(lable_info_style)
                        self.lable_info_app_id.move(20, 20)

                        self.lable_info_pro_id = QLabel("Account Id : %s " % (self.rows[5]), self.group_info)
                        self.lable_info_pro_id.setStyleSheet(lable_info_style)
                        self.lable_info_pro_id.move(290, 20)

                        self.lable_info_app_name = QLabel("App Name : %s" % (self.rows[6]), self.group_info)
                        self.lable_info_app_name.setStyleSheet(lable_info_style)
                        self.lable_info_app_name.move(20, 50)

                        self.lable_info_name = QLabel("Account Name %s" % (self.rows[3]), self.group_info)
                        self.lable_info_name.setStyleSheet(lable_info_style)
                        self.lable_info_name.move(290, 50)

                        self.app_isset = datetime.datetime.fromtimestamp(self.rows[7])
                        self.label_app_isset = QLabel("Issued at : %s" % (self.app_isset), self.group_info)
                        self.label_app_isset.setStyleSheet(lable_info_style)
                        self.label_app_isset.move(20, 80)

                        self.app_end = datetime.datetime.fromtimestamp(self.rows[8])
                        self.label_app_end = QLabel("Expires at : %s" % (self.app_end), self.group_info)
                        self.label_app_end.setStyleSheet(lable_info_style)
                        self.label_app_end.move(290, 80)
                        
                        self.get_time_1 = datetime.datetime.strptime(str(self.app_isset), "%Y-%m-%d %H:%M:%S").timestamp()
                        self.get_time_2 = datetime.datetime.strptime(str(self.app_end), "%Y-%m-%d %H:%M:%S").timestamp()
                        self.total = self.get_time_2-self.get_time_1
                        self.res = datetime.timedelta(seconds=int(self.total))
                        self.label_time = QLabel("Expiration date : %s" % (self.res), self.group_info)
                        self.label_time.setStyleSheet(lable_info_style)
                        self.label_time.move(20, 110)
                        self.label_time.setFixedWidth(350)
                        self.get_time_1_1 = datetime.datetime.now().timestamp()
                        
                        self.get_time_1_2 = datetime.datetime.strptime(str(self.app_end), "%Y-%m-%d %H:%M:%S").timestamp()
                        self.total_1 = self.get_time_1_2-self.get_time_1_1
                        self.res_1 = datetime.timedelta(seconds=int(self.total_1))
                        self.label_time_1 = QLabel("Time remaining : %s" % (self.res_1), self.group_info)
                        self.label_time_1.setStyleSheet(lable_info_style)
                        self.label_time_1.setFixedWidth(350)
                        self.label_time_1.move(20, 140)
                        
                        self.group_edit_info = QGroupBox(self.main_group)
                        self.group_edit_info.setStyleSheet(div_groups_style)
                        self.group_edit_info.setFixedSize(560, 270)
                        self.group_edit_info.move(20, 325)

                        self.lable_info_app_id_fb = QLabel("App Id : ", self.group_edit_info)
                        self.lable_info_app_id_fb.setStyleSheet(lable_info_style)
                        self.lable_info_app_id_fb.move(22, 20)

                        self.edit_app_id_fb = QLineEdit(self.group_edit_info)
                        self.edit_app_id_fb.setFixedSize(435, 40)
                        self.edit_app_id_fb.setStyleSheet(self.input_style)
                        self.edit_app_id_fb.setPlaceholderText("Enter Your App id")
                        self.edit_app_id_fb.setText(str(self.rows[0]))
                        self.edit_app_id_fb.move(20, 45)
                        self.edit_app_id_fb.setReadOnly(True)
                        
                        self.button_copy_id = localTools.mybutton("","cpoy app id",sty_button,40,"icon/edit-copy.svg",x=35,y=40,mv_x=int(460),mv_y=45,posstion=self.group_edit_info,w=35)
                                        
                        self.edit_app_id__check_fb = QCheckBox(self.group_edit_info)
                        self.edit_app_id__check_fb.setStyleSheet(self.check_edit_style)
                        self.edit_app_id__check_fb.setFixedSize(45, 40)
                        self.edit_app_id__check_fb.move(500, 45)
                        self.edit_app_id__check_fb.stateChanged.connect(self.enable_edit_app_id)

                        self.lable_info_app_secert_fb = QLabel("App Secret : ", self.group_edit_info)
                        self.lable_info_app_secert_fb.setStyleSheet(lable_info_style)
                        self.lable_info_app_secert_fb.move(22, 100)

                        self.edit_app_secert_fb = QLineEdit(self.group_edit_info)
                        self.edit_app_secert_fb.setFixedSize(395, 40)
                        self.edit_app_secert_fb.setStyleSheet(self.input_style)
                        self.edit_app_secert_fb.setPlaceholderText("Enter your app secret")
                        self.edit_app_secert_fb.setText(str(self.rows[1]))
                        self.edit_app_secert_fb.move(20, 125)
                        self.edit_app_secert_fb.setReadOnly(True)
                        self.edit_app_secert_fb.setEchoMode(QLineEdit.Password)
                        
                        self.button_copy_secert = localTools.mybutton("","copy secret",sty_button,40,"icon/edit-copy.svg",x=35,y=40,mv_x=int(460),mv_y=125,posstion=self.group_edit_info,w=35)
                        
                        self.button_show_secert_fb = localTools.mybutton("","show and hide password",sty_button,40,"icon/hedd.png",x=55,y=50,mv_x=int(420),mv_y=125,posstion=self.group_edit_info,w=35)
                                                                
                        self.edit_app_secert_check_fb = QCheckBox(self.group_edit_info)
                        self.edit_app_secert_check_fb.setStyleSheet(self.check_edit_style)
                        self.edit_app_secert_check_fb.setFixedSize(45, 40)
                        self.edit_app_secert_check_fb.move(500, 125)
                        self.edit_app_secert_check_fb.stateChanged.connect(self.enable_edit_app_secert)

                        self.lable_info_app_access_fb = QLabel("Access Token : ", self.group_edit_info)
                        self.lable_info_app_access_fb.setStyleSheet(lable_info_style)
                        self.lable_info_app_access_fb.move(22, 180)

                        self.edit_app_access_fb = QLineEdit(self.group_edit_info)
                        self.edit_app_access_fb.setFixedSize(435, 40)
                        self.edit_app_access_fb.setStyleSheet(self.input_style)
                        self.edit_app_access_fb.setPlaceholderText("Enter your access token")
                        self.edit_app_access_fb.setText(str(self.rows[2]))
                        self.edit_app_access_fb.move(20, 205)
                        self.edit_app_access_fb.setReadOnly(True)
                        
                        self.button_copy_access_fb = localTools.mybutton("","copy access token",sty_button,40,"icon/edit-copy.svg",x=35,y=40,mv_x=int(460),mv_y=205,posstion=self.group_edit_info,w=35)
                                                
                        self.edit_app_access_check_fb = QCheckBox(self.group_edit_info)
                        self.edit_app_access_check_fb.setStyleSheet(self.check_edit_style)
                        self.edit_app_access_check_fb.setFixedSize(45, 40)
                        self.edit_app_access_check_fb.move(500, 205)
                        self.edit_app_access_check_fb.stateChanged.connect(self.enable_edit_app_access_token)
                        
                        self.button_back=localTools.mybutton("Back","Back Facebook Tools",style_button_cn,40,"icon/back.png",40,35,60,5,45,1,3,43,20,35,self,int(self.width()-320),int(self.height()-60),140)
                                        
                        self.button_save=localTools.mybutton("Save","Save change",style_button_cn,40,"icon/save.png",40,35,60,5,45,1,3,43,20,35,self,int(self.width()-160),int(self.height()-60),140)
                        
                         
                        self.button_copy_id.clicked.connect(self.copy_id_def)
                        self.button_copy_access_fb.clicked.connect(self.copy_access_def)
                        self.button_copy_secert.clicked.connect(self.copy_secert_def)
                        self.button_show_secert_fb.clicked.connect(self.show_paaswd_secert)
                        self.button_get_info.clicked.connect(self.get_info_def)
                        self.button_back.clicked.connect(self.go_back_main)
                        self.button_save.clicked.connect(self.save_chanage_def)
                    except Exception as e:
                        QMessageBox.warning(self, "Error", "<font color='yellow'>waring :</font> <br><font color='white'>Unable to collect account data, please re-register %s  </font>" % (str(e)))

                def show_paaswd_secert(self):
                    if self.edit_app_secert_fb.echoMode() == QLineEdit.Password:
                        self.edit_app_secert_fb.setEchoMode(QLineEdit.Normal)
                        self.button_show_secert_fb.move(420, 125)
                        self.button_show_secert_fb.setIcon(QIcon("icon/view-hidden.svg"))
                        self.button_show_secert_fb.setIconSize(QSize(35,35))
                    else:
                        self.edit_app_secert_fb.setEchoMode(QLineEdit.Password)
                        self.button_show_secert_fb.move(420, 125)
                        self.button_show_secert_fb.setIcon(QIcon("icon/hedd.png"))
                        self.button_show_secert_fb.setIconSize(QSize(55,50))
                        
                def enable_edit_app_id(self, state):
                    if state:
                        self.edit_app_id_fb.setReadOnly(False)
                    else:
                        self.edit_app_id_fb.setReadOnly(True)

                def enable_edit_app_secert(self, state):
                    if state:
                        self.edit_app_secert_fb.setReadOnly(False)
                    else:
                        self.edit_app_secert_fb.setReadOnly(True)

                def enable_edit_app_access_token(self, state):
                    if state:
                        self.edit_app_access_fb.setReadOnly(False)
                    else:
                        self.edit_app_access_fb.setReadOnly(True)
                def get_info_def(self):
                    th=Thread(target=self.get_info_def_th)
                    th.start()
                def get_info_def_th(self):
                    try:
                        self.graph = facebook.GraphAPI(access_token=self.rows[2])
                        self.token_info = self.graph.debug_access_token(self.rows[2], self.rows[0], self.rows[1])
                        self.profile = self.graph.get_object('me')
                        self.lable_info_app_id.setText("App Id : %s " % (self.token_info['data']['app_id']))
                        self.lable_info_pro_id.setText("Account Id : %s " % (self.token_info['data']['user_id']))
                        self.lable_info_app_name.setText("App Name : %s" % (self.token_info['data']['application']))
                        self.lable_info_name.setText("Account Name %s" % (self.profile['name']))
                        self.app_isset = datetime.datetime.fromtimestamp(self.token_info['data']['issued_at'])
                        self.app_end = datetime.datetime.fromtimestamp(self.token_info['data']['expires_at'])
                    except:
                        QMessageBox.warning(self, "Error", "Check your internet")
                def copy_id_def(self):
                    copy_text=self.edit_app_id_fb.text()
                    QApplication.clipboard().setText(copy_text)
                    
                def copy_access_def(self):
                    copy_text=self.edit_app_access_fb.text()
                    QApplication.clipboard().setText(copy_text)
                    
                def copy_secert_def(self):
                    copy_text=self.edit_app_secert_fb.text()
                    QApplication.clipboard().setText(copy_text)
                    
                def go_back_main(self):
                    stacked_layout.setCurrentWidget(profile_fb)
                def save_chanage_def(self):
                    th=Thread(target=self.save_chanage_def_th)
                    th.start()
                def save_chanage_def_th(self):
                    id_app = self.edit_app_id_fb.text()
                    app_secert = self.edit_app_secert_fb.text()
                    access = self.edit_app_access_fb.text()
                    lable_info_name = self.lable_info_name.text()
                    try:
                        if access != self.rows[2]:

                            self.graph = facebook.GraphAPI(access_token=access)
                            print(1, self.graph)
                            print(id_app, app_secert, access)
                            extended_token = self.graph.extend_access_token(id_app, app_secert)
                            # self.token_info = self.graph.debug_access_token(access,app_secert,id_app)
                            token_info = self.graph.debug_access_token(extended_token['access_token'], id_app, app_secert)
                            # token_info = self.graph.debug_access_token(access, id_app, app_secert)
                            print(2, token_info)
                            profile = self.graph.get_object('me')
                            QMessageBox.information(self, "Login", "<font color='white'>welcome %s in King Marketing</font>" % profile["name"])
                            try:
                                conn = sqlite3.connect("test.db")
                                ex = conn.cursor()
                                ex.execute("SELECT ID_APP FROM ADD_USER WHERE ID_APP=?", (id_app,))
                                re_id_check = ex.fetchone()
                                ex.execute("SELECT APP_SECERT FROM ADD_USER WHERE APP_SECERT=?", (app_secert,))
                                re_secert_check = ex.fetchone()
                                ex.execute("SELECT ACCESS_TOKEN FROM ADD_USER WHERE ACCESS_TOKEN=?", (extended_token['access_token'],))
                                re_accesss_token = ex.fetchone()
                                if re_accesss_token is not None:
                                    QMessageBox.warning(self, "Error", "<font color='yellow'>waring :</font> <br><font color='white'>This account already exists </font>")
                                else:
                                    ex.execute("UPDATE ADD_USER SET ID_APP=?, APP_SECERT=?, ACCESS_TOKEN=?, NAME=?, ID_PTOFILE=?,APP_NAME=?,TIME_START=?,TIME_END=? WHERE NAME=?", (id_app, app_secert,extended_token['access_token'], profile['name'], profile['id'], token_info['data']['application'], token_info['data']['issued_at'], token_info['data']['expires_at'], lable_info_name))
                                    conn.commit()
                                    QMessageBox.information(self, "Success", "<font color='green'>Success :</font> <br><font color='white'>Account registration successful</font>")
                                    conn.close()
                            except Exception as e:
                                QMessageBox.warning(self, "Error", f"<font color='red'>error :</font> <br><font color='white'>Account registration failed{str(e)}</font>")

                        else:
                            QMessageBox.warning(self, "Warning", "The account already exists")
                    except Exception as e:
                        QMessageBox.warning(self, "Error", "Check  internet %s" % (str(e)))

            class T_add_account_fb(QMainWindow):
                def __init__(self, stacked_layout):
                    super().__init__()
                    self.setWindowTitle("add Account Facebook")
                    screen_size = QDesktopWidget().screenGeometry(-1)
                    x = (screen_size.width() - self.frameSize().width()) / 2
                    y = (screen_size.height() - self.frameSize().height()) / 2
                    self.setGeometry(int(x), int(y)+100, 680, 230)
                    self.setStyleSheet('background-color : #23252e;')
                    self.setMinimumSize(680, 230)
                    self.setMaximumSize(681, 231)
                    self.central_widget = QWidget()
                    self.setCentralWidget(self.central_widget)
                    self.layout = QVBoxLayout(self.central_widget)
                    size_icon = QSize(25, 25)
                    lable_style = """
                        QLabel{
                            color : white;
                            font-size: 30px;
                        }
                        """
                    style_button= """
                        QPushButton{
                            color : white;
                            border: 1.1px solid black;
                            border-radius:9px;
                            background-color : #323643;
                            padding-left:3px;
                            text-align:left;
                            font-size:20px;
                        }QPushButton:hover{
                            border:none;
                            border-radius:9px;
                            border:2px solid #2777ff;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                        }
                    """
                    sty_button="""
                         QPushButton{
                            border:none;
                            background-color : #23252e;
                        }QPushButton:hover{
                            border:none;
                            background-color: #323643;
                            border-bottom:2px solid #2777ff;
                        }QToolTip{
                            background-color : #292c37;
                            color:white;
                            padding:5px;
                            }
                    """""
                    
                    self.input_style = """
                        QLineEdit{
                            border-radius: 5px;
                            border: 1px solid #0d0e11;
                            background-color:#292c37;
                            color:#c8c2bb;
                            padding-right:5px;
                            padding-left:5px;
                            font-size:20px;
                        }QLineEdit:hover{
                            border
                        }QLineEdit:focus{
                            background-color:#1b1d24;
                            border-color:#1d66e2;
                            color:white;
                        }
                    """
                    self.messagebox_true = """
                        QLabel{
                            color:white;
                            /*background-color:#292c37;*/
                        }
                        """
                    self.messagebox_false = """
                        QLabel{
                            color:red;
                            background-color:#292c37;
                        }
                    """
                    bg_style="""
                QLabel{
                   background-color:#323643;
                   color:white;
                   font-size:17px;
               }QLabel:hover{
                    color:#2777ff;
                }
                """
                    self.logo = third_window.T_Fb_main.MyLabel(self)
                    self.img = QPixmap('icon/profile.png').scaled(150, 150)
                    self.logo.setPixmap(self.img)
                    self.logo.setGeometry(20, 20, 150, 150)

                    self.input_app_id = QLineEdit(self)
                    self.input_app_id.setFixedSize(430, 40)
                    self.input_app_id.setStyleSheet(self.input_style)
                    self.input_app_id.setPlaceholderText("Enter Your App id")
                    self.input_app_id.move(200, 25)

                    self.input_app_sacert = QLineEdit(self)
                    self.input_app_sacert.setFixedSize(430, 40)
                    self.input_app_sacert.setStyleSheet(self.input_style)
                    self.input_app_sacert.setPlaceholderText("Enter Your App Secret ")
                    self.input_app_sacert.move(200, 75)

                    self.input_api_fb = QLineEdit(self)
                    self.input_api_fb.setFixedSize(430, 40)
                    self.input_api_fb.setStyleSheet(self.input_style)
                    self.input_api_fb.setPlaceholderText("Enter Your Access Token")
                    self.input_api_fb.move(200, 125)
                    
                    self.button_clear_app_id = localTools.mybutton("","reset or clear input id",sty_button,40,"icon/edit-paste-style.svg",x=35,y=40,mv_x=int(635),mv_y=25,posstion=self,w=35)
                    
                    self.button_clear_access = localTools.mybutton("","reset or clear input access token",sty_button,40,"icon/edit-paste-style.svg",x=35,y=40,mv_x=int(635),mv_y=75,posstion=self,w=35)
                    
                    self.button_clear_secert = localTools.mybutton("","reset or clear input secert",sty_button,40,"icon/edit-paste-style.svg",x=35,y=40,mv_x=int(635),mv_y=125,posstion=self,w=35)
                    
                    self.button_add_account = localTools.mybutton("add Account ","Add new account",style_button,40,"icon/add_cc.png",40,35,60,5,45,1,3,43,20,35,self,int(self.width()-210),int(self.height()-50),200)
                    
                 
                    self.button_back=localTools.mybutton("Back","Back Facebook Tools",style_button,40,"icon/back.png",40,35,60,5,45,1,3,43,20,35,self,int(self.width()-480),int(self.height()-50),130)
                                                           
                   
                    self.button_clear=localTools.mybutton("Clear","reset or clear all input",style_button,40,"icon/clearall.png",40,35,58,5,45,1,3,43,20,35,self,int(self.width()-340),int(self.height()-50),120)
                              
                    self.button_clear_app_id.clicked.connect(self.clear_id_fb_def)
                    self.button_clear_access.clicked.connect(self.clear_access_fb_def)
                    self.button_clear_secert.clicked.connect(self.clear_secert_fb_def)
                    self.button_clear.clicked.connect(self.clear_all_input_fb)
                    self.button_add_account.clicked.connect(self.singin_db_fb)
                    self.button_back.clicked.connect(self.go_back_main)
                    
                def clear_id_fb_def(self):
                    self.input_app_id.clear()
                    
                def clear_access_fb_def(self):
                    self.input_api_fb.clear()
                    
                def clear_secert_fb_def(self):
                    self.input_app_sacert.clear()
                    
                def clear_all_input_fb(self):
                    self.input_api_fb.clear()
                    self.input_app_id.clear()
                    self.input_app_sacert.clear()

                def singin_db_fb(self):
                    try:
                        self.app_id = self.input_app_id.text()
                        self.app_sacert = self.input_app_sacert.text()
                        self.access_token = self.input_api_fb.text()
                        graph = facebook.GraphAPI(self.access_token)
                        extended_token = graph.extend_access_token(self.app_id, self.app_sacert)
                        token_info = graph.debug_access_token(extended_token['access_token'], self.app_id, self.app_sacert)

                        profile = graph.get_object('me')
                        QMessageBox.information(self, "Login", "<font color='white'>welcome %s in King Marketing</font>" % profile["name"])
                        try:
                            conn = sqlite3.connect("test.db")
                            ex = conn.cursor()
                            ex.execute("SELECT ID_APP FROM ADD_USER WHERE ID_APP=?", (self.app_id,))
                            re_id_check = ex.fetchone()
                            ex.execute("SELECT APP_SECERT FROM ADD_USER WHERE APP_SECERT=?", (self.app_sacert,))
                            re_secert_check = ex.fetchone()
                            ex.execute("SELECT ACCESS_TOKEN FROM ADD_USER WHERE ACCESS_TOKEN=?", (self.access_token,))
                            re_accesss_token = ex.fetchone()
                            if re_id_check is not None and re_secert_check is not None and re_accesss_token is not None:
                                QMessageBox.warning(self, "Error", "<font color='yellow'>waring :</font> <br><font color='white'>This account already exists </font>")
                            else:
                                ex.execute("INSERT INTO ADD_USER (ID_APP, APP_SECERT, ACCESS_TOKEN, NAME, ID_PTOFILE,APP_NAME,TIME_START,TIME_END) VALUES (?, ?, ?, ?, ?,?,?,?)", (self.app_id, self.app_sacert,extended_token['access_token'], profile['name'], profile['id'], token_info['data']['application'], token_info['data']['issued_at'], token_info['data']['expires_at']))
                                conn.commit()
                                QMessageBox.information(self, "Success", "<font color='green'>Success :</font> <br><font color='white'>Account registration successful</font>")
                                conn.close()
                                self.go_back_main()
                        except Exception as e:
                            QMessageBox.warning(self, "Error", f"<font color='red'>error :</font> <br><font color='white'>Account registration failed{str(e)}</font>")
                        self.input_app_id.clear()
                        self.input_app_sacert.clear()
                        self.input_api_fb.clear()
                    except:
                        QMessageBox.warning(self, "error", "<font color='red'>error :</font> <br><font color='white'>check your date  and try again </font>")
                        self.input_app_id.clear()
                        self.input_app_sacert.clear()
                        self.input_api_fb.clear()

                def go_back_main(self):
                    third_window.T_Fb_main.T_profile_fb_main(stacked_layout)
                    stacked_layout.setCurrentWidget(profile_fb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    stacked_layout = QStackedLayout()
    window = MainWindow(stacked_layout)
    fb_main = SecondWindow.Fb_main(stacked_layout)
    inst_main = SecondWindow.INST_main(stacked_layout)
    tik_main = SecondWindow.TIK_main(stacked_layout)
    snap_main = SecondWindow.SNAP_main(stacked_layout)
    tw_main = SecondWindow.TW_main(stacked_layout)
    wb_main = SecondWindow.WB_main(stacked_layout)
    post_fb_main = third_window.T_Fb_main.T_Post(stacked_layout)
    profile_fb = third_window.T_Fb_main.T_profile_fb_main(stacked_layout)
    add_account_fb = third_window.T_Fb_main.T_profile_fb_main.T_add_account_fb(stacked_layout)

    stacked_layout.addWidget(window)
    stacked_layout.addWidget(fb_main)
    stacked_layout.addWidget(inst_main)
    stacked_layout.addWidget(tik_main)
    stacked_layout.addWidget(snap_main)
    stacked_layout.addWidget(tw_main)
    stacked_layout.addWidget(wb_main)
    stacked_layout.addWidget(post_fb_main)
    stacked_layout.addWidget(profile_fb)
    stacked_layout.addWidget(add_account_fb)

    window.show()
    sys.exit(app.exec_())

