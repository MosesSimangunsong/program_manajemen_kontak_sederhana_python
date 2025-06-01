kontak1= {'nama' : "Sabrina", 'HP': "085762330850", 'email' : "sabrinasitohang21@gmail.com"}
kontak2= {'nama' : "Moses", 'HP': "087769178674", 'email' : "simangunsongmoses21@gmail.com"}
kontak = [kontak1, kontak2]
while True:
  #Program Manajemen Kontak

  print("\nMenu Kontak")
  print("1.Melihat Semua Kontak")
  print("2.Menambahkan Kontak Baru")
  print("3.Menghapus Kontak")
  print("4.Keluar dari Aplikasi")

  pilihan = input("Masukkan pilihan :")

  if pilihan == "1":
    if kontak:
      print("Daftar Kontak:")
      for num, item in enumerate(kontak, start =1):
        print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
      print("\nKontak masih kosong!")

  elif pilihan == "2":
    nama = input("Masukkan nama kontak yang baru: ")
    no_HP = input ("Masukkan hp kontak yang baru: ")
    email = input ("Masukkan email kontak yang baru: ")
    kontak_baru = {'nama':nama , 'HP':no_HP, 'email':email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan!")


  elif pilihan == "3":
    if kontak:
      print("Daftar Kontak:")
      for num, item in enumerate(kontak, start =1):
        print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
      i_hapus= int (input("Masukkan nomor kontak yang akan dihapus: "))
      del kontak[i_hapus - 1]
      print("Kontak berhasil dihapus!")
      print("\nDaftar Kontak:")
      for num, item in enumerate(kontak, start =1):
        print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
      print("\nKontak masih kosong!")
      continue

  elif pilihan == "4":
    #Keluar dari aplikasi
    break

  else:
    #Pilihan salah
    print ("Anda Memasukkan pilihan yang salah")

print("\nKeluar dari Aplikasi")