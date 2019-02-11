from PyQt5 import QtGui
from myConstants import *
from myFunctions import *

class App():

	def __init__(self) :
		self.nbrOfRoots     = 1
		self.pktCnt         = str(DFT_PKT_CNT)
		self.hwAddr         = "-"
		self.file           = ""
		self.pktIntv        = str(DFT_PKT_INTV)
		self.map            = False
		self.allNeighbors         = False
		self.outputFile     = False
		self.outputFilename = "last_testlog.csv"
		self.iteration      = str(DFT_ITERATION)
		self.pktSize        = str(DFT_PKT_SIZE)
		self.pktResTime     = str(DFT_PKT_RESP_TIME)
		self.version        = APP_VERSION
		self.help           = False
		self.testNodes      = []
		self.mapStr         = ""
		self.pans           = {}
		self.fromConfig     = True
		self.mapExt2PanId   = {}
		self.fileList       = []
		self.mapList        = {}
		self.validNodesCnt  = 0
		self.outputData     = []
		self.outputAppData  = []
		self.outputStr      = ""
		self.losts          = 0
		self.exportData = {"header":[], "main":[],"finalStats":[],"mapList":[]}

	def runMap_test(self, interactGuiObj):

		interactGuiObj.ui.upperText.setHtml(interactGuiObj.ui.outputCmd.toHtml())
		interactGuiObj.ui.lowerText.setHtml(self.mapStr)
		interactGuiObj.refresh()

	def display(self):
		print("nbrOfRoots = {}".format(self.nbrOfRoots),end='\t')
		print("pktCnt = {}".format(self.pktCnt))
		print("pktSize = {}".format(self.pktSize),end='\t')
		print("pktIntv = {}".format(self.pktIntv))
		print("pktResTime = {}".format(self.pktResTime),end='\t')
		print("iteration = {}".format(self.iteration))
		print("hwAddr = {}".format(self.hwAddr),end='\t')
		print("map = {}".format(self.map))
		print("outputFile = {}".format(self.outputFile),end='\t')
		print("outputFilename = {}".format(self.outputFilename))
		print("fromConfig = {}".format(self.fromConfig))
		print("fileList = ")
		print (self.fileList)
		print ('----------------------------------------')
		for keyPanId in self.pans:
			pan = self.pans.get(keyPanId)
			print(keyPanId+" "+str(type(pan)))
			pan.display()
			print
		print ('----------------------------------------')
		self.display_test_nodes()        


	def add_test_node(self,extAddr,ipAddr):
		self.testNodes.append({extAddr:ipAddr})

	def display_test_nodes(self):
		print(self.testNodes)

	def process_ping_result(self,extAddr, output, last_mac_tx_succ, last_mac_tx_fail, last_rx_frame_kind_ack, last_rx_frame_kind_rts, last_fsm_ack_send, last_fsm_cts_send):
		panId  = self.mapExt2PanId[extAddr]
		sAddr  = self.mapList[extAddr]
		myNode = self.pans[panId].nodeList[sAddr]
		myNode.tx, myNode.rx, myNode.loss, myNode.time, myNode.minRTT, myNode.avgRTT, myNode.maxRTT, myNode.mdevRTT = output
		mac_tx_succ, mac_tx_fail, rx_frame_kind_ack, rx_frame_kind_rts, fsm_ack_send, fsm_cts_send = self.get_mac_stats(extAddr)
					
		myNode.macTxSucc = mac_tx_succ - last_mac_tx_succ
		myNode.macTxFail = mac_tx_fail - last_mac_tx_fail
		myNode.macRxAck  = rx_frame_kind_ack - last_rx_frame_kind_ack
		myNode.macRxRts  = rx_frame_kind_rts - last_rx_frame_kind_rts
		myNode.macTxAck  = fsm_ack_send - last_fsm_ack_send
		myNode.macTxCts  = fsm_cts_send - last_fsm_cts_send

		
		# final values
		myNode.finalTx        += myNode.tx
		myNode.finalRx        += myNode.rx
		myNode.finalMacTxSucc += myNode.macTxSucc
		myNode.finalMacTxFail += myNode.macTxFail
		myNode.finalMacTxSucc      += myNode.macTxSucc
		myNode.finalMacTxFail      += myNode.macTxFail
		myNode.finalMacTxAck       += myNode.macTxAck
		myNode.finalMacTxCts       += myNode.macTxCts
		myNode.finalMacRxRts       += myNode.macRxRts
		myNode.finalMacRxAck       += myNode.macRxAck
		myNode.finalLoss      = str( round(100 - myNode.finalRx/myNode.finalTx *100)) +'%'
		self.losts            += myNode.tx - myNode.rx #for display
		if not isinstance(myNode.minRTT, str):
			myNode.finalMinRTT    = myNode.minRTT if myNode.minRTT < myNode.finalMinRTT else myNode.finalMinRTT
			myNode.finalMaxRTT    = myNode.maxRTT if myNode.maxRTT > myNode.finalMaxRTT else myNode.finalMaxRTT
			myNode.finalAvgRTT.append(myNode.avgRTT)
	
	def get_mod_rssi(self, extAddr):
		found = False
		panId = self.mapExt2PanId[extAddr]
		pan   = self.pans[panId]
		
		ret, output = test_ssh(pan.rootAddr,CMD_NEIGHBOR_DUMP)
		if ret!=0:
			print("FAILED")
			LOGE(func_name(),"Unable to retrieve neighbor dump from {}. Probably lost connection with the ROOT {}.".format(hex(int(keyPanId)), pan.rootAddr))
			exit()
		
		skipHeaderCnt=9
		lines = output.splitlines()
		if len(lines) <3:
			print ("ERR: cannot get neighbor table. Pleas check the connectivity")
			return RET_FAIL

		for line in lines[skipHeaderCnt:]:
			
			words =  line.split()
			try:
				int(words[0],16)            
			except:
				continue    
			
			if extAddr != words[1]:
				continue
			else:
				found = True
				sAddr = words[0]
				# update
				pan.nodeList[sAddr].best_rf = words[6]
				pan.nodeList[sAddr].RSSI_M  = words[7]
				pan.nodeList[sAddr].RSSI_I  = words[8]
				break

		if found == False:
			LOGE(func_name(),"Cannot find {} in neighbor table. May be this neighbor is removed".format(sAddr))
			return RET_FAIL
		
		return RET_SUCC
	
	def add_to_output_str(self, params, final=0):
		if final == 0 :
			myDate, extAddr, sAddr, hwType, best_RF, RSSI_I, RSSI_M, tx, rx, macTxSucc, macTxFail, loss, minRTT, maxRTT, mdevRTT, avgRTT = params
			self.outputStr += "  {:16s} | {:4s} | {:4s} | {:4s} | {:11s} | {:11s} | {:11s} | {:8s} | {:8s} | {:10s} |".format(extAddr, tx, rx, loss, minRTT, maxRTT, avgRTT, RSSI_I, RSSI_M, best_RF) + '\n'

		else:
			myDate, extAddr, sAddr, hwType, best_RF, RSSI_I, RSSI_M, finalTx, finalRx, finalMacTxSucc, finalMacTxFail, finalLoss, finalMinRTT, finalMaxRTT, finalAvgRTT = params

			self.outputStr += "  {:16s} | {:4s} | {:4s} | {:4s} | {:11s} | {:11s} | {:11s} | {:8s} | {:8s} | {:10s} |".format(extAddr, finalTx, finalRx, finalLoss, finalMinRTT, finalMaxRTT, finalAvgRTT, RSSI_I, RSSI_M, best_RF) + '\n'
		

	def add_to_output_data(self, extAddr, myDate, final=0):

		panId = self.mapExt2PanId[extAddr]
		node = Node()
		if extAddr in self.mapList:
			sAddr  = self.mapList[extAddr] 
			node   = self.pans[panId].nodeList[sAddr]
			params = node.get_params(final)
		else:
			params = unavailable_node(extAddr, final)
		# update the date with the timestamp of the test started on the node if it is not the final result
		if final == 0:
			params[0] = myDate
		else:
			# update the average final avg RTT
			# print(node.finalAvgRTT)
			# print(params[-1])
			params[-1] = str( round (sum( node.finalAvgRTT) / len(node.finalAvgRTT),3 ) ) if len(node.finalAvgRTT) >0 else '-'
			# params[-1] = str( round (float(params[-1]) / int(self.iteration),3 ) ) if params[-1] != '-' else params[-1]

		self.outputData.append(params)
		return params

	
	def get_mac_stats(self, extAddr):
		panId           = self.mapExt2PanId[extAddr]
		pan             = self.pans[panId]
		retCode, output = test_ssh(pan.rootAddr,CMD_MAC_TX_STAT)

		if retCode!=0:
			LOGE(func_name(),"Unable to retrieve MAC TX Stats from {}. Probably lost connection with the ROOT {}.".format(hex(int(panId)),pan.rootAddr))
			print("")
			print("")
			exit()
		lines       = output.splitlines()
		print(output)
		# DataConfirmSuccess
		splitted    = lines[0].split('=')
		mac_tx_succ = int(splitted[1].strip(), 16)
		# DataConfirmFailure
		splitted    = lines[1].split('=')
		mac_tx_fail = int(splitted[1].strip(), 16)
		# rx_frame_kind_ack
		splitted    = lines[2].split('=')
		rx_frame_kind_ack = int(splitted[1].strip(), 16)
		# rx_frame_kind_rts
		splitted    = lines[3].split('=')
		rx_frame_kind_rts = int(splitted[1].strip(), 16)
		# fsm_ack_send
		splitted    = lines[5].split('=')
		fsm_ack_send = int(splitted[1].strip(), 16)
		# fsm_cts_send
		splitted    = lines[6].split('=')
		fsm_cts_send = int(splitted[1].strip(), 16)

		# return mac_tx_succ,mac_tx_fail
		return mac_tx_succ, mac_tx_fail, rx_frame_kind_ack, rx_frame_kind_rts, fsm_ack_send, fsm_cts_send

	def add_map_2_output_data(self):
		self.outputData.append([])
		self.outputData.append(["~~~","MAP_LIST", "~~~"])
		self.outputData.append(["EXT_ADDR", "SADDR", "PAN ID", "PREFIX"])
		
		for item in self.testNodes:
			for extAddr in item:
				ipAddr = item[extAddr]
				panId  = self.mapExt2PanId[extAddr]
				prefix = self.pans[panId].prefix
				sAddr  = IP_NA if ipAddr == IP_NA else self.mapList[extAddr]
				self.outputData.append([extAddr, sAddr, (hex(int(panId))), prefix])

	def add_header_2_output(self, myDate, reps, first = False):
		# for file
		if first == True:
			self.exportData["header"] = []
			self.exportData["header"].append(["PTA",self.version,"REPETITIONS", self.iteration, "RESULT STATS", "Date",myDate])
			self.exportData["header"].append(["pktSize","pktCnt","pktInt","pktResp", "Iteration", "Nodes"])
			self.exportData["header"].append([self.pktSize, self.pktCnt, self.pktIntv, self.pktResTime, self.iteration, "{}/{}".format(self.validNodesCnt, len(self.testNodes))])
			self.exportData["header"].append([])
			self.exportData["header"].append(["TimeStamp","extAddr", "sAddr", "hwType", "best_RF", "RSSI_I", "RSSI_M", "tx", "rx", "macTxSucc", "macTxFail", "loss", "minRTT", "maxRTT", "mdevRTT", "avgRTT"])
			
			
	def verifyInputParams(self):
		errMsg  = ""
		infoMsg = ""
		print("\t - Verifying Input Params...",end='\r')

		# packet count
		if (not self.pktCnt.isdigit()) or int(self.pktCnt)<1:
			errMsg+="\t- Packet count should be a numeric value and greater than 0. '{}' provided.\n".format(self.pktCnt)
		# pkt size
		if (not self.pktSize.isdigit()) or int(self.pktSize) < 16:
			errMsg+="\t- Packet Size should be a numeric value and at least 16 Bytes. '{}' provided.\n".format(self.pktSize)
		# pkt interval
		if (not self.pktIntv.isdigit()) or int(self.pktIntv) < 2*BACT_TIME_SLOT:
			errMsg+="\t- Packet Interval should be a numeric value and at least twice the time slot {}sec. Safer to have at least {}sec. '{}' provided.\n".format(BACT_TIME_SLOT, DFT_PKT_INTV, self.pktSize)
		# pkt response
		if (not self.pktResTime.isdigit()) or int(self.pktResTime) < 2*BACT_TIME_SLOT:
			errMsg+="\t- Packet Response Time should be a numeric value and at least twice the time slot {}sec. Safer to have at least {}sec. '{}' provided.\n".format(BACT_TIME_SLOT, DFT_PKT_RESP_TIME, self.pktResTime)
		# test iterations
		if (not self.iteration.isdigit()) or int(self.iteration) < 1:
			errMsg+="\t- Test Iteration should be a numeric value and greater than 1. '{}' provided.\n".format(self.iteration)  
		# nbr of roots
		if (not self.nbrOfRoots.isdigit()) or int(self.nbrOfRoots) < 1:
			errMsg+="\t- nbr of roots should be a numeric value and greater than 0. '{}' provided.\n".format(self.nbrOfRoots) 
		# check the file name
		if (self.outputFile == True):
			self.outputFilename = self.outputFilename.strip()
			if len(self.outputFilename) < 1  :
				errMsg+="\t- Outfile Name is '{}'. Please provide a filename.\n".format(self.outputFilename)
			self.outputFilename = self.outputFilename.split('.')[0] + '.csv'

		if len(errMsg) >0:      
			print("\t - Verifying Input Params... FAILED")
			print("\n\tERR: " + errMsg)
			print("\tINFO: " + infoMsg)
			return RET_FAIL
		else:
			print("\t - Verifying Input Params... OK")
			return RET_SUCC

	def send_ping(self,addr):
		ret = []        
		# addr = "172.18.200.27"
		p1 = subprocess.Popen([PING_CMD,PING_SIZE, self.pktSize, PING_CNT, self.pktCnt, PING_INTV, self.pktIntv, PING_RESP_TIME, self.pktResTime, addr],stdout=subprocess.PIPE)
		raw_output,err = p1.communicate()
		
		# 0 is success 1 is success with 0 received
		if p1.returncode != 0 and p1.returncode !=1:
			return RET_FAIL, ret

		# proces the ping result to provide an array at the end
		output = str(raw_output.decode())  
		ret = process_ping_output(output,p1.returncode)   

		return RET_SUCC, ret
	
	def disp_line(self, char, word="", printOut=1,length=WIN_LEN,  allign="center"):
	
		retStr = ""
		cnt    = len(word)
		if cnt%2!=0:
			cnt  += 1
			word += " "
		length = round((length-cnt)/2)
		if cnt==0:
			retStr = "  {}{}".format(char*(length+1), char*(length+1))
		else:
			length -= 1
			retStr = "  |{} {} {}|".format(char*length, word, char*length)

		if printOut == 0:
			return retStr
		else:   
			print (retStr)
			return
	
			
