import random
from functools import partial # yek parametr be tavabe bedim
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('design.ui' , None)
        self.ui.show()
        self.Score_X = 0
        self.Score_O = 0
        self.Score_equal = 0
        self.game = [[self.ui.b1 , self.ui.b2 , self.ui.b3] ,
                     [self.ui.b4 , self.ui.b5 , self.ui.b6] ,
                     [self.ui.b7 , self.ui.b8 , self.ui.b9]] # yek araye 3*3
        self.player = 'X'
        
        
        for i in range(3):
            for j in range(3):
                # self.game[i][j].setStyleSheet('color: black ; background-color: red')
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('background-color: rgb(255, 170, 255);')

    
        self.ui.b_NG.clicked.connect(partial (self.New_Game , i , j ))
        self.ui.RBF.clicked.connect(partial(self.on_RBF_clicked , i , j ))
        self.ui.RBA.clicked.connect(partial(self.on_RBA_clicked , i , j ))
        self.ui.b_about.clicked.connect(self.about)


    def about(self):
        MBox = QMessageBox()
        MBox.setText('Creator : Emineh Ghafarzadeh Taji')
        MBox.exec()

    
    def on_RBF_clicked(self , i , j):
        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play_F , i , j))

    def on_RBA_clicked(self , i , j ):
        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play_A , i , j))



    def New_Game(self , i , j):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('background-color: rgb(255, 170, 255);')
        self.Score_X = 0
        self.Score_O = 0
        self.Score_equal = 0
        self.ui.label_SX.setText(f'Score X : {self.Score_X}')
        self.ui.label_SO.setText(f'Score O : {self.Score_O}')
        self.ui.label_equal.setText(f'Score equal : {self.Score_equal}')



    def reset(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('background-color: rgb(255, 170, 255);')



    def play_F(self , i , j):
        if self.game[i][j].text() == '':
            if self.player == 'X' :
                self.game[i][j].setText('X')
                self.player = 'O'
                self.game[i][j].setStyleSheet('color: black ; background-color: rgb(170, 0, 127);')
            else:
                self.game[i][j].setText('O')
                self.player = 'X'
                self.game[i][j].setStyleSheet('color: white ; background-color: rgb(170, 85, 127);')
            
        self.check()


    def play_A(self , i , j):
        if self.game[i][j].text() == '':
            if self.player == 'X' :
                self.game[i][j].setText('X')
                self.player = 'O'
                self.game[i][j].setStyleSheet('color: black ; background-color: rgb(170, 0, 127);')
                empty_cells = []
                for row in self.game:
                    for cell in row:
                        if cell.text() == '':
                            empty_cells.append(cell)
                if empty_cells:
                    computer_move = random.choice(empty_cells)
                    computer_move.setText('O')
                    computer_move.setStyleSheet('color: white ; background-color: rgb(170, 85, 127);')
                    self.player = 'X'
            
        self.check()
        


    def check(self):
        
        empty_cells_found = self.check_empty_cells()
        if empty_cells_found:
            if self.check_winner('X'):
                self.Score_X += 1
                self.ui.label_SX.setText(f'Score X : {self.Score_X}')
                MBox = QMessageBox()
                MBox.setText('Player X Wins')
                MBox.exec()
                self.reset()
            elif self.check_winner('O'):
                self.Score_O += 1
                self.ui.label_SO.setText(f'Score O : {self.Score_O}')
                MBox = QMessageBox()
                MBox.setText('Player O Wins')
                MBox.exec()
                self.reset()
        else:
            self.Score_equal += 1
            self.ui.label_equal.setText(f'Score equal : {self.Score_equal}')
            MBox = QMessageBox()
            MBox.setText('Player X & O Wins')
            MBox.exec()
            self.reset()



    def check_winner(self, player):
        # بررسی سطرها
        for i in range(3):
            if (self.game[i][0].text() == self.game[i][1].text() == self.game[i][2].text() == player):
                return True

        # بررسی ستون‌ها
        for j in range(3):
            if (self.game[0][j].text() == self.game[1][j].text() == self.game[2][j].text() == player):
                return True

        # بررسی قطرها
        if (self.game[0][0].text() == self.game[1][1].text() == self.game[2][2].text() == player) or \
        (self.game[0][2].text() == self.game[1][1].text() == self.game[2][0].text() == player):
            return True

        return False
        

    def check_empty_cells(self):
        empty_cells_found = False
        for i in range(3):
            for j in range(3):
                if self.game[i][j].text() == '':
                    empty_cells_found = True
                    break
            if empty_cells_found:
                break
        return empty_cells_found
    

app = QApplication([])
window = TicTacToe()
app.exec()