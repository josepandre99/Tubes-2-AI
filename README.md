# Tugas Besar 2 IF 3170 Inteligensi Buatan
## Deteksi Bentuk Dasar Geometri berdasarkan Knowledge Based System

### Anggota Kelompok :
###### -Suhailie - 13517045
###### -Vijjasena - 13517084
###### -Josep Andre Ginting - 13517108
###### -Nando Rusrin Pratama - 13517148


### Petunjuk

  Untuk menggunakan program, terlebih dahulu diperlukan library - library seperti pyclips dan opencv. Jika belum terpasang, maka di install dengan :
    pip install numpy
    pip install opencv
    pip install clipspy 

	Setelah terpasang, maka jalankan file ‘tk_GUI.py’ dengan menggunakan Python 3 atau jalankan file 'tk_GUI.exe'. 

Gambar di sebelah kiri atas merupakan input gambar dari hasil browse.
Gambar di sebelah kanan atas merupakan pilihan gambar. Dengan menekan tombol ‘DETECT’, maka proses inferencing akan dilakukan dengan mendeteksi bentuk kedua gambar tersebut.
	
  Hasil dari tombol ‘DETECT’ memberikan hasil perbandingan gambar di kiri dengan gambar di kanan. 
Bila tidak ada, maka akan diberitahu bahwa tidak ada persamaan.
Bila serupa, maka akan diberitahu bahwa bentuknya serupa tapi tidak sama.
Bila sama, maka akan diberitahu bahwa terdapat gambar yang sama.
	
Kolom ‘Matched Facts’ merupakan kolom yang berisi fakta yang dihasilkan oleh CLIPS.
Kolom ‘Detection Image’ akan menampilkan gambar hasil deteksi bila sama atau serupa.
Kolom ‘Activated Rules’ merupakan rule yang diaktivasi oleh CLIPS.

