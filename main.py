"""
Import needed packages from PySide6. Here we import QtCore
and QtWidgets from PySide6 under an alias for easier usage.

QtCore is now called via qtc -> qtc.QTimer
QtWidgets is now called via qtw -> qtw.QMainWindow

This allows us to import an entire sub-class of the framework
and call the needed portions with smaller import lines. Otherwise,
the imports would look like this

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication

Although this method isn't wrong, it's a tad cleaner, in my opinion,
to just import the class and call the items from the class as needed
via the alias its imported under.
"""
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from main_window import Ui_w_MainWindow

import random # needed to select a new random number on each new game
import sys # needed for properly exiting the application


"""
the main class. Since this is a very simple application
it's ok that the program operates in the main class.
If this application was to grow to where it remembered
previous games, allow the user to implement custom settings
and create/login to profiles, then you would use this main
class as the control flow for the application and then each
part of the application would have it's own controller class.
For example:

from app.controllers.history import HistoryController

class MainWindow(qtw.QMainWindow, Ui_w_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pb_history.clicked.connect(self.show_history)

    def show_history(self):
        history_controller = HistoryController()
        self.setCentralWidget(history_controller)


class HistoryController(qtw.QWidget, Ui_widget_HistoryScreen):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
"""
class MainWindow(qtw.QMainWindow, Ui_w_MainWindow):
    def __init__(self):
        super().__init__()

        # use the random library to pick a random number on each new game
        self.winning_number = random.randint(1, 101)
        # set a number of times the user can attempt guessing
        self.tries = 5
        # tell the MainWindow class to setup the UI from main_window.py's conversion via main_window.ui
        self.setupUi(self)
        
        """
        buttons operate off triggered actions basically. When you click the button, it
        triggers an event '.clicked' and then we call the '.connect' function to tell
        the button click which event to trigger (or function to execute)
        """
        # new game triggers reset_game
        self.pb_new_game.clicked.connect(self.reset_game)
        # guess button triggers guess_number
        self.pb_guess.clicked.connect(self.guess_number)
        # exit button triggers the exit_program function
        self.pb_exit.clicked.connect(self.exit_program)

        # Set initial button visibility of the new game and guess button
        # the new game button is set invisible by default as it's only
        # needed to be shown after the user has either ran out of guesses
        # or has won the game and clicks the "New Game" button.
        self.pb_new_game.setVisible(False)
        self.pb_guess.setVisible(True)

        # set the result label to be an empty string (virtually hidden but still there to maintain placement) on each new game
        self.lb_result_label.setText("")
        
        # Timer for clearing messages
        self.timer = qtc.QTimer(self)
        # when the timer runs out, tell it to connect to clearing the result label
        self.timer.timeout.connect(self.clear_message)

    # this function exits the system with code 1
    def exit_program(self):
        # exit code 0 means a clean exit with no problems
        # exit code 1 means there was a problem which caused the program to exit
        sys.exit(0)
    
    # this function resets the game screen for a "new game"
    def reset_game(self):
        """
        In this function, we are resetting all the base
        game values back to their default state for a new
        game setup.

        Default Values:
        winning number: random
        tries: 5
        new game button: hidden
        guess button: shown
        user guess input: empty
        result label: empty
        """
        self.winning_number = random.randint(1, 101)
        self.tries = 5
        self.pb_new_game.setVisible(False)
        self.pb_guess.setVisible(True)
        self.le_user_guess.clear()
        self.lb_result_label.setText("")

    # this function is known as a utility function.
    # it's primary purpose is to display the correct
    # messges with the appropriate styles to the user.
    # It will tell the timer to start which will reset
    # only the label displaying messages to the user
    def handle_error_success(self, msg: str, is_error: bool):
        # Set message text
        self.lb_result_label.setText(msg)
        
        # Set style based on error/success
        if is_error:
            self.lb_result_label.setStyleSheet("color: red;")   # error
        else:
            self.lb_result_label.setStyleSheet("color: green;") # success
        
        # Start timer to clear message after 5 seconds
        self.timer.start(5000)
    
    # a second utility function to strictly handle resetting the result label
    def clear_message(self):
        self.lb_result_label.setText("")
        self.lb_result_label.setStyleSheet("")  # Reset style
        self.timer.stop()
    
    # this is a logic function that handles the user's input
    # and displays back the corresponding message based off
    # what the user entered
    def guess_number(self):
        # wrap the logic in a try/except block for proper error handling
        try:
            # convert the user's input to an integer from a string
            guess = int(self.le_user_guess.text())
            
            # check if the user's input is less than 1 or greater than 100
            if guess < 1 or guess > 100:
                # if so, display the error message to the user
                self.handle_error_success("Please enter a number between 1 and 100", True)
                
                # return back out of the logic function to prevent the rest of the code
                # below this point from executing
                return
                
            # check if the user's input matches the winning number
            if guess == self.winning_number:
                # if so, display the success message to the user
                self.handle_error_success("Congratulations! You guessed the number!", False)

                # invert the current visibility of both buttons so that the guess button
                # is now hidden and the new game button shows
                self.pb_new_game.setVisible(True)
                self.pb_guess.setVisible(False)

                # return back out of the function
                return
            
            # given both checks dont' trigger above,
            # decrement the user's remaing tries by 1
            self.tries -= 1
            
            # check if the user's tries is zero
            if self.tries == 0:
                # if so, display the correct message back to the user
                self.handle_error_success(f"Game Over! The number was {self.winning_number}", True)
                # invert buttons visibility status
                self.pb_new_game.setVisible(True)
                self.pb_guess.setVisible(False)

                # return back out of the logic function
                return
                
            # Give a hint to the user to help them in guessing more accurately within a vast range of numbers
            hint = "higher" if guess < self.winning_number else "lower"
            # display the correct message to the user
            self.handle_error_success(f"Try {hint}! Tries left: {self.tries}", True)
            
        # if converting the user's input to an integer failes,
        # display the correct error message to the user which
        # will trigger resetting the game
        except ValueError:
            self.handle_error_success("Input must be an integer!", True)


if __name__ == '__main__':
    # instantiate the PySide6 application
    app = qtw.QApplication(sys.argv)
    # instantiate the main window
    window = MainWindow()
    # show the main window
    window.show()
    # if the application is exited, tell everybody basically lol
    sys.exit(app.exec())