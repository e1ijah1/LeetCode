
class CaesarCipher:

    def __init__(self, shift):
        """
        chr(int) -> char
        ord(char) -> int
        :param shift:
        """
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k+shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                # 计算偏差值取对应字母
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = 'the EAGLE is IN play: MEET AT JOE"S.'
    coded = cipher.encrypt(message)
    print(coded)
    answer = cipher.decrypt(coded)
    print(answer)
