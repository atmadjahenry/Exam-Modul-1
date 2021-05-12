# Buatlah sebuah return function dengan 1 argumen yang dapat memutar list angka (Putaran 1X counter-clockwise) seperti keterangan di bawah ini .

# List Awal

# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
# Function

# # Function Initialization
#  def counterClockwise(...):
#      .....
     
# # Use the Function
# print(counterClockwise(List_awal))
# List Output

# [[3, 6, 9],
# [2, 5, 8],
# [1, 4, 7]]
# Catatan:

# Silakan Commit & push (Upload) source code project ke Github Anda, buatlah repo dengan nama List_Spinner. Kemudian lampirkan url link repo Github Anda via email ke khumaeni@purwadhika.com dan purwadhika.jcds@gmail.com dan student Bandung email juga ke untuk operational_bdg@purwadhika.com untuk Student BSD email juga ke operational@purwadhika.com

listawal = ([[1,2,3],[4,5,6],[7,8,9]])
print(listawal)


def counterClockwise(listawal) :
    listrotasi = []
    panjanglist = len(listawal)
    for i in range(panjanglist) :
        listrotasi.append([])
        # print(listrotasi)
    for i in range(panjanglist) :
        for j in range(panjanglist) :
            listrotasi[i].append(listawal[j].pop(-1))

    return listrotasi
listbaru = counterClockwise(listawal)

for i in listbaru :
    print(i)