# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui

class Ui_My_App(object):
    def setupUi(self, My_App):
        My_App.setObjectName("My_App")
        My_App.resize(1431, 767)
        self.centralwidget = QtWidgets.QWidget(My_App)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1411, 731))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        self.tabWidget.setStyleSheet("background-color : teal; color : black; ")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.image_uniqe_code = QtWidgets.QLineEdit(self.tab)
        self.image_uniqe_code.setGeometry(QtCore.QRect(0, 410, 261, 25))
        self.image_uniqe_code.setStyleSheet("color:white;")
        self.image_uniqe_code.setObjectName("image_uniqe_code")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 390, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.upload_photo_button = QtWidgets.QPushButton(self.tab)
        self.upload_photo_button.setGeometry(QtCore.QRect(0, 350, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.upload_photo_button.setFont(font)
        self.upload_photo_button.setStyleSheet("color:purple;\n"
"background-color:white;")
        self.upload_photo_button.setObjectName("upload_photo_button")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(270, 0, 140, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(260, 50, 160, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(266, 96, 120, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(270, 150, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(270, 186, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(270, 230, 110, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(270, 280, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.date_of_birth = QtWidgets.QDateTimeEdit(self.tab)
        self.date_of_birth.setGeometry(QtCore.QRect(260, 340, 441, 51))
        self.date_of_birth.setStyleSheet("color:white;")
        self.date_of_birth.setObjectName("date_of_birth")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(0, 450, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.address = QtWidgets.QLineEdit(self.tab)
        self.address.setGeometry(QtCore.QRect(430, 230, 751, 41))
        self.address.setStyleSheet("color:white;")
        self.address.setObjectName("address")
        self.socia_state = QtWidgets.QComboBox(self.tab)
        self.socia_state.setGeometry(QtCore.QRect(400, 190, 91, 25))
        self.socia_state.setStyleSheet("color:white;")
        self.socia_state.setObjectName("socia_state")
        self.socia_state.addItem("")
        self.socia_state.addItem("")
        self.gender_type = QtWidgets.QComboBox(self.tab)
        self.gender_type.setGeometry(QtCore.QRect(380, 150, 111, 25))
        self.gender_type.setStyleSheet("color:white;")
        self.gender_type.setObjectName("gender_type")
        self.gender_type.addItem("")
        self.gender_type.addItem("")
        self.full_name = QtWidgets.QLineEdit(self.tab)
        self.full_name.setGeometry(QtCore.QRect(430, 104, 831, 31))
        self.full_name.setStyleSheet("color:white;")
        self.full_name.setObjectName("full_name")
        self.first_name = QtWidgets.QLineEdit(self.tab)
        self.first_name.setGeometry(QtCore.QRect(450, 10, 811, 31))
        self.first_name.setStyleSheet("color:white;")
        self.first_name.setObjectName("first_name")
        self.second_name = QtWidgets.QLineEdit(self.tab)
        self.second_name.setGeometry(QtCore.QRect(460, 60, 801, 31))
        self.second_name.setStyleSheet("color:white;")
        self.second_name.setObjectName("second_name")
        self.social_security_number = QtWidgets.QLineEdit(self.tab)
        self.social_security_number.setGeometry(QtCore.QRect(260, 450, 790, 31))
        self.social_security_number.setStyleSheet("color:white;")
        self.social_security_number.setObjectName("social_security_number")
        self.insert_data_button = QtWidgets.QPushButton(self.tab)
        self.insert_data_button.setGeometry(QtCore.QRect(290, 520, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.insert_data_button.setFont(font)
        self.insert_data_button.setStyleSheet("color:purple;\n"
"background-color:white;")
        self.insert_data_button.setObjectName("insert_data_button")
        self.image_person = QtWidgets.QLabel(self.tab)
        self.image_person.setGeometry(QtCore.QRect(0, 10, 251, 331))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setBold(True)
        font.setItalic(True)
        
        self.image_person.setFont(font)
        self.image_person.setObjectName("image_person")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ssn_Modify = QtWidgets.QLabel(self.tab_2)
        self.ssn_Modify.setGeometry(QtCore.QRect(0, 0, 240, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        
        self.ssn_Modify.setFont(font)
        self.ssn_Modify.setObjectName("ssn_Modify")
        self.social_security_number_modify = QtWidgets.QLineEdit(self.tab_2)
        self.social_security_number_modify.setGeometry(QtCore.QRect(260, 0, 990, 41))
        self.social_security_number_modify.setStyleSheet("color:white;")
        self.social_security_number_modify.setObjectName("social_security_number_modify")
        self.social_state_modify_2 = QtWidgets.QLabel(self.tab_2)
        self.social_state_modify_2.setGeometry(QtCore.QRect(0, 70, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        
        self.social_state_modify_2.setFont(font)
        self.social_state_modify_2.setObjectName("social_state_modify_2")
        self.social_state_modify = QtWidgets.QComboBox(self.tab_2)
        self.social_state_modify.setGeometry(QtCore.QRect(150, 70, 86, 25))
        self.social_state_modify.setStyleSheet("color:white;")
        self.social_state_modify.setObjectName("social_state_modify")
        self.social_state_modify.addItem("")
        self.social_state_modify.addItem("")
        self.modify_button = QtWidgets.QPushButton(self.tab_2)
        self.modify_button.setGeometry(QtCore.QRect(320, 60, 271, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        
        self.modify_button.setFont(font)
        self.modify_button.setStyleSheet("color:purple;\n"
"background-color:white;")
        self.modify_button.setObjectName("modify_button")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 220, 51))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.social_security_number_delete = QtWidgets.QLineEdit(self.tab_3)
        self.social_security_number_delete.setGeometry(QtCore.QRect(220, 10, 981, 25))
        self.social_security_number_delete.setStyleSheet("color:white;")
        self.social_security_number_delete.setObjectName("social_security_number_delete")
        self.delete_submit_button = QtWidgets.QPushButton(self.tab_3)
        self.delete_submit_button.setGeometry(QtCore.QRect(540, 80, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        
        self.delete_submit_button.setFont(font)
        self.delete_submit_button.setStyleSheet("color:purple;\n"
"background-color:white;")
        self.delete_submit_button.setObjectName("delete_submit_button")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.upload_photo_button_s = QtWidgets.QPushButton(self.tab_4)
        self.upload_photo_button_s.setGeometry(QtCore.QRect(60, 420, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        
        self.upload_photo_button_s.setFont(font)
        self.upload_photo_button_s.setStyleSheet("color:purple;\n"
"background-color:white;")
        self.upload_photo_button_s.setAutoDefault(False)
        self.upload_photo_button_s.setDefault(False)
        self.upload_photo_button_s.setFlat(False)
        self.upload_photo_button_s.setObjectName("upload_photo_button_s")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(520, 110, 411, 231))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(570, 20, 331, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        
        self.label_15.setFont(font)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet("QLabel { background-color : white; color : blue; }")
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.uploaded_image = QtWidgets.QLabel(self.tab_4)
        self.uploaded_image.setGeometry(QtCore.QRect(60, 30, 351, 391))
        self.uploaded_image.setText("")
        self.uploaded_image.setObjectName("uploaded_image")
        self.recognised_image = QtWidgets.QLabel(self.tab_4)
        self.recognised_image.setGeometry(QtCore.QRect(1050, 70, 301, 391))
        self.recognised_image.setText("")
        self.recognised_image.setObjectName("recognised_image")
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(610, 370, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:gold;\n"
"background-color:white;")
        self.pushButton.setObjectName("pushButton")
        self.f_name_2 = QtWidgets.QLabel(self.tab_4)
        self.f_name_2.setGeometry(QtCore.QRect(0, 490, 101, 40))
        font = QtGui.QFont()
        font.setBold(True)
        
        self.f_name_2.setFont(font)
        self.f_name_2.setObjectName("f_name_2")
        self.first_name_text_2 = QtWidgets.QLabel(self.tab_4)
        self.first_name_text_2.setGeometry(QtCore.QRect(120, 490, 881, 40))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.first_name_text_2.setFont(font)
        self.first_name_text_2.setStyleSheet("color:white;")
        self.first_name_text_2.setObjectName("first_name_text_2")
        self.snd_name_2 = QtWidgets.QLabel(self.tab_4)
        self.snd_name_2.setGeometry(QtCore.QRect(0, 530, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        
        self.snd_name_2.setFont(font)
        self.snd_name_2.setObjectName("snd_name_2")
        self.second_name_text_2 = QtWidgets.QLabel(self.tab_4)
        self.second_name_text_2.setGeometry(QtCore.QRect(120, 530, 871, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.second_name_text_2.setFont(font)
        self.second_name_text_2.setStyleSheet("color:white;")
        self.second_name_text_2.setObjectName("second_name_text_2")
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(0, 570, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.full_name_text_2 = QtWidgets.QLabel(self.tab_4)
        self.full_name_text_2.setGeometry(QtCore.QRect(110, 570, 981, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.full_name_text_2.setFont(font)
        self.full_name_text_2.setStyleSheet("color:white;")
        self.full_name_text_2.setObjectName("full_name_text_2")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(0, 630, 90, 17))
        font = QtGui.QFont()
        font.setBold(True)
        
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gender_text_2 = QtWidgets.QLabel(self.tab_4)
        self.gender_text_2.setGeometry(QtCore.QRect(90, 630, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.gender_text_2.setFont(font)
        self.gender_text_2.setStyleSheet("color:white;")
        self.gender_text_2.setObjectName("gender_text_2")
        self.social_state_m_or_s_2 = QtWidgets.QLabel(self.tab_4)
        self.social_state_m_or_s_2.setGeometry(QtCore.QRect(0, 660, 120, 31))
        font = QtGui.QFont()
        font.setBold(True)
        
        self.social_state_m_or_s_2.setFont(font)
        self.social_state_m_or_s_2.setObjectName("social_state_m_or_s_2")
        self.social_state_text_2 = QtWidgets.QLabel(self.tab_4)
        self.social_state_text_2.setGeometry(QtCore.QRect(110, 660, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.social_state_text_2.setFont(font)
        self.social_state_text_2.setStyleSheet("color:white;")
        self.social_state_text_2.setObjectName("social_state_text_2")
        self.f_address_2 = QtWidgets.QLabel(self.tab_4)
        self.f_address_2.setGeometry(QtCore.QRect(210, 620, 90, 31))
        font = QtGui.QFont()
        font.setBold(True)
        
        self.f_address_2.setFont(font)
        self.f_address_2.setObjectName("f_address_2")
        self.full_address_text_2 = QtWidgets.QLabel(self.tab_4)
        self.full_address_text_2.setGeometry(QtCore.QRect(300, 620, 691, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.full_address_text_2.setFont(font)
        self.full_address_text_2.setStyleSheet("color:white;")
        self.full_address_text_2.setObjectName("full_address_text_2")
        self.dob_2 = QtWidgets.QLabel(self.tab_4)
        self.dob_2.setGeometry(QtCore.QRect(660, 550, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        
        self.dob_2.setFont(font)
        self.dob_2.setObjectName("dob_2")
        self.dob_text_2 = QtWidgets.QLabel(self.tab_4)
        self.dob_text_2.setGeometry(QtCore.QRect(780, 550, 901, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.dob_text_2.setFont(font)
        self.dob_text_2.setStyleSheet("color:white;")
        self.dob_text_2.setObjectName("dob_text_2")
        self.uniqe_image_code_2 = QtWidgets.QLabel(self.tab_4)
        self.uniqe_image_code_2.setGeometry(QtCore.QRect(660, 600, 160, 17))
        font = QtGui.QFont()
        font.setBold(True)
        
        self.uniqe_image_code_2.setFont(font)
        self.uniqe_image_code_2.setObjectName("uniqe_image_code_2")
        self.uic_text_2 = QtWidgets.QLabel(self.tab_4)
        self.uic_text_2.setGeometry(QtCore.QRect(840, 600, 671, 20))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.uic_text_2.setFont(font)
        self.uic_text_2.setStyleSheet("color:white;")
        self.uic_text_2.setObjectName("uic_text_2")
        self.uic_text_3 = QtWidgets.QLabel(self.tab_4)
        self.uic_text_3.setGeometry(QtCore.QRect(520, 670, 671, 17))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        
        self.uic_text_3.setFont(font)
        self.uic_text_3.setStyleSheet("color:white;")
        self.uic_text_3.setObjectName("uic_text_3")
        self.uniqe_image_code_3 = QtWidgets.QLabel(self.tab_4)
        self.uniqe_image_code_3.setGeometry(QtCore.QRect(360, 670, 130, 17))
        font = QtGui.QFont()
        font.setBold(True)
        
        self.uniqe_image_code_3.setFont(font)
        self.uniqe_image_code_3.setObjectName("uniqe_image_code_3")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(1040, 19, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel { background-color : black; color : green; }")
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.ssn_text = QtWidgets.QLabel(self.tab_5)
        self.ssn_text.setGeometry(QtCore.QRect(0, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        self.ssn_text.setFont(font)
        self.ssn_text.setObjectName("ssn_text")
        self.social_security_number_searc_ssn = QtWidgets.QLineEdit(self.tab_5)
        self.social_security_number_searc_ssn.setGeometry(QtCore.QRect(200, 0, 801, 31))
        self.social_security_number_searc_ssn.setObjectName("social_security_number_searc_ssn")
        self.snd_name = QtWidgets.QLabel(self.tab_5)
        self.snd_name.setGeometry(QtCore.QRect(0, 100, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        self.snd_name.setFont(font)
        self.snd_name.setObjectName("snd_name")
        self.social_state_m_or_s = QtWidgets.QLabel(self.tab_5)
        self.social_state_m_or_s.setGeometry(QtCore.QRect(0, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        self.social_state_m_or_s.setFont(font)
        self.social_state_m_or_s.setObjectName("social_state_m_or_s")
        self.f_name = QtWidgets.QLabel(self.tab_5)
        self.f_name.setGeometry(QtCore.QRect(0, 50, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        self.f_name.setFont(font)
        self.f_name.setObjectName("f_name")
        self.label_20 = QtWidgets.QLabel(self.tab_5)
        self.label_20.setGeometry(QtCore.QRect(0, 150, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.dob = QtWidgets.QLabel(self.tab_5)
        self.dob.setGeometry(QtCore.QRect(0, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        self.dob.setFont(font)
        self.dob.setObjectName("dob")
        self.label_22 = QtWidgets.QLabel(self.tab_5)
        self.label_22.setGeometry(QtCore.QRect(0, 200, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.f_address = QtWidgets.QLabel(self.tab_5)
        self.f_address.setGeometry(QtCore.QRect(0, 280, 67, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        self.f_address.setFont(font)
        self.f_address.setObjectName("f_address")
        self.dob_text = QtWidgets.QLabel(self.tab_5)
        self.dob_text.setGeometry(QtCore.QRect(120, 330, 901, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        font.setItalic(True)
        self.dob_text.setFont(font)
        self.dob_text.setStyleSheet("color:white;")
        self.dob_text.setObjectName("dob_text")
        self.gender_text = QtWidgets.QLabel(self.tab_5)
        self.gender_text.setGeometry(QtCore.QRect(120, 200, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        font.setItalic(True)
        self.gender_text.setFont(font)
        self.gender_text.setStyleSheet("color:white;")
        self.gender_text.setObjectName("gender_text")
        self.full_address_text = QtWidgets.QLabel(self.tab_5)
        self.full_address_text.setGeometry(QtCore.QRect(120, 280, 691, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        font.setItalic(True)
        self.full_address_text.setFont(font)
        self.full_address_text.setStyleSheet("color:white;")
        self.full_address_text.setObjectName("full_address_text")
        self.full_name_text = QtWidgets.QLabel(self.tab_5)
        self.full_name_text.setGeometry(QtCore.QRect(120, 150, 981, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        font.setItalic(True)
        self.full_name_text.setFont(font)
        self.full_name_text.setStyleSheet("color:white;")
        self.full_name_text.setObjectName("full_name_text")
        self.first_name_text = QtWidgets.QLabel(self.tab_5)
        self.first_name_text.setGeometry(QtCore.QRect(120, 50, 881, 40))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        font.setItalic(True)
        self.first_name_text.setFont(font)
        self.first_name_text.setStyleSheet("color:white;")
        self.first_name_text.setObjectName("first_name_text")
        self.social_state_text = QtWidgets.QLabel(self.tab_5)
        self.social_state_text.setGeometry(QtCore.QRect(120, 240, 611, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        font.setItalic(True)
        self.social_state_text.setFont(font)
        self.social_state_text.setStyleSheet("color:white;")
        self.social_state_text.setObjectName("social_state_text")
        self.second_name_text = QtWidgets.QLabel(self.tab_5)
        self.second_name_text.setGeometry(QtCore.QRect(120, 100, 871, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        font.setItalic(True)
        self.second_name_text.setFont(font)
        self.second_name_text.setStyleSheet("color:white;")
        self.second_name_text.setObjectName("second_name_text")
        self.Photo_Label = QtWidgets.QLabel(self.tab_5)
        self.Photo_Label.setGeometry(QtCore.QRect(1020, 70, 351, 341))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        
        self.Photo_Label.setFont(font)
        self.Photo_Label.setObjectName("Photo_Label")
        self.uniqe_image_code = QtWidgets.QLabel(self.tab_5)
        self.uniqe_image_code.setGeometry(QtCore.QRect(0, 370, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        self.uniqe_image_code.setFont(font)
        self.uniqe_image_code.setObjectName("uniqe_image_code")
        self.uic_text = QtWidgets.QLabel(self.tab_5)
        self.uic_text.setGeometry(QtCore.QRect(160, 370, 671, 17))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        font.setItalic(True)
        self.uic_text.setFont(font)
        self.uic_text.setStyleSheet("color:white;")
        self.uic_text.setObjectName("uic_text")
        self.search = QtWidgets.QPushButton(self.tab_5)
        self.search.setGeometry(QtCore.QRect(1010, 0, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        
        self.search.setFont(font)
        self.search.setStyleSheet("color:purple;\n"
"background-color:white;")
        self.search.setObjectName("search")
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        My_App.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(My_App)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1431, 22))
        self.menubar.setObjectName("menubar")
        self.menuMy_Project = QtWidgets.QMenu(self.menubar)
        self.menuMy_Project.setObjectName("menuMy_Project")
        My_App.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(My_App)
        self.statusbar.setObjectName("statusbar")
        My_App.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMy_Project.menuAction())

        self.retranslateUi(My_App)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(My_App)

    def retranslateUi(self, My_App):
        _translate = QtCore.QCoreApplication.translate
        My_App.setWindowTitle(_translate("My_App", "MainWindow"))
        self.label.setText(_translate("My_App", "IMAGE UNIQE CODE"))
        self.upload_photo_button.setText(_translate("My_App", "Upload Photo"))
        self.label_2.setText(_translate("My_App", "  First Name :-"))
        self.label_3.setText(_translate("My_App", "  Second Name :-"))
        self.label_4.setText(_translate("My_App", " Full Name :-"))
        self.label_5.setText(_translate("My_App", "Gender :-"))
        self.label_6.setText(_translate("My_App", "Social State :-"))
        self.label_7.setText(_translate("My_App", "Address :-"))
        self.label_8.setText(_translate("My_App", "Date of Birth  :-"))
        self.label_10.setText(_translate("My_App", "SOCIAL SECURITY NUMBER"))
        self.socia_state.setItemText(0, _translate("My_App", "Single"))
        self.socia_state.setItemText(1, _translate("My_App", "Married"))
        self.gender_type.setItemText(0, _translate("My_App", "Male"))
        self.gender_type.setItemText(1, _translate("My_App", "Female"))
        self.insert_data_button.setText(_translate("My_App", "Insert Data"))
        self.image_person.setText(_translate("My_App", "image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("My_App", "Insert"))
        self.ssn_Modify.setText(_translate("My_App", "Social Security Number :-"))
        self.social_state_modify_2.setText(_translate("My_App", "Social State :-"))
        self.social_state_modify.setItemText(0, _translate("My_App", "Single"))
        self.social_state_modify.setItemText(1, _translate("My_App", "Married"))
        self.modify_button.setText(_translate("My_App", "Modify"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("My_App", "Modify"))
        self.label_13.setText(_translate("My_App", "Social Security Number :"))
        self.delete_submit_button.setText(_translate("My_App", "SUBMIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("My_App", "Delete"))
        self.upload_photo_button_s.setText(_translate("My_App", "Upload Person Photo"))
        self.label_14.setText(_translate("My_App", "-----=>"))
        self.label_15.setText(_translate("My_App", "STATUS"))
        self.pushButton.setText(_translate("My_App", "Search By Face"))
        self.f_name_2.setText(_translate("My_App", "  First Name :-"))
        self.first_name_text_2.setText(_translate("My_App", "  First Name"))
        self.snd_name_2.setText(_translate("My_App", "  Second Name :-"))
        self.second_name_text_2.setText(_translate("My_App", "  Second Name"))
        self.label_21.setText(_translate("My_App", " Full Name :-"))
        self.full_name_text_2.setText(_translate("My_App", " Full Name"))
        self.label_23.setText(_translate("My_App", "  Gender :-"))
        self.gender_text_2.setText(_translate("My_App", "  Gender"))
        self.social_state_m_or_s_2.setText(_translate("My_App", "  Social State :-"))
        self.social_state_text_2.setText(_translate("My_App", "  Social State"))
        self.f_address_2.setText(_translate("My_App", "  Address :-"))
        self.full_address_text_2.setText(_translate("My_App", "  Address"))
        self.dob_2.setText(_translate("My_App", " Date of Birth  :-"))
        self.dob_text_2.setText(_translate("My_App", " Date of Birth "))
        self.uniqe_image_code_2.setText(_translate("My_App", "unique_image_code:-"))
        self.uic_text_2.setText(_translate("My_App", "uic"))
        self.uic_text_3.setText(_translate("My_App", "SSN"))
        self.uniqe_image_code_3.setText(_translate("My_App", "SSN :-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("My_App", "Search_by_photo"))
        self.ssn_text.setText(_translate("My_App", "SOCIAL SECURITY NUMBER"))
        self.snd_name.setText(_translate("My_App", "  Second Name :-"))
        self.social_state_m_or_s.setText(_translate("My_App", "  Social State :-"))
        self.f_name.setText(_translate("My_App", "  First Name :-"))
        self.label_20.setText(_translate("My_App", " Full Name :-"))
        self.dob.setText(_translate("My_App", " Date of Birth  :-"))
        self.label_22.setText(_translate("My_App", "  Gender :-"))
        self.f_address.setText(_translate("My_App", "  Address :-"))
        self.dob_text.setText(_translate("My_App", " Date of Birth "))
        self.gender_text.setText(_translate("My_App", "  Gender"))
        self.full_address_text.setText(_translate("My_App", "  Address"))
        self.full_name_text.setText(_translate("My_App", " Full Name"))
        self.first_name_text.setText(_translate("My_App", "  First Name"))
        self.social_state_text.setText(_translate("My_App", "  Social State"))
        self.second_name_text.setText(_translate("My_App", "  Second Name"))
        self.Photo_Label.setText(_translate("My_App", "Photo_Label"))
        self.uniqe_image_code.setText(_translate("My_App", "unique_image_code:-"))
        self.uic_text.setText(_translate("My_App", "uic"))
        self.search.setText(_translate("My_App", "Search By SSN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("My_App", "search_by_ssn"))
        self.menuMy_Project.setTitle(_translate("My_App", "My_Data_Base"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    My_App = QtWidgets.QMainWindow()
    ui = Ui_My_App()
    ui.setupUi(My_App)
    My_App.show()
    sys.exit(app.exec_())
