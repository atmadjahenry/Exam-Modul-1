# Buatlah sebuah return function dengan 1 argumen yang dapat memutar list angka (Putaran 1X counter-clockwise) seperti keterangan di bawah ini .

# List Awal

# [[1, 2, 3], 0,0 0,1 0,2
# [4, 5, 6], 1,0 1,1 1,2
# [7, 8, 9]] 2,0 2,1 2,2

# [[3, 6, 9], 0,0 0,1 0,2
# [2, 5, 8], 1,0 1,1 1,2
# [1, 4, 7]] 2,0 2,1 2,2


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


listawal = ([[1,2,3],[4,5,6],[7,8,9]]) # 0(0,1,2) 1(0,1,2) 2(0,1,2)

output = ([[3, 6, 9], [2, 5, 8], [1, 4, 7]]) # 0(0,2 1,2 2,2) 1(0,1 1,1 2,1) 2(0,0 1,0 2,0)
# print(output)

def clockwise(listawal):
    listrotasi=[]
    for i in range(1,4):
        for j in range(len(listawal)):
            listrotasi.append(listawal[j][-i])
    a = listrotasi[0:3]
    b = listrotasi[3:6]
    c = listrotasi[6:9]

    listbaru = [a, b, c]
    for i in listbaru:
        print(i)

clockwise(listawal)