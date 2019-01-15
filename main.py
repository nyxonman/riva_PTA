
from myConstants import *
from mainUI import *
from myClass import *
from interactGUI import *

if __name__ == "__main__":
    import sys
    app     = QtWidgets.QApplication(sys.argv)
    MainObj = QtWidgets.QMainWindow()
    
    # initialize the ui
    ui = Ui_MainObj()
    ui.setupUi(MainObj)
    MainObj.show()
    
    # rename the window
    MainObj.setWindowTitle("Ping Test Application v" + APP_VERSION)
    test change in new branch
    # interact with the ui
    uiInteractObj = interactGUI(ui)
    # uiInteractionInit(ui)
    sys.exit(app.exec_())
