import time

daftar_kursi = {
    'Avengers: Endgame': {
        'A': [''] * 15,
        'B': [''] * 15,
        'C': [''] * 15,
        'D': [''] * 15,
        'E': [''] * 15,
        'F': [''] * 15,
        'G': [''] * 15,
        'H': [''] * 15,
        'I': [''] * 15,
        'J': [''] * 15
    },
    'Joker': {
        'A': [''] * 15,
        'B': [''] * 15,
        'C': [''] * 15,
        'D': [''] * 15,
        'E': [''] * 15,
        'F': [''] * 15,
        'G': [''] * 15,
        'H': [''] * 15,
        'I': [''] * 15,
        'J': [''] * 15
    },
    'The Lion King': {
        'A': [''] * 15,
        'B': [''] * 15,
        'C': [''] * 15,
        'D': [''] * 15,
        'E': [''] * 15,
        'F': [''] * 15,
        'G': [''] * 15,
        'H': [''] * 15,
        'I': [''] * 15,
        'J': [''] * 15
    },
    'Spider-Man: Far From Home': {
        'A': [''] * 15,
        'B': [''] * 15,
        'C': [''] * 15,
        'D': [''] * 15,
        'E': [''] * 15,
        'F': [''] * 15,
        'G': [''] * 15,
        'H': [''] * 15,
        'I': [''] * 15,
        'J': [''] * 15
    },
    'Frozen II': {
        'A': [''] * 15,
        'B': [''] * 15,
        'C': [''] * 15,
        'D': [''] * 15,
        'E': [''] * 15,
        'F': [''] * 15,
        'G': [''] * 15,
        'H': [''] * 15,
        'I': [''] * 15,
        'J': [''] * 15
    }
}

harga_reguler = 50000
harga_VIP = 100000
total_pendapatan = 0  # Menyimpan total pendapatan

daftar_film = [
    "Avengers: Endgame",
    "Joker",
    "The Lion King",
    "Spider-Man: Far From Home",
    "Frozen II"
]

def tampil_daftar_kursi(film):
    for baris, kolom in daftar_kursi[film].items():
        print(baris, kolom)

def tampil_kursi_dipesan():
    print("Kursi yang telah dipesan:")
    for baris, kolom in daftar_kursi.items():
        kursi_dipesan = [str(i+1) for i in range(len(kolom)) if kolom[i] == 'x']
        if kursi_dipesan:
            print(baris + ": " + ", ".join(kursi_dipesan))

def proses_pembayaran(total_harga):
    global total_pendapatan, kembalian
    while True:
        pembayaran = int(input("Masukkan jumlah uang: "))
        if pembayaran < total_harga:
            print("Jumlah uang tidak mencukupi.")
        else:
            break

    kembalian = pembayaran - total_harga
    total_pendapatan += total_harga  
    return pembayaran


def totalpendapatan():
    global total_pendapatan
    print("Total pendapatan keseluruhan adalah: Rp", total_pendapatan)

def pilih_bangku(daftar_kursi, film, harga_tiket):
    tampil_daftar_kursi(film)
    jumlah_kursi = 0
    total_harga = 0
    kursi_dipesan = []

    while True:
        pesan_kursi = input("Masukkan nomor kursi (CONTOH : 'A1' ) : ").upper()
        if pesan_kursi in kursi_dipesan:
            print("Kursi sudah terisi")
            continue

        if pesan_kursi[0] not in daftar_kursi[film].keys():
            print("Kursi tidak ada")
            continue

        elif not pesan_kursi[1:].isdigit() or int(pesan_kursi[1:]) < 1 or int(pesan_kursi[1:]) > 15:
            print("Kursi tidak valid")
            continue
        
        if daftar_kursi[film][pesan_kursi[0]][int(pesan_kursi[1:]) - 1] == 'x':
            print("Kursi sudah dipesan")
            continue

        kursi_dipesan.append(pesan_kursi)
        daftar_kursi[film][pesan_kursi[0]][int(pesan_kursi[1:]) - 1] = 'x'  
        jumlah_kursi += 1
        total_harga += harga_tiket

        print("Kursi", pesan_kursi, "telah berhasil dipesan")
        tampil_daftar_kursi(film)

        print("Jumlah bangku : ", jumlah_kursi)
        print("Harga total : Rp.", total_harga)

        beli_lagi = input("Apakah Anda ingin membeli kursi lagi? (ya/tidak): ")
        if beli_lagi.lower() != 'ya':
            break

    return jumlah_kursi, total_harga, kursi_dipesan

