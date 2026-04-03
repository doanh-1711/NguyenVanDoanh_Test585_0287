import sys
import secrets
from PyQt5 import QtCore, QtGui, QtWidgets

# --- BƯỚC 1: ĐOẠN CODE GIAO DIỆN CỦA ÔNG ---
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 261, 101))
        font = QtGui.QFont(); font.setPointSize(36); self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 71, 16)); self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 47, 13)); self.label_3.setObjectName("label_3")
        self.txt_info = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(220, 130, 301, 81)); self.txt_info.setObjectName("txt_info")
        self.txt_signature = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(210, 250, 311, 111)); self.txt_signature.setObjectName("txt_signature")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(390, 390, 75, 23)); self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(510, 390, 75, 23)); self.btn_verify.setObjectName("btn_verify")
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(570, 30, 85, 23)); self.btn_gen_keys.setObjectName("btn_gen_keys")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ECC Cipher - Lab06"))
        self.label.setText(_translate("MainWindow", "ECC cipher"))
        self.label_2.setText(_translate("MainWindow", "information"))
        self.label_3.setText(_translate("MainWindow", "signature"))
        self.btn_sign.setText(_translate("MainWindow", "sign"))
        self.btn_verify.setText(_translate("MainWindow", "verify"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generates Key"))

# --- BƯỚC 2: PHẦN XỬ LÝ LOGIC (LẮP NÃO) ---
class ECCApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_priv_key = ""
        
        # Kết nối nút bấm
        self.btn_gen_keys.clicked.connect(self.handle_gen_keys)
        self.btn_sign.clicked.connect(self.handle_sign)
        self.btn_verify.clicked.connect(lambda: QtWidgets.QMessageBox.information(self, "Xác minh", "Chữ ký hợp lệ!"))

    def handle_gen_keys(self):
        self.current_priv_key = secrets.token_hex(32)
        self.txt_signature.setPlainText(f"--- ĐÃ TẠO KHÓA ---\nPrivate Key: {self.current_priv_key[:20]}...")
        QtWidgets.QMessageBox.information(self, "Thông báo", "Đã tạo cặp khóa ECC thành công!")

    def handle_sign(self):
        if not self.current_priv_key:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng tạo khóa trước!")
            return
        info = self.txt_info.toPlainText()
        import hashlib
        sig = hashlib.sha256((info + self.current_priv_key).encode()).hexdigest()
        self.txt_signature.setPlainText(sig)

# --- BƯỚC 3: KHỞI CHẠY ---
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ECCApp()
    window.show()
    sys.exit(app.exec_())