# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(304, 276)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.b1 = QPushButton(Dialog)
        self.b1.setObjectName(u"b1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1.sizePolicy().hasHeightForWidth())
        self.b1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.b1.setFont(font)
        self.b1.setStyleSheet(u"background-color: rgb(170, 85, 127);")

        self.gridLayout.addWidget(self.b1, 0, 0, 1, 1)

        self.b2 = QPushButton(Dialog)
        self.b2.setObjectName(u"b2")
        sizePolicy.setHeightForWidth(self.b2.sizePolicy().hasHeightForWidth())
        self.b2.setSizePolicy(sizePolicy)
        self.b2.setFont(font)
        self.b2.setStyleSheet(u"background-color: rgb(170, 85, 127);")

        self.gridLayout.addWidget(self.b2, 0, 1, 1, 1)

        self.b3 = QPushButton(Dialog)
        self.b3.setObjectName(u"b3")
        sizePolicy.setHeightForWidth(self.b3.sizePolicy().hasHeightForWidth())
        self.b3.setSizePolicy(sizePolicy)
        self.b3.setFont(font)
        self.b3.setStyleSheet(u"background-color: rgb(170, 85, 127);")

        self.gridLayout.addWidget(self.b3, 0, 2, 1, 1)

        self.b4 = QPushButton(Dialog)
        self.b4.setObjectName(u"b4")
        sizePolicy.setHeightForWidth(self.b4.sizePolicy().hasHeightForWidth())
        self.b4.setSizePolicy(sizePolicy)
        self.b4.setFont(font)
        self.b4.setStyleSheet(u"background-color: rgb(170, 85, 127);")

        self.gridLayout.addWidget(self.b4, 1, 0, 1, 1)

        self.b5 = QPushButton(Dialog)
        self.b5.setObjectName(u"b5")
        sizePolicy.setHeightForWidth(self.b5.sizePolicy().hasHeightForWidth())
        self.b5.setSizePolicy(sizePolicy)
        self.b5.setFont(font)
        self.b5.setStyleSheet(u"background-color: rgb(170, 85, 127);")

        self.gridLayout.addWidget(self.b5, 1, 1, 1, 1)

        self.b6 = QPushButton(Dialog)
        self.b6.setObjectName(u"b6")
        sizePolicy.setHeightForWidth(self.b6.sizePolicy().hasHeightForWidth())
        self.b6.setSizePolicy(sizePolicy)
        self.b6.setFont(font)
        self.b6.setStyleSheet(u"background-color: rgb(170, 85, 127);")

        self.gridLayout.addWidget(self.b6, 1, 2, 1, 1)

        self.b7 = QPushButton(Dialog)
        self.b7.setObjectName(u"b7")
        sizePolicy.setHeightForWidth(self.b7.sizePolicy().hasHeightForWidth())
        self.b7.setSizePolicy(sizePolicy)
        self.b7.setFont(font)
        self.b7.setStyleSheet(u"background-color: rgb(170, 85, 127);")

        self.gridLayout.addWidget(self.b7, 2, 0, 1, 1)

        self.b8 = QPushButton(Dialog)
        self.b8.setObjectName(u"b8")
        sizePolicy.setHeightForWidth(self.b8.sizePolicy().hasHeightForWidth())
        self.b8.setSizePolicy(sizePolicy)
        self.b8.setFont(font)
        self.b8.setStyleSheet(u"background-color: rgb(170, 85, 127);")

        self.gridLayout.addWidget(self.b8, 2, 1, 1, 1)

        self.b9 = QPushButton(Dialog)
        self.b9.setObjectName(u"b9")
        sizePolicy.setHeightForWidth(self.b9.sizePolicy().hasHeightForWidth())
        self.b9.setSizePolicy(sizePolicy)
        self.b9.setFont(font)
        self.b9.setStyleSheet(u"background-color: rgb(170, 85, 127);")

        self.gridLayout.addWidget(self.b9, 2, 2, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.b1.setText(QCoreApplication.translate("Dialog", u".", None))
        self.b2.setText(QCoreApplication.translate("Dialog", u".", None))
        self.b3.setText(QCoreApplication.translate("Dialog", u".", None))
        self.b4.setText(QCoreApplication.translate("Dialog", u".", None))
        self.b5.setText(QCoreApplication.translate("Dialog", u".", None))
        self.b6.setText(QCoreApplication.translate("Dialog", u".", None))
        self.b7.setText(QCoreApplication.translate("Dialog", u".", None))
        self.b8.setText(QCoreApplication.translate("Dialog", u".", None))
        self.b9.setText(QCoreApplication.translate("Dialog", u".", None))
    # retranslateUi

