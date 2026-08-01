import base64
def encode_str(s): return base64.b64encode(s.encode()).decode()
def decode_str(s): return base64.b64decode(s.encode()).decode()