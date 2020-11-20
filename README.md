# hgss-shiny-modifier
Python script to modify the Shiny encounter rate in Pokemon HeartGold/SoulSilver for NDS

- Currently tested with North American HG/SS
- **TODO:** Add support for other versions

![First shiny encounter!](https://github.com/choogiesaur/hgss-shiny-modifier/blob/main/shiny_hoothoot.png?raw=true)

## Dependencies: 
**Python3**, python library **ndspy**. To install:
```
pip install ndspy
```

## Usage:
1. Place legally obtained HGSS rom in same folder as python script
2. Change the **filename** variable to match your rom's filename
3. Change **shiny_value** variable to a hex value from 0x8 (default, 1/8192 encounter rate) to 0xFF (1/256 encounter rate)
4. In a terminal run ```python arm9_edit.py```
5. Play your edited rom via your method of choice

## For Science:
The shiny encounter rate offset for different versions:
```
Language    Shiny chance
------------------------
Japanese    0×6FAC0
Spanish HG  0×70078
Korean HG   0×7017C
Korean SS   0×70174
Others      0×70080
```
This program uses ndspy to extract and decompress the raw arm9 binary file, modifies the value used to determine shiny encounter rate, then reinserts the arm9 into the rom and resaves it. To be exact we would have to recompress the arm9 before reinsertion, but this causes the game to crash in some cases - so the binary is left decompressed.
