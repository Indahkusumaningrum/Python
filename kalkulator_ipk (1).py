list_nilai = {'A': 4.0,'B+': 3.50, 'B': 3.0,'C': 2.50, 'C': 2.0,'D': 1.0, 'E': 0.0}
total_grade_points = 0

banyak_mk = int(input("Berapa banyak mata kuliah yang diambil? "))

for i in range(banyak_mk):
    grade = input("Masukkan huruf mutu untuk mata kuliah ke-%d: " % (i+1))
    total_grade_points += list_nilai[grade]

ipk = total_grade_points / banyak_mk
print("IPK Anda adalah:", round(ipk, 2))
