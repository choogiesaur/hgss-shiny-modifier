import ndspy.rom
import ndspy.codeCompression as comp

# Change shiny rate in NA Soul Silver !
filename = 'YourUSAPokemonRom.nds'

# Load rom with ndspy
rom = ndspy.rom.NintendoDSRom.fromFile(filename)
print('Rom Name: ', rom.name)

# Raw arm9 bytes
print('\nRaw arm9 byte size:')
print(len(rom.arm9))

# Keep track of raw arm9 bytes and decompress with ndspy
raw_arm9 = rom.arm9
decomp_arm9 = comp.decompress(raw_arm9)
print('\nDecompressed arm9 byte size:')
print(len(decomp_arm9))

# Modify byte at offset 0x70080; default is 0x8
# Check readme for offsets for other versions
shiny_value = 0xFF

print("\nValue before: ", decomp_arm9[0x70080])
decomp_arm9[0x70080] = shiny_value
print("Value after: ", decomp_arm9[0x70080])

# Dont recompress - desmume crash
# recomp_arm9 = comp.compress(decomp_arm9)
# print("\nRecompressed length: ")
# print(len(recomp_arm9))

# rom.arm9 = recomp_arm9
rom.arm9 = decomp_arm9
rom.saveToFile('soulsilver_edit.nds')
