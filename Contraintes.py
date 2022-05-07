from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout,QMessageBox,QPushButton,QApplication
import pandas as pd

class Ui_Form(object):
    def Valider(self):
        file='C:/LotSizing/INPUTS.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)
        if self.HS_text.text()=='' and self.LP_text.text()=='' and self.ST_text.text()=='' :
  
                msg=QMessageBox()
                msg.setWindowTitle("Erreur")
                msg.setText("Remplir les cases")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()   
      
        else :
                if self.HS.isChecked() and self.LP.isChecked() and self.ST.isChecked() :
                        y=self.HS_text.text()
                        df.iloc[6,10]=int(y)
                        print(df.iloc[6,10])
                        y1=self.LP_text.text()
                        df.iloc[7,10]=int(y1)                       
                        print(df.iloc[7,10])       
                        y2=self.ST_text.text()
                        df.iloc[8,10]=int(y2)                     
                        print(df.iloc[8,10])                        
                        df.to_excel(file, index=False)
                        
                elif   self.HS.isChecked() and self.LP_text.text()=='' and self.ST_text.text()==''and self.HS_text.text()!='' :
                        y=self.HS_text.text()
                        df.iloc[6,10]=int(y)
                        df.iloc[7,10]=0
                        df.iloc[8,10]=0
                        print(df.iloc[6,10])
                        df.to_excel(file, index=False)  
                                                  
                elif   self.LP.isChecked() and self.HS_text.text()=='' and self.ST_text.text()==''and self.LP_text.text()!='' :
                        y=self.LP_text.text()
                        df.iloc[7,10]=int(y)
                        df.iloc[6,10]=0
                        df.iloc[8,10]=0 
                        print(df.iloc[7,10])   
                        df.to_excel(file, index=False)
                         
                elif   self.ST.isChecked() and self.LP_text.text()=='' and self.HS_text.text()==''and self.ST_text.text()!='' :
                         y=self.ST_text.text()
                         df.iloc[8,10]=int(y)
                         df.iloc[6,10]=0
                         df.iloc[7,10]=0                        
                         print(df.iloc[8,10])
                         df.to_excel(file, index=False) 
                           
                elif self.HS.isChecked() and self.LP.isChecked() and self.ST_text.text()=='' :
                        y=self.HS_text.text()
                        df.iloc[6,10]=int(y)
                        print(df.iloc[6,10])
                        y1=self.LP_text.text()
                        df.iloc[7,10]=int(y1)                       
                        print(df.iloc[7,10])  
                        df.iloc[8,10]=0
                        df.to_excel(file, index=False)
                          
                elif self.HS.isChecked() and self.ST.isChecked() and self.LP_text.text()=='' :
                        y=self.HS_text.text()
                        df.iloc[6,10]=int(y)
                        print(df.iloc[6,10])
                        y1=self.ST_text.text()
                        df.iloc[8,10]=int(y1)                       
                        print(df.iloc[8,10])
                        df.iloc[7,10]=0     
                        df.to_excel(file, index=False)
                             
                elif self.LP.isChecked() and self.ST.isChecked() and self.HS_text.text()=='' :
                        y=self.LP_text.text()
                        df.iloc[7,10]=int(y)
                        print(df.iloc[7,10])
                        y1=self.ST_text.text()
                        df.iloc[8,10]=int(y1)                       
                        print(df.iloc[8,10])     
                        df.iloc[6,10]=0   
                        df.to_excel(file, index=False)
                                      
                else :  
                    msg=QMessageBox()
                    msg.setWindowTitle("Erreur")
                    msg.setText("Remplir les cases")
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()                                   
    def close(self):
            Form.hide()           
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 230)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 601, 231))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.HS = QtWidgets.QCheckBox(self.widget)
        self.HS.setGeometry(QtCore.QRect(80, 70, 281, 21))
        self.HS.setStyleSheet("color: rgb(0, 0, 127);\n"
"\n"
"font: italic 20pt \"Monotype Corsiva\";")
        self.HS.setObjectName("HS")
        self.LP = QtWidgets.QCheckBox(self.widget)
        self.LP.setGeometry(QtCore.QRect(80, 100, 261, 21))
        self.LP.setStyleSheet("color: rgb(0, 0, 127);\n"
"\n"
"font: italic 20pt \"Monotype Corsiva\";")
        self.LP.setObjectName("LP")
        self.ST = QtWidgets.QCheckBox(self.widget)
        self.ST.setGeometry(QtCore.QRect(80, 130, 251, 21))
        self.ST.setStyleSheet("color: rgb(0, 0, 127);\n"
"\n"
"font: italic 20pt \"Monotype Corsiva\";")
        self.ST.setObjectName("ST")
        self.HS_text = QtWidgets.QLineEdit(self.widget)
        self.HS_text.setGeometry(QtCore.QRect(370, 70, 113, 20))
        self.HS_text.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.HS_text.setObjectName("HS_text")
        self.LP_text = QtWidgets.QLineEdit(self.widget)
        self.LP_text.setGeometry(QtCore.QRect(370, 100, 113, 20))
        self.LP_text.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.LP_text.setObjectName("LP_text")
        self.ST_text = QtWidgets.QLineEdit(self.widget)
        self.ST_text.setGeometry(QtCore.QRect(370, 130, 113, 20))
        self.ST_text.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ST_text.setObjectName("ST_text")
        self.OK = QtWidgets.QPushButton(self.widget)
        self.OK.setGeometry(QtCore.QRect(100, 180, 371, 41))
        self.OK.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 127), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.OK.setObjectName("OK")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(120, 20, 321, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 28pt \"Playball\";")
        self.label.setObjectName("label")
        self.OK.clicked.connect(self.Valider)                     
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #self.OK.clicked.connect(Form.close)
 
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("ContraintesHeuristique", "Choisir les contraintes"))
        self.HS.setText(_translate("Form", "Heures Supplémentaires"))
        self.LP.setText(_translate("Form", "Lissage de la production"))
        self.ST.setText(_translate("Form", "Sous-taitance"))

        self.OK.setText(_translate("Form", "Valider les contraintes"))
        self.label.setText(_translate("Form", "Choisir les contraintes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
