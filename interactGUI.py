# import built in libraries
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDesktopWidget
from PyQt5.QtCore import QThread,pyqtSignal

#import my libraries
from myConstants import *
from myFunctions import *
from myClass import *

class interactGUI(object):
	"""class to interact with the various GUI elements and take necessary actions"""
	def __init__(self, arg):
		super(interactGUI, self).__init__()
		self.ui              = arg
		self.mPktSize        = 0
		self.mPktInt         = 0
		self.mPktRes         = 0
		self.mPktCnt         = 0
		self.mRootCnt        = 0
		self.mIteration      = 0
		self.mShowMap        = 0
		self.mShowAllNeighbors    = 0
		self.mOutputToFile   = 0
		self.mOutputFilename = "last_testlog.csv"
		self.exportData      = {}
		self.centerPoint     = QDesktopWidget().availableGeometry().center()
		self.pingThreadObj   = pingThread(App(), self.ui)
		self.ui.menubar.setNativeMenuBar(False) # for unix
		self.interactObjects()

	def refresh(self):
		'''process the gui events instantly'''
		QtGui.QGuiApplication.processEvents()

	def statusBarMsg(self, msg):
		'''write the message to the status bar'''
		self.ui.statusbar.showMessage(msg)

	def getParams(self):
		'''get the params of the interactGUI object'''
		return (self.mPktSize, self.mPktInt, self.mPktRes, self.mPktCnt, self.mRootCnt, self.mIteration, self.mShowMap, self.mShowAllNeighbors, self.mOutputToFile, self.mOutputFilename)	

	def logCmdHistory(self, funcName, html='', cmdType="default", append=True):
		'''To show the log in the command history field
		funcName: name of the function
		html: the html message
		cmdType: "default", "error", "warn", "succ"
		append: True will always append to the lat, False will insert new log
		'''
		cmdType = cmdType.lower()
		html+= " [" + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "]"
		
		if cmdType == "error":
			html = logErr(html, funcName)
		elif cmdType == "info":
			html = logInfo(html, funcName)
		elif cmdType == "warn":
			html = logWarn(html, funcName)
		elif cmdType == "succ":
			html = logSucc(html, funcName)
		else:
			html = logDef(html, funcName)

		self.ui.cmdHistory.append(html)	if append == True else self.ui.cmdHistory.setHtml(html)
		if (self.ui.scrollToLastCmdHistory.checkState()!=0):
			self.ui.cmdHistory.moveCursor(QtGui.QTextCursor.End)
		self.refresh()

	def closeApp(self):
		'''Closes the app. If a test is running, it will ask for confirmation to close.'''
		ans = QMessageBox.Yes
		# if a ping thread is running, prompt a question.
		if self.pingThreadObj.isRunning():
			ans = self.showDialog("Quit","A Test is running. Do you really want to quit?","question")
		if ans==QMessageBox.Yes:
			QtCore.QCoreApplication.instance().quit()
		

	def verifyInputParams(self):
		'''verify the input parameters like iteration, nbr of roots and file name'''
		errMsg  = ""

		# test iterations
		if (not self.mIteration.isdigit()) or int(self.mIteration) < 1:
			errMsg+="Test Iteration should be a numeric value and greater than 0. '{}' provided.</br>".format(self.mIteration)  
		# nbr of roots
		if (not self.mRootCnt.isdigit()) or int(self.mRootCnt) < 1:
			errMsg+="nbr of roots should be a numeric value and greater than 0. '{}' provided.</br>".format(self.mRootCnt) 
		# check the file name
		if (self.mOutputToFile == True):
			self.mOutputFilename = self.mOutputFilename.strip()
			if len(self.mOutputFilename) < 1  :
				errMsg+="Outfile Name is '{}'. Please provide a filename.</br>".format(self.mOutputFilename)
			self.mOutputFilename = self.mOutputFilename.split('.')[0] + '.csv'
		
		if (not self.mPktSize.isdigit()) or int(self.mPktSize)<MIN_PING_PAYLOAD or int(self.mPktSize)>MAX_PING_PAYLOAD:
			errMsg+="Packet size should be numeric and between {} and {}. '{}' provided.</br>".format(MIN_PING_PAYLOAD, MAX_PING_PAYLOAD,self.mPktSize)

		return errMsg

	def interactObjects(self):
		'''Interact with the GUI objects to link with various functions'''
		self.initializeDefaults()

		# ping controls
		self.ui.pktSizeDial.valueChanged.connect(lambda: self.interact(self.ui.pktSizeDial))
		self.ui.pktSizeVal.textChanged.connect(lambda: self.interact(self.ui.pktSizeVal))
		self.ui.pktCntDial.valueChanged.connect(lambda: self.interact(self.ui.pktCntDial))
		self.ui.pktIntDial.valueChanged.connect(lambda: self.interact(self.ui.pktIntDial))
		self.ui.pktResDial.valueChanged.connect(lambda: self.interact(self.ui.pktResDial))

		# app controls
		self.ui.rootCntVal.textChanged.connect(lambda: self.interact(self.ui.rootCntVal))
		self.ui.IterVal.textChanged.connect(lambda: self.interact(self.ui.IterVal))
		self.ui.showMap.stateChanged.connect(lambda: self.interact(self.ui.showMap))
		self.ui.showAllNeighbors.stateChanged.connect(lambda: self.interact(self.ui.showAllNeighbors))
		self.ui.outputToFile.stateChanged.connect(lambda: self.interact(self.ui.outputToFile))
		self.ui.scrollToLastCmdHistory.stateChanged.connect(lambda: self.interact(self.ui.scrollToLastCmdHistory))
		self.ui.outputFilenameVal.textChanged.connect(lambda: self.interact(self.ui.outputFilenameVal))
		
		# button controls
		self.ui.addRowBtn.clicked.connect(lambda:self.interact(self.ui.addRowBtn))
		self.ui.removeRowBtn.clicked.connect(lambda:self.interact(self.ui.removeRowBtn))
		self.ui.startTestBtn.clicked.connect(lambda:self.interact(self.ui.startTestBtn))
		self.ui.clearLogBtn.clicked.connect(lambda:self.interact(self.ui.clearLogBtn))
		self.ui.resetEntryBtn.clicked.connect(lambda:self.interact(self.ui.resetEntryBtn))
		self.ui.saveEntryBtn.clicked.connect(lambda:self.interact(self.ui.saveEntryBtn))
		self.ui.loadEntryBtn.clicked.connect(lambda:self.interact(self.ui.loadEntryBtn))
		self.ui.exportDataBtn.clicked.connect(lambda:self.interact(self.ui.exportDataBtn))
		# self.ui.resetEntryBtn
		self.ui.quitBtn.clicked.connect(self.closeApp)

		#Menu Actions
		self.ui.actionAbout.triggered.connect(lambda:self.interact(self.ui.actionAbout))
		self.ui.actionDebug_Mode.triggered.connect(lambda:self.interact(self.ui.actionDebug_Mode))

