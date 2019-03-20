# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:51:10 2018

@author: nishakya
"""
import subprocess
import socket
import csv
from pathlib import Path
from sys import stdout
from time import sleep

from myConstants import *
# from myClass import *

def logInfo(myLog, funcName="", plainText=False):

    if funcName:
        myLog = "{}".format(funcName) + myLog
    myLog = '<span style="color:#0000FF;">INFO: ' + myLog + '</span>' if not plainText else 'INFO: ' + myLog
    return myLog

def logWarn(myLog, funcName="", plainText=False):
    if funcName:
        myLog = "{}".format(funcName) + myLog
    myLog = '<span style="color:#FF8C00;">WARN: ' + myLog + '</span>' if not plainText else 'WARN: ' + myLog
    return myLog

def logErr(myLog, funcName="", plainText=False):
    if funcName:
        myLog = "{}".format(funcName) + myLog
    myLog = '<span style="color:#FF0000;">ERROR: ' + myLog + '</span>' if not plainText else 'ERROR: ' + myLog
    return myLog

def logSucc(myLog, funcName="", plainText=False):
    if funcName:
        myLog = "{}".format(funcName) + myLog
    myLog = '<span style="color:#006400;">SUCC: ' + myLog + '</span>' if not plainText else 'SUCC: ' + myLog
    return myLog

def logDef(myLog, funcName="", myColor='#000000'):
    if funcName:
        myLog = "{}".format(funcName) + myLog
    myLog = '<span style="color:'+myColor+';">' + myLog + '</span>' 
    return myLog

def get_date():
    'get current date in a particular format'
    # return (datetime.now().strftime('%d %b %Y %H:%M:%S'))
    return (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def get_current_path():
    '''get the current path'''
    return os.getcwd()

def test_ssh(host, command):
    '''Runs a command on a remote node by passing the password depending upon the OS'''
    HOST    = "root@"+host
    COMMAND = command
    PWD     = "itron"
    
    # show the command running in debug mode
    if glob["DEBUG_MODE"]:
        logDump(func_name(),"COMMAND-> {} in {}\n\r".format(COMMAND, HOST))

    # run ssh or plink depending upon the os
    if os.name == OS_POSIX:
        p1 = subprocess.Popen(['sshpass','-p', PWD, 'ssh', "-o StrictHostKeyChecking=no" ,"-o LogLevel=ERROR", "-o UserKnownHostsFile=/dev/null", HOST,COMMAND], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        # plink -v youruser@yourhost.com -pw yourpw "some linux command"
        p1 = subprocess.Popen(['plink',"-pw", PWD, HOST,COMMAND], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell= True, close_fds=True)

    raw_output,err = p1.communicate()
    
    if p1.returncode != RET_SUCC : 
        logDump(func_name(), str_decode(raw_output), str_decode(err))       
        return p1.returncode,str(err.decode('utf-8', 'ignore')).strip()
        # return p1.returncode,"ERR: Error while running the command '{}' to host {}".format(command, HOST)
    # print(raw_output.decode())
    if glob["DEBUG_MODE"]:
        logDump(func_name(), str_decode(raw_output), str_decode(err))

    return p1.returncode,str(raw_output.decode('utf-8', 'ignore')).strip()

def name2cmd(cmdName=""):
    '''converts a name to the respective command for the Root tab'''

    cmdName = cmdName.lower()
    if cmdName == "modversion":
        return "modversion.sh"
    elif cmdName == "ngcstatus":
        return "ngcstatus.sh"
    elif cmdName == "neighbor-dump t0":
        return "neighbor-dump -t0 -l3"
    elif cmdName == "neighbor-dump t1":
        return "neighbor-dump -t1 -l3"
    elif cmdName == "neighbor-dump t7":
        return "neighbor-dump -t7"
    elif cmdName == "dodag table":
        return "cat /proc/net/ipv6_dodag"

def getLidValue(root, filterStr=""):
    '''Fetch the LID value from root using ssh'''
    lidCmd = ""
    lidCmd = "LoadMonitorInit --verify | grep -i {}".format(filterStr)
    retCode, output = test_ssh(root, lidCmd)
    return retCode, output

def getPibValue(root, filterStr="", pibLayer="All", pibType="All", identifier=""):
    '''Fetch the PIB value from the root'''
    pibCmd = ""
    # print(root, filterStr, pibLayer, pibType, identifier)
    if pibLayer == "All":
        # (pib -gln rf_mac | grep -i pan) && (pib -gln rf_phy |grep -i pan) && (pib -gln mas |grep -i pan)
        pibCmd += "(pib -gln rf_phy | grep -i {}".format(filterStr) + ") ; "
        pibCmd += "(pib -gln rf_mac | grep -i {}".format(filterStr) + ") ; "
        pibCmd += "(pib -gln mas | grep -i {}".format(filterStr) + ")"
    else:
        pibCmd += "pib -gln {} | grep -i {}".format(pibLayer, filterStr)

    retCode, output = test_ssh(root, pibCmd)
    return retCode, output

def checkRootReachability(ipv6Addr):
    '''check the reachability of the Root by sending a small packet of size 8B'''

    if os.name == OS_WIN:
        p1 = subprocess.Popen([PING_CMD, PING_CMD_XTRA, PING_CNT,'1',PING_SIZE,'8', PING_RESP_TIME, '2000',ipv6Addr], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, close_fds=True)
    else:
        p1 = subprocess.Popen([PING_CMD, PING_CNT,'1',PING_SIZE,'8', PING_RESP_TIME, '2',ipv6Addr],stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    raw_output,err = p1.communicate()
    # print(raw_output)
    
    if p1.returncode !=0:
        logDump(func_name(), str_decode(raw_output), str_decode(err))
        return RET_FAIL

    if glob["DEBUG_MODE"]:
        logDump(func_name(), str_decode(raw_output), str_decode(err))
 
    return RET_SUCC

def display_console_str(myApp):
    print(myApp.outputStr)

def str_decode(data, encoding='utf-8', error='ignore'):
    '''Decodes and return the string using the encoding and error type'''
    return str(data.decode(encoding, error)) if data else ""

def logDump(funcName="", rawOuputStr="", rawErrStr=""):
    '''To dump the log into the file. Helpful for debugging'''
    filename = "dumpLog_" + str(get_date().split(' ')[0]) + ".log"
    if rawErrStr or rawOuputStr:
        fd = open(filename,"a")
        if rawOuputStr:
            rawOuputStr = str(get_date()) + " " + funcName +" [O/P]-\n\r" + rawOuputStr 
            fd.writelines(rawOuputStr)
        if rawErrStr:
            rawErrStr = str(get_date())+ " " + funcName +" [ERR]-\n\r" + rawErrStr 
            fd.writelines(rawErrStr)
        fd.close()

#creates a dummy configPTA.csv if it does not exists
def create_dummy_config():
    output = []
    output.append(["pktSize","pktCnt","pktInt","pktResp","Iteration","nbrRoot"])
    output.append([DFT_PKT_SIZE, DFT_PKT_CNT, DFT_PKT_INTV, DFT_PKT_RESP_TIME, DFT_ITERATION, "2"])
    output.append([])
    output.append(["eeee::1","cccc::1"])
    output.append(["0007814700bc0192"," 0007814700bc0193"])
    output.append(["0007814700bc0194"," 0007814700bc0195"])
    output.append([]);
    
    write2csv(CONFIG_FILENAME,output);
    

def conv_ipv6(ipAddr):
    '''Takes the string full ip address notation, verifies it and then return it in printable format
        Return: err, ipAddr
    '''
    err = RET_SUCC
    try:
        myIp   = socket.inet_pton(socket.AF_INET6, ipAddr.strip())        
        ipAddr = socket.inet_ntop(socket.AF_INET6, myIp)
    except:
        err=RET_FAIL
        LOGE(func_name(),"invalid ipAddr {}".format(ipAddr))
        
    return err, ipAddr

def verifyRootAddr(rootIpv6Addr, interactGuiObj):
    '''Verify if the rootIPv6Addr is valid and reachable and collects the version, sync status, pan id.'''
    retMsg       = ""    
    retMsg       = "Verifying ROOT {}".format(rootIpv6Addr)
    interface    = ""
    rootIpv6Addr = rootIpv6Addr.strip()

    if "%" in rootIpv6Addr:
        rootIpv6Addr, interface = rootIpv6Addr.split('%')
        retMsg += " (link-local)..."
    else:
        retMsg += " (global)..."

    # check IPv6 Addr validity
    try:            
        socket.inet_pton(socket.AF_INET6, rootIpv6Addr.strip())
    except :  # not a valid address
        retMsg += "FAILED. '{}' is NOT a valid IPv6 Address".format(rootIpv6Addr)
        return RET_FAIL, RET_FAIL, retMsg
    retMsg += "VALID..."
    interactGuiObj.statusBarMsg(retMsg)

    rootIpv6Addr = rootIpv6Addr if not interface else rootIpv6Addr + '%' + interface
    # check the reachability of the root
    if checkRootReachability(rootIpv6Addr) == RET_FAIL:

        retMsg += "FAILED<br>"
        retMsg +=  " ERR:'{}' is UNREACHABLE.".format(rootIpv6Addr)
        retMsg +=  " If you are using link-local address, please mention the interface as well."
        retMsg +=  " Example: fe80::207:81ff:feff:cc01%eth1"

        return RET_FAIL, RET_FAIL, retMsg
    retMsg += "REACHABLE..."
    interactGuiObj.statusBarMsg(retMsg)

    # check between CAM3 and CAM1 or PIM or ACT ROOT
    ret, output = test_ssh(rootIpv6Addr,CMD_ROOT_VERSION)    
    if ret != RET_SUCC:
        retMsg +="FAILED. Cannot retrieve Version of Root {}".format(rootIpv6Addr)
        return RET_FAIL, RET_FAIL, retMsg
    
    rootVersion = 3 if "CAM3" in output else 1
    set_cam_version(rootVersion)

    retMsg += "CAM{}...".format(rootVersion)
    interactGuiObj.statusBarMsg(retMsg)

    mergedCmd = CMD_RPL_STATUS+";"+glob["CMD_GET_PANID"]

    # check if root is SYCnEt or not and retrieve panID
    ret, output = test_ssh(rootIpv6Addr,mergedCmd)
    # print(ret, output)
    if ret != RET_SUCC:
        retMsg +="FAILED. Cannot retrieve RPL-Status and/or PAN ID of Root {}".format(rootIpv6Addr)
        return RET_FAIL, RET_FAIL, retMsg
    splitted = output.splitlines()

    rplStat = int(splitted[0])
    if rplStat != 1:
        retMsg +="FAILED. ROOT not SYCnEt Yet. Please wait until Root is RUNNING"
        return RET_FAIL, RET_FAIL, retMsg
    retMsg += "SYCnEt..."
    interactGuiObj.statusBarMsg(retMsg)
    
    panId = str(int(splitted[1],16))
    retMsg += "0x{}...".format(splitted[1])
    stdout.flush()    
    retMsg += "OK"
    interactGuiObj.statusBarMsg(retMsg)

    # panId = str(int("597b",16)) if rootIpv6Addr=="eeee::1" else str(int("47de",16))
    return rootVersion, panId, retMsg

def process_dodag_data(pan, panId, data, interactGuiObj):
    '''Process the DODAG data'''
    prefix   = ""
    nodesCnt = 0
    retMsg   = "" 
    lines    = data.splitlines()
    # pprint(lines)
    if len(lines) <3:
        retMsg+="Cannot retrieve DODAG Table for 0x{:x}.".format(panId)
        interactGuiObj.logCmdHistory(func_name(),retMsg, "error")
        return RET_FAIL
    
    # extract prefix, len, nodes from the first line
    words    = lines[0].split()
    prefix   = words[2][0:34]
    prefixLen = int(words[4])
    nodesCnt = int(words[7]) - 1

    if nodesCnt <1:
        retMsg+="DODAG Table Empty. Exiting.."
        interactGuiObj.logCmdHistory(func_name(),retMsg, "error")
        return RET_FAIL
    
    pan.prefix = prefix
    pan.nodes  = nodesCnt
    pan.prefixLen = prefixLen

    for line in lines:
        words = line.split()
        try:
            int(words[0],16)            
        except:
            continue

        pan.add_node("-",words[0], words[1])

    return RET_SUCC

def process_neighbor_data(pan, panId, data, interactGuiObj):
    '''Process the neighbor-table data'''
    skipHeaderCnt=9
    retMsg = ""
    lines = data.splitlines()
    # pprint(lines)
    if len(lines) <3:
        retMsg += "FAILED."
        retMsg += " Cannot get neighbor table. Please check the connectivity."
        interactGuiObj.logCmdHistory(func_name(),retMsg, "error")

        return RET_FAIL

    # extract prefix, len, nodes from the first line
    for line in lines[skipHeaderCnt:]:
        
        words = line.split()
        try:
            int(words[0],16)            
        except:
            continue        
        
        sAddr, extAddr, hwType = words[0:3]
        best_rf=words[6]
        rssi_m,rssi_i = words[7:9]
        pan.add_node(extAddr, sAddr, hwType, best_rf, rssi_i, rssi_m)

    return RET_SUCC
        
def prepare_test(myApp):
    '''Prepare the sorted list of the nodes'''
    validNodesCnt = 0

    # if all neighbors is not checked
    if myApp.fromConfig == True:
        for extAddr in myApp.fileList:
            # item = myApp.fileList[key]
            panId = myApp.mapExt2PanId[extAddr]
            if extAddr in myApp.mapList :
                ipAddr      = myApp.pans[panId].prefix[0:34]+":"+myApp.mapList[extAddr]
                err, ipAddr = conv_ipv6(ipAddr)
                if err == RET_FAIL:
                    return RET_FAIL
                validNodesCnt+=1
            else:
                ipAddr = IP_NA
            myApp.add_test_node(extAddr, ipAddr)

    else:
        for keyPanId in myApp.pans:
            panObj   = myApp.pans.get(keyPanId)
            nodeList = panObj.nodeList
            for keyNode in nodeList:
                nodeObj     = nodeList[keyNode]
                extAddr     = nodeObj.extAddr
                sAddr       = nodeObj.sAddr
                ipAddr      = panObj.prefix[0:34]+":"+sAddr
                err, ipAddr = conv_ipv6(ipAddr)
                if err == RET_FAIL:
                    return RET_FAIL
                myApp.add_test_node(extAddr, ipAddr)
                validNodesCnt+=1
    # print("{} = {}".format(extAddr,sAddr))
    # myApp.display_test_nodes()

    return validNodesCnt

def prepare_mapping(myApp, pan, panId):
    nodeList = pan.nodeList

    for keyNode in nodeList:
        nodeObj                             = nodeList[keyNode]
        myApp.mapList[nodeObj.extAddr]      = nodeObj.sAddr   
        myApp.mapExt2PanId[nodeObj.extAddr] = panId

    return RET_SUCC

def prepare_output_mapping(myApp):
    '''Prepare output mapping table'''

    myApp.mapStr = "<br/>"
    myApp.mapStr += ''' <table border="1" width="100%">
                        <tr>
                            <th colspan="4">MAP LIST</th>
                        </tr>
                        <tr>
                            <th>EXT_ADDR</th>
                            <th>SADDR</th>
                            <th>PAN ID</th>
                            <th>Prefix</th>
                        </tr>
                    '''
    for item in myApp.testNodes:
        for extAddr in item:
            ipAddr       = item.get(extAddr)
            panId        = myApp.mapExt2PanId[extAddr]
            sAddr        = ipAddr.split(":")[-1]
            dump, prefix = conv_ipv6(myApp.pans[panId].prefix + ":0000")
            prefixLen = myApp.pans[panId].prefixLen
            # myApp.mapStr += myApp.disp_line(" ","{:<18s} | {:>04s} | {:<6s}".format(extAddr,sAddr,hex(int(panId))) , 0 , length) + "\n"
            style = ' style="color:#FF0000"' if ipAddr == IP_NA else ""
            myApp.mapStr += '<tr{}><td>{}</td><td>{}</td><td>{}</td><td>{} /{}</td></tr>'.format(style, extAddr,sAddr,hex(int(panId)), prefix, prefixLen)
            params = [extAddr, sAddr, hex(int(panId)), prefix +" /" + str(prefixLen)]
            myApp.exportData["mapList"].append(params)
    myApp.mapStr += "<table>"

    return RET_SUCC   

def unavailable_node(extAddr, final):
    # date, "extAddr", "sAddr", "hwType", "best_RF", "RSSI_I", "RSSI_M", "tx", "time", "rx", "macTxSucc", "macTxFail", "loss", "minRTT", "maxRTT", "mdevRTT", "avgRTT", "finalTx", "finalRx", "finalMacTxSucc", "finalMacTxFail", "finalLoss", "finalMinRTT", "finalMaxRTT", "finalAvgRTT"
    if final == 0:
        return ["", extAddr, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    else:
        return ["", extAddr, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

def process_ping_output(output, retCode):
    '''Process the ping output results to get the necessary counters and RTT values'''

    lines=output.splitlines()  
    
    # process tx, rx, loss and time
    if os.name == OS_POSIX:
        output_stat = lines[-2]
        splitted = output_stat.split()
        tx,rx, loss, time = int(splitted[0]),int(splitted[3]), splitted[5], (splitted[9])
    else:
        if retCode == 1:
            output_stat = str(lines[-1])
        else:
            output_stat = str(lines[-3])
        # splitted = re.split(' |, |(', output_stat)
        output_stat = output_stat.replace( "(",' ' ).replace(","," ")
        splitted = output_stat.split()
        tx,rx, time, loss = int(splitted[3]), int(splitted[6]), "", splitted[10] 
        
    
    # process minRTT, avgRTT, maxRTT, mdevRTT
    # there is a blank line in the RTT info line if ping was not received i.e. with p1.returcode 1
    if (retCode!=1):
        # pprint(lines)
        output_time = lines[-1]
        if os.name == OS_POSIX:
            splitted = output_time.split()
            splitted = splitted[3].split('/')
            minRTT, avgRTT, maxRTT, mdevRTT = float(splitted[0]), float(splitted[1]), float(splitted[2]), float(splitted[3])
        else:
            output_time = output_time.replace("ms","").replace(",","")
            splitted = output_time.split()
            minRTT, avgRTT, maxRTT, mdevRTT = float(splitted[2]), float(splitted[8]), float(splitted[5]), float(0)
        
        ret = [tx, rx, loss, time, minRTT, avgRTT, maxRTT, mdevRTT]
    else:
        ret = [tx, rx, loss, time, '-', '-', '-', '-']
    return ret


def write2csv(csvfile = "testlog.csv", res=""):
    '''write res to the csv file'''

    with open(csvfile, "w", newline='') as output:
        writer = csv.writer(output)
        for r in res:
            writer.writerow(r)

def append2csv(csvfile = "app_testlog.csv", res="", mode="a"):
    '''append to the csv file'''

    with open(csvfile, mode, newline='') as output:
        writer = csv.writer(output)
        for r in res:
            writer.writerow(r)

