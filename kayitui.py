# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit_son.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(781, 514)
        MainWindow.setMinimumSize(QtCore.QSize(100, 100))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 8, 8);")
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buton_kayit = QtWidgets.QPushButton(self.centralwidget)
        self.buton_kayit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buton_kayit.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.buton_kayit.setObjectName("buton_kayit")
        self.gridLayout_2.addWidget(self.buton_kayit, 15, 3, 1, 1)
        self.soyad_line = QtWidgets.QLineEdit(self.centralwidget)
        self.soyad_line.setStyleSheet("background-color: rgb(143, 214, 214);")
        self.soyad_line.setObjectName("soyad_line")
        self.gridLayout_2.addWidget(self.soyad_line, 1, 3, 1, 1)
        self.mail = QtWidgets.QLabel(self.centralwidget)
        self.mail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mail.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mail.setObjectName("mail")
        self.gridLayout_2.addWidget(self.mail, 4, 0, 1, 1)
        self.mail_line = QtWidgets.QLineEdit(self.centralwidget)
        self.mail_line.setStyleSheet("background-color: rgb(143, 214, 214);")
        self.mail_line.setObjectName("mail_line")
        self.gridLayout_2.addWidget(self.mail_line, 4, 3, 1, 1)
        self.mail_tekrar_line = QtWidgets.QLineEdit(self.centralwidget)
        self.mail_tekrar_line.setStyleSheet("background-color: rgb(143, 214, 214);")
        self.mail_tekrar_line.setObjectName("mail_tekrar_line")
        self.gridLayout_2.addWidget(self.mail_tekrar_line, 5, 3, 1, 1)
        self.pasword = QtWidgets.QLabel(self.centralwidget)
        self.pasword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pasword.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.pasword.setObjectName("pasword")
        self.gridLayout_2.addWidget(self.pasword, 6, 0, 1, 1)
        self.pas_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pas_line.setStyleSheet("background-color: rgb(143, 214, 214);")
        self.pas_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pas_line.setObjectName("pas_line")
        self.gridLayout_2.addWidget(self.pas_line, 6, 3, 1, 1)
        self.pasword_tekrar = QtWidgets.QLabel(self.centralwidget)
        self.pasword_tekrar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pasword_tekrar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.pasword_tekrar.setObjectName("pasword_tekrar")
        self.gridLayout_2.addWidget(self.pasword_tekrar, 7, 0, 1, 1)
        self.pas_tek_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pas_tek_line.setStyleSheet("background-color: rgb(143, 214, 214);")
        self.pas_tek_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pas_tek_line.setObjectName("pas_tek_line")
        self.gridLayout_2.addWidget(self.pas_tek_line, 7, 3, 1, 1)
        self.medeni_durum = QtWidgets.QLabel(self.centralwidget)
        self.medeni_durum.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.medeni_durum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.medeni_durum.setObjectName("medeni_durum")
        self.gridLayout_2.addWidget(self.medeni_durum, 8, 0, 2, 1)
        self.Evli = QtWidgets.QRadioButton(self.centralwidget)
        self.Evli.setObjectName("Evli")
        self.gridLayout_2.addWidget(self.Evli, 8, 3, 1, 1)
        self.mail_tekrar = QtWidgets.QLabel(self.centralwidget)
        self.mail_tekrar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mail_tekrar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mail_tekrar.setObjectName("mail_tekrar")
        self.gridLayout_2.addWidget(self.mail_tekrar, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 10, 2, 1, 2)
        self.kontrol = QtWidgets.QCheckBox(self.centralwidget)
        self.kontrol.setObjectName("kontrol")
        self.gridLayout_2.addWidget(self.kontrol, 14, 0, 1, 1)
        self.kurallar = QtWidgets.QTextEdit(self.centralwidget)
        self.kurallar.setEnabled(False)
        self.kurallar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.kurallar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.kurallar.setStyleSheet("font: 10pt \"Wide Latin\";\n"
"background-color: rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);")
        self.kurallar.setFrameShape(QtWidgets.QFrame.Box)
        self.kurallar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.kurallar.setObjectName("kurallar")
        self.gridLayout_2.addWidget(self.kurallar, 13, 0, 1, 6)
        self.buton_esc = QtWidgets.QPushButton(self.centralwidget)
        self.buton_esc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buton_esc.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.buton_esc.setObjectName("buton_esc")
        self.gridLayout_2.addWidget(self.buton_esc, 15, 0, 1, 1)
        self.Bekar = QtWidgets.QRadioButton(self.centralwidget)
        self.Bekar.setObjectName("Bekar")
        self.gridLayout_2.addWidget(self.Bekar, 9, 3, 1, 1)
        self.ad_line = QtWidgets.QLineEdit(self.centralwidget)
        self.ad_line.setStyleSheet("background-color: rgb(143, 214, 214);\n"
"")
        self.ad_line.setObjectName("ad_line")
        self.gridLayout_2.addWidget(self.ad_line, 0, 3, 1, 1)
        self.soyadi = QtWidgets.QLabel(self.centralwidget)
        self.soyadi.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.soyadi.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.soyadi.setObjectName("soyadi")
        self.gridLayout_2.addWidget(self.soyadi, 1, 0, 1, 1)
        self.ad = QtWidgets.QLabel(self.centralwidget)
        self.ad.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ad.setAutoFillBackground(False)
        self.ad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.ad.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ad.setObjectName("ad")
        self.gridLayout_2.addWidget(self.ad, 0, 0, 1, 1)
        self.cinsiyet_group = QtWidgets.QGroupBox(self.centralwidget)
        self.cinsiyet_group.setStyleSheet("background-color: rgb(120, 120, 120);\n"
"")
        self.cinsiyet_group.setObjectName("cinsiyet_group")
        self.gridLayout = QtWidgets.QGridLayout(self.cinsiyet_group)
        self.gridLayout.setObjectName("gridLayout")
        self.erkek = QtWidgets.QRadioButton(self.cinsiyet_group)
        self.erkek.setStyleSheet("color: rgb(255, 255, 255);")
        self.erkek.setObjectName("erkek")
        self.gridLayout.addWidget(self.erkek, 1, 0, 1, 1)
        self.bayan = QtWidgets.QRadioButton(self.cinsiyet_group)
        self.bayan.setStyleSheet("color: rgb(255, 255, 255);")
        self.bayan.setObjectName("bayan")
        self.gridLayout.addWidget(self.bayan, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.cinsiyet_group, 10, 0, 1, 1)
        self.Temizle = QtWidgets.QToolButton(self.centralwidget)
        self.Temizle.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.Temizle.setObjectName("Temizle")
        self.gridLayout_2.addWidget(self.Temizle, 15, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.MENU = QtWidgets.QMenuBar(MainWindow)
        self.MENU.setGeometry(QtCore.QRect(0, 0, 781, 23))
        self.MENU.setObjectName("MENU")
        self.Dosya = QtWidgets.QMenu(self.MENU)
        self.Dosya.setObjectName("Dosya")
        self.Gorunum = QtWidgets.QMenu(self.MENU)
        self.Gorunum.setObjectName("Gorunum")
        self.menuYardim = QtWidgets.QMenu(self.MENU)
        self.menuYardim.setObjectName("menuYardim")
        MainWindow.setMenuBar(self.MENU)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Kayit_ol = QtWidgets.QAction(MainWindow)
        self.Kayit_ol.setShortcutVisibleInContextMenu(True)
        self.Kayit_ol.setObjectName("Kayit_ol")
        self.Iptal = QtWidgets.QAction(MainWindow)
        self.Iptal.setObjectName("iptal")
        self.Yakinlastir = QtWidgets.QAction(MainWindow)
        self.Yakinlastir.setObjectName("Yakinlastir")
        self.Cikis = QtWidgets.QAction(MainWindow)
        self.Cikis.setObjectName("Cikis")
        self.Uzaklastir = QtWidgets.QAction(MainWindow)
        self.Uzaklastir.setObjectName("Uzaklastir")
        self.Dosya.addAction(self.Kayit_ol)
        self.Dosya.addAction(self.Iptal)
        self.Dosya.addAction(self.Cikis)
        self.Gorunum.addAction(self.Yakinlastir)
        self.Gorunum.addAction(self.Uzaklastir)
        self.MENU.addAction(self.Dosya.menuAction())
        self.MENU.addAction(self.Gorunum.menuAction())
        self.MENU.addAction(self.menuYardim.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buton_kayit.setText(_translate("MainWindow", "KAYDET"))
        self.mail.setText(_translate("MainWindow", "  MAIL"))
        self.pasword.setText(_translate("MainWindow", "  PASWORD"))
        self.pasword_tekrar.setText(_translate("MainWindow", "  PASWORD TEKRAR"))
        self.medeni_durum.setText(_translate("MainWindow", "  MEDENI DURUMUNUZ"))
        self.Evli.setText(_translate("MainWindow", "EVLI"))
        self.mail_tekrar.setText(_translate("MainWindow", "  MAIL TEKRAR"))
        self.kontrol.setText(_translate("MainWindow", "OKUDUM KABUL EDIYORUM"))
        self.kurallar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Wide Latin\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\">KURALLAR</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\">1- LUTFEN BILGILERINIZI DOGRU GIRINIZ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\">2- PASWORDUNUZ EN AZ 8 KARAKTERDEN OLUSMALIDIR.LUTFEN GUCLU BIR PASWORD ICIN EN AZ BIR SAYI ,BIR BUYUK HARF,BIR SAYI VE BIR ISARET KARAKTERLERIYLE GUCLENDIRMEYI UNUTMAYIN.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\">3-MAIL ADRESINIZIN ONCEKI KAYITLARLA AYNI OLMAMASINA DIKKAT EDINIZ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\">4- BU BILGILER 3.SAHISLARLA PARA KARSILIGINDA PAYLASILABILIR</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\"><br /></p></body></html>"))
        self.buton_esc.setText(_translate("MainWindow", "IPTAL"))
        self.Bekar.setText(_translate("MainWindow", "BEKAR"))
        self.soyadi.setText(_translate("MainWindow", "  SOYADINIZ"))
        self.ad.setText(_translate("MainWindow", "  ADINIZ"))
        self.cinsiyet_group.setTitle(_translate("MainWindow", "CINSIYET"))
        self.erkek.setText(_translate("MainWindow", "ERKEK"))
        self.bayan.setText(_translate("MainWindow", "BAYAN"))
        self.Temizle.setText(_translate("MainWindow", "TEMIZLE"))
        self.Dosya.setTitle(_translate("MainWindow", "Dosya"))
        self.Gorunum.setTitle(_translate("MainWindow", "Gorunum"))
        self.menuYardim.setTitle(_translate("MainWindow", "Yardim"))
        self.Kayit_ol.setText(_translate("MainWindow", "Kayit Ol"))
        self.Kayit_ol.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.Iptal.setText(_translate("MainWindow", "iptal"))
        self.Iptal.setShortcut(_translate("MainWindow", "Esc"))
        self.Yakinlastir.setText(_translate("MainWindow", "Yakinlastir"))
        self.Yakinlastir.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.Cikis.setText(_translate("MainWindow", "Cikis"))
        self.Cikis.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.Uzaklastir.setText(_translate("MainWindow", "Uzaklastir"))
        self.Uzaklastir.setShortcut(_translate("MainWindow", "Ctrl+U"))
