"""
This is your first python file
"""

# Percabangan
print("Budi diperintah ibunya untuk membeli Susu")
print("Kalau ada telor, beli 6")

# Pemrograman
total_milk_onstore = 1
total_egg_onstore = 4

if total_milk_onstore > 0:
    print("Budi membeli 1 susu")
    if total_egg_onstore > 6:
        print("Budi juga membeli 6 telor")
    else:
        print("Budi membeli", total_egg_onstore, "botol")
        print(f"Jadi yang di beli Budi sejumlah {total_egg_onstore} telor dan {total_milk_onstore} susu")
else:
    print("Budi tidak membeli Susu")

print("Budi pulang kerumah")