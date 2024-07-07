![PDF Mover](/src/images/banner.png)

# PDF Mover - Dibangun untuk Mahasiswa

## Deskripsi

Jikai kamu mahasiswa, kamu pasti pernah mengalami masalah mengorganisir jurnal referensi kamu. Saat kamu mendownload jurnal dari internet, kamu harus membuka folder Download dan memindahkan jurnah yang baru saja kamu download ke folder referensi pada penelitian yang sedang kau kerjakan.

Yang menjadi masalah adalah proses pencarian jurnal itu bukanlah proses yang sekali jalan langsung selesai. Kadang harus bolak-balik dari folder Download ke folder referensi untuk mengorganisir jurnal referensi tersebut.

Sehingga itulah program PDF Mover ini hadir untuk menyelesaikan masalah yang kamu dan aku hadapi.
Program ini memungkinkan Kamu untuk secara otomatis memantau dan memindahkan file PDF dari folder asal dan folder tujuan yang kamu tentukan. Kamu bisa mengkonfigurasi path folder asal (misalnya folder Download) untuk memantau, jika ada file PDF yang baru terdownload maka akan langsung dipindahkan ke folder tujuan tenpat kamu menyimpan semua referensimu.

## Fitur

- Memindahkan file PDF yang baru diunduh ke folder tujuan.
- Menambahkan timestamp di awal nama file yang dipindahkan.
- Menggunakan ikon khusus untuk executable.
- Konfigurasi path folder sumber dan tujuan menggunakan program terpisah.

## List Kontent

1. [Untuk Mahasiswa](#untuk-mahasiswa)

2. [Untuk Developer](#untuk-developer)


# Untuk Mahasiswa

Jika kamu sebagai Mahasiswa dan ingin menggunakan program ini, ikuti langkah-langkah berikut:

1. Download repository ini dengan cara mengklik tombol `<>code`  dan pilih 'Download ZIP'.

    ![Download Repository](/src/images/um1.png)

2. Extrack file ZIP tersebut.

3. Copy file `config.exe` dan `pdf_mover.exe` ke folder penelitian yang sedang kau kerjakan.

    ![Copy file](/src/images/um2.png)

4. Setelah itu jalankan file `config.exe`
    
    Setelah program berjalan akan muncul window terminal.

    Kemudian masukkan path asal yang akan dipantau (Misalnya path folder Download). Kemudian tekan Enter.

    Setelah itu masukkan path tujuan tempat filde pdf akan dipindahkan. Kemudian tekan Enter.

    ![Copy file](/src/images/um3.png)

    Setelah itu window akan tertutup.

5. Akan muncul sebuah file bernama `config.ino`. JANGAN HAPUS FILE INI!

6. Selanjutnya tinggal jalankan program `pdf_mover.exe` dan kamu sudah siap untuk mendownload berapapun file pdf tanpa harus memindahkannya secara manual.



# Untuk Developer

## Persyaratan

- Python 3.x
- Library Python:
  - `watchdog`
  - `configparser`
  - `shutil`
  - `os`
  - `datetime`

## Instalasi

1. **Clone repositori atau unduh file ZIP dan ekstrak**:

    ```sh
    git clone https://github.com/username/pdf-mover.git
    cd pdf-mover
    ```

2. **Install dependensi**:

    ```sh
    pip install watchdog configparser
    ```

3. **Tambahkan ikon** (Opsional):

   Pastikan Anda memiliki file ikon (`icon.ico`) yang ingin Anda gunakan dan letakkan di direktori yang sama dengan skrip Python.

## Cara Menggunakan

### Langkah 1: Konfigurasi Path Folder

1. **Jalankan program konfigurasi**:
   
    Jalankan `config.exe` untuk menentukan path folder Downloads dan references.

    ```sh
    config.exe
    ```

    Masukkan path folder saat diminta, misalnya:

    ```
    Masukkan path folder Downloads (misalnya, C:\Users\YourUsername\Downloads): C:\Users\YourUsername\Downloads
    Masukkan path folder references (misalnya, C:\Users\YourUsername\references): C:\Users\YourUsername\references
    ```

2. **Konfigurasi disimpan**:

    Program akan menyimpan path folder ke dalam file `config.ini`.

### Langkah 2: Jalankan Program Utama

1. **Jalankan `pdf_mover.exe`**:

    Jalankan program utama untuk mulai memantau folder Downloads dan memindahkan file PDF yang baru diunduh ke folder references.

    ```sh
    pdf_mover.exe
    ```

2. **Proses otomatis**:

    Program akan secara otomatis memindahkan file PDF baru dari folder Downloads ke folder references dan menambahkan timestamp di awal nama file.

## Pembuatan Executable

Jika Anda ingin membuat executable sendiri, ikuti langkah-langkah ini:

1. **Install PyInstaller**:

    ```sh
    pip install pyinstaller
    ```

2. **Buat executable untuk program konfigurasi**:

    ```sh
    pyinstaller --onefile --icon=icon.ico config.py
    ```

3. **Buat executable untuk program utama**:

    ```sh
    pyinstaller --onefile --icon=icon.ico pdf_mover.py
    ```

4. **Temukan executable**:

    File executable akan berada di dalam folder `dist`.

## Lisensi

Its Open Source ; )
