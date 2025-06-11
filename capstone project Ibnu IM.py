Kontaklist = [
    {
        'Nama': 'Doni Pratama',
        'Company': 'PT Barito Satu',
        'Telepon': '081234567890',
        'Kategori': 'Rekan Kerja',
        'Email': 'Doni@barito.com'
    },
    {
        'Nama': 'Kania Dwi',
        'Company': 'PT Dentist Duo',
        'Telepon': '089876543210',
        'Kategori': 'Keluarga',
        'Email': 'Kaniad@gmail.com'
    },
    {
        'Nama': 'Rudi Tri Utama',
        'Company': 'Freelance',
        'Telepon': '082112345678',
        'Kategori': 'Teman',
        'Email': 'Ruditu@yahoo.com'
    },
    {
        'Nama': 'Dimas Putra',
        'Company': 'PT Bank Abadi',
        'Telepon': '081234123412',
        'Kategori': 'Bisnis',
        'Email': 'Dimasp@abadi.co.id'
    }
]

def tampilkanDetailKontak(kontak):
    print(f"Nama    : {kontak['Nama']}")
    print(f"Company : {kontak['Company']}")
    print(f"Kategori: {kontak['Kategori']}")
    print(f"Telepon : {kontak['Telepon']}")
    print(f"Email   : {kontak['Email']}")
    print('=' * 50 )

def inputTelepon():
    while True:
        telepon = input('Telepon: ')
        if telepon.isdigit():
            return telepon
        else:
            print("Nomor telepon hanya boleh berisi angka. Silakan coba lagi.")

def konfirmasiYesNo(pesan):
    while True:
        jawaban = input(pesan).strip().lower()
        if jawaban in ['yes', 'no']:
            return jawaban
        else:
            print("Input tidak valid. Harap ketik 'yes' atau 'no'.")

def tambahKontak(nama, company, kategori, email):
    telepon = inputTelepon()

    for kontak in Kontaklist:
        if kontak['Telepon'] == telepon:
            print(f"\nKontak dengan nomor '{telepon}' sudah ada.")
            return

    print("\nBerikut adalah data yang akan ditambahkan:")
    tampilkanDetailKontak({
        'Nama': nama,
        'Company': company,
        'Telepon': telepon,
        'Kategori': kategori,
        'Email': email
    })

    konfirmasi = konfirmasiYesNo("Apakah Anda yakin ingin menambahkan kontak ini? (yes/no): ")
    if konfirmasi == 'yes':
        kontakbaru = {
            'Nama': nama,
            'Company': company,
            'Telepon': telepon,
            'Kategori': kategori,
            'Email': email
        }
        Kontaklist.append(kontakbaru)
        print(f'Kontak "{nama}" berhasil ditambahkan.')
    else:
        print("Penambahan kontak dibatalkan.")

##

def tampilkanKontak():
    while True:
        print("\n=== SUBMENU TAMPILKAN KONTAK ===\n")
        print("1. Semua kontak lengkap\n")
        print("2. Daftar email\n")
        print("3. Kategori: Rekan Kerja\n")
        print("4. Kategori: Keluarga\n")
        print("5. Kategori: Teman\n")
        print("6. Kategori: Bisnis\n")
        print("7. Kembali ke menu utama\n")

        pilihan = input("Pilih submenu (1-7): ")

        if pilihan == '1':
            i = 1
            for kontak in Kontaklist:
                print(f"\n{i}. Kontak")
                tampilkanDetailKontak(kontak)
                print("=" * 50)
                i += 1
        elif pilihan == '2':
            print("\nDaftar Email:")
            i = 1
            for kontak in Kontaklist:
                print(f"{i}. Kontak \nNama   : {kontak['Nama']} \nEmail  : {kontak['Email']}")
                print('=' * 50 )
                i += 1
        elif pilihan in ['3', '4', '5', '6']:
            kategoridict = {
                '3': 'rekan kerja',
                '4': 'keluarga',
                '5': 'teman',
                '6': 'bisnis'
            }
            kategoripilihan = kategoridict[pilihan]
            hasil = [k for k in Kontaklist if k['Kategori'].lower() == kategoripilihan]
            if hasil:
                print(f"\nKontak {kategoripilihan.title()}:")
                i = 1
                for k in hasil:
                    print(f"{i}.")
                    tampilkanDetailKontak(k)
                    print()
                    i += 1
            else:
                print("Tidak ada kontak dalam kategori ini.")
        elif pilihan == '7':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def updateKontak(index, namabaru=None, companybaru=None, kategoribaru=None, teleponbaru=None, emailbaru=None):
    if 0 <= index < len(Kontaklist):
        tampilkanDetailKontak(Kontaklist[index])
        konfirmasi = konfirmasiYesNo("Apakah Anda yakin ingin mengupdate kontak ini? (yes/no): ")
        if konfirmasi == 'yes':
            if namabaru: Kontaklist[index]['Nama'] = namabaru
            if companybaru: Kontaklist[index]['Company'] = companybaru
            if kategoribaru: Kontaklist[index]['Kategori'] = kategoribaru
            if teleponbaru: Kontaklist[index]['Telepon'] = teleponbaru
            if emailbaru: Kontaklist[index]['Email'] = emailbaru
            print("Kontak berhasil diperbarui.")
        else:
            print("Update dibatalkan.")
    else:
        print("Indeks tidak valid.")

