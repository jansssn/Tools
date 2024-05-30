# Custom Wordlist Generator

Custom Wordlist Generator adalah skrip Python yang menghasilkan wordlist berdasarkan informasi pribadi yang diberikan oleh pengguna. Skrip ini meminta input seperti tanggal lahir, nama saudara kandung, dan hal-hal yang disukai untuk membuat wordlist yang lebih relevan dan personal.

## Cara Kerja

Skrip ini mengkombinasikan input yang diberikan oleh pengguna untuk membuat berbagai variasi kata yang dapat digunakan sebagai wordlist. Kombinasi ini disimpan dalam sebuah file teks yang dapat digunakan untuk tujuan pengujian keamanan atau keperluan lainnya.

## Penggunaan

### Prasyarat

Pastikan Anda memiliki Python 3 terinstal di sistem Anda.

### Menjalankan Skrip

1. Simpan skrip berikut ke dalam sebuah file, misalnya `generate_wordlist.py`:

    ```python
    import itertools
    import argparse

    def generate_custom_wordlist(birthdate, sibling_names, favorite_things, output_file):
        elements = []
        
        # Tambahkan tanggal lahir dalam berbagai format
        elements.append(birthdate)
        elements.append(birthdate.replace('-', ''))
        elements.append(birthdate.split('-')[0])  # Tahun
        elements.append(birthdate.split('-')[1])  # Bulan
        elements.append(birthdate.split('-')[2])  # Hari
        
        # Tambahkan nama saudara kandung
        elements.extend(sibling_names)
        
        # Tambahkan hal-hal yang disukai
        elements.extend(favorite_things)
        
        # Buat kombinasi kata dari elemen-elemen tersebut
        with open(output_file, 'w') as f:
            for length in range(1, len(elements) + 1):
                for combo in itertools.permutations(elements, length):
                    word = ''.join(combo)
                    f.write(word + '\n')
        
        print(f'Wordlist generated and saved to {output_file}')

    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Custom Wordlist Generator Script')
        parser.add_argument('-o', '--output', required=True, help='Output file name (e.g., wordlist.txt)')
        
        args = parser.parse_args()

        # Ambil input dari pengguna
        birthdate = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
        sibling_names = input("Masukkan nama saudara kandung (pisahkan dengan koma): ").split(',')
        favorite_things = input("Masukkan hal-hal yang disukai (pisahkan dengan koma): ").split(',')
        
        # Bersihkan input
        sibling_names = [name.strip() for name in sibling_names]
        favorite_things = [thing.strip() for thing in favorite_things]

        # Generate wordlist
        generate_custom_wordlist(birthdate, sibling_names, favorite_things, args.output)
    ```

2. Jalankan skrip dari command line dengan perintah berikut:

    ```bash
    python3 generate_wordlist.py -o wordlist.txt
    ```

3. Ikuti petunjuk di terminal untuk memasukkan informasi yang diminta:

    - Masukkan tanggal lahir (format: YYYY-MM-DD)
    - Masukkan nama saudara kandung (pisahkan dengan koma jika lebih dari satu)
    - Masukkan hal-hal yang disukai (pisahkan dengan koma jika lebih dari satu)

4. Skrip akan menghasilkan wordlist berdasarkan informasi yang Anda masukkan dan menyimpannya ke file yang Anda tentukan (misalnya, `wordlist.txt`).

### Contoh

Jika Anda memasukkan informasi berikut:

- Tanggal lahir: `1990-01-01`
- Nama saudara kandung: `John, Jane`
- Hal-hal yang disukai: `soccer, pizza`

Skrip akan menghasilkan file `wordlist.txt` yang berisi kombinasi dari informasi ini dalam berbagai format.

## Catatan

- Skrip ini menghasilkan wordlist berdasarkan kombinasi input pengguna, yang dapat menghasilkan jumlah kombinasi yang besar tergantung pada banyaknya elemen input.
- Gunakan wordlist ini dengan bijak dan hanya untuk tujuan pengujian keamanan pada sistem yang Anda miliki atau Anda memiliki izin untuk diuji.

## Lisensi

Skrip ini dilisensikan di bawah [MIT License](LICENSE).
