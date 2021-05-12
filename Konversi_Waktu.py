# Soal 1 - Konversi Waktu (30 Poin)
# Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").

# HH : Hours, 2 digits, range: 00 - 99

# MM : Minutes, 2 digits, range: 00 - 59

# SS : Seconds, 2 digits, range: 00 - 59

# Case Flow: Saat dieksekusi, program akan mencetak nilai return function.

# def timeConverter(seconds):
#       .....
 

# Masukkan detik : 3600
# Konversi : 01:00:00

# Masukkan detik : 3665
# Konversi : 01:01:05
# Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999, jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun memasukkan string akan keluar notifikasi. Invalid Input

# Masukkan detik : ujian
# Invalid Input!

# Masukkan detik : 20.5
# Invalid Input!
# Catatan:

# Silakan Commit & push (Upload) source code project ke Github Anda, buatlah repo dengan nama Konversi_Waktu. Kemudian lampirkan url link repo Github Anda via email ke khumaeni@purwadhika.com dan purwadhika.jcds@gmail.com dan student Bandung email juga ke untuk operational_bdg@purwadhika.com untuk Student BSD email juga ke operational@purwadhika.com



import math

def TimeConverter() :
    try :
        detik = int(input('Masukkan detik : '))
        sejam = 3600
        semenit = 60

        jam = math.floor(detik/sejam)
        sisajam = detik % sejam

        menit = math.floor(sisajam/semenit)
        detiknya = sisajam % semenit

        if 359999 > detik > 0 :
            detik = detik

            if jam < 10 :
                jam = ('0' + str(jam))
            
            if menit < 10 :
                menit = ('0' + str(menit))

            if detiknya < 10 :
                detiknya = ('0' + str(detiknya))
           

            hasil = f'Konversi : {jam}:{menit}:{detiknya}'

        else :
            hasil = 'Invalid Input'

    except :
        hasil = 'Invalid Input'

    return hasil

print(TimeConverter())