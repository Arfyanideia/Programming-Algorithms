#kELOMPOK 2
#Program Penambahan Prokduk

Produk <- c()
Jumlah <- c()

repeat{
  writeLines("[+]== MENU ==[+]\n1. Tambah Produk\n2. Tampilkan Produk")

  choice = readline("Pilih Menu : ")
  if(choice == 1){
    n = readline("Banyak Produk yang akan ditambah : ")
    for(i in 1 : n){
      nama_produk = readline("Nama Produk : ")
      jumlah_produk = readline("Jumlah Produk : ")
      jumlah_produk = as.integer(jumlah_produk)
      
      Produk <- append(Produk, nama_produk)
      Jumlah <- append(Jumlah, jumlah_produk)
    }
    
    
  } else if(choice == 2){
    class.df <- data.frame(Produk, Jumlah)
    print(class.df)
  } else{
    "Menu yang anda masukkan salah!"
  }
  lanjut = readline("Apakah anda ingin melanjutkan program ini ? (y/n) : ")
  if(lanjut != "y"){
    break
  }
}

