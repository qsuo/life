#!/usr/bin/python3.6

import sys
import time

from PySide2.QtWidgets import QApplication, QLabel, QWidget, QGraphicsScene
from PySide2.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QGraphicsView
from PySide2.QtCore import Slot, SIGNAL
from PySide2.QtCore import Qt, QRectF, QTimer

import engine


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.game = GameWidget(self)

        self.buttonStep = QPushButton("Step")
        self.buttonStep.clicked.connect(self.game.step) 

        self.buttonRun = QPushButton("Run")
        self.buttonRun.clicked.connect(self.game.run) 
        
        self.buttonStop = QPushButton("Stop")
        self.buttonStop.clicked.connect(self.game.stop) 


        layout = QVBoxLayout()
        layout.addWidget(self.game)
        layout.addWidget(self.buttonStep)
        layout.addWidget(self.buttonRun)
        layout.addWidget(self.buttonStop)

        self.setLayout(layout) 
        self.setWindowTitle('LIFE')
        self.setFixedSize(1000, 800)
        
    def showEvent(self, event):
        self.game.drawUniverse()

class GameWidget(QGraphicsView):
    def __init__(self, parent=None):
        super(GameWidget, self).__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.scene.setSceneRect(0, 0, self.width(), self.height())
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.universe = engine.Universe(100, 100)
        self.universe.generate_random_map()
        #self.scene.addRect(0, 0, 100, 100, brush=Qt.green) 

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.step)
        #self.timer.start()
    
    def drawUniverse(self):
        width = self.width()
        height = self.height()
        
        cellWidth = width / self.universe.n
        cellHeight = height / self.universe.m

        x = 0
        y = 0
        for this_list in self.universe.map:
            y = 0
            for elem in this_list:
                color = Qt.gray
                if elem == 1:
                    color = Qt.green
                self.scene.addRect(x, y, cellWidth, cellHeight, brush=color)
                y += cellHeight
            x += cellWidth
    
    def step(self):
        self.scene.clear()
        self.universe.step()
        self.drawUniverse()
        self.scene.update()

    def run(self):
        self.timer.start()
    
    def stop(self):
        self.timer.stop()

def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()    

    app.exec_()
    
    
if __name__ == '__main__':
    main()


