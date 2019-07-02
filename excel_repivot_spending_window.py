
# coding: utf-8

# In[1]:


import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QPushButton,QMessageBox,QMainWindow,
                             QTextEdit,QAction,QFileDialog,QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QCoreApplication,QRect
import excel_repivot_spending

# In[2]:


class Excel_Pandas_Tools(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100,100,600,400)
        self.setWindowTitle("Excel Pandas Tools")
        self.show()
        
        sbtn = QPushButton('selete a file',self)# 创建按钮组件并为其设置选择文件提示框  
        sbtn.setObjectName('sbtn')
        sbtn.clicked.connect(self.select_file)
        
        self.textEdit = QTextEdit(self)
        
        rbtn = QPushButton('run the procedure',self)# 创建按钮组件并为其设置运行程序提示框
        rbtn.setObjectName('rbtn')
        rbtn.clicked.connect(lambda:excel_repivot_spending.main(self.filename))
#         rbtn.setGeometry(QRect(100, self.geometryTop, 60, 20))

#         qbtn = QPushButton('Quit', self)# 创建按钮组件并为其设置关闭提示框
   
        hbox = QHBoxLayout()
        hbox.addStretch(1) # 在两个按钮间增加一个弹性空间
        hbox.addWidget(sbtn)
        hbox.addWidget(self.textEdit)
        hbox.addWidget(rbtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox) 

        
    def select_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')
        filename = fname[0]
        if filename:
            self.textEdit.setText(filename)
            self.filename = filename
        print(self.textEdit)
        print(type(self.textEdit))
#         print(self.textEdit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Excel_Pandas_Tools()
    sys.exit(app.exec_())

