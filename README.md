# Prankware: "Game Over" Panic Script
written in `Python` & packaged as an application with `PyInstaller`
féaux-malware for enertainment and educational purposes. 
====================================================================================
**Disclaimer:**
the author does not condone the use or the manipulation of the
information found in this repository for any illegal, immoral or
otherwise nefarious acticivity.
=======================================================================================
## Overview
A simple python APP that opens a GUI conatiner with a "click here" button. When pressed, the monitor 
screen goes black and a "GAME OVER" red font appears. The mouse and keyboaard are disabled 
and the screen remains frozen, seemingly succumbing to an offensive malicious malware attack. If applicable-
for extra anxiety-the P.C. tower beeps every 10 seconds until 2 minutes have passed. At this point the app 
container self-kills and the screen+mouse+keyboard are restored as if nothing happened. A perplexing 
finale to an otherwise startling event for anyone caught off-guard by your prank.   
#
________________________________________________________________________________________________________
#
Utilizing 'tkinter' functions, simply add 'root.after(10000, beep)'. This schedules the 'beep()' function
to be called after '10,000 milliseconds (o>seconds)' have elapsed. Similarly, when we set 'root.after(120000, root.destroy)', 
it schedules the 'root.destroy()' function (which closes the 'tkinter' window) to be called after '120,000 milliseconds 
(>2 minutes)' have elapsed. **Easily customize functions to fit your own "Game Over" malware-prank script.**
<---satanicsmores-04/25/2024-->
_________________________________________________________________________________________________________
## PyInstaller Integration
*PyInstaller: PyInstaller is a popular tool for packaging Python applications into standalone
executables. You can use PyInstaller to create an executable file (.exe on Windows, or an
equivalent binary on other platforms) that includes all the necessary Python dependencies
and resources. This is a basic example of how you might use PyInstaller to package your GTK 
application-which is already packaged in this repo.*
-----------------------------------------------------------------------------------------------------
### Generating Standalone Executable

To create a standalone executable using PyInstaller, simply run the following command:

```bash
pyinstaller --onefile game_over.py
=======
**Other than a few on-screen commands in the terminal, that's it. Windows, mac and linux 
packages from a single cmd snippet. A very usefull and powerful script.**
*<---satanicsmores-04/26/2024-->*

>>>>>>> master
