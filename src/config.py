import configparser

def create_config():
    config = configparser.ConfigParser()

    source_folder = input("Masukkan path folder Asal (misalnya, C:\\Users\\YourUsername\\Downloads): ")
    destination_folder = input("Masukkan path folder Tujuan (misalnya, C:\\Users\\YourUsername\\FolderSkripsi\\Referensi): ")

    config['Paths'] = {
        'source_folder': source_folder,
        'destination_folder': destination_folder
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("Konfigurasi telah disimpan ke config.ini")

def greating():
    gretaing = """
 ___ ___  ___   __  __  _____   _____ ___ 
| _ \   \| __| |  \/  |/ _ \ \ / / __| _ \\
|  _/ |) | _|  | |\/| | (_) \ V /| _||   /
|_| |___/|_|   |_|  |_|\___/ \_/ |___|_|_\\
                                        
Sebuah program yang dapat membantumu mengumpulkan referensi!
Dibuat oleh Zumaku.

Dokumentasi => https://github.com/zumaku/pdf_mover
============================================================
"""
    print(gretaing)
    print("[Menjalankan konfigurasi path folder]")

if __name__ == "__main__":
    greating()
    create_config()