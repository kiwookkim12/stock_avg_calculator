import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class StockAvgCalculator(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("/home/kw/dev_ws/stock_calculator/stock_avg_calculator.ui", self)
        
        # 버튼 클릭 이벤트 연결
        self.button_calculate.clicked.connect(self.calculate_average_price)
        
    def calculate_average_price(self):
        try:
            current_price = float(self.input_current_price.text())
            new_price = float(self.input_new_price.text())
            quantity = int(self.input_quantity.text())
            
            # 새로운 평균 단가 계산
            total_quantity = quantity + 1
            avg_price = ((current_price + (new_price * quantity)) / total_quantity)
            
            # 결과 표시
            self.label_result.setText(f"결과: 새로운 평균 단가는 {avg_price:.2f} 원입니다.")
            
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "모든 필드에 올바른 숫자를 입력하세요.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockAvgCalculator()
    window.show()
    sys.exit(app.exec_())