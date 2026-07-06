import tensorflow as tf
from tf_keras.models import load_model
# System Compoents
import sys
import os
import threading
import time
import asyncio
from datetime import datetime

# Database & Sercurity Components
import mysql.connector
import bcrypt

# Vision Components
import cv2
# import cv2.xfeatures2d

# Process Components

import numpy as np
# PyQT Components
import PyQt5
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, pyqtSlot
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtGui import QTextCursor  # Import QTextCursor từ PyQt5.QtGui

# AI LLM Processing
from ai_process import process_input  # Import mô-đun hỗ trợ

# Global Variables 
classifier = load_model('models/ASLModel.h5')  # loading the model
currentMode = 'A'
recognizedResult = 'Z'
count = 0
# recognizedString = ""

def fileSearch():
    fileEntry = []
    for file in os.listdir("SampleGestures"):
        if file.endswith(".png"):
            fileEntry.append(file)
    return fileEntry
'''
predicator using Keras
Không nên có phụ thuộc PyQt.
'''

def predictor():
    import numpy as np
    from tf_keras.preprocessing import image
    test_image = image.load_img('1.png', target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    # detected_text = ''
    gesname = ''
    fileEntry = fileSearch()
    # đọc bảng``
    for i in range(len(fileEntry)):
        image_to_compare = cv2.imread("./SampleGestures/" + fileEntry[i])
        original = cv2.imread("1.png")
        sift = cv2.SIFT_create()
        kp_1, desc_1 = sift.detectAndCompute(original, None)
        kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(desc_1, desc_2, k=2)

        good_points = []
        ratio = 0.7
        for m, n in matches:
            if m.distance < ratio * n.distance:
                good_points.append(m)
        if (abs(len(good_points) + len(
                matches)) > 20):
            gesname = fileEntry[i]
            gesname = gesname.replace('.png', '')
            if (gesname == 'sp'):
                gesname = ' '
            # print("Đã hoàn thành chữ : ", gesname)
            return gesname

    if result[0][0] == 1:
        return 'A'
    elif result[0][1] == 1:
        return 'B'
    elif result[0][2] == 1:
        return 'C'
    elif result[0][3] == 1:
        return 'D'
    elif result[0][4] == 1:
        return 'E'
    elif result[0][5] == 1:
        return 'F'
    elif result[0][6] == 1:
        return 'G'
    elif result[0][7] == 1:
        return 'H'
    elif result[0][8] == 1:
        return 'I'
    elif result[0][9] == 1:
        return 'J'
    elif result[0][10] == 1:
        return 'K'
    elif result[0][11] == 1:
        return 'L'
    elif result[0][12] == 1:
        return 'M'
    elif result[0][13] == 1:
        return 'N'
    elif result[0][14] == 1:
        return 'O'
    elif result[0][15] == 1:
        return 'P'
    elif result[0][16] == 1:
        return 'Q'
    elif result[0][17] == 1:
        return 'R'
    elif result[0][18] == 1:
        return 'S'
    elif result[0][19] == 1:
        return 'T'
    elif result[0][20] == 1:
        return 'U'
    elif result[0][21] == 1:
        return 'V'
    elif result[0][22] == 1:
        return 'W'
    elif result[0][23] == 1:
        return 'X'
    elif result[0][24] == 1:
        
        return 'Y'
    elif result[0][25] == 1:
        
        return 'Z'


class MainAppWindow(QMainWindow):
    def __init__(self):
        super(MainAppWindow, self).__init__()
        uic.loadUi('pyqt_UI/last_ui_rabbit.ui', self)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53)) 
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)
        self.setWindowTitle('Rabbit AI - NaVin AIF')
        self.setWindowIcon(QIcon('resource/UI/logo_com.png'))
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        """ Cho biết chế độ hiện tại (tất cả logic được xử lý bằng biến này, ví dụ: mode = A -> Hiển thị ảnh hướng dẫn 'A' """
        """ OnFirstRun """
        self.notifyModeChanged(currentMode)
        self.setTutorialButton()
        self.heightOfCamView = self.label_camView.height()
        self.widthOfCamView = self.label_camView.width()
        self.roiLeftTop = (530, 100)
        self.roiRightBottom = (750, 300)
        self.video_thread(MainAppWindow)
        self.playProgress()
        self.label_doneTutorial.hide()
        self.label_3.setPixmap(QPixmap("resource/UI/logo_com.png").scaled(41, 41))
        # Đặt ảnh vào QPushButton
        self.pushButton.setIcon(QIcon("pyqt_UI/OIP.jpeg"))
        # Nếu muốn điều chỉnh kích thước của biểu tượng trên nút:
        self.pushButton.setIconSize(QtCore.QSize(41, 41))  # Kích thước biểu tượng 100x100
        self.is_running = True
        self.pushButton_2.clicked.connect(self.logout)
        
        self.recognizedString = ""  # Thuộc tính của đối tượng
        # Kích hoạt tính năng tự động xuống dòng
        self.textEdit.setLineWrapMode(True)  # Tự động xuống dòng theo chiều rộng widget
        self.textEdit.moveCursor(QTextCursor.Start)
        # self.setup_text_edit()
        # self.label_recognizedText_4 = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        # main_layout.addWidget(self.label_recognizedText_4)
        self.textEdit.textChanged.connect(self.update_recognized_string)
        # Button Edit
        self.pushButton_7.clicked.connect(self.edit_string)
        # Button Delete
        self.pushButton_6.clicked.connect(self.delete_string)
        # Button Send
        self.pushButton_5.clicked.connect(self.send_string)
        
        
        # AI LLM Processing Gểnate
        self.pushButton_3.clicked.connect(self.call_ai)
    
        self.history = []
        
    def setup_text_edit(self):
        # Kích hoạt tự động xuống dòng
        self.textEdit.setLineWrapMode(True)
        self.textEdit.setFixedWidth(250)  # Điều chỉnh chiều rộng nếu cần
        font = QFont("Arial", 11)
        self.textEdit.setFont(font)

    def logout(self):
        # Kiểm tra và giải phóng camera nếu nó đang mở
        if self.cap.isOpened():
            self.cap.release()
            cv2.destroyAllWindows()
        # Đóng giao diện chính
        self.close()
        # Quay trở về giao diện đăng nhập
        self.login_window = MainWindow()
        self.login_window.show()

    def playProgress(self):
        # Chơi ngay sau khi mở chế độ xem
        self.progressBarThread = ProgressThread()
        # Cài đặt sự kiện
        self.progressBarThread.countChanged.connect(self.onCountChanged)
        self.progressBarThread.start()

    # recognizedString = ""
    # Được gọi bất cứ khi nào giá trị đếm thay đổi.
    def onCountChanged(self, value):
        self.progressBar.setValue(value)
        # global recognizedString  # Tham chiếu đến biến toàn cục
        if value == 100:
            print("Đã hoàn thành quá trình nhận diện chữ:", recognizedResult) # Kết quảsau khi đã hoàn thành chữ cái đó
            # Lưu ký tự nhận diện vào chuỗi
            self.recognizedString += recognizedResult
            # In ra chuỗi hiện tại đã nhận diện
            print("Chuỗi ký tự hiện tại:", self.recognizedString)
            # self.label_recognizedText_4.setText(recognizedString)
            self.textEdit.setText(self.recognizedString)
            # self.lineEdit.setText(recognizedString)
            self.showDoneTutorial()
        # return recognizedString

    def update_recognized_string(self):
        """Cập nhật biến recognizedString khi người dùng thay đổi văn bản trong textEdit."""
        self.recognizedString = self.textEdit.toPlainText()  # Cập nhật recognizedString từ nội dung trong textEdit
        print("Cập nhật recognizedString:", self.recognizedString)

    def edit_string(self):
        """Chỉnh sửa chuỗi ký tự nhận diện."""
        print("Hãy chỉnh sửa văn bản!")
        # Cho phép chỉnh sửa văn bản trong textEdit
        self.textEdit.setReadOnly(False)  # Cho phép chỉnh sửa
        self.textEdit.setText(self.recognizedString)  # Đặt nội dung hiện tại vào textEdit
        print("Chỉnh sửa chuỗi ký tự:", self.recognizedString)
        
    def delete_string(self):
        """Xóa chuỗi ký tự nhận diện."""
        self.recognizedString = ''  # Xóa chuỗi
        self.textEdit.setText(self.recognizedString)  # Cập nhật giao diện
        print("Đã xóa chuỗi ký tự nhận diện")
        
    def send_string(self):
        """Gửi chuỗi nhận diện."""
        # global recognizedString  # Tham chiếu đến biến toàn cục
        print("Đã gửi chuỗi ký tự:", self.recognizedString)
        chat_history = f"Data Receive:\n{self.recognizedString}"
        # self.label_recognizedText_2.setText(f"Kết quả từ AI:\n{response}")
        self.label_recognizedText_2.setText(f"{chat_history}")
        # self.label_recognizedText_2.setText(self.recognizedString)
        # Thực hiện các hành động gửi chuỗi (ví dụ, gọi API hoặc lưu trữ)
        
    def call_ai(self):
        """Gọi mô-đun AI và xử lý kết quả."""
        input_text = self.textEdit.toPlainText()
        if not input_text.strip():
            self.label_recognizedText_2.setText("Vui lòng nhập dữ liệu trước khi gọi AI.")
            return
        # Xử lý bất đồng bộ với asyncio
        asyncio.run(self.process_with_ai(input_text))

    async def process_with_ai(self, input_text):
        """Gửi chuỗi tới AI và cập nhật giao diện với kết quả."""
        self.label_recognizedText_2.setText("Đang xử lý...")
        response = await process_input(input_text)
        # Lấy thời gian trả lời
        current_time = datetime.now().strftime("%H:%M:%S, %d-%m-%Y")

        # Lưu lại câu hỏi và câu trả lời vào lịch sử
        self.history.append((input_text, response, current_time))
        # Tạo chuỗi để hiển thị toàn bộ lịch sử trò chuyện
        chat_history = ""
        for i, (question, answer, time) in enumerate(self.history):
            # Thêm thẻ HTML vào câu hỏi và câu trả lời
            chat_history += f"<b>Time Response: {time}</b><br>"  # In đậm phần thời gian
            chat_history += f"<font size='4'>Recognized Result {i + 1}: {question}</font><br>"  # Thay đổi cỡ chữ cho câu hỏi
            chat_history += f"<i>Aero Response {i + 1}: {answer}</i><br><br>"  # In nghiêng phần câu trả lời


        # self.label_recognizedText_2.setText(f"Kết quả từ AI:\n{response}")
        # self.label_recognizedText_2.setText(f"{chat_history}")
        # Đảm bảo text được hiển thị dưới dạng HTML
        self.label_recognizedText_2.setText(chat_history)

    # Hàm show kết quả thành công hướng dẫn 
    def showDoneTutorial(self):
        # tạo nhanx show label huớng dẫn show
        self.label_doneTutorial.show()
        # hàm khởi tại chiều cao của label
        height = self.label_doneTutorial.height()
        # hàm khởi tạo chiều ngang của label
        width = self.label_doneTutorial.width()
        # hiển thị hình ảnh label sau khi đã thực hiện detect thành công 
        pixmap = QPixmap("./resource/UI/aftertutorial.png")
        # hàm tạo cơ chế chiều cao, ngang, chuyển đổi smooth,
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_doneTutorial.setPixmap(pixmap)

    def hideDoneTutorial(self):
        self.label_doneTutorial.hide()

    # TODO: Tôi không muốn các nút được liệt kê trông xấu nên tôi cần tối ưu hóa chúng (kế thừa và biến nó thành một lớp ??)
    @pyqtSlot()
    def setTutorialButton(self):
        self.button_A.setIcon(QtGui.QIcon("./resource/alphabet/button/A.png"))
        self.button_A.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(self.alphabetButtonClicked)

        self.button_B.setIcon(QtGui.QIcon("./resource/alphabet/button/B.png"))
        self.button_B.setIconSize(QSize(30, 30))
        self.button_B.clicked.connect(self.alphabetButtonClicked)

        self.button_C.setIcon(QtGui.QIcon("./resource/alphabet/button/C.png"))
        self.button_C.setIconSize(QSize(30, 30))
        self.button_C.clicked.connect(self.alphabetButtonClicked)

        self.button_D.setIcon(QtGui.QIcon("./resource/alphabet/button/D.png"))
        self.button_D.setIconSize(QSize(30, 30))
        self.button_D.clicked.connect(self.alphabetButtonClicked)

        self.button_E.setIcon(QtGui.QIcon("./resource/alphabet/button/E.png"))
        self.button_E.setIconSize(QSize(30, 30))
        self.button_E.clicked.connect(self.alphabetButtonClicked)

        self.button_F.setIcon(QtGui.QIcon("./resource/alphabet/button/F.png"))
        self.button_F.setIconSize(QSize(30, 30))
        self.button_F.clicked.connect(self.alphabetButtonClicked)

        self.button_G.setIcon(QtGui.QIcon("./resource/alphabet/button/G.png"))
        self.button_G.setIconSize(QSize(30, 30))
        self.button_G.clicked.connect(self.alphabetButtonClicked)

        self.button_H.setIcon(QtGui.QIcon("./resource/alphabet/button/H.png"))
        self.button_H.setIconSize(QSize(30, 30))
        self.button_H.clicked.connect(self.alphabetButtonClicked)

        self.button_I.setIcon(QtGui.QIcon("./resource/alphabet/button/I.png"))
        self.button_I.setIconSize(QSize(30, 30))
        self.button_I.clicked.connect(self.alphabetButtonClicked)

        self.button_J.setIcon(QtGui.QIcon("./resource/alphabet/button/J.png"))
        self.button_J.setIconSize(QSize(30, 30))
        self.button_J.clicked.connect(self.alphabetButtonClicked)

        self.button_K.setIcon(QtGui.QIcon("./resource/alphabet/button/K.png"))
        self.button_K.setIconSize(QSize(30, 30))
        self.button_K.clicked.connect(self.alphabetButtonClicked)

        self.button_L.setIcon(QtGui.QIcon("./resource/alphabet/button/L.png"))
        self.button_L.setIconSize(QSize(30, 30))
        self.button_L.clicked.connect(self.alphabetButtonClicked)

        self.button_M.setIcon(QtGui.QIcon("./resource/alphabet/button/M.png"))
        self.button_M.setIconSize(QSize(30, 30))
        self.button_M.clicked.connect(self.alphabetButtonClicked)

        self.button_N.setIcon(QtGui.QIcon("./resource/alphabet/button/N.png"))
        self.button_N.setIconSize(QSize(30, 30))
        self.button_N.clicked.connect(self.alphabetButtonClicked)

        self.button_O.setIcon(QtGui.QIcon("./resource/alphabet/button/O.png"))
        self.button_O.setIconSize(QSize(30, 30))
        self.button_O.clicked.connect(self.alphabetButtonClicked)

        self.button_P.setIcon(QtGui.QIcon("./resource/alphabet/button/P.png"))
        self.button_P.setIconSize(QSize(30, 30))
        self.button_P.clicked.connect(self.alphabetButtonClicked)

        self.button_Q.setIcon(QtGui.QIcon("./resource/alphabet/button/Q.png"))
        self.button_Q.setIconSize(QSize(30, 30))
        self.button_Q.clicked.connect(self.alphabetButtonClicked)

        self.button_R.setIcon(QtGui.QIcon("./resource/alphabet/button/R.png"))
        self.button_R.setIconSize(QSize(30, 30))
        self.button_R.clicked.connect(self.alphabetButtonClicked)

        self.button_S.setIcon(QtGui.QIcon("./resource/alphabet/button/S.png"))
        self.button_S.setIconSize(QSize(30, 30))
        self.button_S.clicked.connect(self.alphabetButtonClicked)

        self.button_T.setIcon(QtGui.QIcon("./resource/alphabet/button/T.png"))
        self.button_T.setIconSize(QSize(30, 30))
        self.button_T.clicked.connect(self.alphabetButtonClicked)

        self.button_U.setIcon(QtGui.QIcon("./resource/alphabet/button/U.png"))
        self.button_U.setIconSize(QSize(30, 30))
        self.button_U.clicked.connect(self.alphabetButtonClicked)

        self.button_V.setIcon(QtGui.QIcon("./resource/alphabet/button/V.png"))
        self.button_V.setIconSize(QSize(30, 30))
        self.button_V.clicked.connect(self.alphabetButtonClicked)

        self.button_W.setIcon(QtGui.QIcon("./resource/alphabet/button/W.png"))
        self.button_W.setIconSize(QSize(30, 30))
        self.button_W.clicked.connect(self.alphabetButtonClicked)

        self.button_X.setIcon(QtGui.QIcon("./resource/alphabet/button/X.png"))
        self.button_X.setIconSize(QSize(30, 30))
        self.button_X.clicked.connect(self.alphabetButtonClicked)

        self.button_Y.setIcon(QtGui.QIcon("./resource/alphabet/button/Y.png"))
        self.button_Y.setIconSize(QSize(30, 30))
        self.button_Y.clicked.connect(self.alphabetButtonClicked)

        self.button_Z.setIcon(QtGui.QIcon("./resource/alphabet/button/Z.png"))
        self.button_Z.setIconSize(QSize(30, 30))
        self.button_Z.clicked.connect(self.alphabetButtonClicked)

    def alphabetButtonClicked(self):
        button = self.sender()
        self.hideDoneTutorial()
        self.playProgress()
        objName = button.objectName()
        # Tôi biết đó là một vụ hack. lấy tên đối tượng 'button_A' và cắt thành 'A'
        self.notifyModeChanged(objName[-1])

    """ Tất cả các tiện ích trong chế độ xem được làm mới bằng cách gọi hàm này """
    # Hàm thông báo thay đổi chế độ
    def notifyModeChanged(self, modeName):
        global currentMode
        global count
        count = 0
        currentMode = modeName
        self.loadTutorialImageFromMode()
        self.statusBar().showMessage('Ký tự bạn hiện đang học là {}.'.format(modeName))
    """ label_tutorialView Chèn hình ảnh hướng dẫn phù hợp với chế độ hiện tại."""

    def loadTutorialImageFromMode(self):
         self.image = QPixmap("./resource/alphabet/overlay_image/{}.png".format(currentMode))
         self.image = self.image.scaled(180, 100, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
         self.label_tutorialView.setPixmap(self.image)
         image_position = (560, 260, 180, 100)  # Thay thế x_position và y_position bằng giá trị bạn mong muốn
         self.label_tutorialView.setGeometry(*image_position)
        # Đặt hình ảnh cho QLabel
         self.label_tutorialView.setPixmap(self.image)
        #  self.label_tutorialView.setGeometry((150, 100),self.image.size())
        #  self.label_tutorialView.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        
    def videoToFrame(self, MainAppWindow):
        global recognizedResult
        cap = cv2.VideoCapture(0)

        while self.is_running:  # Kiểm tra trạng thái của cờ
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            resizedImage = cv2.resize(frame, (self.widthOfCamView, self.heightOfCamView))
            self.saveToPredictor(resizedImage)
            rgbImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2RGB)
            img1 = cv2.rectangle(rgbImage, self.roiLeftTop, self.roiRightBottom, (0, 255, 0), thickness=1, lineType=8, shift=0)
            h, w, c = img1.shape
            qImg = QImage(img1.data, w, h, c * w, QImage.Format_RGB888)
            self.label_camView.setPixmap(QPixmap.fromImage(qImg))
            self.label_camView.update()
            self.updatePredictedResult()

        cap.release()  # Giải phóng camera
        cv2.destroyAllWindows()  # Đóng cửa sổ OpenCV

    def logout(self):
        # Đặt cờ để dừng vòng lặp camera
        self.is_running = False
        # Đóng giao diện chính
        self.close()
        # Quay trở lại giao diện đăng nhập
        self.login_window = MainWindow()
        self.login_window.show()

    def saveToPredictor(self, frame):
        # Binarize thành inRange dựa trên giá trị HSV màu của bàn tay
        lower_blue = np.array([0, 58, 50])
        upper_blue = np.array([30, 255, 255])
        imcrop = frame[self.roiLeftTop[1]:self.roiRightBottom[1], self.roiLeftTop[0]:self.roiRightBottom[0]]
        hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        save_img = cv2.resize(mask, (64, 64))
        cv2.imwrite('1.png', save_img)

    def updatePredictedResult(self):
        global recognizedResult
        recognizedResult = predictor()
        # print("Kết quả chữ cái nhận diện 1: ", recognizedResult)
        self.label_recognizedText.setText(recognizedResult)
        # print("Kết quả chữ cái nhận diện 2: ", self.label_recognizedText.setText(recognizedResult))

    # video_to_frame - sử dụng như một chủ đề
    def video_thread(self, MainAppWindow):
        thread = threading.Thread(target=self.videoToFrame, args=(self,))
        thread.daemon = True  # Khi chương trình kết thúc, tiến trình cũng kết thúc (phát trong nền X)
        thread.start()

