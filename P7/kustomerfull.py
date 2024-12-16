# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kustomerfull.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_FormKustomer(object):
    def setupUi(self, FormKustomer):
        FormKustomer.setObjectName("FormKustomer")
        FormKustomer.resize(700, 712)
        self.verticalLayoutWidget = QtWidgets.QWidget(FormKustomer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 10, 110, 140))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(FormKustomer)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(200, 10, 431, 140))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_id = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout_2.addWidget(self.lineEdit_id)
        self.lineEdit_nik = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_nik.setObjectName("lineEdit_nik")
        self.verticalLayout_2.addWidget(self.lineEdit_nik)
        self.lineEdit_nama = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_nama.setObjectName("lineEdit_nama")
        self.verticalLayout_2.addWidget(self.lineEdit_nama)
        self.lineEdit_alamat = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_alamat.setObjectName("lineEdit_alamat")
        self.verticalLayout_2.addWidget(self.lineEdit_alamat)
        self.lineEdit_telp = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_telp.setObjectName("lineEdit_telp")
        self.verticalLayout_2.addWidget(self.lineEdit_telp)
        self.horizontalLayoutWidget = QtWidgets.QWidget(FormKustomer)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(69, 170, 551, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.pushButton.clicked.connect(self.insertKustomer)
        font = QtGui.QFont()
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.pushButton_2.clicked.connect(self.updateKustomer)
        font = QtGui.QFont()
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.pushButton_3.clicked.connect(self.deleteKustomer)
        font = QtGui.QFont()
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.pushButton_4.clicked.connect(self.loadKustomer)
        font = QtGui.QFont()
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.label_3 = QtWidgets.QLabel(FormKustomer)
        self.label_3.setGeometry(QtCore.QRect(69, 210, 750, 40))
        font = QtGui.QFont()
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(FormKustomer)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(69, 260, 551, 361))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget.cellClicked.connect(self.cellClick)

        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(FormKustomer)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(115, 640, 500, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)

        self.lineEdit_3.textChanged.connect(self.clearData)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)

        self.pushButton_5.clicked.connect(self.cariData)
        font = QtGui.QFont()
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.retranslateUi(FormKustomer)
        QtCore.QMetaObject.connectSlotsByName(FormKustomer)

    def cellClick(self, row, column):
        try:
            id = self.tableWidget.item(row, 0).text()
            nik = self.tableWidget.item(row, 1).text()
            name = self.tableWidget.item(row, 2).text()
            alamat = self.tableWidget.item(row, 3).text()
            telp = self.tableWidget.item(row, 4).text()

            self.lineEdit_id.setText(id)
            self.lineEdit_nik.setText(nik)
            self.lineEdit_nama.setText(name)
            self.lineEdit_alamat.setText(alamat)
            self.lineEdit_telp.setText(telp)
        except Exception as e:
            error_message = f"Error: {e}"
            self.label_3.setText(error_message)

    def insertKustomer(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "penjualan"
            )
            cursor = mydb.cursor()
            id = self.lineEdit_id.text()
            nik = self.lineEdit_nik.text()
            name = self.lineEdit_nama.text()
            alamat = self.lineEdit_alamat.text()
            telp = self.lineEdit_telp.text()

            sql = "INSERT INTO customer (id, NIK_cust, name, alamat_cust, telp_cust) VALUES (%s, %s, %s, %s, %s)"
            val = (id, nik, name, alamat, telp)
            cursor.execute(sql, val)
            mydb.commit()
            self.label_3.setText("Data Kustomer Berhasil Dimasukkan!")
            self.lineEdit_id.setText("")
            self.lineEdit_nik.setText("")
            self.lineEdit_nama.setText("")
            self.lineEdit_alamat.setText("")
            self.lineEdit_telp.setText("")
            self.loadKustomer()
        except mc.Error as e:
            error_message = f"Error: {e}"
            self.label_3.setText(error_message)

    def updateKustomer(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "penjualan"
            )
            cursor = mydb.cursor()
            id = self.lineEdit_id.text()
            nik = self.lineEdit_nik.text()
            name = self.lineEdit_nama.text()
            alamat = self.lineEdit_alamat.text()
            telp = self.lineEdit_telp.text()

            sql = "UPDATE customer SET NIK_cust = %s, name = %s, alamat_cust = %s, telp_cust = %s WHERE id = %s"
            val = (nik, name, alamat, telp, id)
            cursor.execute(sql, val)
            mydb.commit()
            self.label_3.setText("Data Kustomer Berhasil Diubah!")
            self.lineEdit_id.setText("")
            self.lineEdit_nik.setText("")
            self.lineEdit_nama.setText("")
            self.lineEdit_alamat.setText("")
            self.lineEdit_telp.setText("")
            self.loadKustomer()
        except mc.Error as e:
            error_message = f"Error: {e}"
            self.label_3.setText(error_message)


    def deleteKustomer(self):
        try:
            mydb = mc.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "penjualan"
            )
            cursor = mydb.cursor()
            selected_row = self.tableWidget.currentRow()
            id = self.tableWidget.item(selected_row, 0).text()
            sql = "DELETE FROM customer WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            mydb.commit()
            self.label_3.setText("Data Kustomer Berhasil Dihapus!")
            self.lineEdit_id.setText("")
            self.lineEdit_nik.setText("")
            self.lineEdit_nama.setText("")
            self.lineEdit_alamat.setText("")
            self.lineEdit_telp.setText("")
            self.loadKustomer()
        except mc.Error as e:
            error_message = f"Error: {e}"
            self.label_3.setText(error_message)


    def loadKustomer(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "penjualan"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM customer ORDER BY id ASC")
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                    self.label_3.setText("Data Kustomer Berhasil Ditampilkan!")
        except mc.Error as err:
            self.label_3.setText("Data Kustomer Gagal Ditampilkan!")

    def cariData(self):
        try:
            keyword = self.lineEdit_3.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="penjualan2"
            )
            cursor = mydb.cursor()
            sql = "SELECT * FROM kustomer WHERE id LIKE %s OR nik LIKE %s OR name LIKE %s OR alamat LIKE %s OR telp LIKE %s"
            val = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword),  "%{}%".format(keyword),  "%{}%".format(keyword))
            cursor.execute(sql, val)
            result = cursor.fetchall()
        
            if not result:
                self.label_3.setText("Data Kustomer Yang Dicari Tidak Ada")
                self.tableWidget.setRowCount(0)
                return

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
            self.label_3.setText("Data Kustomer Yang Dicari Ditampilkan")
        except mc.Error as e:
            self.label_3.setText(f"Terjadi Kesalahan Saat Mencari Data: {e}")

    def clearData (self):
        try:
            keyword = self.lineEdit_3.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="penjualan"
            )
            self.loadKustomer()
        except mc.Error as e:
            self.labelInfo.setText(e)

    def retranslateUi(self, FormKustomer):
        _translate = QtCore.QCoreApplication.translate
        FormKustomer.setWindowTitle(_translate("FormKustomer", "Form"))
        self.label.setText(_translate("FormKustomer", "ID Kustomer"))
        self.label_2.setText(_translate("FormKustomer", "NIK"))
        self.label_4.setText(_translate("FormKustomer", "Nama"))
        self.label_6.setText(_translate("FormKustomer", "Alamat"))
        self.label_5.setText(_translate("FormKustomer", "Telpon"))
        self.pushButton.setText(_translate("FormKustomer", "INSERT"))
        self.pushButton_2.setText(_translate("FormKustomer", "UPDATE"))
        self.pushButton_3.setText(_translate("FormKustomer", "DELETE"))
        self.pushButton_4.setText(_translate("FormKustomer", "LOAD DATA"))
        self.label_3.setText(_translate("FormKustomer", "TextLabel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FormKustomer", "No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FormKustomer", "NIK"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FormKustomer", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FormKustomer", "Alamat"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FormKustomer", "Telpon"))
        self.pushButton_5.setText(_translate("FormKustomer", "SEARCHING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormKustomer = QtWidgets.QWidget()
    ui = Ui_FormKustomer()
    ui.setupUi(FormKustomer)
    FormKustomer.show()
    sys.exit(app.exec_())