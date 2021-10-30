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
print("1.Berapa kecepatan rossi")
print("2.Jarak rumah pak jul ke kantor")
print("3.Waktu tempuh pak yunan")
print("Masukan Pilihan :")

pilihan = int(input())
if pilihan == 1:
    print("Kecepatan Rossi adalah :" + str(hitungKecepatan(700, 5)) + " km/jam")

elif pilihan == 2:
    print("Jarak rumah pak jul ke kantor adalah : " + str(hitungJarak(20, 30)) + " km")

elif pilihan == 3:
    print("Waktu tempuh yang dibutuhkan pak yunan adalah : " + str(hitungWaktu(180, 50)) + " jam")
    
else:
    print("Pilihan Invalid")
