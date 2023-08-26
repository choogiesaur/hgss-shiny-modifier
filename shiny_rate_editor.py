import ndspy.rom
import ndspy.codeCompression as comp
import sys

## Change shiny rate in Pokemon HeartGold/SoulSilver! ##
# Place your .nds file in the same folder as this script.
# Usage: python shiny_rate_editor.py <filename> [<shiny_offset>] [<new_shiny_rate>]

def modify_shiny_rate(filename, shiny_offset='AUTO', new_shiny_rate=0xFF):
    # Load rom with ndspy and print rom information
    rom = ndspy.rom.NintendoDSRom.fromFile(filename)
    print(f'Rom Name: {rom.name.decode()} Rom idCode: {rom.idCode.decode()}')
    print(f'\nRaw arm9 byte size: {len(rom.arm9)}')

    # Map for title IDs and their shiny offsets
    shiny_offsets = {
        'IPKJ': 0x6FAC0, 'IPGJ': 0x6FAC0,  # Japanese HG or SS
        'IPKS': 0x70078,  # Spanish HG
        'IPKK': 0x7017C,  # Korean HG
        'IPGK': 0x70174   # Korean SS
    }

    # Use appropriate shiny offset if custom offset not supplied
    # 0x70080 is the default, used in the US version and a few others
    shiny_offset = shiny_offsets.get(rom.idCode.decode(), 0x70080) if shiny_offset == 'AUTO' else shiny_offset

    # Decompress arm9 with ndspy
    decompressed_arm9 = comp.decompress(rom.arm9)
    print(f'\nDecompressed arm9 byte size: {len(decompressed_arm9)}')

    print(f"\nShiny Value at offset {shiny_offset} before: {decompressed_arm9[shiny_offset]}")
    decompressed_arm9[shiny_offset] = new_shiny_rate
    print(f"Shiny Value at offset {shiny_offset} after: {decompressed_arm9[shiny_offset]}")

    # Note that we do not recompress to avoid crashes.
    rom.arm9 = decompressed_arm9
    rom.saveToFile('shiny_rate_patched.nds')


if __name__ == "__main__":
    argc = len(sys.argv)
    if 2 <= argc <= 4:
        filename = sys.argv[1]
        shiny_offset = int(sys.argv[2], 16) if argc >= 3 else 'AUTO'
        new_shiny_rate = int(sys.argv[3], 16) if argc >= 4 else 0xFF
        modify_shiny_rate(filename, shiny_offset, new_shiny_rate)
    else:
        print("Usage: python shiny_editor.py <filename> [<shiny_offset>] [<new_shiny_rate>]")
