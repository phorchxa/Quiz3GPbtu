from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys

from main import Ui_MainWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ღილაკის კლიკის დაკავშირება ფუნქციასთან
        self.ui.pushButton.clicked.connect(self.on_add_button_clicked)

    def on_add_button_clicked(self):
        # 3 ტექსტური ველის მნიშვნელობები
        text1 = self.ui.lineEdit_3.text()
        text2 = self.ui.lineEdit_6.text()
        text3 = self.ui.lineEdit_5.text()

        # radiobutton-ებდან რომელია მონიშნული
        if self.ui.radioButton_2.isChecked():
            productivity = "პროდუქტიული"
        elif self.ui.radioButton.isChecked():
            productivity = "საშუალოდ პროდუქტიული"
        elif self.ui.radioButton_3.isChecked():
            productivity = "არაპროდუქტიული"
        else:
            productivity = "არაფერია მონიშნული"

        # comboBox-დან დღე
        day = self.ui.comboBox.currentText()

        # calendarWidget-დან თარიღი
        date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")

        #შეამოწმო ცარიელია თუ არა ტექსტები და დავანახოთ შეტყობინება
        if not (text1 and text2 and text3):
            QMessageBox.warning(self, "შეცდომა", "გთხოვთ შეავსოთ ყველა ტექსტური ველი.")
            return

        # ინფორმაციის გაშვება popup-ში
        message = f"""შეყვანილი მონაცემები:
        ტექსტები: {text1}, {text2}, {text3}
        პროდუქტიულობა: {productivity}
        დღე: {day}
        თარიღი: {date}"""

        QMessageBox.information(self, "ინფორმაცია", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())