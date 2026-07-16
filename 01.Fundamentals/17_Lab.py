
#! File I/O
#! OS --> Oparating System

#region Dosya Açma ve İçerisine Bilgi Yazma
try:
    file = open(file='new_file.txt', mode='w', encoding='utf-8')
    file.write('Full Name: Burak Yılmaz\nOccupation: Developer\n')
    file.close()
except FileExistsError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
#endregion

#region Dosya Yeni Bilgi Yazma
try:
    file = open(file='new_file.txt', mode='a', encoding='utf-8')
    file.write('Full Name: İpek Yılmaz\nOccupation: Art Historian\n')
    file.close()
except FileExistsError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
#endregion

#region Dosyadan Veri Okuma
try:
    file = open(file='new_file.txt', mode='r', encoding='utf-8')
    for line in file.readlines():
        print(line)
    file.close()
except FileExistsError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
#endregion


with open(file='new_file.txt', mode='a', encoding='utf-8') as file:
    file.write('Full Name: Hakan Yılmaz\nOccupation: Chemist\n')