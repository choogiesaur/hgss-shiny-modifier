# hgss-shiny-modifier

A Python script designed to change the Shiny Pokémon encounter rate in the Pokémon HeartGold/SoulSilver Nintendo DS games. Works by modifying the Shiny rate offset in the game ROM file. Now with automatic game version detection!

![First shiny encounter!](https://github.com/choogiesaur/hgss-shiny-modifier/blob/main/shiny_hoothoot.png?raw=true)

## Features:
- Change the Shiny encounter rate to any desired value within the allowed range.
- Automatically detects the game version based on the game ID and selects the correct Shiny rate offset.
- Can be manually adjusted for different game versions and regions.
- Easy-to-use command line interface.
- Currently tested with North American HG/SS versions.

## Dependencies:
Requires **Python3** and the **ndspy** Python library. Install ndspy with pip:

```bash
pip install ndspy
```

## Usage:
1. Place your `.nds` file (the game ROM) in the same folder as the `shiny_rate_editor.py` script.
2. The script will auto-detect the game version and use the correct Shiny rate offset. If you want to manually set the Shiny rate offset or the new Shiny rate, you can provide them as command-line arguments. 
3. Run the script from your terminal, replacing `<filename>` with the name of your `.nds` file, `<shiny_offset>` with the hexadecimal value of your desired shiny rate offset (if you want to set it manually), and `<new_shiny_rate>` with your preferred shiny encounter rate. The shiny encounter rate should be a hexadecimal value between `0x0` and `0xFF`.

```bash
# Arguments in [square brackets] are optional
python shiny_rate_editor.py <filename> [<shiny_offset>] [<new_shiny_rate>]
```

For example, if you have a file named `pokemon.nds` and you want to set the Shiny encounter rate to `0xFF` (1/256, the maximum), you would use:

```bash
python shiny_rate_editor.py pokemon.nds 0x70080 0xFF
```

If you don't provide a shiny offset or new shiny rate, the script will use the default values based on the auto-detected game version and a default shiny rate of `0xFF`.

4. The script will create a new modified game ROM file called `shiny_rate_patched.nds`. Use your method of choice to play the edited game ROM file.

## Shiny Encounter Rate Offsets:
Here are the offsets for different versions of the game:

| Language | Shiny chance |
| ------------- | ------------- |
| Japanese | 0x6FAC0 |
| Spanish HG | 0x70078 |
| Korean HG | 0x7017C |
| Korean SS | 0x70174 |
| Others (Including North America) | 0x70080 |

The script works by using ndspy to extract and decompress the raw ARM9 binary file from the game ROM. It then modifies the value used to determine Shiny encounter rates and reinserts the modified ARM9 binary back into the ROM file. Ideally, we would recompress the ARM9 binary before reinsertion, but this can cause crashes in some cases. So, we leave the binary decompressed, which seems to work just fine.

## Contributions and Future Work:
Feel free to contribute to this project! In the future, we hope to expand this tool to work with more games and versions. We'd also like to add more robust error handling and user interaction features. Your suggestions and pull requests are welcome!

## License:
This project is licensed under the terms of the MIT license.
