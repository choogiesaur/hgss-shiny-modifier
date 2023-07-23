import ndspy.rom
import ndspy.codeCompression as comp
import sys

## Change shiny rate in Pokemon HeartGold/SoulSilver! ##
# Place your .nds file in the same folder as this script.
# Modify 'shiny_offset' and 'new_shiny_rate' below.
# Usage: python shiny_rate_editor.py <filename> [<shiny_offset>] [<new_shiny_rate>]

def modify_shiny_rate(filename, shiny_offset='AUTO', new_shiny_rate=0xFF):

    # Load rom with ndspy and print rom information
    rom = ndspy.rom.NintendoDSRom.fromFile(filename)
    print('Rom Name:', rom.name.decode(), ' Rom idCode: ', rom.idCode.decode())
    print('\nRaw arm9 byte size:', len(rom.arm9))

    # Auto-detect HGSS version and use appropriate shiny offset if custom offset not supplied
    title_id = rom.idCode.decode()
    if shiny_offset == 'AUTO':
        # Japanese HG or SS
        if title_id == 'IPKJ' or title_id =='IPGJ':
            shiny_offset = 0x6FAC0
        # Spanish HG
        elif title_id == 'IPKS':
            shiny_offset = 0x70078
        # Korean HG
        elif title_id == 'IPKK':
            shiny_offset = 0x7017C
        # Korean SS
        elif title_id == 'IPGK':
            shiny_offset = 0x70174
        # Other regions (USA included)...
        else:
            shiny_offset = 0x70080

    # Japanese IPKJ (HG) IPGJ (SS)
    # Spanish HG - IPKS
    # Korean HG - IPKK
    # Korean SS - IPGK
    # Others...

    # Keep track of raw arm9 bytes and decompress with ndspy
    decompressed_arm9 = comp.decompress(rom.arm9)
    print('\nDecompressed arm9 byte size:', len(decompressed_arm9))

    print("\nShiny Value at offset ", shiny_offset, " before:", decompressed_arm9[shiny_offset])
    decompressed_arm9[shiny_offset] = new_shiny_rate
    print("Shiny Value at offset ", shiny_offset, " after:", decompressed_arm9[shiny_offset])

    rom.arm9 = decompressed_arm9
    rom.saveToFile('shiny_rate_patched.nds')

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python shiny_editor.py <filename> [<shiny_offset>] [<new_shiny_rate>]")
    else:
        filename = sys.argv[1]
        shiny_offset = int(sys.argv[2], 16) if len(sys.argv) >= 3 else 0x70080
        new_shiny_rate = int(sys.argv[3], 16) if len(sys.argv) >= 4 else 0xFF
        modify_shiny_rate(filename, shiny_offset, new_shiny_rate)
