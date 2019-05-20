#!/usr/bin/python3.6

import sys
import os
import time

from PySide2.QtWidgets import QApplication, QLabel, QWidget, QGraphicsScene
from PySide2.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QGraphicsView, QAbstractButton, QComboBox
from PySide2.QtCore import Slot, SIGNAL
from PySide2.QtCore import Qt, QRectF, QTimer

import engine


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.game = GameWidget(self)

        self.box = QComboBox()
        
        maps = [elem for elem in os.listdir() if '.l' in elem]
        for elem in maps:
            self.box.addItem(elem)

        self.buttonRandom = QPushButton('Random')
        self.buttonRandom.clicked.connect(self.random) 

        self.buttonLoad = QPushButton('Load')
        self.buttonLoad.clicked.connect(self.load) 
        
        self.buttonStep = QPushButton("Step")
        self.buttonStep.clicked.connect(self.game.step) 

        self.buttonRun = QPushButton("Run")
        self.buttonRun.clicked.connect(self.game.run) 
        
        self.buttonStop = QPushButton("Stop")
        self.buttonStop.clicked.connect(self.game.stop) 
        

        self.child = QWidget(self)
        childLayout = QHBoxLayout()
        layout = QVBoxLayout()

        layout.addWidget(self.game)
        childLayout.addWidget(self.buttonRun)
        childLayout.addWidget(self.buttonStop)
        childLayout.addWidget(self.buttonStep)
        
        self.child.setLayout(childLayout)
        layout.addWidget(self.child)
        layout.addWidget(self.box)
        layout.addWidget(self.buttonLoad)
        layout.addWidget(self.buttonRandom)
        self.setLayout(layout) 


        self.setWindowTitle('LIFE')
        self.setFixedSize(1500, 1000)
    
    def load(self):
        item = self.box.currentText()
        f = open(item, 'r')
        self.game.load(f)
        f.close()
        self.game.drawUniverse()

    def random(self):
        self.game.universe.generate_random_map()
        self.game.drawUniverse()

    def showEvent(self, event):
        self.game.drawUniverse()

class GameWidget(QGraphicsView):
    def __init__(self, parent=None):
        super(GameWidget, self).__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.m = 150
        self.n = 150

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.scene.setSceneRect(0, 0, self.width(), self.height())
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.universe = engine.Universe(self.n, self.m)

        print(Qt.red)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.step)
    
    def load(self, item):
         self.universe.file_input(item)
    
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



