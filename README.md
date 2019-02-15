# riva_PTA

# CHANGELOGS

(9 minutes ago) (2019-02-15 13:07:46 +0100) <Shakya> Merge branch 'master' into 1_3_3
|\  
(3 hours ago) (2019-02-15 10:05:37 +0100) <Shakya> removed emtpy from the last commit fix
(3 hours ago) (2019-02-15 10:00:15 +0100) <Shakya> fix when mac stats are empty
(3 hours ago) (2019-02-15 10:38:28 +0100) <Shakya> fixed adding row after the selected row
(3 hours ago) (2019-02-15 09:49:02 +0100) <Shakya> add row at any row
(20 hours ago) (2019-02-14 17:39:08 +0100) <Shakya> remove button action changed to support selected row removal as well
(20 hours ago) (2019-02-14 17:03:22 +0100) <Shakya> new branch
|/  
(24 hours ago) (2019-02-14 13:04:11 +0100) <Shakya> fix on stopping the thread
(24 hours ago) (2019-02-14 12:48:54 +0100) <Shakya> pktSize Dial from 16 to 1024
(25 hours ago) (2019-02-14 11:48:11 +0100) <Shakya> fixes to cmd to read mac status for different CAM Versions
(2 days ago) (2019-02-13 17:33:15 +0100) <Shakya> changed the date format to Y-m-d HH:mm:ss
(2 days ago) (2019-02-13 17:05:14 +0100) <Shakya> fixes to stop action
(2 days ago) (2019-02-13 16:36:20 +0100) <Shakya> stop button disabled at first in the UI
(2 days ago) (2019-02-13 16:35:32 +0100) <Shakya> stop button added in the ui
(2 days ago) (2019-02-13 15:05:23 +0100) <Shakya> added date at the end of test at status bar
(2 days ago) (2019-02-13 15:00:32 +0100) <Shakya> after finishing the test, the ui stays in the result tab
(2 days ago) (2019-02-13 14:58:48 +0100) <Shakya> centered the UI
(2 days ago) (2019-02-13 14:34:55 +0100) <Shakya> merged fixes
|\  
(2 days ago) (2019-02-13 14:22:39 +0100) <Shakya> fixes
| |\  
(2 days ago) (2019-02-13 14:16:46 +0100) <Shakya> fixes to support CAM Versioning
(2 days ago) (2019-02-13 14:16:31 +0100) <Shakya> removed importing constant.py as it is imported from other files
(2 days ago) (2019-02-13 13:14:45 +0100) <Shakya> cam versioning
(3 days ago) (2019-02-12 13:35:51 +0100) <Shakya> interaction with the CAM version dropbox
(3 days ago) (2019-02-12 12:40:56 +0100) <Shakya> CAM Version added to the UI
(3 days ago) (2019-02-12 10:31:01 +0100) <Shakya> min ping payload changed to 16
(3 days ago) (2019-02-12 10:28:24 +0100) <Shakya> changed min size in the dial to be 16 because below 16 bytes payload, ping application does not return the RTTs
(4 days ago) (2019-02-11 18:00:18 +0100) <Shakya> submission
(4 days ago) (2019-02-11 17:57:11 +0100) <Shakya> added pktsize and iteration to the file name while exporting
(4 days ago) (2019-02-11 17:47:25 +0100) <Shakya> bugfix on output stat
(4 days ago) (2019-02-11 17:39:19 +0100) <Shakya> fixed bug in the header output for extra mac stats
(4 days ago) (2019-02-11 17:30:25 +0100) <Shakya> minor
(4 days ago) (2019-02-11 17:28:55 +0100) <Shakya> removed redundant macTx succ calculation in the final
(4 days ago) (2019-02-11 17:23:03 +0100) <Shakya> changes to adapt rts, cts and ack counts
(4 days ago) (2019-02-11 16:12:02 +0100) <Shakya> indentation error
(4 days ago) (2019-02-11 16:09:47 +0100) <Shakya> updated get_params to include extra mac stats
(4 days ago) (2019-02-11 16:02:59 +0100) <Shakya> added functionality for rts, cts and acks stats
(4 days ago) (2019-02-11 15:22:58 +0100) <Shakya> added rts, cts and ack counts
(3 weeks ago) (2019-01-24 16:29:34 +0100) <Shakya> Packet Size text edit added to be variable value between MIN_PING_PAYLOAD and MAX_PING_PAYLOAD
(3 weeks ago) (2019-01-24 16:27:35 +0100) <Shakya> MIN_PING_PAYLOAD added to constants
(3 weeks ago) (2019-01-24 16:26:49 +0100) <Shakya> MAX_PING_PAYLOAD constant defined
(3 weeks ago) (2019-01-24 13:20:35 +0100) <Shakya> changed min time before iterate to 12
(2 days ago) (2019-02-13 14:29:25 +0100) <Shakya> merged fix
(2 days ago) (2019-02-13 14:25:17 +0100) <Shakya> merged fix
| |/  
|/|   
(3 weeks ago) (2019-01-25 10:03:17 +0100) <Shakya> merged fixes
(3 weeks ago) (2019-01-25 10:02:22 +0100) <Shakya> merged changes for pktsize value from 1_3_1
|/  
(4 weeks ago) (2019-01-16 13:33:48 +0100) <Shakya> changes to prepare_test for mapping and pinging all neighbors option
(4 weeks ago) (2019-01-16 13:23:16 +0100) <Shakya> changed the variable from allmap to all neighbors
(4 weeks ago) (2019-01-16 13:10:29 +0100) <Shakya> updated createCMDStr function to show/hide for all neighbors
(4 weeks ago) (2019-01-16 13:05:45 +0100) <Shakya> re-positioned and renamed the show all neighbors
(4 weeks ago) (2019-01-16 13:02:38 +0100) <Shakya> make up work
(4 weeks ago) (2019-01-16 13:00:44 +0100) <Shakya> Merge branch 'master' of https://github.com/nyxonman/riva_PTA
|\  
| * f622ddc - (4 weeks ago) (2019-01-16 12:49:02 +0100) <nyxonman> Delete Version.txt
(4 weeks ago) (2019-01-16 12:50:57 +0100) <Shakya> remove Version.txt
(4 weeks ago) (2019-01-16 12:46:36 +0100) <Shakya> Added Version.txt to the ignore list
|/  
(4 weeks ago) (2019-01-16 11:38:38 +0100) <Shakya> Adjusted the export function to handle various options from the GUI
(4 weeks ago) (2019-01-16 11:25:54 +0100) <Shakya> Added extra options(header, data, finalstat,map) on the export file
(4 weeks ago) (2019-01-16 11:19:19 +0100) <Shakya> Added ping test info when exporting
(4 weeks ago) (2019-01-16 10:27:08 +0100) <Shakya> added headers to the map and final statistics when exporting the data
(4 weeks ago) (2019-01-15 13:26:14 +0100) <Shakya> interact with show all map option
(4 weeks ago) (2019-01-15 13:17:48 +0100) <Shakya> Added all mapping option to the GUI
(4 weeks ago) (2019-01-15 13:09:32 +0100) <Shakya> Header size reduced to 120
(4 weeks ago) (2019-01-15 13:08:15 +0100) <Shakya> changed to 130
(4 weeks ago) (2019-01-15 13:04:08 +0100) <Shakya> added __pycache__ folder to the ignore list
(4 weeks ago) (2019-01-15 12:59:08 +0100) <Shakya> Version updated to 1.3.1 added alternate colors to the table and float to right
(4 weeks ago) (2019-01-15 12:57:07 +0100) <Shakya> added *.pyc temp files to the gitignore
(4 weeks ago) (2019-01-15 12:44:22 +0100) <Shakya> Added date to the end of the filename
(4 weeks ago) (2019-01-15 11:50:10 +0100) <Shakya> added *.json file to gitignore
(4 weeks ago) (2019-01-15 11:47:29 +0100) <Shakya> Version updated to 1.3.1
(4 weeks ago) (2019-01-15 11:29:41 +0100) <Shakya> revereted back
(4 weeks ago) (2019-01-15 11:20:48 +0100) <Shakya> test on new branch
(4 weeks ago) (2019-01-15 11:08:41 +0100) <Shakya> Initial commits
(4 weeks ago) (2019-01-15 11:07:13 +0100) <Shakya> reversed to previous version in the text
(4 weeks ago) (2019-01-15 11:06:17 +0100) <Shakya> changed version
(4 weeks ago) (2019-01-15 11:04:03 +0100) <Shakya> added .gitignore and Version.txt
* 25dba95 - (origin/PTA_1_3_0) (5 months ago) (2018-10-03 13:53:29 +0200) <nyxonman> Initial commit