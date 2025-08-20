Steps to run **old_version.py**

1. Install Python. If you are not familiar, it's a coding language and runtime (an engine that will let you run .py files). The program we are running, the shiny rate editor, is a Python script.
Go here and download any recent stable release. I recommend 3.13 or whatever is not currently in alpha.
Install it, if there is an option to install pip make sure to select it. if you're on Windows, select an option to add Python to your path.

2. Open up a terminal. A terminal is essentially a command interface for doing various things on your OS you couldn't do by just clicking buttons. in this case we will be using it to tell your computer to run our Python script.

3. In your terminal (cmd or Powershell for Windows, simply Terminal on mac), type 'pip install ndspy' and hit enter.
This will download and install the ndspy library, which is an open source collection of code written by community devs to open Nintendo DS files and do various operations with them. The shiny script uses ndspy to open your rom.

4. Now you have the required dependencies. Open up the script in your vscode or editor of choice.
In the script there are a couple values you may want to change depending on your needs. When I describe "changing the value" you change what you see after the = sign. Think of this as applying a setting in a regular program.

 - For shiny_offset, change the 0x70080 to whichever offset corresponds to your version. It's in a table in the script. If your version is USA, you need not change this. For example if your version is Spanish HeartGold, change the 0x70080 to 0×70078 and save the file.

 - For new_shiny_rate, this could be a bit confusing, but essentially 0x08 is the default rate of 1/8192 shiny chance. By default the script changes it to 0xFF which is the easiest shiny rate at 1/256. If you want something in between, use a hex calculator to pick a value between 0x08 and 0xFF. However, I think 1/256 is already hard enough to test as you'll want to go in-game and fight roughly 256 battles to see if you are encountering shinies more than normal. 

 - output_file_name is what you want your patched file to be called. pick something you can easily find on your desktop, default is "shiny_rate_patched.nds"
```
# Region      Shiny rate offset
# -----------------------------
# Japanese    0×6FAC0
# Spanish HG  0×70078
# Korean HG   0×7017C
# Korean SS   0×70174
# Others      0×70080

# Set the appropriate shiny rate offset here from the table shown above.
# For most versions of HGSS it is located at 0x70080
shiny_offset = 0x70080

# Set the desired shiny rate. 0x08 or 1/8192 is the in-game default.
# 0xFF or 1/256 is this script's default, and the highest that can be set.
# You can select a value from 0x08 to 0xFF.
new_shiny_rate = 0xFF

# Modify the value here to change your output file name
output_file_name = 'shiny_rate_patched.nds'
```

5. In your terminal you've opened in the same directory as the script and rom file, type and enter:
```
python old_version.py <filename>
```

replacing filename with the name of the rom.
