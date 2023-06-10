# hgss-shiny-modifier
Python script to modify the Shiny encounter rate in Pokemon HeartGold/SoulSilver for NDS!

- Currently tested with North American HG/SS
- **TODO:** Auto-detect version by reading Game ID.

![First shiny encounter!](https://github.com/choogiesaur/hgss-shiny-modifier/blob/main/shiny_hoothoot.png?raw=true)

## Dependencies: 
**Python3**, python library **ndspy**. To install:
```
pip install ndspy
```

## Usage:
1. Place your .nds file in the same folder as this script.
2. Modify `shiny_offset` in the script to your correct region if not North America. Other region's values are listed below.
3. Modify `new_shiny_rate` to your liking. `0x8` or 1/8192 is the ingame default, `0xFF` or 1/256 is the script default and highest you can set. I have not tried making shinies less likely (0x0 -> 0x7) but in theory you could do it :-) The average user will want to set a value from 0x8 to 0xFF though.
5. From your OS terminal of choice, run `python shiny_editor.py <filename>`
6. Play your edited file via your method of choice.

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
This program uses ndspy to extract and decompress the raw arm9 binary file, modifies the value used to determine shiny encounter rate, then reinserts the arm9 into the rom. To be 100% correct we would have to recompress the arm9 before reinsertion, but since this causes the game to crash in some cases, we leave the binary decompressed (tends to work just fine this way).
