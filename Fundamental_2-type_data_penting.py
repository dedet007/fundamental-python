print('Type data sederhana -> type data skalar:')
bil1 = 'satu'
bil2 = 'dua'
bil3 = 'tiga'
bil4 = 'empat'

print(bil1)
print(bil2)
print(bil3)
print(bil4)

print('\nType data list/daftar/list:')
angka = ['satu-satu', 'dua-satu', 'tiga-satu', 'empat-satu']
print(angka)

print('\nMenyebutkan bilayngan ke-2 dari list')
print(f'Ini adalah bilangan ke-2 dalam daftar/list: {angka[1]}')

print('\nMenyebutkan semua bilangan berurutan dan ganti baris:')
i = 1
for x in angka:
    print(f'Bilangan ke-{i} adalah {x}')
    i += 1

print('\nMenyebutkan semua bilangan dengan for dan range:')
# x (variabel setelah for) menjadi index items dalam list
for x in range(0, len(angka)):
    print(f'{x + 1}. Bilangan ke-{x + 1} adalah {angka[x]}')

print('\nUrutan dibalik (dengan for in range):')
for x in range(len(angka) - 1, -1, -1):
    print(f'{len(angka) - x}. Bilangan ke-{x + 1} adalah {angka[x]}')
