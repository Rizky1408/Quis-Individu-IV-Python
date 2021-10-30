def hitungJarak(kecepatan, waktu):
    jarak = kecepatan * waktu
    
    return jarak

def hitungKecepatan(jarak, waktu):
    kecepatan = float(jarak) / waktu
    
    return kecepatan

def hitungWaktu(kecepatan, jarak):
    waktu = float(kecepatan) / jarak
    
    return waktu

# Main
print("1.Hitung Kecepatan")
print("2.Hitung Jarak")
print("3.Hitung Waktu")
print("Masukan Pilihan :")
pilihan = float(input())
if pilihan == 1:
    jarak = float(input("Masukan Jarak :"))
    waktu = float(input("Masukan Waktu : "))
    print("Kecepatan adalah :" + str(hitungKecepatan(jarak, waktu)) + " km/jam")

elif pilihan == 2:
    kecepatan = float(input("Masukan Kecepatan :"))
    waktu = float(input("Masukan waktu :"))
    print("Jarak adalah : " + str(hitungJarak(kecepatan, waktu)) + " km")

elif pilihan == 3:
    kecepatan = float(input("Masukan Kecepatan : "))
    jarak = float(input("Masukan jarak : "))
    print("Waktu tempuh adalah : " + str(hitungWaktu(kecepatan, jarak)) + " jam")
    
else:
    print("Pilihan Invalid")
