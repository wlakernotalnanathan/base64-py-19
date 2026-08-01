import codec
if __name__ == '__main__':
    enc = codec.encode_str('Hello')
    print('Enc:', enc)
    print('Dec:', codec.decode_str(enc))