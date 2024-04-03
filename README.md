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

# New Features Added!
- `for` Loop added.<br>
- Next line function added.<br>
- TYPE and TYNL supports " ".<br>
- Multiple statements are supported inside for loop.<br>
- Restrict PRESS mnemonic inside for loop.<br>
- WRITE function added.<br>

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
  <th>TYPE</th>
  <th>It add text want to type in the code and put the cursor on the same line.</th>
  <th>TYPE Hello World!</th>
 </tr>
  <tr>
  <th>TYNL</th>
  <th>It add text want to type in the code and put the cursor on the next line.</th>
  <th>TYNL ArduinoHID Scripter</th>
 </tr>
  <tr>
  <th>WAIT</th>
  <th>It add time in the code.</th>
  <th>WAIT 1000</th>
 </tr>
 <tr>
  <th>PRESS</th>
  <th>It press and hold the key(s) and then release all key(s).</th>
  <th>PRESS GUI R</th>
 </tr>
  <tr>
  <th>REDO</th>
  <th>It add loop in the code.</th>
  <th>REDO 6 TYPE Hello World!</th>
 </tr>
  <tr>
  <th>WRITE</th>
  <th>It add ASCII characters in the code.</th>
  <th>WRITE *</th>
 </tr>
</table>

# Details of Mnemonics
## 1. TYPE
- It add text want to type in the code and put the cursor on the same line.<br>
- *NEW* - It supports " " in the TYPE.<br>
- Example - TYPE Hello World!<br>
## 2. TYNL
- It add text want to type in the code and put the cursor on the next line.<br>
- *NEW* - It supports " " in the TYNL.<br>
- Example - TYNL Hello World!<br>
## 3. WAIT
- It add time in the code.<br>
- It gives time to execute between two commands.<br>
- Time is in milliseconds.<br>
- 1000 ms = 1 second.<br>
- Example - WAIT 1000<br>
## 4. PRESS
- It press and hold the key(s) and then release all key(s).<br>
- The supported mnemonics given below works with PRESS.<br>
- Example -
<ol>
  <li>PRESS GUI R</li>
  <li>PRESS CTRL SHIFT N</li>
  <li>PRESS CTRL SHIFT ENTER</li>
</ol>

## 5. REDO
- It add loop in the code.<br>
- The loop used in this is ```for``` loop.<br>
- It takes two values : Number of repeatation and Statement inside the loop.<br>
- Example - REDO 6 TYPE Hello World!<br>
- Here, 6 is number of repetations and TYPE Hello World! is the statement.<br>
- *NEW* - It supports multi statements.<br>
- Multi statement are separated by comma ```,```.<br>
- Example - REDO 9 TYPE Hello World!, WAIT 1000, TYPE This is a test for script!<br>
- Here, `TYPE Hello World!`, `WAIT 1000` and `TYPE This is a test for script!` are three statements and they are separated by commas.<br>
- REDO only supports TYPE, TYNL and WAIT Only.<br>
## 6. WRITE
- It add ASCII characters in the code.<br>
- It supports some ASCII characters not all and supported ASCII characters are defined in the code.<br>
- It press and release the key immediately.<br>
- Example - `WRITE @`<br>

# Supported Mnemonics
## Alphabet Keys
```A``` ```B``` ```C``` ```D``` ```E``` ```F``` ```G``` ```H``` ```I``` ```J```
```K``` ```L``` ```M``` ```N``` ```O``` ```P``` ```Q``` ```R``` ```S``` ```T```
```U``` ```V``` ```W``` ```X``` ```Y``` ```Z```
## Function Keys
```F1``` ```F2``` ```F3``` ```F4``` ```F5``` ```F6``` ```F7``` ```F8``` ```F9``` ```F10```
```F11``` ```F12```
## Navigation Keys
```LEFT``` ```UP``` ```RIGHT``` ```DOWN``` ```TAB``` ```HOME``` ```END``` ```PGUP``` ```PGDN```
## Lock Keys
```CAPS``` ```NUM``` ```SCROLL```
## System and GUI Keys
```GUI``` ```ESC``` ```PRTSCR``` ```PAUSE```
## Editing Keys
```INSERT``` ```DEL``` ```BKSP``` ```ENTER```
## Modifier Keys
```CTRL``` ```SHIFT``` ```ALT```
## ASCII Characters
`` ` `` `!` `@` `#` `$` `%` `^` `&` `*` `(` `)` `-` `=` `[` `]` `\` `;` 
`'` `,` `.` `/` `SPACE` `~` `_` `+` `{` `}` `|` `:` `"` `<` `>` `?` `0`
`1` `2` `3` `4` `5` `6` `7` `8` `9`

