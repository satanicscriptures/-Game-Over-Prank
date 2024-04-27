>>>>>>> master
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
container self-kills and the screen+mouse+keyboard are restored as if nothing happened. A perplexing ## PyInstaller Integration

`PyInstaller` is a popular tool for packaging Python applications into standalone executables. With PyInstaller, you can create a single executable 
file (.exe on Windows, or an equivalent binary on other platforms) that includes all the necessary Python dependencies and resources. This repository
includes a basic example of how you can use PyInstaller to package your Python script.

### Generating Standalone Executable

To create a standalone executable using PyInstaller, simply run the following command:

```bash
pyinstaller --onefile game_over.py



