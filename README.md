# riva_PTA

*   a2488b4 - (HEAD -> master, origin/master, origin/HEAD, 1_3_3) (9 minutes ago) (2019-02-15 13:07:46 +0100) <Shakya> Merge branch 'master' into 1_3_3
|\  
| * 55a9c74 - (3 hours ago) (2019-02-15 10:05:37 +0100) <Shakya> removed emtpy from the last commit fix
| * 847cb6c - (3 hours ago) (2019-02-15 10:00:15 +0100) <Shakya> fix when mac stats are empty
* | 22cd535 - (3 hours ago) (2019-02-15 10:38:28 +0100) <Shakya> fixed adding row after the selected row
* | 1df38be - (origin/1_3_3) (3 hours ago) (2019-02-15 09:49:02 +0100) <Shakya> add row at any row
* | 38cdd57 - (20 hours ago) (2019-02-14 17:39:08 +0100) <Shakya> remove button action changed to support selected row removal as well
* | 9cc1a91 - (20 hours ago) (2019-02-14 17:03:22 +0100) <Shakya> new branch
|/  
* 84eb236 - (24 hours ago) (2019-02-14 13:04:11 +0100) <Shakya> fix on stopping the thread
* 7bf85ac - (24 hours ago) (2019-02-14 12:48:54 +0100) <Shakya> pktSize Dial from 16 to 1024
* 4b2fb70 - (25 hours ago) (2019-02-14 11:48:11 +0100) <Shakya> fixes to cmd to read mac status for different CAM Versions
* da294a1 - (2 days ago) (2019-02-13 17:33:15 +0100) <Shakya> changed the date format to Y-m-d HH:mm:ss
* e4785a8 - (2 days ago) (2019-02-13 17:05:14 +0100) <Shakya> fixes to stop action
* 268c649 - (2 days ago) (2019-02-13 16:36:20 +0100) <Shakya> stop button disabled at first in the UI
* cc20ca6 - (2 days ago) (2019-02-13 16:35:32 +0100) <Shakya> stop button added in the ui
* a76cb8d - (2 days ago) (2019-02-13 15:05:23 +0100) <Shakya> added date at the end of test at status bar
* 2c68d63 - (2 days ago) (2019-02-13 15:00:32 +0100) <Shakya> after finishing the test, the ui stays in the result tab
* 88a77a8 - (2 days ago) (2019-02-13 14:58:48 +0100) <Shakya> centered the UI
*   cb55615 - (2 days ago) (2019-02-13 14:34:55 +0100) <Shakya> merged fixes
|\  
| *   b26fa41 - (origin/1_3_1, 1_3_1) (2 days ago) (2019-02-13 14:22:39 +0100) <Shakya> fixes
| |\  
| * | 5b803d0 - (2 days ago) (2019-02-13 14:16:46 +0100) <Shakya> fixes to support CAM Versioning
| * | 0384ae4 - (2 days ago) (2019-02-13 14:16:31 +0100) <Shakya> removed importing constant.py as it is imported from other files
| * | 579477c - (2 days ago) (2019-02-13 13:14:45 +0100) <Shakya> cam versioning
| * | 3472f2d - (3 days ago) (2019-02-12 13:35:51 +0100) <Shakya> interaction with the CAM version dropbox
| * | c22540b - (3 days ago) (2019-02-12 12:40:56 +0100) <Shakya> CAM Version added to the UI
| * | a67ceb7 - (3 days ago) (2019-02-12 10:31:01 +0100) <Shakya> min ping payload changed to 16
| * | e80ca76 - (3 days ago) (2019-02-12 10:28:24 +0100) <Shakya> changed min size in the dial to be 16 because below 16 bytes payload, ping application does not return the RTTs
| * | 516f66a - (4 days ago) (2019-02-11 18:00:18 +0100) <Shakya> submission
| * | e1f7f25 - (4 days ago) (2019-02-11 17:57:11 +0100) <Shakya> added pktsize and iteration to the file name while exporting
| * | c2fdcb9 - (4 days ago) (2019-02-11 17:47:25 +0100) <Shakya> bugfix on output stat
| * | d767d03 - (4 days ago) (2019-02-11 17:39:19 +0100) <Shakya> fixed bug in the header output for extra mac stats
| * | bdf8486 - (4 days ago) (2019-02-11 17:30:25 +0100) <Shakya> minor
| * | bf5944c - (4 days ago) (2019-02-11 17:28:55 +0100) <Shakya> removed redundant macTx succ calculation in the final
| * | 414e67f - (4 days ago) (2019-02-11 17:23:03 +0100) <Shakya> changes to adapt rts, cts and ack counts
| * | 3c53140 - (4 days ago) (2019-02-11 16:12:02 +0100) <Shakya> indentation error
| * | 089e6e1 - (4 days ago) (2019-02-11 16:09:47 +0100) <Shakya> updated get_params to include extra mac stats
| * | 282e0bd - (4 days ago) (2019-02-11 16:02:59 +0100) <Shakya> added functionality for rts, cts and acks stats
| * | db00ba8 - (4 days ago) (2019-02-11 15:22:58 +0100) <Shakya> added rts, cts and ack counts
| * | c9f119d - (3 weeks ago) (2019-01-24 16:29:34 +0100) <Shakya> Packet Size text edit added to be variable value between MIN_PING_PAYLOAD and MAX_PING_PAYLOAD
| * | 0a85aaf - (3 weeks ago) (2019-01-24 16:27:35 +0100) <Shakya> MIN_PING_PAYLOAD added to constants
| * | 047253f - (3 weeks ago) (2019-01-24 16:26:49 +0100) <Shakya> MAX_PING_PAYLOAD constant defined
| * | a4d2301 - (3 weeks ago) (2019-01-24 13:20:35 +0100) <Shakya> changed min time before iterate to 12
* | | 592a475 - (2 days ago) (2019-02-13 14:29:25 +0100) <Shakya> merged fix
* | | 92641d0 - (2 days ago) (2019-02-13 14:25:17 +0100) <Shakya> merged fix
| |/  
|/|   
* | df665ea - (3 weeks ago) (2019-01-25 10:03:17 +0100) <Shakya> merged fixes
* | 3587812 - (3 weeks ago) (2019-01-25 10:02:22 +0100) <Shakya> merged changes for pktsize value from 1_3_1
|/  
* e85d37d - (4 weeks ago) (2019-01-16 13:33:48 +0100) <Shakya> changes to prepare_test for mapping and pinging all neighbors option
* d995380 - (4 weeks ago) (2019-01-16 13:23:16 +0100) <Shakya> changed the variable from allmap to all neighbors
* 45a7ced - (4 weeks ago) (2019-01-16 13:10:29 +0100) <Shakya> updated createCMDStr function to show/hide for all neighbors
* b5586a9 - (4 weeks ago) (2019-01-16 13:05:45 +0100) <Shakya> re-positioned and renamed the show all neighbors
* c66377a - (4 weeks ago) (2019-01-16 13:02:38 +0100) <Shakya> make up work
*   144c220 - (4 weeks ago) (2019-01-16 13:00:44 +0100) <Shakya> Merge branch 'master' of https://github.com/nyxonman/riva_PTA
|\  
| * f622ddc - (4 weeks ago) (2019-01-16 12:49:02 +0100) <nyxonman> Delete Version.txt
* | 7391015 - (4 weeks ago) (2019-01-16 12:50:57 +0100) <Shakya> remove Version.txt
* | ce58da5 - (4 weeks ago) (2019-01-16 12:46:36 +0100) <Shakya> Added Version.txt to the ignore list
|/  
* 6483a25 - (4 weeks ago) (2019-01-16 11:38:38 +0100) <Shakya> Adjusted the export function to handle various options from the GUI
* 99c5d5a - (4 weeks ago) (2019-01-16 11:25:54 +0100) <Shakya> Added extra options(header, data, finalstat,map) on the export file
* c13db79 - (4 weeks ago) (2019-01-16 11:19:19 +0100) <Shakya> Added ping test info when exporting
* 0a53c2f - (4 weeks ago) (2019-01-16 10:27:08 +0100) <Shakya> added headers to the map and final statistics when exporting the data
* e2b8594 - (list) (4 weeks ago) (2019-01-15 13:26:14 +0100) <Shakya> interact with show all map option
* 836f8bf - (4 weeks ago) (2019-01-15 13:17:48 +0100) <Shakya> Added all mapping option to the GUI
* eccdcf7 - (4 weeks ago) (2019-01-15 13:09:32 +0100) <Shakya> Header size reduced to 120
* 1f6c706 - (4 weeks ago) (2019-01-15 13:08:15 +0100) <Shakya> changed to 130
* 6c0baaf - (4 weeks ago) (2019-01-15 13:04:08 +0100) <Shakya> added __pycache__ folder to the ignore list
* efb0bc8 - (4 weeks ago) (2019-01-15 12:59:08 +0100) <Shakya> Version updated to 1.3.1 added alternate colors to the table and float to right
* a7f71fb - (4 weeks ago) (2019-01-15 12:57:07 +0100) <Shakya> added *.pyc temp files to the gitignore
* 46b7862 - (4 weeks ago) (2019-01-15 12:44:22 +0100) <Shakya> Added date to the end of the filename
* e8ea70f - (4 weeks ago) (2019-01-15 11:50:10 +0100) <Shakya> added *.json file to gitignore
* 462e2dc - (4 weeks ago) (2019-01-15 11:47:29 +0100) <Shakya> Version updated to 1.3.1
* eeda12b - (origin/1_3_0, 1_3_0) (4 weeks ago) (2019-01-15 11:29:41 +0100) <Shakya> revereted back
* a8399a6 - (4 weeks ago) (2019-01-15 11:20:48 +0100) <Shakya> test on new branch
* 4ba45af - (4 weeks ago) (2019-01-15 11:08:41 +0100) <Shakya> Initial commits
* 406296b - (4 weeks ago) (2019-01-15 11:07:13 +0100) <Shakya> reversed to previous version in the text
* e726ba2 - (4 weeks ago) (2019-01-15 11:06:17 +0100) <Shakya> changed version
* 5f24271 - (4 weeks ago) (2019-01-15 11:04:03 +0100) <Shakya> added .gitignore and Version.txt
* 25dba95 - (origin/PTA_1_3_0) (5 months ago) (2018-10-03 13:53:29 +0200) <nyxonman> Initial commit