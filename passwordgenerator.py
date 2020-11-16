import secrets
import string

def get_secure_random_string(length):
    secure_str = ''.join((secrets.choice(string.ascii_letters + string.digits) for i in range(length)))
    return secure_str

print("Primer Token seguro de 8 digitos:", get_secure_random_string(8))
print("Segundo Token seguro de 10 digitos:", get_secure_random_string(10))
