from email import message
from operator import index
from pickle import FALSE, TRUE
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout
from re import U
import pandas as pd
import matplotlib.pyplot as plt
from cmath import sqrt
import numpy as np
import img
import os
from PyQt5.QtWidgets import QHBoxLayout,QMessageBox,QPushButton,QApplication
from ContraintesAnnuel import Ui_ContraintesHeuristique
from fpdf import FPDF


class Ui_QECAnnuel(object):
    def openContraintes(self): 
         self.window = QtWidgets.QMainWindow()
         self.ui= Ui_QECAnnuel()
         self.ui.setupUi(self.window)
         self.window.show()


    def loadaQEC(self):
          #import QEC
        file='C:/LotSizing/INPUTSAnnuel.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)
        nbr_row=df.shape[0]#sheet1
        nbr_cel=len(df.iloc[0])
        l=[]
        l=df.iloc[0,1:13].to_list()
        x=len(l) 
        ln=x+1
        D=(df.iloc[0,1:ln].sum()/x)
        Cc=df.iloc[16,1]
        Cp=df.iloc[17,1]
        Q=round(sqrt((2*Cc*D)/Cp).real)
        df.iloc[27,1]=Q
        df.iloc[1,1]=df.iloc[27,1]
        df.iloc[2,1]=df.iloc[1,1]-df.iloc[0,1]

        for j in range (2,ln):
            for i in range (1):
                if df.iloc[0,j]>=df.iloc[2,j-1]:
                 df.iloc[1,j] = df.iloc[27,1]
                 df.iloc[2,j]=df.iloc[2,j-1]+df.iloc[1,j]-df.iloc[0,j] 

                else :
                    df.iloc[1,j]=0
                    df.iloc[2,j]=df.iloc[2,j-1]+df.iloc[1,j]-df.iloc[0,j]

        for j in range (1,ln):
            df.iloc[5,j]=df.iloc[1,j]
            df.iloc[7,j]=df.iloc[5,j]/df.iloc[6,j]  
            
            if df.iloc[7,j]>1 : 

                df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                if ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0):
                    df.iloc[10,j]=0
                    df.iloc[11,j]=0
                    df.iloc[12,j]=0   
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[11,j]=0
                 df.iloc[12,j]=0    
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[12,j]=0   
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=0
                 df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]  
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[12,j]=0
                      df.iloc[11,j]=0    
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]       
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[11,j]=0  
                    elif(df.iloc[10,1:ln].sum()*df.iloc[22,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]     
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[12,j]=0
                      df.iloc[11,j]= 0        
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[11,j]= 0                                                                                                                           
                elif ((df.iloc[21,1])>0 and (df.iloc[22,1])>0 and (df.iloc[23,1])>0) :       
                    if ((df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )and (df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ))and (df.iloc[21,1])and (df.iloc[22,1]):
                        df.iloc[10,j]=0
                        df.iloc[12,j]=0
                        df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                        
                            
                    elif  ((df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )or(df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] )and (df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] ))and (df.iloc[23,1])and (df.iloc[22,1]) :
                        df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[12,j]=0
                        df.iloc[11,j]=0
                    else :    
                        df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[11,j]=0
                        df.iloc[10,j]=0

        for j in range (1,ln):
                if df.iloc[1,j]>0:
                    l=[]
                    l=df.iloc[1,1:ln].to_list()
                    try:
                        while True:
                            l.remove(0)
                    except ValueError:
                        pass

                    x=len(l)

        y=[]
        y=df.iloc[2,1:ln].to_list()
        for item in df.iloc[2,1:ln]: 
            if item >0: 
                y.remove(item)

        abs(sum(y))
        df.iloc[18,1]=x*df.iloc[16,1]+abs(abs(df.iloc[2,1:ln].sum()))*df.iloc[17,1]
        df.iloc[25,1]=df.iloc[18,1]+df.iloc[10,1:ln].sum()*df.iloc[21,1]+df.iloc[11,1:ln].sum()*df.iloc[22,1]+df.iloc[12,1:ln].sum()*df.iloc[23,1]+abs(sum(y))*df.iloc[24,1]
        df.to_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSQEC.xlsx', index=False)

        df = pd.read_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSQEC.xlsx')
        if df.size == 0:
            return

        df.fillna('', inplace=True)
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        # returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0.2f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row[0], col_index, tableItem)

        print("importer")
        self.tableWidget.setColumnWidth(3, 100)       
        self.tableWidget.setColumnWidth(11, 100) 
        l1=df.iloc[10,1:13].tolist()
        l1.remove(0)
        c1=len(l1)
        l2=df.iloc[11,1:13].tolist()
        l2.remove(0)
        c2=len(l2)
        l3=df.iloc[12,1:13].tolist()
        l3.remove(0)
        c3=len(l3)
        if  ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0)  :  
         if  (c1>0 or c2>0 or c3>0) : 
                  msg=QMessageBox()
                  msg.setWindowTitle("Erreur")
                  msg.setText("La capacité n'est pas suffisante .\n "
                              "voulez-vous résoudre ce problème? \n")
                  msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                  
                  msg.setIcon(QMessageBox.Critical)
                  x = msg.exec_()
                  if x==QtWidgets.QMessageBox.Yes: 
                          self.window = QtWidgets.QMainWindow()
                          self.ui= Ui_ContraintesHeuristique()
                          self.ui.setupUi(self.window)
                          self.window.show()
                  else: 
                         msg.close() 
         
    def imprimerapport(self):        

        data=pd.read_excel("C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSQEC.xlsx")
        df=pd.DataFrame(data)         
        pdf = FPDF() # A4 (210 by 297 mm)
        ''' First Page '''
        pdf.add_page()
        
        pdf.set_font('arial', 'B', 28)
        pdf.set_text_color(255,0,0)
        pdf.cell(60)
        pdf.cell(70, 30, 'Rapport statistique', 0, 2, 'C')
        pdf.cell(-40)
        pdf.ln(1.5)

        
        pdf.set_font('arial', 'B', 12)
        pdf.set_text_color(0,0,255)
        pdf.cell(50, 10, 'Période', 1, 0, 'C')
        pdf.cell(40, 10, 'Besoins Nets', 1, 0, 'C')
        pdf.cell(70, 10, 'Récéption prévisionnelles', 1, 2, 'C')
        pdf.cell(-90)
        pdf.set_font('arial', '', 12)
        for j in range(1, 13):
            col_ind = str(j)
            col_a = str(df.iloc[0,j])
            col_b = str(df.iloc[1,j])
            pdf.set_font('arial', '', 12)
            pdf.cell(50, 10, '%s' % (col_ind), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (col_a), 0, 0, 'C')
            pdf.cell(40, 10, '%s' % (col_b), 0, 2, 'C')
            pdf.cell(-90) 
               
        ''' Second Page '''
        pdf.add_page()
        
        pdf.set_font('arial', 'B', 28)
        pdf.set_text_color(0,0,0)
        pdf.cell(60)
        pdf.cell(70, 30, 'Rapport Charge/Capacité', 0, 2, 'C')
        pdf.cell(-40)

        pdf.set_font('arial', 'B', 12)
        pdf.set_text_color(0,0,255)
        pdf.cell(50, 10, 'Charge', 1, 0, 'C')
        pdf.cell(40, 10, 'Capacité', 1, 0, 'C')
        pdf.cell(70, 10, 'Rapport Charge/Capacité', 1, 2, 'C')
        pdf.cell(-90)
        pdf.set_font('arial', '', 12)
        for j in range(1, 13):
            col_ind = str(df.iloc[5,j])
            col_a = str(df.iloc[6,j])
            col_b = str(df.iloc[7,j])
            pdf.set_font('arial', '', 12)
            pdf.cell(50, 10, '%s' % (col_ind), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (col_a), 0, 0, 'C')
            pdf.cell(40, 10, '%s' % (col_b), 0, 2, 'C')
            pdf.cell(-90)
        ''' third Page '''
        pdf.add_page()
        
        pdf.set_font('arial', 'B', 28)
        pdf.set_text_color(0,0,0)
        pdf.cell(60)
        pdf.cell(70, 30, 'Choix de contrainte', 0, 2, 'C')
        pdf.cell(-40)

        pdf.set_font('arial', 'B', 12)
        pdf.set_text_color(0,0,255)
        pdf.cell(50, 10, 'Heures Supplémentaires', 1, 0, 'C')
        pdf.cell(40, 10, 'Lissage de Charge', 1, 0, 'C')
        pdf.cell(50, 10, 'Sous_traitance', 1, 2, 'C')
        pdf.cell(-90)
        pdf.set_font('arial', '', 12)
        for j in range(1, 13):
            col_ind = str(df.iloc[10,j])
            col_a = str(df.iloc[11,j])
            col_b = str(df.iloc[12,j])
            pdf.set_font('arial', '', 12)
            pdf.cell(50, 10, '%s' % (col_ind), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (col_a), 0, 0, 'C')
            pdf.cell(40, 10, '%s' % (col_b), 0, 2, 'C')
            pdf.cell(-90)
        ''' fourth Page '''
        pdf.add_page()
        
        pdf.set_font('arial', 'B', 28)
        pdf.set_text_color(0,0,0)
        pdf.cell(60)
        pdf.cell(70, 30, 'Choix de contrainte', 0, 2, 'C')
        pdf.cell(-40)

        pdf.set_font('arial', 'B', 12)
        pdf.set_text_color(0,0,255)
        pdf.cell(50, 10, 'Coût de production', 1, 0, 'C')

        pdf.cell(-90)
        pdf.set_font('arial', '', 12)
        for j in range(25, 1):
            col_ind = str(df.iloc[12,10])

            pdf.set_font('arial', '', 12)
            pdf.cell(50, 10, '%s' % (col_ind), 2, 2, 'C')

            pdf.cell(-90)

            
        pdf.add_page() 

        pdf.image("C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSQEC.png",0,30,200)
        pdf.ln(3)
        a=df.iloc[7,1:13].tolist()
        a.remove(0)
        c1=len(a) 
        if c1>0:
             pdf.ln(1.5) 
             pdf.set_font('arial', 'B', 12)
             pdf.set_text_color(255,0,0)
             pdf.cell(50, 10, "Votre capacité n'est pas suffisate pour covrir la demande")
             pdf.cell(-90)         
        else :
             pdf.ln(1.5) 
             pdf.set_font('arial', 'B', 12)
             pdf.set_text_color(255,0,0)
             pdf.cell(50, 10, "Votre capacité dépasse la demande")
             pdf.cell(-90)         
        pdf.output('C:/LotSizing/OUTPUTSAnnuel/RapportQECAnnuelle.pdf', 'F')
        
    def imprimegraphe(self):
        filepath2="C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSQEC.png"
        os.startfile(filepath2,'print')          
           
    def loaddata(self):
        df = pd.read_excel('C:/LotSizing/INPUTSAnnuel.xlsx')
        if df.size == 0:
            return

        df.fillna('', inplace=True)
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        # returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0.2f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row[0], col_index, tableItem)

        print("importer")
        self.tableWidget.setColumnWidth(0, 300)  
        
    def export(self):
        columnHeaders = []

        # create column header list
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders)

        # create dataframe object recordset
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                df.at[row, columnHeaders[col]] = self.tableWidget.item(row, col).text()

        df.to_csv('C:/LotSizing/INPUTSAnnuel.csv',index=False)
        csv=pd.read_csv('C:/LotSizing/INPUTSAnnuel.csv')
        csv['P1'].astype(float).head()
        csv['P2'].astype(float).head()
        csv['P3'].astype(float).head()
        csv['P4'].astype(float).head()
        csv['P5'].astype(float).head()
        csv['P6'].astype(float).head()
        csv['P8'].astype(float).head()
        csv['P10'].astype(float).head()
        csv['P11'].astype(float).head()
        csv['P12'].astype(float).head()


  
        csv.to_excel('C:/LotSizing/INPUTSAnnuel.xlsx',index=False,float_format='%2f')
        print('Excel file exported')
        
    def loadaGrapheQEC(self):
        file='C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSQEC.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)   
        X=df.iloc[5,1:14]
        Y=df.iloc[25,1]
        index = ['P1', 'P2', 'P3','P4', 'P5', 'P6', 'P7','P8','P9','P10','P11','P12']
        f = pd.DataFrame({'Charge': X,'Capacité': Y}, index=index)       
        ax = f.plot.bar(rot=0)
        ax.set_ylabel('Capacité')
        ax.set_xlabel('Périodes')
        ax.set_title('Histogramme de charge et capacité') 
        plt.show()
        plt.savefig('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSQEC.png')
   
    def comparaisonGraphe(self): 
        file='C:/LotSizing/INPUTSAnnuel.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)


        l=[]
        l=df.iloc[0,1:13].to_list()
        x=len(l) 
        ln=x+1
        D=(df.iloc[0,1:ln].sum()/x)
        Cc=df.iloc[16,1]
        Cp=df.iloc[17,1]
        Q=round(sqrt((2*Cc*D)/Cp).real)
        df.iloc[27,1]=Q
        EPQ=round(Q/D)
        print(EPQ)

        df.iloc[2,1]=df.iloc[1,1] -df.iloc[0,1]
        for j in range (1,EPQ):
            df.iloc[1,1]=df.iloc[0,1:EPQ+1].sum()
        for l in range (EPQ,ln-1):
            if l%EPQ==0:
    
              df.iloc[1,l+1]=df.iloc[0,l+1:l+EPQ+1].sum()
            else:
              df.iloc[1,l]==0


        df.iloc[2,1]=df.iloc[1,1] -df.iloc[0,1]
        for j in range (2,ln):
            df.iloc[2,j] =df.iloc[2,j-1] +df.iloc[1,j] -df.iloc[0,j]

        for j in range (1,ln):
            df.iloc[5,j]=df.iloc[1,j]
            df.iloc[7,j]=df.iloc[5,j]/df.iloc[6,j]  
            
            if df.iloc[7,j]>1 : 

                df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                if ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0):
                    df.iloc[10,j]=0
                    df.iloc[11,j]=0
                    df.iloc[12,j]=0   
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[11,j]=0
                 df.iloc[12,j]=0    
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[12,j]=0   
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=0
                 df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]  
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[12,j]=0
                      df.iloc[11,j]=0    
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]       
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[11,j]=0  
                    elif(df.iloc[10,1:ln].sum()*df.iloc[22,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]     
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[12,j]=0
                      df.iloc[11,j]= 0        
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[11,j]= 0                                                                                                                           
                elif ((df.iloc[21,1])>0 and (df.iloc[22,1])>0 and (df.iloc[23,1])>0) :       
                    if ((df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )and (df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ))and (df.iloc[21,1])and (df.iloc[22,1]):
                        df.iloc[10,j]=0
                        df.iloc[12,j]=0
                        df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                        
                            
                    elif  ((df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )or(df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] )and (df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] ))and (df.iloc[23,1])and (df.iloc[22,1]) :
                        df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[12,j]=0
                        df.iloc[11,j]=0
                    else :    
                        df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[11,j]=0
                        df.iloc[10,j]=0

        for j in range (1,ln):
                if df.iloc[1,j]>0:
                    l=[]
                    l=df.iloc[1,1:ln].to_list()
                    try:
                        while True:
                            l.remove(0)
                    except ValueError:
                        pass

                    x=len(l)

        y=[]
        y=df.iloc[2,1:ln].to_list()
        for item in df.iloc[2,1:ln]: 
            if item >0: 
                y.remove(item)

        abs(sum(y))
        df.iloc[18,1]=x*df.iloc[16,1]+abs(df.iloc[2,1:ln].sum())*df.iloc[17,1]
        df.iloc[25,1]=df.iloc[18,1]+df.iloc[10,1:ln].sum()*df.iloc[21,1]+df.iloc[11,1:ln].sum()*df.iloc[22,1]+df.iloc[12,1:ln].sum()*df.iloc[23,1]+abs(sum(y))*df.iloc[24,1]
        df.to_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSEPQ.xlsx', index=False)

          #import QEC
        file='C:/LotSizing/INPUTSAnnuel.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)

        l=[]
        l=df.iloc[0,1:13].to_list()
        x=len(l) 
        ln=x+1        
        D=(df.iloc[0,1:ln].sum()/x)
        Cc=df.iloc[16,1]
        Cp=df.iloc[17,1]
        Q=round(sqrt((2*Cc*D)/Cp).real)
        df.iloc[27,1]=Q


        #remplir les tables

        for j in range (2,ln):
            df.iloc[1,1]=df.iloc[0,1]   
            df.iloc[1,j]=df.iloc[0,j]
            df.iloc[2,j]=df.iloc[2,j-1]+df.iloc[1,j]-df.iloc[0,j] 

        for j in range (1,ln):
            df.iloc[5,j]=df.iloc[1,j]
            df.iloc[7,j]=df.iloc[5,j]/df.iloc[6,j]  
            
            if df.iloc[7,j]>1 : 

                df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                if ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0):
                    df.iloc[10,j]=0
                    df.iloc[11,j]=0
                    df.iloc[12,j]=0   
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[11,j]=0
                 df.iloc[12,j]=0    
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[12,j]=0   
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=0
                 df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]  
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[12,j]=0
                      df.iloc[11,j]=0    
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]       
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[11,j]=0  
                    elif(df.iloc[10,1:ln].sum()*df.iloc[22,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]     
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[12,j]=0
                      df.iloc[11,j]= 0        
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[11,j]= 0                                                                                                                           
                elif ((df.iloc[21,1])>0 and (df.iloc[22,1])>0 and (df.iloc[23,1])>0) :       
                    if ((df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )and (df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ))and (df.iloc[21,1])and (df.iloc[22,1]):
                        df.iloc[10,j]=0
                        df.iloc[12,j]=0
                        df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                        
                            
                    elif  ((df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )or(df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] )and (df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] ))and (df.iloc[23,1])and (df.iloc[22,1]) :
                        df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[12,j]=0
                        df.iloc[11,j]=0
                    else :    
                        df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[11,j]=0
                        df.iloc[10,j]=0

        for j in range (1,ln):
                if df.iloc[1,j]>0:
                    l=[]
                    l=df.iloc[1,1:ln].to_list()
                    try:
                        while True:
                            l.remove(0)
                    except ValueError:
                        pass

                    x=len(l)

        y=[]
        y=df.iloc[2,1:ln].to_list()
        for item in df.iloc[2,1:ln]: 
            if item >0: 
                y.remove(item)

        abs(sum(y))
        df.iloc[18,1]=x*df.iloc[16,1]+abs(df.iloc[2,1:ln].sum())*df.iloc[17,1]
        df.iloc[25,1]=df.iloc[18,1]+df.iloc[10,1:ln].sum()*df.iloc[21,1]+df.iloc[11,1:ln].sum()*df.iloc[22,1]+df.iloc[12,1:ln].sum()*df.iloc[23,1]+abs(sum(y))*df.iloc[24,1]
        df.to_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSLFL.xlsx', index=False)

        file='C:/LotSizing/INPUTSAnnuel.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)

        l=[]
        l=df.iloc[0,1:13].to_list()
        x=len(l) 
        ln=x+1
        D=(df.iloc[0,1:ln].sum()/x)
        Cc=df.iloc[16,1]
        Cp=df.iloc[17,1]
        Q=round(sqrt((2*Cc*D)/Cp).real)
        df.iloc[27,1]=Q



        CS = [90000000000,90000000000]
        Cout = df.iloc[16,1]
        BNI = df.iloc[0,1]
        k = 1
        I =0
        LC = []
        LR= [1]

        for i in range (2,ln):
                if CS[-2] >= CS[-1] :
                    Cout = (Cout + df.iloc[17,1] * df.iloc[0,i] * (i-k))
                    BNI = BNI + df.iloc[0,i] 
                    CTM = Cout/(BNI)
                    CS.append(CTM)
                    L2 = list(CS)
                if CS[-1] >= CS[-2] :
                    L2.pop()
                    BNI = df.iloc[0,i]
                    Cout = df.iloc[16,1]
                    k = k + len(L2)-1
                    LC.append(L2)
                    I = I + len(L2) -1
                    LR.append(I+1)
                    del CS[2:]


        j = 0
        for z in LR:
            j = j + 1
            if z == LR[-1]:
                for kk in range (z,ln):
                    df.iloc[1,z] = df.iloc[1,z] + df.iloc[0,kk]
            else :
                for k in range(z,LR[j]):
                    df.iloc[1,z] = df.iloc[1,z] + df.iloc[0,k]
                continue


        df.iloc[2,1]= df.iloc[1,1] - df.iloc[0,1]
        for j in range (2,ln):
            df.iloc[2,j]=df.iloc[2,j-1]+df.iloc[1,j]-df.iloc[0,j]

        for j in range (1,ln):
            df.iloc[5,j]=df.iloc[1,j]
            df.iloc[7,j]=df.iloc[5,j]/df.iloc[6,j]  
            
            if df.iloc[7,j]>1 : 

                df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                if ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0):
                    df.iloc[10,j]=0
                    df.iloc[11,j]=0
                    df.iloc[12,j]=0   
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[11,j]=0
                 df.iloc[12,j]=0    
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[12,j]=0   
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=0
                 df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]  
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[12,j]=0
                      df.iloc[11,j]=0    
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]       
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[11,j]=0  
                    elif(df.iloc[10,1:ln].sum()*df.iloc[22,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]     
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[12,j]=0
                      df.iloc[11,j]= 0        
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[11,j]= 0                                                                                                                           
                elif ((df.iloc[21,1])>0 and (df.iloc[22,1])>0 and (df.iloc[23,1])>0) :       
                    if ((df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )and (df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ))and (df.iloc[21,1])and (df.iloc[22,1]):
                        df.iloc[10,j]=0
                        df.iloc[12,j]=0
                        df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                        
                            
                    elif  ((df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )or(df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] )and (df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] ))and (df.iloc[23,1])and (df.iloc[22,1]) :
                        df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[12,j]=0
                        df.iloc[11,j]=0
                    else :    
                        df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[11,j]=0
                        df.iloc[10,j]=0

        for j in range (1,ln):
                if df.iloc[1,j]>0:
                    l=[]
                    l=df.iloc[1,1:ln].to_list()
                    try:
                        while True:
                            l.remove(0)
                    except ValueError:
                        pass

                    x=len(l)

        y=[]
        y=df.iloc[2,1:ln].to_list()
        for item in df.iloc[2,1:ln]: 
            if item >0: 
                y.remove(item)

        abs(sum(y))
        df.iloc[18,1]=x*df.iloc[16,1]+abs(df.iloc[2,1:ln].sum())*df.iloc[17,1]
        df.iloc[25,1]=df.iloc[18,1]+df.iloc[10,1:ln].sum()*df.iloc[21,1]+df.iloc[11,1:ln].sum()*df.iloc[22,1]+df.iloc[12,1:ln].sum()*df.iloc[23,1]+abs(sum(y))*df.iloc[24,1]
        df.to_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSLUC.xlsx', index=False)

        file='C:/LotSizing/INPUTSAnnuel.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)

        l=[]
        l=df.iloc[0,1:13].to_list()
        x=len(l) 
        ln=x+1
        D=(df.iloc[0,1:ln].sum()/x)
        Cc=df.iloc[16,1]
        Cp=df.iloc[17,1]
        Q=round(sqrt((2*Cc*D)/Cp).real)
        df.iloc[27,1]=Q

        T=x
        demands=df.iloc[0,1:ln]
        CS=df.iloc[16,1]
        Cout=df.iloc[17,1]

        M=[[0 for i in range(T)]for j in range(T)]
        z=0
        OC=[0]*T
        M[0][0]=CS
        OC[0]=CS 
        S=[-1]*T    
        S[0]=0
        for i in range(1,T):
            mi=float("inf")
            ind=z   
            for j in range(z,i+1):  
                v=0  
                if j==0:
                    v+=CS
                else:
                    v=OC[j-1]+CS
                
                for k in range(j+1,i+1):
                    v+=demands[k]*(k-j)*Cout
                M[i][j]=v        
                if v<mi: 
                    ind=j
                    mi=v
            OC[i]=mi
            z=ind
            S[i]=z
        RES=[[0 for i in range(T)]for j in range(T)] 
        for i in range(T):
            for j in range(T):
                RES[i][j]=M[j][i]        


        Resption=[0]*T
        for i in range(T):
            Resption[S[i]]+=demands[i]
        for i in range(T):
            df.iloc[1,i+1]=Resption[i]

        
        df.iloc[2,1]= df.iloc[1,1] - df.iloc[0,1]
        for j in range (2,ln):
            df.iloc[2,j]=df.iloc[2,j-1]+df.iloc[1,j]-df.iloc[0,j]


        for j in range (1,ln):
            df.iloc[5,j]=df.iloc[1,j]
            df.iloc[7,j]=df.iloc[5,j]/df.iloc[6,j]  
            
            if df.iloc[7,j]>1 : 

                df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                if ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0):
                    df.iloc[10,j]=0
                    df.iloc[11,j]=0
                    df.iloc[12,j]=0   
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[11,j]=0
                 df.iloc[12,j]=0    
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[12,j]=0   
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=0
                 df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]  
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[12,j]=0
                      df.iloc[11,j]=0    
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]       
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[11,j]=0  
                    elif(df.iloc[10,1:ln].sum()*df.iloc[22,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]     
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[12,j]=0
                      df.iloc[11,j]= 0        
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[11,j]= 0                                                                                                                           
                elif ((df.iloc[21,1])>0 and (df.iloc[22,1])>0 and (df.iloc[23,1])>0) :       
                    if ((df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )and (df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ))and (df.iloc[21,1])and (df.iloc[22,1]):
                        df.iloc[10,j]=0
                        df.iloc[12,j]=0
                        df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                        
                            
                    elif  ((df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )or(df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] )and (df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] ))and (df.iloc[23,1])and (df.iloc[22,1]) :
                        df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[12,j]=0
                        df.iloc[11,j]=0
                    else :    
                        df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[11,j]=0
                        df.iloc[10,j]=0

        for j in range (1,ln):
                if df.iloc[1,j]>0:
                    l=[]
                    l=df.iloc[1,1:ln].to_list()
                    try:
                        while True:
                            l.remove(0)
                    except ValueError:
                        pass

                    x=len(l)

        y=[]
        y=df.iloc[2,1:ln].to_list()
        for item in df.iloc[2,1:ln]: 
            if item >0: 
                y.remove(item)

        abs(sum(y))
        df.iloc[18,1]=x*df.iloc[16,1]+abs(df.iloc[2,1:ln].sum())*df.iloc[17,1]
        df.iloc[25,1]=df.iloc[18,1]+df.iloc[10,1:ln].sum()*df.iloc[21,1]+df.iloc[11,1:ln].sum()*df.iloc[22,1]+df.iloc[12,1:ln].sum()*df.iloc[23,1]+abs(sum(y))*df.iloc[24,1]
        df.to_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSME.xlsx', index=False)        

        file='C:/LotSizing/INPUTSAnnuel.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)

        l=[]
        l=df.iloc[0,1:13].to_list()
        x=len(l) 
        ln=x+1
        D=(df.iloc[0,1:ln].sum()/x)
        Cc=df.iloc[16,1]
        Cp=df.iloc[17,1]
        Q=round(sqrt((2*Cc*D)/Cp).real)
        df.iloc[27,1]=Q



        CS = [0,0]
        Cout = 0
        k = 1
        for i in range (2,ln):
            if (CS[-1] - df.iloc[16,1] )< (df.iloc[16,1] - CS[-2]) and (df.iloc[16,1] < Cout):
                Cout = 0
                k = len(CS)

            elif CS[-1] - df.iloc[17,1] >= df.iloc[16,1] - CS[-2]:
                CS.pop()
                Cout = 0
                k = len(CS)
                CS.append(0)

            elif df.iloc[16,1] >= Cout :
                Cout = Cout + df.iloc[17,1] * df.iloc[0,i] * (i-k)
                CS.append(Cout)
        
        CS.remove(0)
        

        FS=[]
        for j in range(len(CS)):
            if CS[j]==0.0:
                FS.append(j+1)

        i = 0
        for j in FS:
            i = i + 1
            if j == FS[-1]:
                for kk in range (j,ln):
                    df.iloc[1,j] = df.iloc[1,j] + df.iloc[0,kk]
            else :
                for k in range(j,FS[i]):
                    df.iloc[1,j] = df.iloc[1,j] + df.iloc[0,k]
                continue 
            

        df.iloc[2,1]= df.iloc[1,1] - df.iloc[0,1]
        for j in range (2,ln):
            df.iloc[2,j]=df.iloc[2,j-1]+df.iloc[1,j]-df.iloc[0,j]
        for j in range (1,ln):
            df.iloc[5,j]=df.iloc[1,j]
            df.iloc[7,j]=df.iloc[5,j]/df.iloc[6,j]  
            
            if df.iloc[7,j]>1 : 

                df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                if ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0):
                    df.iloc[10,j]=0
                    df.iloc[11,j]=0
                    df.iloc[12,j]=0   
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[11,j]=0
                 df.iloc[12,j]=0    
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[12,j]=0   
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=0
                 df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]  
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[12,j]=0
                      df.iloc[11,j]=0    
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]       
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[11,j]=0  
                    elif(df.iloc[10,1:ln].sum()*df.iloc[22,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]     
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[12,j]=0
                      df.iloc[11,j]= 0        
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[11,j]= 0                                                                                                                           
                elif ((df.iloc[21,1])>0 and (df.iloc[22,1])>0 and (df.iloc[23,1])>0) :       
                    if ((df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )and (df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ))and (df.iloc[21,1])and (df.iloc[22,1]):
                        df.iloc[10,j]=0
                        df.iloc[12,j]=0
                        df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                        
                            
                    elif  ((df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )or(df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] )and (df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] ))and (df.iloc[23,1])and (df.iloc[22,1]) :
                        df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[12,j]=0
                        df.iloc[11,j]=0
                    else :    
                        df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[11,j]=0
                        df.iloc[10,j]=0

        for j in range (1,ln):
                if df.iloc[1,j]>0:
                    l=[]
                    l=df.iloc[1,1:ln].to_list()
                    try:
                        while True:
                            l.remove(0)
                    except ValueError:
                        pass

                    x=len(l)

        y=[]
        y=df.iloc[2,1:ln].to_list()
        for item in df.iloc[2,1:ln]: 
            if item >0: 
                y.remove(item)

        abs(sum(y))
        df.iloc[18,1]=x*df.iloc[16,1]+abs(df.iloc[2,1:ln].sum())*df.iloc[17,1]
        df.iloc[25,1]=df.iloc[18,1]+df.iloc[10,1:ln].sum()*df.iloc[21,1]+df.iloc[11,1:ln].sum()*df.iloc[22,1]+df.iloc[12,1:ln].sum()*df.iloc[23,1]+abs(sum(y))*df.iloc[24,1]
        df.to_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSPPB.xlsx', index=False)

        file='C:/LotSizing/INPUTSAnnuel.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)
        nbr_row=df.shape[0]#sheet1
        nbr_cel=len(df.iloc[0])
        l=[]
        l=df.iloc[0,1:13].to_list()
        x=len(l) 
        ln=x+1
        D=(df.iloc[0,1:ln].sum()/x)
        Cc=df.iloc[16,1]
        Cp=df.iloc[17,1]
        Q=round(sqrt((2*Cc*D)/Cp).real)
        df.iloc[27,1]=Q
        df.iloc[1,1]=df.iloc[27,1]
        df.iloc[2,1]=df.iloc[1,1]-df.iloc[0,1]

        for j in range (2,ln):
            for i in range (1):
                if df.iloc[0,j]>=df.iloc[2,j-1]:
                 df.iloc[1,j] = df.iloc[27,1]
                 df.iloc[2,j]=df.iloc[2,j-1]+df.iloc[1,j]-df.iloc[0,j] 

                else :
                    df.iloc[1,j]=0
                    df.iloc[2,j]=df.iloc[2,j-1]+df.iloc[1,j]-df.iloc[0,j]

        for j in range (1,ln):
            df.iloc[5,j]=df.iloc[1,j]
            df.iloc[7,j]=df.iloc[5,j]/df.iloc[6,j]  
            
            if df.iloc[7,j]>1 : 

                df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                if ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0):
                    df.iloc[10,j]=0
                    df.iloc[11,j]=0
                    df.iloc[12,j]=0   
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[11,j]=0
                 df.iloc[12,j]=0    
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[12,j]=0   
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=0
                 df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]  
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[12,j]=0
                      df.iloc[11,j]=0    
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]       
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[11,j]=0  
                    elif(df.iloc[10,1:ln].sum()*df.iloc[22,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]     
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[12,j]=0
                      df.iloc[11,j]= 0        
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[11,j]= 0                                                                                                                           
                elif ((df.iloc[21,1])>0 and (df.iloc[22,1])>0 and (df.iloc[23,1])>0) :       
                    if ((df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )and (df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ))and (df.iloc[21,1])and (df.iloc[22,1]):
                        df.iloc[10,j]=0
                        df.iloc[12,j]=0
                        df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                        
                            
                    elif  ((df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )or(df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] )and (df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] ))and (df.iloc[23,1])and (df.iloc[22,1]) :
                        df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[12,j]=0
                        df.iloc[11,j]=0
                    else :    
                        df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[11,j]=0
                        df.iloc[10,j]=0

        for j in range (1,ln):
                if df.iloc[1,j]>0:
                    l=[]
                    l=df.iloc[1,1:ln].to_list()
                    try:
                        while True:
                            l.remove(0)
                    except ValueError:
                        pass

                    x=len(l)

        y=[]
        y=df.iloc[2,1:ln].to_list()
        for item in df.iloc[2,1:ln]: 
            if item >0: 
                y.remove(item)

        abs(sum(y))
        df.iloc[18,1]=x*df.iloc[16,1]+abs(abs(df.iloc[2,1:ln].sum()))*df.iloc[17,1]
        df.iloc[25,1]=df.iloc[18,1]+df.iloc[10,1:ln].sum()*df.iloc[21,1]+df.iloc[11,1:ln].sum()*df.iloc[22,1]+df.iloc[12,1:ln].sum()*df.iloc[23,1]+abs(sum(y))*df.iloc[24,1]
        df.to_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSQEC.xlsx', index=False)

        file='C:/LotSizing/INPUTSAnnuel.xlsx'
        data=pd.read_excel(file)
        df=pd.DataFrame(data)

        l=[]
        l=df.iloc[0,1:13].to_list()
        x=len(l) 
        ln=x+1
        D=(df.iloc[0,1:ln].sum()/x)
        Cc=df.iloc[16,1]
        Cp=df.iloc[17,1]
        Q=round(sqrt((2*Cc*D)/Cp).real)
        df.iloc[27,1]=Q
        CS = []
        CS.append(df.iloc[16,1]) 
        CS.append(df.iloc[16,1])
        Cout = df.iloc[16,1]
        k = 1
        I =0
        LC = []
        LR= [1]

        for i in range (2,ln):
                if CS[-2] >= CS[-1] :
                    Cout = (Cout + df.iloc[17,1] * df.iloc[0,i] * (i-k))
                    CTM = Cout/(len(CS))
                    CS.append(CTM)
                    L2 = list(CS)
                if CS[-1] >= CS[-2] :
                    L2.pop()
                    Cout = df.iloc[16,1]
                    k = k + len(L2)-1
                    LC.append(L2)
                    I = I + len(L2) -1
                    LR.append(I+1)
                    del CS[2:]
        j = 0
        for z in LR:
            j = j + 1
            if z == LR[-1]:
                for kk in range (z,ln):
                    df.iloc[1,z] = df.iloc[1,z] + df.iloc[0,kk]
            else :
                for k in range(z,LR[j]):
                    df.iloc[1,z] = df.iloc[1,z] + df.iloc[0,k]
                continue
        df.iloc[2,1]= df.iloc[1,1] - df.iloc[0,1]
        for j in range (2,ln):
            df.iloc[2,j]=df.iloc[2,j-1]+df.iloc[1,j]-df.iloc[0,j]

        for j in range (1,ln):
            df.iloc[5,j]=df.iloc[1,j]
            df.iloc[7,j]=df.iloc[5,j]/df.iloc[6,j]  
            
            if df.iloc[7,j]>1 : 

                df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                if ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0):
                    df.iloc[10,j]=0
                    df.iloc[11,j]=0
                    df.iloc[12,j]=0   
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[11,j]=0
                 df.iloc[12,j]=0    
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                 df.iloc[12,j]=0   
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                 df.iloc[10,j]=0
                 df.iloc[11,j]=0
                 df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]  
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])==0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[12,j]=0
                      df.iloc[11,j]=0    
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]       
                elif ((df.iloc[21,1])==0 and (df.iloc[22,1])!=0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                      df.iloc[11,j]=0  
                    elif(df.iloc[10,1:ln].sum()*df.iloc[22,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=0
                      df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]     
                elif ((df.iloc[21,1])!=0 and (df.iloc[22,1])==0 and (df.iloc[23,1])!=0): 
                    if(df.iloc[10,1:ln].sum()*df.iloc[21,1])<(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[12,j]=0
                      df.iloc[11,j]= 0        
                    elif(df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[23,1] ):
                      df.iloc[10,j]=0
                      df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j] 
                      df.iloc[11,j]= 0                                                                                                                           
                elif ((df.iloc[21,1])>0 and (df.iloc[22,1])>0 and (df.iloc[23,1])>0) :       
                    if ((df.iloc[10,1:ln].sum()*df.iloc[21,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )and (df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] ))and (df.iloc[21,1])and (df.iloc[22,1]):
                        df.iloc[10,j]=0
                        df.iloc[12,j]=0
                        df.iloc[11,j]=df.iloc[1,j]-df.iloc[6,j]
                        
                            
                    elif  ((df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[22,1] )or(df.iloc[10,1:ln].sum()*df.iloc[23,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] )and (df.iloc[10,1:ln].sum()*df.iloc[22,1])>(df.iloc[10,1:ln].sum()*df.iloc[21,1] ))and (df.iloc[23,1])and (df.iloc[22,1]) :
                        df.iloc[10,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[12,j]=0
                        df.iloc[11,j]=0
                    else :    
                        df.iloc[12,j]=df.iloc[1,j]-df.iloc[6,j]
                        df.iloc[11,j]=0
                        df.iloc[10,j]=0

        for j in range (1,ln):
                if df.iloc[1,j]>0:
                    l=[]
                    l=df.iloc[1,1:ln].to_list()
                    try:
                        while True:
                            l.remove(0)
                    except ValueError:
                        pass

                    x=len(l)

        y=[]
        y=df.iloc[2,1:ln].to_list()
        for item in df.iloc[2,1:ln]: 
            if item >0: 
                y.remove(item)

        abs(sum(y))
        df.iloc[18,1]=x*df.iloc[16,1]+abs(df.iloc[2,1:ln].sum())*df.iloc[17,1]
        df.iloc[25,1]=df.iloc[18,1]+df.iloc[10,1:ln].sum()*df.iloc[21,1]+df.iloc[11,1:ln].sum()*df.iloc[22,1]+df.iloc[12,1:ln].sum()*df.iloc[23,1]+abs(sum(y))*df.iloc[24,1]
        df.to_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSSM.xlsx', index=False)        

        #Recherche optimum
        data=pd.read_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSLFL.xlsx')
        df=pd.DataFrame(data)

        dataLFL=pd.read_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSLFL.xlsx')
        dfLFL=pd.DataFrame(dataLFL)

        dataEPQ=pd.read_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSEPQ.xlsx')
        dfEPQ=pd.DataFrame(dataEPQ)

        dataLUC=pd.read_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSLUC.xlsx')
        dfLUC=pd.DataFrame(dataLUC)

        dataME=pd.read_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSME.xlsx')
        dfME=pd.DataFrame(dataME)

        dataPPB=pd.read_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSPPB.xlsx')
        dfPPB=pd.DataFrame(dataPPB)

        dataQEC=pd.read_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSQEC.xlsx')
        dfQEC=pd.DataFrame(dataQEC)

        dataSM=pd.read_excel('C:/LotSizing/OUTPUTSAnnuel/AnnuelOUTPUTSSM.xlsx')
        dfSM=pd.DataFrame(dataSM)

        X1=dfLFL.iloc[25,1]
        X2=dfEPQ.iloc[25,1]
        X3=dfLUC.iloc[25,1]
        X4=dfME.iloc[25,1]
        X5=dfPPB.iloc[25,1]
        X6=dfQEC.iloc[25,1]
        X7=dfSM.iloc[25,1]
        print(X1,X2,X3,X4,X5,X6,X7)


        Coût=[X1,X2,X3,X4,X5,X6,X7]
        index = ['Coût LFL ', 'Coût EPQ', 'Coût Luc','Coût PPB', 'Coût ME', 'Coût QEC', 'Coût SM']

        x = np.arange(len(index))  
        width = 0.35 

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, Coût, width)

        ax.set_xlabel('Heurestique')
        ax.set_title('Histogramme de Coût de production pour les différentes Heurestique')     
        ax.set_xticks(x, index)
        ax.legend()

        ax.bar_label(rects1, padding=3)

        fig.tight_layout()

        plt.show()  

    def setupUi(self, QECAnnuel):
        QECAnnuel.setObjectName("QECAnnuel")
        QECAnnuel.resize(1342, 597)
        self.tableWidget = QtWidgets.QTableWidget(QECAnnuel)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1341, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(QECAnnuel)
        self.widget.setGeometry(QtCore.QRect(0, 380, 111, 211))
        self.widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.Importer = QtWidgets.QPushButton(self.widget)
        self.Importer.setGeometry(QtCore.QRect(30, 10, 41, 51))
        self.Importer.setStyleSheet("border-image: url(:/pic/Arrow-download-3-icon.png);\n"
"border-radius:13px;")
        self.Importer.setText("")
        self.Importer.setObjectName("Importer")
        self.Save = QtWidgets.QPushButton(self.widget)
        self.Save.setGeometry(QtCore.QRect(30, 100, 41, 51))
        self.Save.setStyleSheet("border-image: url(:/pic/Button-Upload-icon.png);\n"
"border-radius:13px;")
        self.Save.setText("")
        self.Save.setObjectName("Save")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(30, 70, 41, 21))
        self.label_8.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(30, 160, 51, 21))
        self.label_9.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.widget = QtWidgets.QWidget(QECAnnuel)
        self.widget.setGeometry(QtCore.QRect(110, 380, 1231, 221))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.GrapheBtn = QtWidgets.QPushButton(self.widget)
        self.GrapheBtn.setGeometry(QtCore.QRect(60, 30, 371, 41))
        self.GrapheBtn.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 107), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.GrapheBtn.setObjectName("GrapheBtn")
        self.ComparaisonGraphique = QtWidgets.QPushButton(self.widget)
        self.ComparaisonGraphique.setGeometry(QtCore.QRect(580, 30, 371, 41))
        self.ComparaisonGraphique.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 107), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.ComparaisonGraphique.setObjectName("ComparaisonGraphique")
        self.ValiderModification = QtWidgets.QPushButton(self.widget)
        self.ValiderModification.setGeometry(QtCore.QRect(290, 120, 371, 41))
        self.ValiderModification.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 107), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.ValiderModification.setObjectName("ValiderModification")
        self.PrintG = QtWidgets.QPushButton(self.widget)
        self.PrintG.setGeometry(QtCore.QRect(10, 30, 41, 41))
        self.PrintG.setStyleSheet("\n"
"border-image: url(:/pic/Printer-icon.png);")
        self.PrintG.setText("")
        self.PrintG.setObjectName("PrintG")
        self.Printerrapport = QtWidgets.QPushButton(self.widget)
        self.Printerrapport.setGeometry(QtCore.QRect(230, 120, 41, 41))
        self.Printerrapport.setStyleSheet("\n"
"border-image: url(:/pic/Printer-icon.png);")
        self.Printerrapport.setText("")
        self.Printerrapport.setObjectName("Printerrapport")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(460, 30, 61, 41))
        self.label.setStyleSheet("border-image: url(:/pic/SEO-icon.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(980, 30, 61, 41))
        self.label_2.setStyleSheet("border-image: url(:/pic/SEO-icon.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(680, 120, 47, 41))
        self.label_4.setStyleSheet("border-image: url(:/pic/ok-icon.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(1050, 40, 171, 171))
        self.label_5.setStyleSheet("border-image: url(:/pic/logo.PNG);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.widget.raise_()
        self.widget.raise_()
        self.tableWidget.raise_()
        self.Importer.clicked.connect(self.loaddata)
        self.Save.clicked.connect(self.export)
        self.ValiderModification.clicked.connect(self.loadaQEC)
        self.GrapheBtn.clicked.connect(self.loadaGrapheQEC)
        self.ComparaisonGraphique.clicked.connect(self.comparaisonGraphe)
        self.Printerrapport.clicked.connect(self.imprimerapport)
        self.PrintG.clicked.connect(self.imprimegraphe)        
        self.retranslateUi(QECAnnuel)
        QtCore.QMetaObject.connectSlotsByName(QECAnnuel)
        

    def retranslateUi(self, QECAnnuel):
        _translate = QtCore.QCoreApplication.translate
        QECAnnuel.setWindowTitle(_translate("QECAnnuel", "QECAnnuel"))
        self.label_8.setText(_translate("QECAnnuel", "load"))
        self.label_9.setText(_translate("QECAnnuel", "Save"))

        self.GrapheBtn.setText(_translate("QECAnnuel", "Visualiser le graphiqe"))

        self.ComparaisonGraphique.setText(_translate("QECAnnuel", "Comparer les autres graphique"))

        self.ValiderModification.setText(_translate("QECAnnuel", "Valider Les modifications"))
import img



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QECAnnuel = QtWidgets.QWidget()
    ui = Ui_QECAnnuel()
    ui.setupUi(QECAnnuel)
    QECAnnuel.show()
    sys.exit(app.exec_())