class ProgressThread(QThread):
    """
    Runs a counter thread.
    """
    # Cung cấp sự kiện
    countChanged = pyqtSignal(int)

    def run(self):
        TIME_LIMIT = 100
        global count
        count = 0
        while count < TIME_LIMIT:
            time.sleep(0.1)
            # print(currentMode, recognizedResult)
            if currentMode == recognizedResult:
                count += 2
                #print("Chữ hiện tại: ", currentMode)
                #print("Chữ nhận diện: ", recognizedResult)
            self.countChanged.emit(count)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Tải file UI từ main_window.ui
        uic.loadUi('auth_app/log_in.ui', self)
        
        # Kết nối các sự kiện
        self.pushButton_sign_in.clicked.connect(self.sign_in)
        self.pushButton_JoinNow.clicked.connect(self.open_registration_window)
        # Kết nối nút ẩn/hiện mật khẩu với phương thức toggle_password_visibility
        self.pushButton_show_hide.clicked.connect(self.toggle_password_visibility)
        # Cờ để theo dõi trạng thái hiển thị mật khẩu
        self.password_visible = False
        # Kết nối đến cơ sở dữ liệu
        self.db_connection = self.connect_to_db()
        
        

    def connect_to_db(self):
        try:
            # Kết nối đến cơ sở dữ liệu MySQL
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123456789Mc@',
                database='user_db'
            )
            print("Connected to the database successfully!")
            return connection
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            return None

    def sign_in(self):
        # Lấy thông tin đăng nhập từ giao diện
        email = self.lineEdit_login_email.text()
        password = self.lineEdit_login_password.text()
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                sql = "SELECT password FROM users WHERE username = %s"
                cursor.execute(sql, (email,))
                result = cursor.fetchone()
                if result:
                    stored_password = result[0]
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        QMessageBox.information(self, "Thành Công", "Đăng nhập thành công!")
                        print("Login successful!")
                        # Ẩn giao diện đăng nhập và hiển thị giao diện chính sau khi đăng nhập
                        self.main_app_window = MainAppWindow()
                        self.main_app_window.show()
                        self.close()  # Tắt giao diện đăng nhập
                    else:
                        QMessageBox.warning(self, "Lỗi", "Mật khẩu không đúng.")
                        print("Password is incorrect.")
                else:
                    QMessageBox.warning(self, "Lỗi", "Tài khoản không tồn tại.")
                    print("Account does not exist.")
                cursor.close()
            except mysql.connector.Error as e:
                print(f"Error during login: {e}")
                QMessageBox.warning(self, "Lỗi", f"Đăng nhập thất bại: {e}")
        else:
            QMessageBox.warning(self, "Database Error", "Failed to connect to the database.")

    def toggle_password_visibility(self):
        # Chuyển đổi trạng thái của trường mật khẩu
        if self.password_visible:
            self.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.pushButton_show_hide.setText("show")
        else:
            self.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.pushButton_show_hide.setText("hide")
        # Đảo ngược giá trị của cờ password_visible
        self.password_visible = not self.password_visible

    def open_registration_window(self):
        self.registration_window = RegistrationWindow(self.db_connection)
        self.registration_window.show()

class RegistrationWindow(QtWidgets.QWidget):
    def __init__(self, db_connection):
        super().__init__()
        # Tải file UI từ join_now.ui
        uic.loadUi('auth_app/register.ui', self)
        # Kết nối sự kiện
        self.pushButton_agree_and_join.clicked.connect(self.register)
        # Lưu kết nối đến cơ sở dữ liệu
        self.db_connection = db_connection

    def register(self):
        email = self.lineEdit_new_email.text()
        password = self.lineEdit_new_password.text()
        if self.db_connection:
            try:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                cursor = self.db_connection.cursor()
                sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(sql, (email, hashed_password.decode('utf-8')))
                self.db_connection.commit()
                print("User registered successfully!")
                QMessageBox.information(self, "Thành Công", "Đăng ký thành công!")
                cursor.close()
            except mysql.connector.Error as e:
                print(f"Error while inserting user: {e}")
                QMessageBox.warning(self, "Error", f"Registration failed: {e}")
        else:
            QMessageBox.warning(self, "Database Error", "Failed to connect to the database.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainAppWindow()
    window.show()
    sys.exit(app.exec_())
