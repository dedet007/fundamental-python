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
bil= ['satu-satu', 'dua-satu', 'tiga-satu', 'empat-satu']
print(bil)

print('\nMenyebutkan bilangan ke-2 dari list')
print(f'Ini adalah bilangan ke-2 dalam daftar/list: {bil[1]}')

print('\nMenyebutkan semua bilangan berurutan dan ganti baris:')
i = 1
for x in bil:
    print(f'Bilangan ke-{i} adalah {x}')
    i += 1

print('\nMenyebutkan semua bilangan dengan for dan range:')
# x (variabel setelah for) menjadi index items dalam list
for x in range(0, len(bil)):
    print(f'{x+1}. Bilangan ke-{x+1} adalah {bil[x]}')

print('\nUrutan dibalik:')
for x in range(len(bil)-1, -1, -1):
    print(f'{len(bil)-x}. Bilangan ke-{x+1} adalah {bil[x]}')