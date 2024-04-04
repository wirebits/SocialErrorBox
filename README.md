# SocialErrorBox
A tool which generates error message boxes for social engineering and fun

# Key Features
- Simple and clean GUI.<br>
- Two large windows one for mnemonics and other for VB Script.<br>
- Convert Button - Convert mnemonics to VB scripts.<br>
- Reset Button - Clear all data from both windows.<br>
- Save Button - Save VB scripts on the system for future use.<br>
- Exit Button - Close the application.<br>

# OS Support
Windows

# Setup
Make sure the latest python and pip3 is installed on your system (Windows/Linux/MacOS).<br>

# Mnemonic Table
<table>
 <tr>
  <th>Mnemonics</th>
  <th>Description</th>
  <th>Example</th>
 </tr>
 <tr>
  <th>TITLE</th>
  <th>It add title of the box.</th>
  <th>TITLE python</th>
 </tr>
  <tr>
  <th>MSG</th>
  <th>It add text in the box.</th>
  <th>MSG This is a python script</th>
 </tr>
  <tr>
  <th>BUTTON</th>
  <th>It add button in the box.</th>
  <th>BUTTON 0</th>
 </tr>
 <tr>
  <th>ICON</th>
  <th>It add icon of the box.</th>
  <th>ICON 0</th>
 </tr>
  <tr>
  <th>VAR</th>
  <th>It add variable where box code is stored.</th>
  <th>VAR code TITLE python MSG This is a python script BUTTON 0 ICON 0</th>
 </tr>
  <tr>
  <th>INF</th>
  <th>It run the box infinitely.</th>
  <th>INF VAR code TITLE python MSG This is a python script BUTTON 0 ICON 0</th>
 </tr>
 <tr>
  <th>REDO</th>
  <th>It run the box for a number of times.</th>
  <th>REDO 5 VAR code TITLE python MSG This is a python script BUTTON 0 ICON 0</th>
 </tr>
 <tr>
  <th>SET</th>
  <th>It add the variable for the run of other commands.</th>
  <th>SET game</th>
 </tr>
 <tr>
  <th>RUN</th>
  <th>It run the box and its hidden command.</th>
  <th>RUN game code python Test.py</th>
 </tr>
</table>

# Buttons and Icon

<table>
 <tr>
  <th>Button Input</th>
  <th>Button Output</th>
 </tr>
 <tr>
  <th>0</th>
  <th>OK Button</th>
 </tr>
  <tr>
  <th>1</th>
  <th>OK and Cancel Buttons</th>
 </tr>
  <tr>
  <th>2</th>
  <th>Abort, Retry and Ignore Buttons</th>
 </tr>
 <tr>
  <th>3</th>
  <th>Yes, No and Cancel Buttons</th>
 </tr>
  <tr>
  <th>4</th>
  <th>Yes and No Buttons</th>
 </tr>
  <tr>
  <th>5</th>
  <th>Retry and Cancel Buttons</th>
 </tr>
</table>
<table>
 <tr>
  <th>Icon Input</th>
  <th>Icon Output</th>
 </tr>
 <tr>
  <th>0</th>
  <th>No Icon</th>
 </tr>
 <tr>
  <th>16</th>
  <th>Critical Icon ❌</th>
 </tr>
 <tr>
  <th>32</th>
  <th>Question Icon ❓</th>
 </tr>
 <tr>
  <th>48</th>
  <th>Warning Icon ⚠</th>
 </tr>
 <tr>
  <th>64</th>
  <th>Info Icon ❗</th>
 </tr>
 <tr>
  <th>4096</th>
  <th>System Modal Icon</th>
 </tr>
</table>

# Install and Run
1. Download or Clone the Repository.<br>
2. Open the folder and just double click on ArduinoHIDScripter.py file.<br>
3. Type the mnemonics in the left window.<br>
4. Click on ```Convert``` button to get corresponding VB script.<br>
5. Save the VB Script.<br>
6. Double click on the vb script file.<br>
Done!

# Examples
## Example - 1 : Simple Error Message Box for a game

```
VAR game TITLE Skateboarder MSG Do you want to try again? BUTTON 3 ICON 32
```
after click on ```Convert``` button, the arduino script of the following mnemonic is :<br>

```
game = MsgBox("Do you want to try again?", 3+32, "Skateboarder")
```
Just save this code in the tool and run.<br>

## Example - 2 : Simple Error Message Box for a game for 6 times
```
REDO 6 game TITLE Skateboarder MSG Do you want to try again? BUTTON 3 ICON 32
```
after click on ```Convert``` button, the arduino script of the following mnemonic is :<br>
```
For i = 1 to 6
    game = MsgBox("Do you want to try again?", 3+32, "Skateboarder")
Next
```
Just save this code in the tool and run.<br>

## Example - 3 : Simple Error Message Box for a game infinite times
```
INF game TITLE Skateboarder MSG Do you want to try again? BUTTON 3 ICON 32
```
after click on ```Convert``` button, the arduino script of the following mnemonic is :<br>
```
Do
game = MsgBox("Do you want to try again?", 3+32, "Skateboarder")
Loop
```
Just save this code in the tool and run.<br>

## Example - 4 : Run other commands or other scripts with simple error message box
```
SET runcode
VAR game TITLE Skateboarder MSG Do you want to try again? BUTTON 3 ICON 32
RUN game runcode notepad
```
after click on ```Convert``` button, the arduino script of the following mnemonic is :<br>
```
Dim runcode
Set runcode = WScript.CreateObject("WScript.Shell")
game = MsgBox("Do you want to try again?", 3+32, "Skateboarder")
If game = 1 Then
    runcode.Run "notepad", 1, True
End If
```
Just save this code in the tool and run.<br>
