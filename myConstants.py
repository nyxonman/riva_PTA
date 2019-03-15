import inspect # for function name
import os
from datetime import datetime
import pprint

# list of global variables subject to change
glob={}

OS_POSIX   = "posix"
OS_WIN     = "nt"
glob["DEBUG_MODE"] = False
logMsg     = ""

__VERSION__        = "1.3.4"
APP_VERSION        = __VERSION__ +" {OS: " + os.name + "} (debug)" if glob["DEBUG_MODE"] == True else __VERSION__ +" {OS: " + os.name + "}"

glob["CAM_VERSION"] = 3
DFT_PKT_CNT         = "1"
DFT_PKT_INTV        = "180"
DFT_PKT_SIZE        = "64"
DFT_ITERATION       = "2"
DFT_PKT_RESP_TIME   = "156"
DFT_ROOTS_CNT       = "1"
BACT_TIME_SLOT      = 6
CONFIG_FILENAME     = "configPTA.csv"
DFT_OUTPUTFILENAME  = "testlog_"+str(datetime.now().strftime('%d_%m_%Y'))+".csv"

RET_SUCC = 0
RET_FAIL = -1

ADD_ROW = 1
DEL_ROW = -1

MIN_TIME_BEFORE_ITERATE = 30
MAX_PING_PAYLOAD        = 1024
MIN_PING_PAYLOAD        = 16

NEIGHBOR_DUMP  = 1
DODAG_DUMP     = 2
BPD_HW_TYPE_ID = 2

# commands to run with ssh
CMD_ROOT_VERSION  = "head -1 /etc/Version.txt"
CMD_PIB_TABLE     = "cat /etc/pib_table.csv"
CMD_NEIGHBOR_DUMP = "neighbor-dump -t0"
CMD_DODAG_DUMP    = "cat /proc/net/ipv6_dodag"
# CMD_MAC_TX_STAT   = 'pib -gln /mas/statistics/f2_txmgr |grep "DataConfirmSuccess\|DataConfirmFailure"'
glob["CMD_MAC_TX_STAT"]   = 'pib -gln /mas/statistics/f2_txmgr |grep "DataConfirmSuccess\|DataConfirmFailure" && pib -gln /rf_mac/statistics/chan_mgr |grep "rx_frame_kind_rts\|fsm_cts_send\|rx_frame_kind_ack\|fsm_ack_send"'

glob["CMD_GET_PANID"]   = "pib -gn /rf_mac/dynamic_config/f0_MAC_IDs/macSrcPANid" if glob["CAM_VERSION"] == 1 else "pib -gn /rf_mac/dynamic_config/mac_mgr/macPANID"
CMD_RPL_STATUS    = "pib -gn /mas/status/f0_core/NetRegisteredFlag"


RPL_STATUS_SYNC = "SYCnEt"
IP_NA           = "N/A"

# pings
if os.name == OS_POSIX:
	PING_CMD       = 'ping6'
	PING_CMD_XTRA  = ''
	PING_CNT       = '-c'
	PING_SIZE      = '-s'
	PING_INTV      = '-i'
	PING_RESP_TIME = '-W'

	CLEAR_CMD = 'clear'
	

elif os.name == OS_WIN:
	PING_CMD       = 'ping'
	PING_CMD_XTRA  = '-6'
	PING_CNT       = '-n'
	PING_SIZE      = '-l'
	PING_INTV      = '-i' # OS_WIN does not support this
	PING_RESP_TIME = '-w'

	CLEAR_CMD = 'cls'


CHECKBOX_STATE_CHECKED   = 2
CHECKBOX_STATE_UNCHECKED = 0

def set_debug_mode(mode):
	glob["DEBUG_MODE"] = mode

def set_cam_version(version):
	glob["CAM_VERSION"]     = int(version)
	glob["CMD_GET_PANID"]   = "pib -gn /rf_mac/dynamic_config/f0_MAC_IDs/macSrcPANid" if glob["CAM_VERSION"] == 1 else "pib -gn /rf_mac/dynamic_config/mac_mgr/macPANID"
	glob["CMD_MAC_TX_STAT"] = "pib -gn /mas/statistics/f2_txmgr/DataConfirmSuccess;pib -gn /mas/statistics/f2_txmgr/DataConfirmFailure;pib -gn /rf_mac/statistics/f1_ChannelAccessDataExchange/RTSRxForMeCnt3;pib -gn /rf_mac/statistics/f1_ChannelAccessDataExchange/CTSsentCnt32;pib -gn /rf_mac/statistics/f1_ChannelAccessDataExchange/ACKrxForMeCnt32;pib -gn /rf_mac/statistics/f1_ChannelAccessDataExchange/ACKsentCnt32" if glob["CAM_VERSION"] == 1 else "pib -gn /mas/statistics/f2_txmgr/DataConfirmSuccess;pib -gn /mas/statistics/f2_txmgr/DataConfirmFailure;pib -gn /rf_mac/statistics/chan_mgr/rx_frame_kind_rts;pib -gn /rf_mac/statistics/chan_mgr/fsm_cts_send;pib -gn /rf_mac/statistics/chan_mgr/rx_frame_kind_ack;pib -gn /rf_mac/statistics/chan_mgr/fsm_ack_send"

def func_name():
    return "["+inspect.stack()[1][3]+"] " if glob["DEBUG_MODE"] == True else ""

last_fin  = '\n'
last_func = ''

def MYPRINT(type, func, str,fin='\n'):
	global last_fin
	global last_func
	if last_fin=='' and last_func == func:
		print(" {}".format(str),end = fin)
	else:
		print(" {}: [{}] - {}".format(type, func, str),end = fin)
	last_fin = fin
	last_func = func

def LOGE(func, str, fin='\n'):
	MYPRINT("ERR", func, "{}".format(str), fin)

def LOGW(func, str, fin='\n'):
	MYPRINT("WAR", func, "{}".format(str), fin)

def LOGI(func, str, fin='\n'):
	MYPRINT("INF", func, "{}".format(str), fin)
