import sys
import time
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography_module import ceaser_cipher, symmetric_key, asymmetric_key

"""
Module Name: pyUi
Functions:   setupUi(object) - Used to declare & initialize GUI 
             retranslateUi(object) - Used to set values to components
             uiActionChecker() - Used to check user's actions on buttons
             actionEncrypt() - Used to call encryption operation
             actionDecrypt() - Used to call decryption operation  
             actionClear() - Used to clear user inputs
             actionExit() - Used to exit from application       
Classes: Ui_PyCrypt - Contains different functions to perform operation of PyCrypt Application     
Description: Graphical User Interface(GUI) of PyCrypt Application module
"""


class Ui_PyCrypt(object):
    def setupUi(self, PyCrypt):
        print("Initializing UI...")
        PyCrypt.setObjectName("PyCrypt")
        PyCrypt.setFixedSize(658, 582)
        self.centralwidget = QtWidgets.QWidget(PyCrypt)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 641, 520))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.description_text = QtWidgets.QLabel(self.frame)
        self.description_text.setGeometry(QtCore.QRect(10, 0, 611, 141))
        self.description_text.setTextFormat(QtCore.Qt.AutoText)
        self.description_text.setObjectName("description_text")

        self.encrypt_button = QtWidgets.QPushButton(self.frame)
        self.encrypt_button.setGeometry(QtCore.QRect(140, 300, 75, 23))
        self.encrypt_button.setObjectName("encrypt_button")

        self.decrypt_button = QtWidgets.QPushButton(self.frame)
        self.decrypt_button.setGeometry(QtCore.QRect(490, 300, 75, 23))
        self.decrypt_button.setObjectName("decrypt_button")

        self.message_input = QtWidgets.QPlainTextEdit(self.frame)
        self.message_input.setGeometry(QtCore.QRect(80, 250, 191, 31))
        self.message_input.setObjectName("message_input")

        self.enter_message_label = QtWidgets.QLabel(self.frame)
        self.enter_message_label.setGeometry(QtCore.QRect(0, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.enter_message_label.setFont(font)
        self.enter_message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_message_label.setObjectName("enter_message_label")

        self.cipher_text = QtWidgets.QPlainTextEdit(self.frame)
        self.cipher_text.setGeometry(QtCore.QRect(80, 340, 191, 31))
        self.cipher_text.setObjectName("cipher_text")

        self.cipher_text_label = QtWidgets.QLabel(self.frame)
        self.cipher_text_label.setGeometry(QtCore.QRect(0, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.cipher_text_label.setFont(font)
        self.cipher_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cipher_text_label.setWordWrap(True)
        self.cipher_text_label.setObjectName("cipher_text_label")

        self.enter_cipher_label = QtWidgets.QLabel(self.frame)
        self.enter_cipher_label.setGeometry(QtCore.QRect(340, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.enter_cipher_label.setFont(font)
        self.enter_cipher_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_cipher_label.setWordWrap(True)
        self.enter_cipher_label.setObjectName("enter_cipher_label")

        self.cipher_input = QtWidgets.QPlainTextEdit(self.frame)
        self.cipher_input.setGeometry(QtCore.QRect(430, 250, 191, 31))
        self.cipher_input.setObjectName("cipher_input")

        self.decrypted_text = QtWidgets.QPlainTextEdit(self.frame)
        self.decrypted_text.setGeometry(QtCore.QRect(430, 340, 191, 31))
        self.decrypted_text.setObjectName("decrypted_text")

        self.decrypted_text_label = QtWidgets.QLabel(self.frame)
        self.decrypted_text_label.setGeometry(QtCore.QRect(350, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.decrypted_text_label.setFont(font)
        self.decrypted_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.decrypted_text_label.setWordWrap(True)
        self.decrypted_text_label.setObjectName("decrypted_text_label")

        self.select_algo_comboBox = QtWidgets.QComboBox(self.frame)
        self.select_algo_comboBox.setGeometry(QtCore.QRect(320, 190, 201, 21))
        self.select_algo_comboBox.setObjectName("select_algo_comboBox")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_label = QtWidgets.QLabel(self.frame)
        self.select_algo_label.setGeometry(QtCore.QRect(50, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.select_algo_label.setFont(font)
        self.select_algo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.select_algo_label.setWordWrap(True)
        self.select_algo_label.setObjectName("select_algo_label")

        self.sender_name_label = QtWidgets.QLabel(self.frame)
        self.sender_name_label.setGeometry(QtCore.QRect(10, 150, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.sender_name_label.setFont(font)
        self.sender_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sender_name_label.setWordWrap(True)
        self.sender_name_label.setObjectName("sender_name_label")

        self.sender_name = QtWidgets.QPlainTextEdit(self.frame)
        self.sender_name.setGeometry(QtCore.QRect(100, 150, 151, 21))
        self.sender_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sender_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sender_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sender_name.setObjectName("sender_name")

        self.reciever_name_label = QtWidgets.QLabel(self.frame)
        self.reciever_name_label.setGeometry(QtCore.QRect(330, 150, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.reciever_name_label.setFont(font)
        self.reciever_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.reciever_name_label.setWordWrap(True)
        self.reciever_name_label.setObjectName("reciever_name_label")

        self.reciever_name = QtWidgets.QPlainTextEdit(self.frame)
        self.reciever_name.setGeometry(QtCore.QRect(430, 150, 151, 21))
        self.reciever_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.reciever_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.reciever_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.reciever_name.setObjectName("reciever_name")

        self.encryptor_grp = QtWidgets.QGroupBox(self.frame)
        self.encryptor_grp.setGeometry(QtCore.QRect(0, 220, 301, 161))
        self.encryptor_grp.setObjectName("encryptor_grp")

        self.decryptor_grp = QtWidgets.QGroupBox(self.frame)
        self.decryptor_grp.setGeometry(QtCore.QRect(340, 220, 301, 161))
        self.decryptor_grp.setObjectName("decryptor_grp")

        self.key_grp = QtWidgets.QGroupBox(self.frame)
        self.key_grp.setGeometry(QtCore.QRect(0, 389, 641, 85))
        self.key_grp.setObjectName("key_grp")

        self.public_key_label = QtWidgets.QLabel(self.key_grp)
        self.public_key_label.setGeometry(QtCore.QRect(10, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.public_key_label.setFont(font)
        self.public_key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.public_key_label.setObjectName("public_key_label")

        self.private_key_label = QtWidgets.QLabel(self.key_grp)
        self.private_key_label.setGeometry(QtCore.QRect(10, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.private_key_label.setFont(font)
        self.private_key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.private_key_label.setObjectName("private_key_label")

        self.public_key = QtWidgets.QLabel(self.key_grp)
        self.public_key.setGeometry(QtCore.QRect(100, 20, 500, 51))
        self.public_key.setWordWrap(True)
        self.public_key.setStyleSheet("padding:5px")
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.public_key.setFont(font)
        self.public_key.setAlignment(QtCore.Qt.AlignLeft)
        self.public_key.setObjectName("public_key")

        self.hidden_label = QtWidgets.QLabel(self.key_grp)
        self.hidden_label.setGeometry(QtCore.QRect(100, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(10)
        self.hidden_label.setFont(font)
        self.hidden_label.setAlignment(QtCore.Qt.AlignLeft)
        self.hidden_label.setObjectName("hidden_label")

        self.progress_bar = QtWidgets.QProgressBar(self.frame)
        self.progress_bar.setGeometry(QtCore.QRect(30, 495, 421, 21))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")

        self.clear_button = QtWidgets.QPushButton(self.frame)
        self.clear_button.setGeometry(QtCore.QRect(460, 495, 75, 23))
        self.clear_button.setObjectName("clear_button")

        self.exit_button = QtWidgets.QPushButton(self.frame)
        self.exit_button.setGeometry(QtCore.QRect(550, 495, 75, 23))
        self.exit_button.setObjectName("exit_button")

        self.encryptor_grp.raise_()
        self.decryptor_grp.raise_()
        self.description_text.raise_()
        self.encrypt_button.raise_()
        self.decrypt_button.raise_()
        self.message_input.raise_()
        self.enter_message_label.raise_()
        self.cipher_text.raise_()
        self.cipher_text_label.raise_()
        self.enter_cipher_label.raise_()
        self.cipher_input.raise_()
        self.decrypted_text.raise_()
        self.decrypted_text_label.raise_()
        self.select_algo_comboBox.raise_()
        self.select_algo_label.raise_()
        self.sender_name_label.raise_()
        self.sender_name.raise_()
        self.reciever_name_label.raise_()
        self.reciever_name.raise_()
        self.key_grp.raise_()
        self.progress_bar.raise_()
        self.clear_button.raise_()
        self.exit_button.raise_()
        self.pycrypt_label = QtWidgets.QLabel(self.centralwidget)
        self.pycrypt_label.setGeometry(QtCore.QRect(230, 0, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pycrypt_label.setFont(font)
        self.pycrypt_label.setTextFormat(QtCore.Qt.AutoText)
        self.pycrypt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pycrypt_label.setObjectName("pycrypt_label")

        PyCrypt.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PyCrypt)
        self.statusbar.setObjectName("statusbar")
        PyCrypt.setStatusBar(self.statusbar)
        print("UI Initialization Done...")
        print("Retranslating UI...")
        self.retranslateUi(PyCrypt)
        print("Almost Done...")
        QtCore.QMetaObject.connectSlotsByName(PyCrypt)
        print("Done...")
        print("\nAction Listener Running...")
        self.UiActionChecker()

    def retranslateUi(self, PyCrypt):
        _translate = QtCore.QCoreApplication.translate
        PyCrypt.setWindowTitle(_translate("PyCrypt", "PyCrypt Application"))
        self.description_text.setText(_translate("PyCrypt", "<html><head/><body><p><span style=\" font-size:12pt; "
                                                            "font-weight:600;\">Description:</span></p><p><span "
                                                            "style=\" font-family:\'Arial\'; font-size:10pt; "
                                                            "font-weight:600; color:#000000;\">PyCrypt</span><span "
                                                            "style=\" font-family:\'Arial\'; font-size:10pt; "
                                                            "color:#000000;\"> is an cryptography application which "
                                                            "will use python as the core programming "
                                                            "language.</span></p><p><span style=\" "
                                                            "font-family:\'Arial\'; font-size:10pt; "
                                                            "color:#000000;\">It is used to converts your plain text "
                                                            "into a secure encrypted message</span></p><p><span "
                                                            "style=\" font-family:\'Arial\'; font-size:10pt; "
                                                            "color:#000000;\">Uses encryption  technique "
                                                            "like</span><span style=\" font-family:\'Arial\'; "
                                                            "font-size:10pt; font-weight:600; color:#000000;\"> "
                                                            "Caesar Cipher, Fernet Symmetric Key, Asymmetric Key "
                                                            "encryption </span></p><p><span style=\" "
                                                            "font-family:\'Arial\'; font-size:10pt; "
                                                            "color:#000000;\">technique</span></p><p><br/></p></body"
                                                            "></html>"))
        self.encrypt_button.setText(_translate("PyCrypt", "Encrypt"))
        self.decrypt_button.setText(_translate("PyCrypt", "Decrypt"))
        self.enter_message_label.setText(_translate("PyCrypt", "Enter Text "))
        self.cipher_text_label.setText(_translate("PyCrypt", "<html><head/><body><p>   Cipher Text</p></body></html>"))
        self.enter_cipher_label.setText(_translate("PyCrypt", "<html><head/><body><p>Enter Cipher "
                                                              "Text</p><p><br/></p></body></html>"))
        self.decrypted_text_label.setText(_translate("PyCrypt", "<html><head/><body><p>Decrypted "
                                                                "Result</p><p><br/></p></body></html>"))
        algorithm_list = ["Ceaser Cipher", "Symmetric Key", "Asymmetric Key"]
        i = 0
        for algo_name in algorithm_list:
            self.select_algo_comboBox.setItemText(i, _translate("PyCrypt", algo_name))
            i = i + 1
        self.select_algo_label.setText(_translate("PyCrypt", "Select type of algorithm you want to use?"))
        self.sender_name_label.setText(_translate("PyCrypt", "Sender Name"))
        self.reciever_name_label.setText(_translate("PyCrypt", "Reciever Name"))
        self.encryptor_grp.setTitle(_translate("PyCrypt", "Encryptor"))
        self.decryptor_grp.setTitle(_translate("PyCrypt", "Decryptor"))
        self.key_grp.setTitle(_translate("PyCrypt", "Keys"))
        self.private_key_label.setText(_translate("PyCrypt", "Private Key :"))
        self.public_key_label.setText(_translate("PyCrypt", "Public Key : "))
        self.public_key.setText(_translate("PyCrypt", ""))
        self.hidden_label.setText(_translate("PyCrypt", "Hidden"))
        self.clear_button.setText(_translate("PyCrypt", "Clear"))
        self.exit_button.setText(_translate("PyCrypt", "Exit"))
        self.pycrypt_label.setText(_translate("PyCrypt", "PyCrypt"))

    def UiActionChecker(self):
        self.encrypt_button.clicked.connect(self.actionEncrypt)
        self.decrypt_button.clicked.connect(self.actionDecrypt)
        self.clear_button.clicked.connect(self.actionClear)
        self.exit_button.clicked.connect(self.actionExit)

    def actionEncrypt(self):
        print("Encrypt Pressed")
        plain_message = self.message_input.toPlainText()
        plain_message = plain_message.strip()
        if len(plain_message) == 0:
            print("Nothing...")
        else:
            if self.select_algo_comboBox.currentIndex() == 0:
                cipher_seq = ceaser_cipher(plain_message, "encrypt")
                self.progress_bar.setValue(0)
                self.progressBar()
                self.decrypted_text.clear()
                self.cipher_input.clear()
                self.cipher_text.setPlainText(cipher_seq[0])
                self.public_key.setText(str(cipher_seq[1]))
            elif self.select_algo_comboBox.currentIndex() == 1:
                global symmetric
                symmetric = symmetric_key()
                symmetric.generate_key()
                cipher_seq = symmetric.encrypt(plain_message)
                self.progress_bar.setValue(0)
                self.progressBar()
                self.decrypted_text.clear()
                self.cipher_input.clear()
                self.cipher_text.setPlainText(cipher_seq[0])
                self.public_key.setText(str(cipher_seq[1]))
            elif self.select_algo_comboBox.currentIndex() == 2:
                global asymmetric
                asymmetric = asymmetric_key()
                asymmetric.generate_key()
                cipher_seq = asymmetric.encrypt(plain_message)
                self.progress_bar.setValue(0)
                self.progressBar()
                self.decrypted_text.clear()
                self.cipher_input.clear()
                self.cipher_text.setPlainText(cipher_seq[0])
                self.public_key.setText(str(cipher_seq[1]))
                self.public_key.setWordWrap(True)
            else:
                print("Exception Occurred...")
                self.showExceptionDialog()

    def actionDecrypt(self):
        print("Decrypt Pressed")
        cipher_message = self.cipher_input.toPlainText()
        cipher_message = cipher_message.strip()
        if len(cipher_message) == 0:
            print("Nothing")
        else:
            if self.select_algo_comboBox.currentIndex() == 0:
                decrpyted_txt = ceaser_cipher(cipher_message, "decrypt")
                self.progress_bar.setValue(0)
                self.progressBar()
                self.decrypted_text.setPlainText(decrpyted_txt[0])
                self.public_key.setText(str(decrpyted_txt[1]))
            elif self.select_algo_comboBox.currentIndex() == 1:
                global symmetric
                try:
                    decrypted_txt = symmetric.decrypt(cipher_message)
                    self.progress_bar.setValue(0)
                    self.progressBar()
                    self.decrypted_text.setPlainText(decrypted_txt[0])
                    self.public_key.setText(str(decrypted_txt[1]))
                except Exception as exp:
                    self.progress_bar.setValue(0)
                    self.progressBar()
                    print(exp)
                    print("Exception Occurred")
                    self.decrypted_text.setPlainText("Exception Occurred!!")
                    self.public_key.setText("Failed!!")
            elif self.select_algo_comboBox.currentIndex() == 2:
                global asymmetric
                try:
                    if self.cipher_text.toPlainText() == cipher_message:
                        decrypted_txt = asymmetric.decrypt()
                        self.progress_bar.setValue(0)
                        self.progressBar()
                        self.decrypted_text.setPlainText(decrypted_txt[0])
                        self.public_key.setText(str(decrypted_txt[1]))
                    else:
                        raise Exception("Invalid Cipher message")
                except Exception as exp:
                    self.progress_bar.setValue(0)
                    self.progressBar()
                    print(exp)
                    print("Exception Occurred")
                    self.decrypted_text.setPlainText("Exception Occurred!!")
                    self.public_key.setText("Failed!!")
            else:
                print("Exception Occurred...")
                self.showExceptionDialog()

    def actionClear(self):
        print("Clear Pressed")
        self.message_input.clear()
        self.cipher_input.clear()
        self.sender_name.clear()
        self.reciever_name.clear()
        self.cipher_text.clear()
        self.decrypted_text.clear()
        self.public_key.setText("")
        self.progress_bar.setValue(0)
        self.select_algo_comboBox.setCurrentIndex(0)

    def actionExit(self):
        print("Exit Pressed")
        sys.exit(app.exec_())
        print("Exiting...")

    def showExceptionDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.setFixedSize(300, 100)
        exceptDesc = QtWidgets.QLabel("Exit", dialog)
        exceptDesc.move(10, 20)
        exitButton = QtWidgets.QPushButton("OK", dialog)
        exitButton.move(100, 70)
        dialog.setWindowTitle("PyCrypt (Not Responding)")
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)

    def exitFunc(self):
        sys.exit(app.exec_())

    def progressBar(self):
        completed = 0
        while completed < 100:
            completed += random.randint(1, 30)
            time.sleep(random.randint(1, 15) * 0.05)
            self.progress_bar.setValue(completed)
        self.progress_bar.setValue(100)

app = QtWidgets.QApplication(sys.argv)
PyCrypt = QtWidgets.QMainWindow()
ui = Ui_PyCrypt()
symmetric = None
asymmetric = None
asymmetric_cipher = None
print("PyCrypt Application Running...")
ui.setupUi(PyCrypt)
PyCrypt.show()
sys.exit(app.exec_())
