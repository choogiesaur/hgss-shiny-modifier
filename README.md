# hgss-shiny-modifier
Python script to modify the Shiny encounter rate in Pokemon HeartGold/SoulSilver for NDS

- **Currently tested with North American HG/SS
- Todo: Add support for other versions

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
