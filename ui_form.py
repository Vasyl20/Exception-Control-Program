# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QTimeEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(807, 587)
        self.timeEdit = QTimeEdit(Widget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(40, 60, 118, 25))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 60, 80, 24))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 181, 16))
        self.timeEdit_2 = QTimeEdit(Widget)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setGeometry(QRect(630, 70, 118, 25))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(580, 30, 161, 16))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 271, 81))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u0427\u0430\u0441 \u0432\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u0412\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044f \u043f\u043e \u0432\u043a\u0430\u0437\u0435\u043d\u0456\u0439 \u0433\u043e\u0434\u0438\u043d\u0456", None))
    # retranslateUi

