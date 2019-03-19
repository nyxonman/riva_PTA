# Riva PTA
This is a guideline documentation for a **RIVA BACT Ping Test Application**, later written as **PTA**. The main purpose of this application is to run a test on a network and compare the performance of BACT modules using IPv6 ping application.

This application is written in Python and two instances are available for Windows environment and Linux environment. The application has been so far tested for **Ubuntu 14.04 LTS Trusty Tahr** and **Windows 10** machine There are some requirements for this application to work which is detailed below.

## Network Requirements

 - A host having a IPv6 connectivity with the ROOT(s). 
	 - May be directly or via VPN.
	 - May be via global or link-local IPv6 address.
 - A host may be a LINUX machine or WINDOWs machine. 

## Application Requirements
### Linux Environment
 - **Python3+**  As the program is built in python therefore the python interpreter is necessary.  
 - **SSHPASS**  This is used to pass the password through the SSH for accessing the ROOTs.

### Windows Environment
 - **Python 3+** As the program is built in python therefore the python interpreter is necessary. It is not necessary for standalone executable
 - **Plink** if not installed previously.  Like SSHPASS in Linux, this is required to send the passcode to get access to the ROOT. Plink comes with the installation of Putty
  
 ## Installation
  ### Linux Environment
 It is quite easy to install all the requirements and the application for linux. The following steps shows how to install the dependencies of the application and the application itself.
 - Download the Installation zip file (*Installer_x_y_z.zip*). Open a Terminal and change the directory to this file.
	 ````shell
	 cd /path/to/the/directory/of/zipfile/
	 ````
 - Unzip the Installer file *Installer_x_y_z.zip*
	 ````shell
	 unzip -o Installer_x_y_z.zip
	 ````
  - You will see a list of files and then execute the install.sh file. This shell file will install all the dependencies and the application automatically.
	 ````shell
	./install.sh
	 ````
	 If you face any problem, try to change the mode of the file by running the following command.
	  ````shell
	chmod +x install.sh
	 ````
	 
 - Your Executable named ***PTA_x_y_z*** should be ready in the current folder.
##### Example: (A case when sshpass, python and PyQt5 has already been installed)
  ````shell
nikeshman@nikeshman:~$ cd Test/py_PTA/Test1/exe/1_3_4/
nikeshman@nikeshman:~/Test/py_PTA/Test1/exe/1_3_4$ ls
Installer_1_3_4.zip

nikeshman@nikeshman:~/Test/py_PTA/Test1/exe/1_3_4$ unzip -o Installer_1_3_4.zip 
Archive:  Installer_1_3_4.zip
 extracting: PTA_1_3_4.zip           
  inflating: install.sh              
  inflating: changelogs.txt          
 extracting: Version.txt             

nikeshman@nikeshman:~/Test/py_PTA/Test1/exe/1_3_4$ ./install.sh 

~~~~~ Installer v1.0 (APP v1_3_4)~~~~~

 -> SSHPASS already installed... /usr/bin/sshpass
 -> python already installed... /usr/bin/python
 -> python installer already installed... /usr/local/bin/pyinstaller
 -> python pyqt5 already installed...
.
.
.
18322 INFO: Appending archive to ELF section in EXE /home/nikeshman/Test/py_PTA/Test1/exe/1_3_4/dist/PTA_1_3_4
18375 INFO: Building EXE from out00-EXE.toc completed successfully.

 ***** The Executable PTA_1_3_4 is ready in /home/nikeshman/Test/py_PTA/Test1/exe/1_3_4
