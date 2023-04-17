def encrypt(text, shift):
    """Fungsi untuk melakukan enkripsi menggunakan Caesar cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            # Mendapatkan nilai ASCII dari karakter dan menghitung posisi baru
            new_pos = ord(char) + shift
            # Jika posisi melebihi nilai ASCII untuk huruf terakhir, kembali ke huruf pertama
            if char.isupper():
                if new_pos > ord('Z'):
                    new_pos -= 26
                elif new_pos < ord('A'):
                    new_pos += 26
            else:
                if new_pos > ord('z'):
                    new_pos -= 26
                elif new_pos < ord('a'):
                    new_pos += 26
            # Mengubah nilai ASCII ke karakter baru dan menambahkan ke hasil enkripsi
            result += chr(new_pos)
        else:
            result += char
    return result

def decrypt(text, shift):
    """Fungsi untuk melakukan dekripsi menggunakan Caesar cipher"""
    return encrypt(text, -shift)

plain_text = input('Masukan kata yang diinginkan : ')
shift = 3

encrypted_text = encrypt(plain_text, shift)
print("Hasil enkripsi:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Hasil dekripsi:", decrypted_text)
