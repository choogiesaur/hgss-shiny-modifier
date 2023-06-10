import ndspy.rom
import ndspy.codeCompression as comp
import sys

## Change shiny rate in Pokemon HeartGold/SoulSilver! ##
# Place your .nds file in the same folder as this script.
# Modify 'shiny_offset' and 'new_shiny_rate' below.
# Usage: python shiny_editor.py <filename>

def modify_shiny_rate(filename):

	# Load rom with ndspy
	rom = ndspy.rom.NintendoDSRom.fromFile(filename)
	print('Rom Name: ', rom.name)
	print('\nRaw arm9 byte size:', len(rom.arm9))

	# Keep track of raw arm9 bytes and decompress with ndspy
	raw_arm9 = rom.arm9
	decompressed_arm9 = comp.decompress(raw_arm9)
	print('\nDecompressed arm9 byte size:', len(decompressed_arm9))

	# Set the appropriate shiny rate offset here.
	# For most versions of HGSS it is located at 0x70080;
	# If yours is one of the regions below, change 'shiny_offset' accordingly.
	shiny_offset = 0x70080
	
	# Region      Shiny rate offset
	# -----------------------------
	# Japanese    0×6FAC0
	# Spanish HG  0×70078
	# Korean HG   0×7017C
	# Korean SS   0×70174
	# Others      0×70080

	# Set the desired shiny rate. 0x8 or 1/8192 is the in-game default.
	# 0xFF or 1/256 is this script's default, and the highest that can be set.
	# You can select a value from 0x08 to 0xFF.
	new_shiny_rate = 0xFF

	print("\nValue before: ", decompressed_arm9[shiny_offset])
	decompressed_arm9[shiny_offset] = new_shiny_rate
	print("Value after: ", decompressed_arm9[shiny_offset])

	rom.arm9 = decompressed_arm9
	rom.saveToFile('shiny_rate_patched.nds')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python shiny_editor.py <filename>")
    else:
        filename = sys.argv[1]
        modify_shiny_rate(filename)