````

 ### Windows Environment
 - First, you need to install plink if it is is not already present.
	 - To check if it is present or not. Open the command interface (Win+R and type cmd and press Enter).
	 - Type cmd and Press Enter. A console will open
	 - Type plink -V 
		````
		C:\Users\nishakya>plink -V
		plink: Release 0.70
		Build platform: 64-bit Windows
		Compiler: clang 5.0.0 (http://llvm.org/git/clang.git dba970f4d143480b964f77b363ec23f22cea0390) (http://llvm.org/git/llvm.git 52ebe03cb0a728134e66d04f85281bc5a60d7091), emulating Visual Studio 2013 / MSVC++ 12.0 (_MSC_VER=1800)
		Source commit: 3cd10509a51edf5a21cdc80aabf7e6a934522d47
		````
	 - If it shows something similar like above, plink is already installed. In this case, skip the next two steps else proceed.
	 - Install putty from this [link](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html). The putty will install the plink as well.
	 - In order to use Plink, the file plink.exe will need either to be on your PATH or in your current directory. To add the directory containing Plink to your PATH environment variable, type 
*set PATH=C:\path\to\putty\directory;%PATH%* into the console window:
		````
		C:\Users\nishakya>set PATH=C:\path\to\putty\directory;%PATH%
		````

- Now you have all the pre-requisites; download the Installation zip file (*Installer_x_y_z.zip*) and goto the directory.
 - Extract the files to a folder.
 - You application is **PTA_x_y_z.exe**



## Running the tests
Once the installation is finished, goto the installation directory and open the PTA_x_y_z file. It should show a GUI. 
**Important:** Before running the application, there is one important step to take into action if you are running this with a new ROOT. For a new ROOT IPv6 address, **perform one ssh to the address from the terminal** to pass the fingerprint key word. The current version for windows does not support auto accepting the ssh keys.


### Break down into end to end tests

## Versioning

 - 1.3.4
 - 1.3.3
 - 1.3.2
 - 1.3.1
 - 1.3.0


## Authors

* **Nikesh Man Shakya** - shakya.nikeshman@itron.com



## CHANGELOGS

* cf077d8 - (HEAD -> master, origin/master, (2019-03-19 14:59:11 +0100) <Shakya> updated README
* (2019-03-18 11:24:22 +0100) <Shakya> installation steps
* (2019-03-18 10:02:07 +0100) <Shakya> auto loading of the config file if, the file is present with the default name
* (2019-03-18 09:41:20 +0100) <Shakya> space added in the log dump
* (2019-03-15 22:29:23 +0100) <Shakya> added debug mode logs
* (2019-03-15 15:02:52 +0100) <Shakya> added extra status bar update during root verification function
* (2019-03-15 14:58:32 +0100) <Shakya> fixed issue with utf decoding when working with french characters
* (2019-03-15 10:47:46 +0100) <Shakya> bugfix for interval which was enabled after performing a test
* (2019-03-13 17:49:34 +0100) <Shakya> added comment for ms waiting time and s waiting time for windows and linux resp.
* (2019-03-13 17:47:58 +0100) <Shakya> daily error logs
* (2019-03-13 17:45:06 +0100) <Shakya> packet interval disabled coz it is not supported in windows ping and not implemented for linux yet
* (2019-03-13 17:43:23 +0100) <Shakya> bugfix on windows- checkRoot reachability wait time is in ms so it is set to 2000
* (2019-03-13 17:42:26 +0100) <Shakya> Added error logging to a file
* (2019-03-13 15:45:18 +0100) <Shakya> min time before iterate changed to 30s because for supporting a case when PING is acked but ack is lost all time, we may flood it with additional pings if it is less than 30
* (2019-03-13 14:06:33 +0100) <Shakya> remove extra print
* (2019-03-13 14:03:41 +0100) <Shakya> fixed the mac tx status grep
* (2019-03-13 13:10:01 +0100) <Shakya> waiting time -w option in the ping for windows is in ms in contrast to the -W option in linux which is in sec
* (2019-03-13 11:22:33 +0100) <Shakya> Added icon to the application for both windows and linux
* (2019-03-13 10:32:16 +0100) <Shakya> loaded the last root address to the root ipv6 addr in the root tab
* (2019-03-13 10:26:19 +0100) <Shakya> combo box added for some pre listed commands in the root tab
* (2019-03-12 17:25:58 +0100) <Shakya> Added pre-listed commands for running commands
* (2019-03-12 17:15:50 +0100) <Shakya> updated changelogs
* (2019-03-12 17:13:34 +0100) <Shakya> updated readme
* (2019-03-12 16:53:14 +0100) <Shakya> icon file added for windows
* (2019-03-12 15:51:57 +0100) <Shakya> minor fixes
* (2019-03-12 15:46:13 +0100) <Shakya> added .exe file to the git ignore list
* (2019-03-12 15:45:20 +0100) <Shakya> batch file added for making exe in windows
* (2019-03-12 14:59:56 +0100) <Shakya> directed std in out and error to pipe in Popen to fix the bug for pyinstaller without console in windows
* (2019-03-12 13:58:32 +0100) <Shakya> Added extra logs in the status bar during the test.
* (2019-03-12 13:42:19 +0100) <Shakya> fixes to the status bar message
* (2019-03-12 13:30:58 +0100) <Shakya> optimized the verify root function to do multiple actions in single ssh command
* (2019-03-12 12:58:13 +0100) <Shakya> changed cat to head for reading the first line only
* (2019-03-12 10:34:54 +0100) <Shakya> added status bar update for verifying root
* (2019-03-12 10:13:18 +0100) <Shakya> changed the colorizing the filter string to have a higlight effect
* (2019-03-07 11:55:00 +0100) <Shakya> cosmetics work
* (2019-03-07 11:45:31 +0100) <Shakya> changed default packet response time to 156s
* (2019-03-06 09:43:53 +0100) <Shakya> get/set pib disabled and alligned the set value for pib and lid on the same line
* (2019-03-05 15:43:12 +0100) <Shakya> change italics to font for found pib/lid
* (2019-03-05 15:07:04 +0100) <Shakya> default tab to control
* (2019-03-05 15:03:19 +0100) <Shakya> export all pibs to csv functionality added
* (2019-03-05 14:25:44 +0100) <Shakya> append logs in root logs added
* (2019-03-05 14:15:20 +0100) <Shakya> removed cam Version dropbox and added append logs to the root tab
* (2019-03-05 14:12:41 +0100) <Shakya> support for auto cam version detection added
* (2019-03-05 14:11:46 +0100) <Shakya> removed camVersion interaction
* (2019-03-05 13:27:23 +0100) <Shakya> enter action added for the strings in root tab
* (2019-03-05 13:14:12 +0100) <Shakya> Lid search added together with pib search
* (2019-03-05 13:13:46 +0100) <Shakya> redesigned root tab
* (2019-03-05 13:13:39 +0100) <Shakya> re-designed root tab
* (2019-03-05 12:41:59 +0100) <Shakya> changed the layout and added lid search
* (2019-03-05 12:41:53 +0100) <Shakya> changed the layout and added lid search
* (2019-03-05 11:13:35 +0100) <Shakya> bugfix while formatting the search pib
* (2019-03-05 10:56:41 +0100) <Shakya> formatting for searched pib values
* (2019-03-05 09:48:52 +0100) <Shakya> searchPib functionality added
* (2019-03-04 13:34:59 +0100) <Shakya> changed the process do while 1.. break for simplicity
* (2019-03-04 13:25:47 +0100) <Shakya> renamed the pib search values and the btn
* (2019-03-04 13:25:12 +0100) <Shakya> search pib interaction created
* (2019-03-01 17:02:58 +0100) <Shakya> added status bar msg update on running commands
* (2019-03-01 16:55:10 +0100) <Shakya> buttons in root tab disabled after pressing and is turned on after task completion
* (2019-03-01 16:18:16 +0100) <Shakya> scroll to last and clear log btn added in root tab
* (2019-03-01 16:02:40 +0100) <Shakya> any error for test_ssh is send to the PIPE
* (2019-03-01 14:53:17 +0100) <Shakya> first interaction added to support the Root Tab
* (2019-03-01 14:22:18 +0100) <Shakya> new tab added for the ROOT config
* d9db85a - (origin/(2019-03-01 13:24:47 +0100) <Shakya> updated changelogs
* (2019-02-28 17:42:01 +0100) <Shakya> extra print function deleted when row is deleted
* (2019-02-27 13:49:01 +0100) <Shakya> added cam version in the output file name
* (2019-02-27 10:35:26 +0100) <Shakya> Now supports link-local address for the ROOT addresses as well
* (2019-02-21 12:48:56 +0100) <Shakya> bugfix when the mac_stats return empty string
* (2019-02-15 13:18:41 +0100) <Shakya> change logs added to readme
* (2019-02-15 13:17:22 +0100) <Shakya> added updates
*   a2488b4 - (2019-02-15 13:07:46 +0100) <Shakya> Merge branch 'master' into 1_3_3
|\  
| * (2019-02-15 10:05:37 +0100) <Shakya> removed emtpy from the last commit fix
| * (2019-02-15 10:00:15 +0100) <Shakya> fix when mac stats are empty
* | (2019-02-15 10:38:28 +0100) <Shakya> fixed adding row after the selected row
* | 1df38be - ((2019-02-15 09:49:02 +0100) <Shakya> add row at any row
* | (2019-02-14 17:39:08 +0100) <Shakya> remove button action changed to support selected row removal as well
* | (2019-02-14 17:03:22 +0100) <Shakya> new branch
|/  
* (2019-02-14 13:04:11 +0100) <Shakya> fix on stopping the thread
* (2019-02-14 12:48:54 +0100) <Shakya> pktSize Dial from 16 to 1024
* (2019-02-14 11:48:11 +0100) <Shakya> fixes to cmd to read mac status for different CAM Versions
* (2019-02-13 17:33:15 +0100) <Shakya> changed the date format to Y-m-d HH:mm:ss
* (2019-02-13 17:05:14 +0100) <Shakya> fixes to stop action
* (2019-02-13 16:36:20 +0100) <Shakya> stop button disabled at first in the UI
* (2019-02-13 16:35:32 +0100) <Shakya> stop button added in the ui
* (2019-02-13 15:05:23 +0100) <Shakya> added date at the end of test at status bar
* (2019-02-13 15:00:32 +0100) <Shakya> after finishing the test, the ui stays in the result tab
* (2019-02-13 14:58:48 +0100) <Shakya> centered the UI
*   (2019-02-13 14:34:55 +0100) <Shakya> merged fixes
|\  
| *   (2019-02-13 14:22:39 +0100) <Shakya> fixes
| |\  
| * | (2019-02-13 14:16:46 +0100) <Shakya> fixes to support CAM Versioning
| * | (2019-02-13 14:16:31 +0100) <Shakya> removed importing constant.py as it is imported from other files
| * | (2019-02-13 13:14:45 +0100) <Shakya> cam versioning
| * | (2019-02-12 13:35:51 +0100) <Shakya> interaction with the CAM version dropbox
| * | (2019-02-12 12:40:56 +0100) <Shakya> CAM Version added to the UI
| * | (2019-02-12 10:31:01 +0100) <Shakya> min ping payload changed to 16
| * | (2019-02-12 10:28:24 +0100) <Shakya> changed min size in the dial to be 16 because below 16 bytes payload, ping application does not return the RTTs
| * | (2019-02-11 18:00:18 +0100) <Shakya> submission
| * | (2019-02-11 17:57:11 +0100) <Shakya> added pktsize and iteration to the file name while exporting
| * | (2019-02-11 17:47:25 +0100) <Shakya> bugfix on output stat
| * | (2019-02-11 17:39:19 +0100) <Shakya> fixed bug in the header output for extra mac stats
| * | (2019-02-11 17:30:25 +0100) <Shakya> minor
| * | (2019-02-11 17:28:55 +0100) <Shakya> removed redundant macTx succ calculation in the final
| * | (2019-02-11 17:23:03 +0100) <Shakya> changes to adapt rts, cts and ack counts
| * | (2019-02-11 16:12:02 +0100) <Shakya> indentation error
| * | (2019-02-11 16:09:47 +0100) <Shakya> updated get_params to include extra mac stats
| * | (2019-02-11 16:02:59 +0100) <Shakya> added functionality for rts, cts and acks stats
| * | (2019-02-11 15:22:58 +0100) <Shakya> added rts, cts and ack counts
| * | (2019-01-24 16:29:34 +0100) <Shakya> Packet Size text edit added to be variable value between MIN_PING_PAYLOAD and MAX_PING_PAYLOAD
| * | (2019-01-24 16:27:35 +0100) <Shakya> MIN_PING_PAYLOAD added to constants
| * | (2019-01-24 16:26:49 +0100) <Shakya> MAX_PING_PAYLOAD constant defined
| * | (2019-01-24 13:20:35 +0100) <Shakya> changed min time before iterate to 12
* | | (2019-02-13 14:29:25 +0100) <Shakya> merged fix
* | | (2019-02-13 14:25:17 +0100) <Shakya> merged fix
| |/  
|/|   
* | (2019-01-25 10:03:17 +0100) <Shakya> merged fixes
* | (2019-01-25 10:02:22 +0100) <Shakya> merged changes for pktsize value from 1_3_1
|/  
* (2019-01-16 13:33:48 +0100) <Shakya> changes to prepare_test for mapping and pinging all neighbors option
* (2019-01-16 13:23:16 +0100) <Shakya> changed the variable from allmap to all neighbors
* (2019-01-16 13:10:29 +0100) <Shakya> updated createCMDStr function to show/hide for all neighbors
* (2019-01-16 13:05:45 +0100) <Shakya> re-positioned and renamed the show all neighbors
* (2019-01-16 13:02:38 +0100) <Shakya> make up work
*   (2019-01-16 13:00:44 +0100) <Shakya> Merge branch 'master' of https://github.com/nyxonman/riva_PTA
|\  
| * f622ddc - (9 weeks ago) (2019-01-16 12:49:02 +0100) <nyxonman> Delete Version.txt
* | (2019-01-16 12:50:57 +0100) <Shakya> remove Version.txt
* | (2019-01-16 12:46:36 +0100) <Shakya> Added Version.txt to the ignore list
|/  
* (2019-01-16 11:38:38 +0100) <Shakya> Adjusted the export function to handle various options from the GUI
* (2019-01-16 11:25:54 +0100) <Shakya> Added extra options(header, data, finalstat,map) on the export file
* (2019-01-16 11:19:19 +0100) <Shakya> Added ping test info when exporting
* (2019-01-16 10:27:08 +0100) <Shakya> added headers to the map and final statistics when exporting the data
* e2b8594 - (2019-01-15 13:26:14 +0100) <Shakya> interact with show all map option
* (2019-01-15 13:17:48 +0100) <Shakya> Added all mapping option to the GUI
* (2019-01-15 13:09:32 +0100) <Shakya> Header size reduced to 120
* (2019-01-15 13:08:15 +0100) <Shakya> changed to 130
* (2019-01-15 13:04:08 +0100) <Shakya> added __pycache__ folder to the ignore list
* (2019-01-15 12:59:08 +0100) <Shakya> Version updated to 1.3.1 added alternate colors to the table and float to right
* (2019-01-15 12:57:07 +0100) <Shakya> added *.pyc temp files to the gitignore
* (2019-01-15 12:44:22 +0100) <Shakya> Added date to the end of the filename
* (2019-01-15 11:50:10 +0100) <Shakya> added *.json file to gitignore
* (2019-01-15 11:47:29 +0100) <Shakya> Version updated to 1.3.1
* eeda12b - (origin/(2019-01-15 11:29:41 +0100) <Shakya> revereted back
* (2019-01-15 11:20:48 +0100) <Shakya> test on new branch
* (2019-01-15 11:08:41 +0100) <Shakya> Initial commits
* (2019-01-15 11:07:13 +0100) <Shakya> reversed to previous version in the text
* (2019-01-15 11:06:17 +0100) <Shakya> changed version
* (2019-01-15 11:04:03 +0100) <Shakya> added .gitignore and Version.txt
* 25dba95 - (origin/PTA_1_3_0) (6 months ago) (2018-10-03 13:53:29 +0200) <nyxonman> Initial commit
