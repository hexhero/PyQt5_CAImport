import sys

from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import *
from frame import frame
from yangb import yangb

yb = yangb()

username = None
filepath = None

class Worker(QtCore.QThread):
    _signal = pyqtSignal(list)
    _signal2 = pyqtSignal(bool)

    def __init__(self,parent=None):
        super(Worker, self).__init__(parent)
    
    def __del__(self):
        self.wait()

    def run(self):
        self._signal2.emit(False)
        yb.trans(username,filepath,func=self.callback)

    def callback(self,row,success = False):
        if success:
            self._signal2.emit(True)
        else:
            self._signal.emit(row)

class main(frame):
    
    def __init__(self,widget):
        self.widget = widget
        self.setupUi(widget)
        self.initUI()

    def initUI(self):
        for name in yangb.did.keys():
            self.comboBox.addItem(name)
        
        self.pushButton_2.clicked.connect(self.choseFile)
        self.pushButton.clicked.connect(self.upload)
        pass
    
    def choseFile(self):
        filename,filetype = QtWidgets.QFileDialog.getOpenFileName(self.widget,
                                    "选取文件",
                                    ".",
                                    "csv Files (*.csv)")
        self.lineEdit.setText(filename)
        pass

    def upload(self):
        global username
        global filepath
        username = self.comboBox.currentText()
        filepath = self.lineEdit.text()
        print(username, filepath)

        self.thread = Worker()
        self.thread._signal.connect(self.running)
        self.thread._signal2.connect(self.runstate)
        self.thread.start()

    a = 0
    def running(self,msg):
        main.a += 1
        self.lcdNumber.display(main.a)
        self.textEdit.append(msg[1] + msg[2])

    def runstate(self,flag):
        if flag == True:
            self.stop()
        else:
            self.start()

    def start(self):
        self.pushButton.setEnabled(False)
        self.pushButton.setText("正在导入...")
        self.textEdit.append("开始导入>>>>>>>>>>>>>>>>>>>")
        self.label_3.setText("正在导入...")
        pass
    
    def stop(self):
        self.pushButton.setEnabled(True)
        self.pushButton.setText("开始导入")
        self.textEdit.append(">>>>>>>>>>>>>>>>>>>导入完成")
        self.label_3.setText("导入完成")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    m = main(widget)
    widget.show()
    sys.exit(app.exec_())
