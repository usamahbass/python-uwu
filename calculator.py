''' Program Kalkulator dengan bahasa Python '''
import time

def jumlah(x, y):
    return x + y


def kurang(x, y):
    return x - y


def kali(x, y):
    return x * y


def bagi(x, y):
    return x / y


def awal():
    print ('proccessing ...')
    time.sleep(2)

    print ('')
    print ('')
    print ('')
    print ('Welcome to Calculator')
    time.sleep(1)

#menu operasi
    print ('')
    print ('1. Penjumlahan')
    print ('2. Pengurangan')
    print ('3. Perkalian')
    print ('4. Pembagian')

#menu input user
    tanya = input('Masukkan pilihan Anda (1/2/3/4): ')
    time.sleep(1)

    print ('')
    x = int(input('Masukkan bilangan pertama: '))
    print ('')
    y = int(input('Masukkan bilangan kedua: '))

#working..
    if tanya == 1:
        print ('proccessing ...')
        time.sleep(0.5)
        print ('')
        print ('||| Hasil |||')
        print ('')
        print (x , "+", y , "=", jumlah(x,y))
        print ('')
        print ('')
        pilih()

    elif tanya == 2:
        print ('proccessing ...')
        time.sleep(0.5)
        print ('')
        print ('||| Hasil |||')
        print ('')
        print (x , "-", y , "=", kurang(x,y))
        print ('')
        print ('')
        pilih()

    elif tanya == 3:
        print ('proccessing ...')
        time.sleep(0.5)
        print ('')
        print ('||| Hasil |||')
        print ('')
        print (x , "*", y , "=", kali(x,y))
        print ('')
        print ('')
        pilih()

    elif tanya == 4:
        print ('proccessing ...')
        time.sleep(0.5)
        print ('')
        print ('||| Hasil |||')
        print ('')
        print (x , "/", y , "=", bagi(x,y))
        print ('')
        print ('')
        pilih()

    else:
        print ("command not valid !")

def pilih():
    print ("wait ...")
    time.sleep(2)

    print ('')
    print ('')
    time.sleep(2)
    awal()

    #break
awal()

