# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_w_MainWindow(object):
    def setupUi(self, w_MainWindow):
        if not w_MainWindow.objectName():
            w_MainWindow.setObjectName(u"w_MainWindow")
        w_MainWindow.resize(500, 600)
        font = QFont()
        font.setPointSize(12)
        w_MainWindow.setFont(font)
        self.actionExit_Game = QAction(w_MainWindow)
        self.actionExit_Game.setObjectName(u"actionExit_Game")
        self.centralwidget = QWidget(w_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.pb_new_game = QPushButton(self.frame)
        self.pb_new_game.setObjectName(u"pb_new_game")

        self.gridLayout_2.addWidget(self.pb_new_game, 6, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.pb_exit = QPushButton(self.frame)
        self.pb_exit.setObjectName(u"pb_exit")

        self.gridLayout_2.addWidget(self.pb_exit, 8, 0, 1, 1)

        self.le_user_guess = QLineEdit(self.frame)
        self.le_user_guess.setObjectName(u"le_user_guess")
        self.le_user_guess.setMaxLength(3)
        self.le_user_guess.setCursorPosition(0)
        self.le_user_guess.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.le_user_guess, 2, 0, 1, 1)

        self.pb_guess = QPushButton(self.frame)
        self.pb_guess.setObjectName(u"pb_guess")

        self.gridLayout_2.addWidget(self.pb_guess, 7, 0, 1, 1)

        self.lb_result_label = QLabel(self.frame)
        self.lb_result_label.setObjectName(u"lb_result_label")
        self.lb_result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_result_label, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        w_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(w_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        w_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(w_MainWindow)

        QMetaObject.connectSlotsByName(w_MainWindow)
    # setupUi

    def retranslateUi(self, w_MainWindow):
        w_MainWindow.setWindowTitle(QCoreApplication.translate("w_MainWindow", u"Number Guess", None))
        self.actionExit_Game.setText(QCoreApplication.translate("w_MainWindow", u"Exit Game", None))
        self.pb_new_game.setText(QCoreApplication.translate("w_MainWindow", u"New Game", None))
        self.label.setText(QCoreApplication.translate("w_MainWindow", u"Guess The Number 1-100", None))
        self.pb_exit.setText(QCoreApplication.translate("w_MainWindow", u"Exit", None))
        self.le_user_guess.setInputMask("")
        self.le_user_guess.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"Enter Your Guess Here...", None))
        self.pb_guess.setText(QCoreApplication.translate("w_MainWindow", u"Guess", None))
        self.lb_result_label.setText(QCoreApplication.translate("w_MainWindow", u"TextLabel", None))
    # retranslateUi

