"""
Type Data Dictionary  { }
Menghubungkan antara pasangan KEY dan VALUE
KVP = Key Value Pair
"""
kamus_ind_eng = {}
kamus_ind_eng['anak'] = 'child'
kamus_ind_eng['bapak'] = 'father'
kamus_ind_eng['ibu'] = 'mother'
kamus_ind_eng['paklik'] = 'uncle'
kamus_ind_eng['bulik'] = 'aunt'
"""
Bisa diringkas jadi: 
kamus_ind_eng = {'anak': 'child', 'bapak': 'father', 'ibu': 'mother', 'paklik': 'uncle', 'bulik': 'aunt'}
"""

print(kamus_ind_eng)
print(kamus_ind_eng['paklik'])
print(kamus_ind_eng['anak'])

print('\nData ini dikirimkan server Gojek untuk memberikan informasi driver di sekitar user aplikasi')
data_dari_server_gojek = {
    'tanggal': '2021-05-28',
    'driver_list':[
                { 'nama' : 'Chiky', 'jarak' : 100},
                { 'nama' : 'Bruno', 'jarak' : 20},
                { 'nama' : 'Brown', 'jarak' : 300},
                { 'nama' : 'Pluto', 'jarak' : 450},
                { 'nama' : 'Mini', 'jarak' : 900},
    ]
}

print(data_dari_server_gojek)
print(f"driver di sekitar: {data_dari_server_gojek['driver_list']}")
print(f"driver #1: {data_dari_server_gojek['driver_list'][0]}")

b = []
for x in data_dari_server_gojek['driver_list']:
    #print(x)
    a = x['jarak']
    b.append(a)
i = (b.index(min(b)))

print(f"driver terdekat: {data_dari_server_gojek['driver_list'][i]['nama']} berjarak {min(b)} meter")
