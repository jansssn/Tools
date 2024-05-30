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
