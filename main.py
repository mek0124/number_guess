from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from main_window import Ui_w_MainWindow

import random
import sys
 
 
class MainWindow(qtw.QMainWindow, Ui_w_MainWindow):
    def __init__(self):
        super().__init__()

        self.winning_number = random.randint(1, 101)
        self.tries = 5
 
        self.setupUi(self)

        self.pb_new_game.clicked.connect(self.reset_game)
        self.pb_guess.clicked.connect(self.guess_number)
        self.pb_exit.clicked.connect(self.exit_program)

        # Set initial button visibility
        self.pb_new_game.setVisible(False)
        self.pb_guess.setVisible(True)

        self.lb_result_label.setText("")
        
        # Timer for clearing messages
        self.timer = qtc.QTimer(self)
        self.timer.timeout.connect(self.clear_message)

    def exit_program(self):
        sys.exit(1)
    
    def reset_game(self):
        self.winning_number = random.randint(1, 101)
        self.tries = 5
        self.pb_new_game.setVisible(False)
        self.pb_guess.setVisible(True)
        self.le_user_guess.clear()
        self.lb_result_label.setText("")

    def handle_error_success(self, msg: str, is_error: bool):
        # Set message text
        self.lb_result_label.setText(msg)
        
        # Set style based on error/success
        if is_error:
            self.lb_result_label.setStyleSheet("color: red;")
        else:
            self.lb_result_label.setStyleSheet("color: green;")
        
        # Start timer to clear message after 5 seconds
        self.timer.start(5000)
    
    def clear_message(self):
        self.lb_result_label.setText("")
        self.lb_result_label.setStyleSheet("")  # Reset style
        self.timer.stop()
    
    def guess_number(self):
        try:
            guess = int(self.le_user_guess.text())
            
            if guess < 1 or guess > 100:
                self.handle_error_success("Please enter a number between 1 and 100", True)
                return
                
            if guess == self.winning_number:
                self.handle_error_success("Congratulations! You guessed the number!", False)
                self.pb_new_game.setVisible(True)
                self.pb_guess.setVisible(False)
                return
            
            self.tries -= 1
            
            if self.tries == 0:
                self.handle_error_success(f"Game Over! The number was {self.winning_number}", True)
                self.pb_new_game.setVisible(True)
                self.pb_guess.setVisible(False)
                return
                
            # Give hint
            hint = "higher" if guess < self.winning_number else "lower"
            self.handle_error_success(f"Try {hint}! Tries left: {self.tries}", True)
            
        except ValueError:
            self.handle_error_success("Input must be an integer!", True)
 
 
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
 
    window = MainWindow()
    window.show()
 
    sys.exit(app.exec())