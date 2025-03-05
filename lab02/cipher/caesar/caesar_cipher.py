from cipher.caesar import BANGCHUCAI

class CaesarCipher:
    def __init__(self):
        self.bangchucai = BANGCHUCAI

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.bangchucai)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            letter_index = self.bangchucai.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = self.bangchucai[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)
    
    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.bangchucai)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            letter_index = self.bangchucai.index(letter)
            output_index = (letter_index - key) % alphabet_len
            output_letter = self.bangchucai[output_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)