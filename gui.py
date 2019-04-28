#!/usr/bin/python3.6

import sys
import time

from PySide2.QtWidgets import QApplication, QLabel, QWidget, QGraphicsScene
from PySide2.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QGraphicsView
from PySide2.QtCore import Slot
from PySide2.QtCore import Qt, QRectF

import engine


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.view = QGraphicsView()
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.button = QPushButton("Step")
        self.button.clicked.connect(self.step) 

        self.button2 = QPushButton("Run")
        self.button2.clicked.connect(self.run) 


        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        
        self.setLayout(layout) 
        self.setWindowTitle('Simple')
        self.setFixedSize(1000, 800)
        
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
        self.view.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.universe = engine.Universe(25, 25)
        f = open('init2', 'r')
        self.universe.file_input(f)
        #self.drawGrid()
        #self.scene.addRect(0, 0, 100, 100, brush=Qt.gray)
        #self.scene.addRect(400, 400, 100, 100, brush=Qt.green)
        
    def drawUniverse(self):
        width = self.view.width()
        height = self.view.height()
        
        cellWidth = width / self.universe.n
        cellHeight = height / self.universe.m

        x = 0
        y = 0
        """
        while x < width:
            y = 0
            while y < height:
                self.scene.addRect(x, y, cellWidth, cellHeight, brush=Qt.gray)
                y += cellHeight
            x += cellWidth
        """
        for i, this_list in enumerate(self.universe.map):
            y = 0
            for j, elem in enumerate(this_list):
                color = Qt.gray
                if elem == 1:
                    color = Qt.green
                self.scene.addRect(x, y, cellWidth, cellHeight, brush=color)
                y += cellHeight
            x += cellWidth

    def showEvent(self, event):
        self.drawUniverse() 

    def step(self):
        self.scene.clear()
        self.universe.step()
        self.drawUniverse()
        self.scene.update()
    
    def run(self):
        while 1:
            time.sleep(1)
            self.step()


    def draw(self):
        self.scene.addRect(200, 200, 100, 100, brush=Qt.blue)
        self.scene.update()

def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()    

    app.exec_()
    
    
if __name__ == '__main__':
    main()