def hapusKontak(index):
    if 0 <= index < len(Kontaklist):
        kontak = Kontaklist[index]
        tampilkanDetailKontak(kontak)
        konfirmasi = konfirmasiYesNo("Yakin ingin menghapus kontak ini? (yes/no): ")
        if konfirmasi == 'yes':
            removed = Kontaklist.pop(index)
            print(f"Kontak '{removed['Nama']}' telah dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Indeks tidak valid.")

def cariKontak(keyword):
    hasil = []
    keyword = keyword.lower()
    for kontak in Kontaklist:
        if (
            keyword in kontak['Nama'].lower() or
            keyword in kontak['Company'].lower() or
            keyword in kontak['Telepon'] or
            keyword in kontak['Kategori'].lower() or
            keyword in kontak['Email'].lower()
        ):
            hasil.append(kontak)

    if hasil:
        print(f"\nHasil pencarian untuk '{keyword}':")
        i = 1
        for kontak in hasil:
            print(f"{i}.")
            tampilkanDetailKontak(kontak)
            print()
            i += 1
    else:
        print(f"Tidak ditemukan kontak yang cocok dengan kata kunci '{keyword}'.")

def tampilkanDaftarKontak():
    if not Kontaklist:
        print("\nDaftar kontak kosong.")
        return
    print("\nDaftar Kontak:")
    i = 1
    for kontak in Kontaklist:
        print(f"{i}. Kontak \nNama    : {kontak['Nama']} \nTelepon : {kontak['Telepon']} \nEmail   : {kontak['Email']}")
        print('=' * 50 )
        i += 1

def menu():
    while True:
        print("\n=== KONTAK PRIBADI ===\n")
        print("1. Tampilkan Kontak\n")
        print("2. Tambah Kontak\n")
        print("3. Update Kontak\n")
        print("4. Hapus Kontak\n")
        print("5. Cari Kontak\n")
        print("6. Keluar\n")

        pilihan = input("Pilih menu (1-6): ")
        if pilihan == '1':
            tampilkanKontak()
        elif pilihan == '2':
            print("\n=== Tambah Kontak Baru ===")
            nama = input("Nama: ")
            company = input("Company: ")
            kategori = input("Kategori: ")
            email = input("Email: ")
            tambahKontak(nama, company, kategori, email)
        elif pilihan == '3':
            tampilkanDaftarKontak()
            try:
                index = int(input("Masukkan nomor kontak yang ingin diupdate: ")) - 1
                if index < 0 or index >= len(Kontaklist):
                    print("Indeks kontak tidak valid.")
                    continue
                print("Kosongkan jika tidak ingin mengupdate data.")
                nama = input("Nama baru: ")
                company = input("Company baru: ")
                kategori = input("Kategori baru: ")
                telepon = input("Telepon baru: ")
                email = input("Email baru: ")
                updateKontak(index, nama or None, company or None, kategori or None, telepon or None, email or None)
            except ValueError:
                print("Input tidak valid.")
        elif pilihan == '4':
            tampilkanDaftarKontak()
            try:
                index = int(input("Masukkan nomor kontak yang ingin dihapus: ")) - 1
                if index < 0 or index >= len(Kontaklist):
                    print("Indeks kontak tidak valid.")
                    continue
                hapusKontak(index)
            except ValueError:
                print("Input tidak valid.")
        elif pilihan == '5':
            keyword = input("Masukkan kata kunci pencarian: ")
            cariKontak(keyword)
        elif pilihan == '6':
            print("Terima kasih telah menggunakan aplikasi kontak.")
            break
        else:
            print("Menu tidak valid. Silakan coba lagi.")
menu()