# Examples
## Example - 1 : Mnemonic for Open Notepad and Type

```
WAIT 1000
PRESS GUI R
WAIT 1000
TYPE notepad
WAIT 1000
PRESS ENTER
WAIT 1000
TYPE This is a test for arduino script developed by ArduinoHID Scripter!
```
after click on ```Convert``` button, the arduino script of the following mnemonic is :<br>

```
#include<Keyboard.h>
void setup()
{
 Keyboard.begin();
 delay(1000);
 Keyboard.press(KEY_LEFT_GUI);
 Keyboard.press('r');
 Keyboard.releaseAll();
 delay(1000);
 Keyboard.print("notepad");
 delay(1000);
 Keyboard.press(KEY_RETURN);
 Keyboard.releaseAll();
 delay(1000);
 Keyboard.print("This is a test for arduino script developed by ArduinoHID Scripter!");
 Keyboard.end();
}
void loop()
{
 //Nothing to do here ;)
}
```
Just copy this code and paste it in the Arduino IDE.<br>

## Example - 2 : Mnemonic for Open Notepad and Type 6 times
```
WAIT 1000
PRESS GUI R
WAIT 1000
TYPE notepad
WAIT 1000
PRESS ENTER
WAIT 1000
REDO 6 TYNL This is a test for arduino script developed by ArduinoHID Scripter!
```
after click on ```Convert``` button, the arduino script of the following mnemonic is :<br>
```
#include<Keyboard.h>
void setup()
{
 Keyboard.begin();
 delay(1000);
 Keyboard.press(KEY_LEFT_GUI);
 Keyboard.press('r');
 Keyboard.releaseAll();
 delay(1000);
 Keyboard.print("notepad");
 delay(1000);
 Keyboard.press(KEY_RETURN);
 Keyboard.releaseAll();
 delay(1000);
 for (int i=1; i<=6; i++)
 {
  Keyboard.println("This is a test for arduino script developed by ArduinoHID Scripter!");
 }
 Keyboard.end();
}
void loop()
{
 //Nothing to do here ;)
}
```
Just copy this code and paste it in the Arduino IDE.<br>
# Tested Systems
The tool is currently tested on : <br>
- Windows (10)<br>

# Before coding...
Start your code with ```WAIT``` so that board get time to initiate.<br>

# Install and Run
1. Download or Clone the Repository.<br>
2. Open the folder and just double click on ArduinoHIDScripter.py file.<br>
3. Type the mnemonics in the left window.<br>
4. Click on ```Convert``` button to get corresponding arduino script.<br>
5. Click on ```Copy``` button to copy the arduino script to the clipboard.<br>
6. Paste the code in the Arduino IDE.<br>
7. Connect your board to the PC/Laptop.<br>
8. Compile the code.<br>
9. Select the board from the ```Tools```.<br>
10. Select the port number of that board.<br>
11. Upload the code.<br>
-Be Careful! As it is uploaded the script start executing.<br>

# Start/Stop the Arduino Board
Arduino Leonardo and Arduino Mico has a reset button on it.<br>
Just press and hold the button to stop execution and release to start execution.<br>
For Arduino Pro Micro : <br>
1. If want to stop Arduino Pro Micro from execution, then connect the Male-To-Male jumper wires as shown in image below : <br>

![Untitled Sketch 2_bb](https://github.com/wirebits/ArduinoHID-Scripter/assets/159493381/d2b2e09b-971f-416f-ab47-31584f757970)

2. If want to start again the execution, simply remove the jumper wires.
