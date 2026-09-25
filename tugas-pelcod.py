nama = "andi"

jumlah_buku = 3
harga_buku  = 15000

jumlah_boulpen = 2
harga_boulpen = 5000

total_buku = jumlah_buku * harga_buku

total_boulpen = jumlah_boulpen * harga_boulpen

total_belanja = total_buku + total_boulpen

if total_belanja >= 50000:
    diskon = total_belanja * 10 / 100
    total_bayar = total_belanja - diskon

print("nama", nama)
print("total harga buku", total_buku)
print("total harga boulpen", total_boulpen)
print("total belanja sebelum diskon", total_belanja)
print("besarnya diskon", diskon)
print("total yang harus di bayar", total_bayar)