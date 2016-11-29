# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from workform import WorkForm


def main():
    app = QtGui.QApplication(sys.argv)
    form=WorkForm()
    form.MainWindow.show()

    sys.exit(app.exec_())
    pass

if __name__ == '__main__':
    main()