while True:
    print("\nPilih menu : ")
    print("1. Beli tiket bioskop")
    print("2. Beli makanan dan minuman")
    print("3. Menu admin")

    pilih_menu_utama = int(input("Masukkan pilihan anda : "))

    if pilih_menu_utama == 1:
        while True:
            print("\nPilih film yang ingin ditonton:")
            for idx, film in enumerate(daftar_film, start=1):
                print(f"{idx}. {film}")

            pilih_film = int(input("Pilih film (masukkan nomor film): "))
            if 1 <= pilih_film <= len(daftar_film):
                film_dipilih = daftar_film[pilih_film - 1]
                print(f"Anda memilih untuk menonton film: {film_dipilih}")

                while True:
                    print("\nPilih jenis tiket : ")
                    print("1. Beli tiket VIP")
                    print("2. Beli tiket reguler")
                    print("3. Kembali ke menu utama")

                    pilih_kelas_tiket = int(input("Masukkan pilihan anda : "))

                    if pilih_kelas_tiket == 1:
                        jumlah_kursi, total_harga, kursi_dipesan = pilih_bangku(daftar_kursi, film_dipilih, harga_VIP)  # Perbaikan disini
                        metode_pembayaran = input("Pilih metode pembayaran (Cash/Debit): ")
                        if metode_pembayaran.lower() == '1':
                            total_pembayaran = proses_pembayaran(total_harga)
                            totalpendapatan()  # Menampilkan total pendapatan saat ini
                            print("===Invoice===")
                            print(f"Film: {film_dipilih}")
                            print(f"Jumlah kursi: {jumlah_kursi}")
                            print(f"Kursi dipesan: {', '.join(kursi_dipesan)}")
                            print(f"Total harga: Rp. {total_harga}")
                            print("Kembalian: Rp.", kembalian)
                            print("Terima kasih!")
                        elif metode_pembayaran.lower() == '2':
                            nomor_kartu = input("Masukkan nomor kartu debit: ")
                            total_pembayaran = proses_pembayaran(total_harga)
                            totalpendapatan()  # Menampilkan total pendapatan saat ini
                            print("===Invoice===")
                            print(f"Film: {film_dipilih}")
                            print(f"Jumlah kursi: {jumlah_kursi}")
                            print(f"Kursi dipesan: {', '.join(kursi_dipesan)}")
                            print(f"Total harga: Rp. {total_harga}")
                            print("Kembalian: Rp.", kembalian)
                            print("Terima kasih!")
                        else:
                            print("Metode pembayaran tidak valid.")

                    elif pilih_kelas_tiket == 2:
                        jumlah_kursi, total_harga, kursi_dipesan = pilih_bangku(daftar_kursi, film_dipilih, harga_reguler)  # Perbaikan disini
                        metode_pembayaran = input("Pilih metode pembayaran (Cash/Debit): ")
                        if metode_pembayaran.lower() == '1':
                            total_pembayaran = proses_pembayaran(total_harga)
                            totalpendapatan() 
                            print("===Invoice===")
                            print(f"Film: {film_dipilih}")
                            print(f"Jumlah kursi: {jumlah_kursi}")
                            print(f"Kursi dipesan: {', '.join(kursi_dipesan)}")
                            print(f"Total harga: Rp. {total_harga}")
                            print("Kembalian: Rp.", kembalian)
                            print("Terima kasih!")
                        elif metode_pembayaran.lower() == '2':
                            nomor_kartu = input("Masukkan nomor kartu debit: ")
                            total_pembayaran = proses_pembayaran(total_harga)
                            totalpendapatan()  
                            print("===Invoice===")
                            print(f"Film: {film_dipilih}")
                            print(f"Jumlah kursi: {jumlah_kursi}")
                            print(f"Kursi dipesan: {', '.join(kursi_dipesan)}")
                            print(f"Total harga: Rp. {total_harga}")
                            print("Kembalian: Rp.", kembalian)
                            print("Terima kasih!")
                        else:
                            print("Metode pembayaran tidak valid.")

                    elif pilih_kelas_tiket == 3:
                        break  
                break  # Kembali ke menu utama setelah selesai memilih jenis tiket
            else:
                print("Nomor film tidak valid")

    elif pilih_menu_utama == 2:
     while True:
        print("Pilih menu:")
        print("1. Makanan")
        print("2. Minuman")
        print("3. Kembali ke menu utama")
        
        pilih_menu_makanan_minuman = int(input("Masukkan pilihan anda : "))

        if pilih_menu_makanan_minuman == 1:  
            print("Pilih makanan:")
            print("1. Popcorn Caramel")
            print("2. Popcorn Balado")
            print("3. Popcorn Original")
            print("4. Kembali ke menu utama")

            pilih_popcorn = int(input("Masukkan pilihan anda : "))

            if pilih_popcorn in [1, 2, 3]:
                ukuran_popcorn = input("Pilih ukuran popcorn (small/medium): ")
                if ukuran_popcorn.lower() == "1":
                    harga_popcorn = [30000, 30000, 30000][pilih_popcorn - 1]
                elif ukuran_popcorn.lower() == "2":
                    harga_popcorn = [55000, 55000, 55000][pilih_popcorn - 1]
                else:
                    print("Pilihan ukuran tidak valid.")
                    continue

                jumlah_popcorn = int(input("Masukkan jumlah popcorn yang ingin Anda beli: "))
                total_harga_popcorn = harga_popcorn * jumlah_popcorn

                print("Total harga popcorn: Rp.", total_harga_popcorn)

                while True:
                    pembayaran_popcorn = int(input("Masukkan jumlah uang: "))
                    if pembayaran_popcorn < total_harga_popcorn:
                        print("Jumlah uang tidak mencukupi.")
                    else:
                        break

                kembalian = pembayaran_popcorn - total_harga_popcorn
                print("Kembalian: Rp.", kembalian)
                print("Terima kasih!")
                total_pembayaran = pembayaran_popcorn
                total_pendapatan += total_pembayaran 
         
            elif pilih_popcorn == 4:
                break
            else:
                print("Pilihan tidak valid.")

        elif pilih_menu_makanan_minuman == 2: 
            print("Pilih minuman:")
            print("1. Milo (Rp. 20000)")
            print("2. Air Mineral (Rp. 10000)")
            print("3. Kembali ke menu utama")

            pilih_minuman = int(input("Masukkan pilihan anda : "))

            if pilih_minuman in [1, 2]:
                harga_minuman = [20000, 10000][pilih_minuman - 1]

                jumlah_minuman = int(input("Masukkan jumlah minuman yang ingin Anda beli: "))
                total_harga_minuman = harga_minuman * jumlah_minuman

                print("Total harga minuman: Rp.", total_harga_minuman)

                while True:
                    pembayaran_minuman = int(input("Masukkan jumlah uang: "))
                    if pembayaran_minuman < total_harga_minuman:
                        print("Jumlah uang tidak mencukupi.")
                    else:
                        break

                kembalian = pembayaran_minuman - total_harga_minuman
                print("Kembalian: Rp.", kembalian)
                print("Terima kasih!")
                total_pembayaran = pembayaran_minuman
                total_pendapatan += total_pembayaran 
            elif pilih_minuman == 3:
                break
            else:
                print("Pilihan tidak valid.")
                continue

        elif pilih_menu_makanan_minuman == 3:
            break
        else:
            print("Pilihan tidak valid.")
    
    elif pilih_menu_utama == 3:
        password_admin = "102042"  
        password_input = input("Masukkan password admin: ")
        if password_input == password_admin:
            totalpendapatan() 
        else:
            print("Password salah.")