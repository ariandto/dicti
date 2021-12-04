from typing import ItemsView, ValuesView

kontak={
"Ari":"081267888",
"Dina":"087677776",
}
#tambah kontak Riko
kontak["Riko"]="087654544"

#ubah nomor dina
kontak['Dina']="088999776"
header = "#"'\x1B[3m NAMA KONTAK   \t\x1B[23m'
print(header)
print("="*15)
for item in kontak.items():
    print("# "f"\x1B[3m{item[0]}\t\x1B[23m")

print()
header = "#"'\x1B[3m\tNAMA  \t|  Nomor Telepon\x1B[23m'
print(header)
print("="*28)
for item in kontak.items():
    print("# "f"\x1B[3m{item[0]}\t| {item[1]}\x1B[23m")