# 		impAct = QAction('Import mail', self) 
# impMenu.addAction(impAct)

	# ALL integer arguments
	def createCmdStr(self):
		'''Create a command string for the output'''
		mCmdStr = "*** COMMAND *** <br>"
		if self.mShowMap==1:
			mCmdStr+=" Show <b>MAPPING between SHORT_ADR and H/W or EXT_addr</b>"
		else:
			mCmdStr+=" Send <b>'{}' PING{}</b>".format(self.mPktCnt,"(s)" if int(self.mPktCnt) > 1 else "")
			if int(self.mPktCnt) > 1:
				mCmdStr+=" with an INTERVAL of <b>'{}'' seconds</b> each ".format(self.mPktCnt)
			mCmdStr+=" of SIZE <b>'{}' Bytes</b> with ".format(self.mPktSize)        
			mCmdStr+="RESPONSE TIME of <b>'{}' seconds</b>".format(self.mPktRes)

		if self.mShowAllNeighbors:
			mCmdStr+=" for <b>ALL neighbors</b>"
		# mCmdStr+=" 'all BACTs'"
		if self.mShowMap==0 and int(self.mIteration) > 1:
		    mCmdStr+=", REPEAT Test <b>'x{}'</b>".format(self.mIteration)

		if self.mOutputToFile == 1:
			mCmdStr+=" and WRITE the result statistics to <b>file '{}'</b>".format(self.mOutputFilename)

		mCmdStr = "<center>" + mCmdStr + "</center>"
		return (mCmdStr)

	def initializeDefaults(self):
		'''initialize various defaults'''
		# variable defaults
		self.mPktSize        = DFT_PKT_SIZE
		self.mPktInt         = DFT_PKT_INTV
		self.mPktRes         = DFT_PKT_RESP_TIME
		self.mPktCnt         = DFT_PKT_CNT
		self.mRootCnt        = DFT_ROOTS_CNT
		self.mIteration      = DFT_ITERATION
		self.mShowMap        = 0
		self.mOutputToFile   = 0
		self.mOutputFilename = DFT_OUTPUTFILENAME
		
		# gui items defaults
		self.ui.rootCntVal.setText(str(DFT_ROOTS_CNT))
		self.ui.IterVal.setText(str(DFT_ITERATION))
		self.ui.showMap.setChecked(CHECKBOX_STATE_UNCHECKED)
		self.ui.outputToFile.setChecked(CHECKBOX_STATE_UNCHECKED)
		self.ui.outputFilenameVal.setText(DFT_OUTPUTFILENAME)

		self.ui.actionDebug_Mode.setChecked(DEBUG_MODE)
		
		self.updateTable(DFT_ROOTS_CNT)

		cmdStr = self.createCmdStr() 
		self.ui.outputCmd.setHtml(cmdStr)


	def interact(self, myObj):
		'''Handles the interaction with the GUI'''
		mError    = 0
		exclude   = 0
		retMsg    = ""
		myObjName = myObj.property("objectName")
		
		if myObjName=="pktSizeVal":
			myObjVal      = myObj.text()
			self.mPktSize = str(myObjVal)
		
		elif myObjName=="pktSizeDial":
			myObjVal      = myObj.value()
			myObjVal      = 2<<(myObjVal-1)
			self.mPktSize = str(myObjVal)
			self.ui.pktSizeVal.setText(str(myObjVal))            

		elif myObjName=="pktCntDial":
			myObjVal     = myObj.value()
			self.mPktCnt = str(myObjVal)
			self.ui.pktCntVal.setText(str(myObjVal))

		elif myObjName=="pktIntDial":
			myObjVal     = myObj.value()
			myObjVal     = 12*myObjVal
			self.mPktInt = str(myObjVal)
			self.ui.pktIntVal.setText(str(myObjVal))
			if int(self.mPktCnt) < 2:
				self.showDialog("Warning","The interval value has no meaning when <br>packet count value is <b>less than 1.<b>","warning")

		elif myObjName=="pktResDial":
			myObjVal     = myObj.value()
			myObjVal     = 12*myObjVal
			self.mPktRes = str(myObjVal)
			self.ui.pktResVal.setText(str(myObjVal))
			if myObjVal < 30:
				self.showDialog("Warning","The response value <b>less than 30 seconds</b> is not recommended","warning")

		elif myObjName == "rootCntVal":
			myObjVal      = myObj.text() if myObj.text() !="" else "0"
			self.mRootCnt = myObjVal

		elif myObjName == "IterVal":
			myObjVal        = myObj.text() if myObj.text() !="" else "0"
			self.mIteration = myObjVal

		elif myObjName == "addRowBtn":
			self.updateTable(self.mRootCnt,1)
			myObjVal = "1 row added"

		elif myObjName == "removeRowBtn":
			self.updateTable(self.mRootCnt,-1)
			myObjVal = "1 row removed"

		elif myObjName == "startTestBtn":
			myObjVal="pressed"
			exclude = 1
			self.ui.startTestBtn.setEnabled(0)
			self.startTest()

		elif myObjName == "clearLogBtn":
			myObjVal="pressed"
			self.ui.cmdHistory.setHtml('')
		elif myObjName == "exportDataBtn":
			self.exportData2csv()
			myObjVal="pressed"

		elif myObjName == "resetEntryBtn":
			myObjVal="pressed"
			self.initializeDefaults()

		elif myObjName == "saveEntryBtn":
			myObjVal="pressed"
			self.saveEntries()

		elif myObjName == "loadEntryBtn":
			myObjVal="pressed"
			self.loadEntries()

		elif myObjName == "showMap":
			myObjVal      = 0 if myObj.checkState() == 0 else 1
			if myObjVal == 1:
				self.ui.pktCntDial.setEnabled(0)
				self.ui.pktIntDial.setEnabled(0)
				self.ui.pktResDial.setEnabled(0)
				self.ui.pktSizeDial.setEnabled(0)
				self.ui.IterVal.setEnabled(0)
			else:
				self.ui.pktCntDial.setEnabled(1)
				self.ui.pktIntDial.setEnabled(1)
				self.ui.pktResDial.setEnabled(1)
				self.ui.pktSizeDial.setEnabled(1)
				self.ui.IterVal.setEnabled(1)
			self.mShowMap = myObjVal

		elif myObjName == "showAllNeighbors":
			myObjVal         = 0 if myObj.checkState() == 0 else 1
			self.mShowAllNeighbors = True if myObjVal == 1 else False

		elif myObjName == "outputToFile":
			myObjVal           = 0 if myObj.checkState() == 0 else 1
			self.ui.outputFilenameVal.setEnabled(myObjVal)
			self.mOutputToFile = myObjVal

		elif myObjName == "scrollToLastCmdHistory":
			myObjVal = 0 if myObj.checkState() == 0 else 1
			if myObjVal == 1:
				self.ui.cmdHistory.moveCursor(QtGui.QTextCursor.End)
			

		elif myObjName == "outputFilenameVal":
			myObjVal             = self.ui.outputFilenameVal.text().strip()
			self.mOutputFilename = myObjVal

		elif myObjName == "actionAbout":
			myObjVal = "pressed"
			exclude = True
			self.logCmdHistory(func_name(),"<b><center>PING TEST APPLICATION<b><br/>v{}<br/>This application is created by Nikesh Man Shakya.<br>nikeshman.shakya@itron.com</center>".format(APP_VERSION), "info")
			
		elif myObjName == "actionDebug_Mode":
			myObjVal = myObj.isChecked()
			set_debug_mode(myObjVal)

		else:
			myObjVal = "Not Found"
			mError   = 1

		if mError == 0:
			# validate here the inputs
			retMsg = self.verifyInputParams()
			if len(retMsg) == 0:
				cmdStr = self.createCmdStr()
				self.ui.outputCmd.setHtml(cmdStr)
				self.updateTable(self.mRootCnt)
				if not self.pingThreadObj.isRunning():
					self.ui.startTestBtn.setEnabled(1)
			else:
				self.ui.startTestBtn.setEnabled(0)

		# command history logs
		if not exclude:
			self.logCmdHistory(func_name(),myObjName +":" + str(myObjVal))
		if len(retMsg) > 1:
			self.logCmdHistory(func_name(),retMsg, "error")
		

	def updateTable(self, nRootCnt, addRow=0):
		nRootCnt = int(nRootCnt)
		# self.ui.tableWidget.clearContents()
		rows = self.ui.tableWidget.rowCount()
		cols = self.ui.tableWidget.columnCount()
		self.ui.tableWidget.setColumnCount(nRootCnt)

		if addRow==1 or rows>2:
			self.ui.tableWidget.setRowCount(rows+addRow)
			item = QtWidgets.QTableWidgetItem()
			self.ui.tableWidget.setVerticalHeaderItem(rows, item)
			item.setText("Entry " + str(rows)) 

		if addRow==0:
			# adding columns which is the number of nRootCnt
			for i in range(nRootCnt):
				item = QtWidgets.QTableWidgetItem()
				self.ui.tableWidget.setHorizontalHeaderItem(i, item)
				item.setText("ROOT_" + str(i+1))       

	def showDialog(self, title="Title", message="Message", boxType="about"):
		'''show diaglog with the title, message
			boxType = "critical", "warning", "information", "question", "about"
		'''
		boxType = boxType.lower()
		dialogBox = QtWidgets.QWidget()
		# center the widget
		dialogBox.move(self.centerPoint)
		if boxType == "critical":
			ret = QMessageBox.critical(dialogBox, str(title).strip(), str(message).strip())
		elif boxType == "warning":
			ret = QMessageBox.warning(dialogBox, str(title).strip(), str(message).strip())
		elif boxType == "information":
			ret = QMessageBox.information(dialogBox, str(title).strip(), str(message).strip())
		elif boxType == "question":
			ret = QMessageBox.question(dialogBox, str(title).strip(), str(message).strip(),QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		else:
			ret = QMessageBox.about(dialogBox, str(title).strip(), str(message).strip())

		return ret

	def verifyEntries(self,myApp):
		'''Verify table entries'''
		cnt = 0
		panArray = []
		retMsg = ""
		itemCnt = 0
		first = 1

		# read all entries form the table widget and verify the contents
		for row in range(self.ui.tableWidget.rowCount()):
			rowdata = []
			i=0
			for column in range(self.ui.tableWidget.columnCount()):
				item = self.ui.tableWidget.item(row,column)
				
				if item is not None:
					itemVal = item.text().strip()
					
					# first row is the root ipv6 address. verify it and retrieve the pan ID
					if first:
						ret = verifyRootAddr(itemVal, self)
						if ret == RET_FAIL:
							return RET_FAIL
						panId = ret
						myApp.pans[panId] = Pan(rootAddr=itemVal)
						panArray.append(panId)

					# process the rest of the items
					else:
						length = len(itemVal)
						if (length==0):
							self.logCmdHistory(func_name(),"Entry ({},{}) Empty".format(row,column),"warn")
							i+=1
							continue

						if (length!=16 and length!=0):
							retMsg += "In row {}, EXT/MAC Address should be 16 characters[{} provided]".format(cnt, length)
							self.logCmdHistory(func_name(),retMsg,"error")
							return RET_FAIL
						if itemVal in myApp.fileList:
						
							retMsg += "In row {}, EXT/MAC Address '{}' is redundant. Please check entries".format(cnt+1, itemVal)
							self.logCmdHistory(func_name(),retMsg,"error")
							return RET_FAIL

						myApp.mapExt2PanId[itemVal] = panArray[i]
						myApp.fileList.append(itemVal)

					itemCnt+=1
					i+=1
				
				# an empty item is skipped especially when creating a new column or row
				else:
					i+=1
					self.logCmdHistory(func_name(),"Entry ({},{}) Empty".format(row,column),"warn")
			first = 0

		# print(myApp.fileList)
		# print(myApp.mapExt2PanId)
		return RET_SUCC

	def exportData2csv(self):
		itemCnt = 0
		empty = []
		incTestInfo = 0 if self.ui.exportIncTestInfo.checkState() == 0 else 1
		incData = 0 if self.ui.exportIncData.checkState() == 0 else 1
		incFinalStats = 0 if self.ui.exportIncFinalStats.checkState() == 0 else 1
		incMapList = 0 if self.ui.exportIncMapList.checkState() == 0 else 1
		filename = "testlog_"+str(datetime.now().strftime('%d_%m_%Y'))+"_{}B_{}reps".format(self.mPktSize, self.mIteration)+".csv"
		path, fileType = QFileDialog.getSaveFileName(QtWidgets.QWidget(), 'Export CSV File', DFT_OUTPUTFILENAME, 'CSV(*.csv)')
		if path:
			with open(path,"w", newline='') as stream:
				writer = csv.writer(stream)
				# write the headers
				if incTestInfo:
					for r in self.exportData["header"]:
						writer.writerow(r)

				# write main data
				if incData:
					if not incTestInfo:
						writer.writerow(["TimeStamp","extAddr","sAddr","hwType","best_RF","RSSI_I","RSSI_M","tx","rx","loss","macTxSucc","macTxFail","macTxAck","macTxCts","macRxRts","macRxAck","minRTT","maxRTT","mdevRTT","avgRTT"])
					for r in self.exportData["main"]:
						writer.writerow(r)
					writer.writerow(empty)

				# write the final stats
				if incFinalStats:
					writer.writerow(["final"])
					writer.writerow(["TimeStamp","extAddr","sAddr","hwType","best_RF","RSSI_I","RSSI_M","tx","rx","loss","macTxSucc","macTxFail","macTxAck","macTxCts","macRxRts","macRxAck","minRTT","maxRTT","avgRTT"])

					for r in self.exportData["finalStats"]:
						writer.writerow(r)
					writer.writerow(empty)

				# write the maplist
				if incMapList:
					writer.writerow(["mapList"])
					writer.writerow(["EXT_ADDR", "SADDR", "PAN ID"])
					for r in self.exportData["mapList"]:
						writer.writerow(r)

			msg = "Exported to {}".format(path)
			# self.showDialog("Saved",msg )		
			self.logCmdHistory(func_name(),msg,"info")
			self.showDialog("Export successfull", msg,"information")
		else:
			self.logCmdHistory(func_name(),"Filename not provided","error")	
			self.showDialog("Export Failed", "Filename not provided","critical")


	def saveEntries(self, filename="configPTA.csv"):
		itemCnt = 0
		rootCnt = int(self.mRootCnt)

		path, fileType = QFileDialog.getSaveFileName(QtWidgets.QWidget(), 'Save config CSV File', CONFIG_FILENAME, 'CSV(*.csv)')
		if path:
			with open(path,"w", newline='') as stream:
				writer = csv.writer(stream)
				for row in range(self.ui.tableWidget.rowCount()):
					rowdata = []
					for column in range(self.ui.tableWidget.columnCount()):

						item = self.ui.tableWidget.item(row,column)
						# print(row, column, item)
						if item is not None:
							itemCnt+=1
							rowdata.append((item.text()))
					if rowdata:
						writer.writerow(rowdata)

			msg = "Saved {} ROOT{} and {} records to {}".format(rootCnt, "s" if rootCnt>1 else "", itemCnt - rootCnt, path)
			# self.showDialog("Saved",msg )		
			self.logCmdHistory(func_name(),msg,"info")
		else:
			self.logCmdHistory(func_name(),"Filename not provided","error")	

	def loadEntries(self, filename="configPTA.csv"):
		itemCnt = 0
		rootCnt = 0
		first = 1

		path, fileType = QFileDialog.getOpenFileName(QtWidgets.QWidget(), 'Choose config CSV File', CONFIG_FILENAME, 'CSV(*.csv)')
		if path:
			with open(path,'r') as stream:
				self.ui.tableWidget.clearContents()
				self.ui.tableWidget.setRowCount(0)
				self.ui.tableWidget.setColumnCount(0)
				for rowdata in csv.reader(stream):
					item = QtWidgets.QTableWidgetItem()
					row = self.ui.tableWidget.rowCount()
					self.ui.tableWidget.insertRow(row)
					self.ui.tableWidget.setColumnCount(len(rowdata))
					self.ui.tableWidget.setVerticalHeaderItem(row, item)
					item.setText("Entry " + str(row)) if row != 0 else item.setText("Root Addr")
					for column, data in enumerate(rowdata):
						item = QtWidgets.QTableWidgetItem(data)
						# print("{}==={},{}->{}".format(data,row,column,item.text()))
						self.ui.tableWidget.setItem(row, column, item)
						itemCnt+=1
						if first:
							rootCnt+=1
					first = 0
			
			msg = "Loaded {} ROOT{} and {} items from {}".format(rootCnt, "(s)" if rootCnt>1 else "", itemCnt - rootCnt, path)
			self.ui.rootCntVal.setText(str(rootCnt))
			self.mRootCnt = str(rootCnt)
			# self.showDialog("Loaded",msg)	
			self.logCmdHistory(func_name(),msg,"info")

		
		else:
			self.logCmdHistory(func_name(),"File not selected","error")	

	def output2console(self, myApp, file="", reps=0):
		myHtml = ''
		row = 1
		if file:
			self.ui.lowerText.setHtml('')
			with open(file,'r') as stream:
				myHtml = '<table border="1" width="100%">'
		                        
				for rowdata in csv.reader(stream):
					if row < 5:
						pass
					else:
						myHtml+= "<tr>"
						for column, data in enumerate(rowdata):
							style = ' align="center" style="color:#FF0000"' if data == "-" or data =="100%" else ''
							myHtml += "<th>{}</th>".format(data) if row ==5 else "<td{}>{}</td>".format(style, data)
						myHtml+= "</tr>"

					row+=1
			myHtml += "</table>"	

			myHtml += "<br/>"
			myHtml += '<table border="1" width="100%">'
			myHtml += ''' 	<tr>
								<th colspan=16>FINAL STATISTICS</th>
							</tr>
							<tr>
								<th>TimeStamp</th>
								<th>extAddr</th>
								<th>sAddr</th>
								<th>hwType</th>
								<th>best_RF</th>
								<th>RSSI_I</th>
								<th>RSSI_M</th>
								<th>tx</th>
								<th>rx</th>
								<th>loss</th>
								<th>macTxSucc</th>
								<th>macTxFail</th>
								<th>macTxAck</th>
								<th>macTxCts</th>
								<th>macRxRts</th>
								<th>macRxAck</th>
								<th>minRTT</th>
								<th>maxRTT</th>								
								<th>avgRTT</th>
							</tr>
					'''			
			myApp.exportData["finalStats"]=[]
			for item in myApp.testNodes:
				for extAddr in item:
					# ipAddr  = item[extAddr]
					myDate = get_date()
					# params = self.add_to_output_data(extAddr,myDate, 1)
					panId = myApp.mapExt2PanId[extAddr]
					node = Node()
					if extAddr in myApp.mapList:
						sAddr  = myApp.mapList[extAddr] 
						node   = myApp.pans[panId].nodeList[sAddr]
						params = node.get_params(1)
					else:
						params = unavailable_node(extAddr, 1)
					myHtml+= "<tr>"

					params[-1] = str( round (sum( node.finalAvgRTT) / len(node.finalAvgRTT),3 ) ) if len(node.finalAvgRTT) >0 else '-'
					for col in params:
						style = ' align="center" style="color:#FF0000"' if col == "-" or col =="100%" else ''
						myHtml += "<td{}>{}</td>".format(style, col)
					myHtml+= "</tr>"
					myApp.exportData["finalStats"].append(params)

			myHtml += "</table><br/>"
					
			# print(myHtml)
			self.ui.lowerText.setHtml(myHtml)
		self.ui.lowerText.moveCursor(QtGui.QTextCursor.End)
		self.refresh()

	def enableInputs(self, enable):

		self.ui.pktSizeDial.setEnabled(enable)
		self.ui.pktCntDial.setEnabled(enable)
		self.ui.pktIntDial.setEnabled(enable)
		self.ui.pktResDial.setEnabled(enable)
		self.ui.IterVal.setEnabled(enable)
		self.ui.rootCntVal.setEnabled(enable)
		self.ui.outputToFile.setEnabled(enable)
		self.ui.showMap.setEnabled(enable)
		self.ui.tableWidget.setEnabled(enable)
		self.ui.addRowBtn.setEnabled(enable)
		self.ui.removeRowBtn.setEnabled(enable)
		self.ui.loadEntryBtn.setEnabled(enable)
		self.ui.saveEntryBtn.setEnabled(enable)
		self.ui.resetEntryBtn.setEnabled(enable)
		self.ui.startTestBtn.setEnabled(enable)

	# def enableAllInputs()

	def startTest(self):
		RUN_OK = True
		myApp = App()
		self.statusBarMsg("Test Started")
		# myApp.fileList =[]

		myApp.pktSize, myApp.pktIntv, myApp.pktResTime, myApp.pktCnt, myApp.nbrOfRoots, myApp.iteration, myApp.map, myApp.allNeighbors, myApp.outputFile, myApp.outputFilename	= self.getParams()

		# if all neighbors is checked from config is False
		if myApp.allNeighbors:
			myApp.fromConfig = False

		while 1:
			ret = self.verifyEntries(myApp)
			if ret == RET_FAIL:
				RUN_OK = False
				break;

			self.logCmdHistory(func_name(),"Test Started Successfully.","succ")
			# myApp.display()
			panCnt = 1
			for keyPanId in myApp.pans:

				pan = myApp.pans.get(keyPanId)
				
				# retrieve a dodag dump on the cam and process it
				logMsg = "Retrieving DODAG Dump for PAN {} [{}]...".format(panCnt, hex(int(keyPanId)))
				ret, output = test_ssh(pan.rootAddr ,CMD_DODAG_DUMP)
				if ret!=0:
					logMsg+="FAILED"
					# self.logCmdHistory(func_name(),"Retrieving DODAG Dump for PAN {} [{}]...FAILED".format(panCnt, hex(int(keyPanId))), "error")
					RUN_OK = False
					break
				
				ret = process_dodag_data(pan, keyPanId, output, self)
				if ret !=RET_SUCC:
					logMsg+="FAILED"
					RUN_OK = False
					break
				logMsg+="OK"
				self.logCmdHistory(func_name(),logMsg, "info")

				# retrieve neighbordump and process it
				logMsg = "Retrieving Neighbor Dump for PAN {} [{}]...".format(panCnt, hex(int(keyPanId)))
				ret, output = test_ssh(pan.rootAddr,CMD_NEIGHBOR_DUMP)
				if ret!=0:
					logMsg += "FAILED"	
					logMsg += "Unable to retrieve neighbor dump from {}".format(hex(int(keyPanId)))
					RUN_OK = False
					break
				ret = process_neighbor_data(pan, keyPanId, output, self)
				if ret == RET_FAIL:
					logMsg += "FAILED"
					RUN_OK = False
					break
				logMsg +="OK"
				self.logCmdHistory(func_name(),logMsg, "info")

				# prepare mapping between the short addr and the ext addr from dodag tree and neighbor dump
				ret = prepare_mapping(myApp, pan, keyPanId)
				if ret == RET_FAIL:
					RUN_OK = False
					break

				panCnt+=1
			# end of processing each PAN

			if not RUN_OK:	
				self.logCmdHistory(func_name(),logMsg, "error")
				break
			# prepare the test nodes	
			logMsg = "Mapping Nodes for the Test ..."
			ret = prepare_test(myApp)
			if ret == RET_FAIL:
				RUN_OK = False
				break				
			logMsg += "OK [{}/{}]".format(ret,len(myApp.testNodes))
			myApp.validNodesCnt = ret
			self.logCmdHistory(func_name(),logMsg,"info")

			# prepare the output mapping
			prepare_output_mapping(myApp)

			# if show only map show the mapstr and exit
			if myApp.map == True:
				self.ui.tabWidget.setCurrentIndex(1)
				myApp.runMap_test(self)
				self.ui.showMap.setChecked(0)
				RUN_OK = True
				break
			
			break
			# end of while loop

		# start a thread to send pings and process
		if RUN_OK == True and myApp.map == False:
			self.enableInputs(0)
			self.ui.lowerText.setHtml('')
			self.statusBarMsg("Test Running...")
			
			tot    = len(myApp.testNodes)
			total_iterations = int(myApp.iteration)
			myDate = get_date()

			self.logCmdHistory(func_name(),"<br/><b>TEST STARTED at {}<b>".format(myDate))
			self.ui.upperText.setHtml("<br/><center><b>~~~ TEST STARTED at {} ~~~<b></center>".format(myDate))
			self.ui.upperText.append(self.ui.outputCmd.toHtml())
			self.ui.tabWidget.setCurrentIndex(1)
			self.refresh()

			# progressbar initialization
			self.ui.progressBar.setMaximum(total_iterations * tot)
			self.ui.progressBar.setValue(0)
			self.ui.exportDataBtn.setEnabled(0)

			# create a thread to unfreeze the gui during pings
			self.pingThreadObj = pingThread(myApp, self.ui)
			
			self.pingThreadObj.sigDisplayMap.connect(self.slotDisplayMap)
			self.pingThreadObj.sigCopyExportData.connect(self.slotCopyExportData)
			self.pingThreadObj.sigUpperText.connect(self.slotUpperText)
			self.pingThreadObj.sigOutput2console.connect(self.output2console)
			self.pingThreadObj.sigProgressBar.connect(self.slotProgressBar)
			self.pingThreadObj.sigStatusBar.connect(self.slotStatusBar)
			self.pingThreadObj.sigDone.connect(self.slotDone)
			self.pingThreadObj.start()

		if RUN_OK == False:
			self.slotDone(RUN_OK)

	def slotProgressBar(self, val=0):
		self.ui.progressBar.setValue(val)

	def slotStatusBar(self, msg=""):
		self.ui.statusbar.showMessage(msg)

	def slotCopyExportData(self, exportData):
		self.exportData = exportData
	
	def slotDisplayMap(self, mapStr):
		# print(myApp.mapStr)
		self.ui.lowerText.append(mapStr)

	def slotUpperText(self, html, cmdType):
		cmdType = cmdType.lower()
		html+= " [" + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "]"
		
		if cmdType == "error":
			html = logErr(html)
		elif cmdType == "info":
			html = logInfo(html)
		elif cmdType == "warn":
			html = logWarn(html)
		elif cmdType == "succ":
			html = logSucc(html)
		else:
			html = logDef(html)

		self.ui.upperText.append(html)	
		
		self.refresh()

	def slotDone(self, runOk):
		"""		
		Disable Stop button, enable the Start one and reset progress bar to 0
		"""
		self.ui.upperText.append(logDef("<br/><b><center>~~~ TEST FINISHED at {} ~~~<b></center>".format(get_date()),"","#006400"))
		if(self.ui.scrollToLastOutput.checkState!=0):
			self.ui.lowerText.moveCursor(QtGui.QTextCursor.End)
		self.logCmdHistory(func_name(),"BACT Ping Test <b>{}</b>".format("SUCCESS" if runOk == True else "FAILED"), "succ" if runOk == True else "error")
		self.statusBarMsg("Test Completed")
		self.showDialog("Success","Test Success","information") if runOk == True else self.showDialog("FAILED","Test Failed. Please try again.","critical")
		self.enableInputs(1)
		self.ui.progressBar.setValue(0)
		

class pingThread(QThread):
	"""Ping Thread class to handle the ping operations """
	sigCopyExportData = pyqtSignal(dict)
	sigDisplayMap     = pyqtSignal(str)
	sigUpperText      = pyqtSignal(str, str)
	sigOutput2console = pyqtSignal(object, str, int)
	sigProgressBar    = pyqtSignal(int)
	sigStatusBar      = pyqtSignal(str)
	sigDone           = pyqtSignal(bool)
	sigRefresh        = pyqtSignal()

	def __init__(self, myApp, ui):
		super(pingThread, self).__init__()
		self.myApp = myApp
		self.ui    = ui

	def __del__(self):
		self.wait()
	
	def run(self):
		tot                 = len(self.myApp.testNodes)
		reps                = 1
		total_iterations    = int(self.myApp.iteration)
		myDate              = get_date()
		last_iteration_time = 0

		self.myApp.add_header_2_output(myDate,reps, True)
		append2csv(self.myApp.outputFilename,self.myApp.exportData["header"],"w")
		
		self.myApp.exportData["main"]=[]

		# iterate through each repetitions
		for reps in range(1,total_iterations+1):
			self.myApp.outputAppData=[]
			cnt    = 0

			if reps > 1 :
				# when higher reps, if the time between the iterations for a same node  is less than MIN_TIME_BEFORE_ITERATE, we need to sleep befre repeating the nodes
				delta = abs(last_iteration_time - datetime.today()).total_seconds()
				if delta < MIN_TIME_BEFORE_ITERATE:
					self.ui.statusbar.showMessage("Waiting for {} seconds from {} before iterating... ".format(int(MIN_TIME_BEFORE_ITERATE - delta), get_date()))
					sleep(MIN_TIME_BEFORE_ITERATE - delta)
				myDate = get_date()
				# self.myApp.add_header_2_output(myDate,reps, False)

			last_iteration_time = datetime.today()

			# iterate through each test nodes
			for item in self.myApp.testNodes:
				for extAddr in item:
					panId  = self.myApp.mapExt2PanId[extAddr]
					ipAddr = item[extAddr]
					sAddr  = self.myApp.mapList[extAddr] if ipAddr != IP_NA else IP_NA

					# update the status bar
					if ipAddr == IP_NA:
						self.sigStatusBar.emit("TEST for {}".format(extAddr))
					else:
						myNode = self.myApp.pans[panId].nodeList[sAddr]
						self.sigStatusBar.emit("Test for {} (losts {}) in [{}/{}]  ".format(extAddr, myNode.finalTx - myNode.finalRx, reps, total_iterations))
					
					retCode = RET_FAIL
					myDate = get_date()

					if ipAddr != IP_NA:
						last_mac_tx_succ, last_mac_tx_fail, last_rx_frame_kind_ack, last_rx_frame_kind_rts, last_fsm_ack_send, last_fsm_cts_send = self.myApp.get_mac_stats(extAddr)
						retCode, ret = (self.myApp.send_ping(ipAddr))
					if retCode == RET_FAIL:  
						self.sigUpperText.emit("Failed for...{} in [{}/{}]".format(extAddr,reps, total_iterations),"error")
					else:
						self.myApp.process_ping_result(extAddr, ret, last_mac_tx_succ, last_mac_tx_fail, last_rx_frame_kind_ack, last_rx_frame_kind_rts, last_fsm_ack_send, last_fsm_cts_send)
						self.myApp.get_mod_rssi(extAddr)
					
					params = self.myApp.add_to_output_data(extAddr,myDate)
					self.myApp.outputAppData.append(params)
					# self.myApp.add_to_output_str(params)
					
					cnt+=1
					self.sigProgressBar.emit(self.ui.progressBar.value() + 1)
				# end of one repetition

			# write the result to the file after each repetition
			append2csv(self.myApp.outputFilename,self.myApp.outputAppData)
			self.myApp.exportData["main"].extend(self.myApp.outputAppData)
			self.sigOutput2console.emit(self.myApp, self.myApp.outputFilename, reps)
			# end of for loop reps

		# prepare final statistics if more iterations
		if int(self.myApp.iteration) > 1:

			myDate = get_date()
			# self.myApp.add_header_2_output(myDate,int(self.myApp.iteration) +1, False)
			for item in self.myApp.testNodes:
				for extAddr in item:
					# ipAddr  = item[extAddr]
					myDate = get_date()
					params = self.myApp.add_to_output_data(extAddr,myDate, 1)
					# self.myApp.add_to_output_str(params, 1)
					
		myDate = get_date()
				
		self.ui.exportDataBtn.setEnabled(1)

		# display the mapping
		self.sigDisplayMap.emit(self.myApp.mapStr)

		# copy export data
		self.sigCopyExportData.emit(self.myApp.exportData)
		
		self.ui.tabWidget.setCurrentIndex(0)

		self.sigDone.emit(True)
		