__author__ = "Nikesh Man Shakya"
from mainUI import *
from myClass import *
from interactGUI import *
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    import sys
    app         = QtWidgets.QApplication(sys.argv)
    MainObj     = QtWidgets.QMainWindow()
    centerPoint = QDesktopWidget().availableGeometry().center()
    icon        = QIcon('icon.png')
    
    if (os.name == 'nt'):
        # This is needed to display the app icon on the taskbar on Windows 7+
        import ctypes
        myappid = 'Itron.PTA.'+APP_VERSION # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # initialize the ui
    ui = Ui_MainObj()
    ui.setupUi(MainObj)
    MainObj.setWindowIcon(icon) 

    # centralize the window. was not working in linux automatically
    centerPoint = centerPoint - QtCore.QPoint(MainObj.width()/2,MainObj.height()/2)
    MainObj.move(centerPoint)
    
    # rename the window
    MainObj.setWindowTitle("Ping Test Application v" + APP_VERSION)
    
    # show the window
    MainObj.show()

    # interact with the ui
    uiInteractObj = interactGUI(ui)
    
    sys.exit(app.exec_())
