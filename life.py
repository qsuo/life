#!/usr/bin/python3.6

import sys
import gui


def main():
    app = gui.QApplication(sys.argv)
    
    window = gui.MainWindow()
    window.show()    
    app.exec_()
    
    
if __name__ == '__main__':
    main()

