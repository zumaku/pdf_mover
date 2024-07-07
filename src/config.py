import configparser

def create_config():
    config = configparser.ConfigParser()

    source_folder = input("Masukkan path folder Downloads (misalnya, C:\\Users\\YourUsername\\Downloads): ")
    destination_folder = input("Masukkan path folder references (misalnya, C:\\Users\\YourUsername\\FolderSkripsi\\Referensi): ")

    config['Paths'] = {
        'source_folder': source_folder,
        'destination_folder': destination_folder
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("Konfigurasi telah disimpan ke config.ini")

if __name__ == "__main__":
    create_config()