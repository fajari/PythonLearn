"""
Perulangan dengan While
"""
jumlah_buku = 100
print(f"Baca semua {jumlah_buku} bukumu")

jumlah_buku_yang_sudah_dibaca = 0
print(f"Jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_dibaca}")

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca=jumlah_buku_yang_sudah_dibaca+1
    print(f"Membaca buku yang ke {jumlah_buku_yang_sudah_dibaca}")