Prerequisites:
- Python3 

Cara menjalankan:
Jalankan command ini di terminal `python3 cleanse_data.py`

Asumsi:
- Berat dengan keterangan "rata2", "kurang dari" akan dibulatkan menjadi sama dengan berat yang tertera.
- Berat dengan keterangan "sampai", akan diambil angka pertama. Misal berat 3-4, akan dianggap berat 3kg.
- Karena data terlalu kotor, jadi saya akan mulai cleansing dengan dengan metode populasi. Saya akan fokus ke top 10 komoditi yang paling berat timbangannya. Selain 10 besar, data komoditi bisa kita abaikan data kotornya (misalnya typo penulisan nama). Setelah dilakukan cleansing & transformasi, didapat data seperti ini:
    1. lele	2204
    2. mas	1517
    3. nila	945
    4. tongkol	880
    5. kakap	328
    6. kembung	311
    7. mujaer	285
    8. gurame	232
    9. bawal	229
    10. mujair	130
    11. laut	106
    12. patin	69
    13. kerapu	39
    14. udang	13
Artinya saya akan fokus ke 10 komoditas teratas untuk membersihkan nama komoditas nya jika terdapat typo. 
Faktanya, diluar 10 komoditas terbesar hanya berisi kurang dari 5% populasi.