class Node() :
	def __init__(self, extAddr="", sAddr="", hwType=0, best_RF='-', RSSI_I='-',RSSI_M='-'):
		self.timeStamp      = get_date()
		self.extAddr        = extAddr
		self.sAddr          = sAddr
		self.hwType         = hwType
		self.best_RF        = best_RF
		self.RSSI_I         = RSSI_I
		self.RSSI_M         = RSSI_M
		self.tx             = 0
		self.rx             = 0
		self.loss           = 0
		self.macTxSucc      = 0
		self.macTxFail      = 0
		self.macTxAck       = 0
		self.macTxCts       = 0
		self.macRxRts       = 0
		self.macRxAck       = 0
		self.minRTT         = 86400000
		self.maxRTT         = 0
		self.mdevRTT        = 0
		self.avgRTT         = 0
		self.finalTx        = 0
		self.finalRx        = 0
		self.finalLoss      = 0
		self.finalMacTxSucc = 0
		self.finalMacTxFail = 0
		self.finalMacTxAck  = 0
		self.finalMacTxCts  = 0
		self.finalMacRxRts  = 0
		self.finalMacRxAck  = 0
		self.finalMinRTT    = 86400000
		self.finalMaxRTT    = 0
		self.finalAvgRTT    = []
		self.time           = 0

		# change in get_params,add_header_2_output, unavailable node

	def get_params(self, final):

 		if final==0:
			return [str(self.timeStamp), str(self.extAddr), str(self.sAddr), str(self.hwType), str(self.best_RF), str(self.RSSI_I), str(self.RSSI_M), str(self.tx), str(self.rx), str(self.loss), str(self.macTxSucc), str(self.macTxFail), str(self.macTxAck), str(self.macTxCts), str(self.macRxRts), str(self.macRxAck), str(self.minRTT), str(self.maxRTT), str(self.mdevRTT), str(self. avgRTT)]
		else:
			return [str(self.timeStamp), str(self.extAddr), str(self.sAddr), str(self.hwType), str(self.best_RF), str(self.RSSI_I), str(self.RSSI_M), str(self.finalTx), str(self.finalRx), str(self.finalLoss), str(self.finalMacTxSucc), str(self.finalMacTxFail), str(self.finalMacTxAck), str(self.finalMacTxCts), str(self.finalMacRxRts), str(self.finalMacRxAck), str(self.finalMinRTT), str(self.finalMaxRTT), str(self.finalAvgRTT)]


	def ping_stat(self, tx, rx, loss, minRTT, maxRTT, avgRTT):
		self.tx          = tx
		self.rx          = rx
		self.loss        = loss
		self.minRTT      = minRTT
		self.maxRTT      = maxRTT
		self.avgRTT      = avgRTT
		
		self.finalTx     +=tx
		self.finalRx     +=rx
		self.finalLoss   = self.finalRx/self.finalTx
		self.finalMinRTT = self.finalMinRTT if self.finalMinRTT < minRTT else minRTT
		self.finalMaxRTT = self.finalMaxRTT if self.finalMaxRTT > maxRTT else maxRTT
		self.finalAvgRTT.append(avgRTT)

class Pan():
	def __init__(self, prefix="", length="", nodes="", saddr="", rootAddr=""):
		self.rootAddr = rootAddr
		self.prefix   = prefix
		self.length   = length
		self.nodes    = nodes
		self.sAddr    = saddr
		self.nodeList = {}

	def add_node(self, extAddr, sAddr, hwType, best_RF='-', RSSI_I='-',RSSI_M='-' ):
		# self, extAddr, sAddr, hwType, best_RF='-', RSSI_I='-',RSSI_M='-'
		self.nodeList[sAddr] = Node(extAddr, sAddr, hwType, best_RF, RSSI_I, RSSI_M)

	def display(self):
		print ("prefix:{}".format(self.prefix))
		print ("len:{}".format(self.length))
		print ("sAddr:{}".format(self.sAddr))
		print ("Nodes:{}".format(self.nodes))
		print ("Ipv6Addr:{}".format(self.rootAddr))

		print 
		# print ("hwType:{}".format(self.hwType))
		for node in self.nodeList:
			print("\t\t" +node+" "+str(type(self.nodeList)))
			pprint(vars(self.nodeList.get(node)))
			print

