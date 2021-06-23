import secrets
import string

def get_secure_random_string(length):
    secure_str = ''.join((secrets.choice(string.ascii_letters + string.digits) for i in range(length)))
    return secure_str

print("First 8 digit token: ", get_secure_random_string(8))
print("Second 10 digit token: ", get_secure_random_string(10))
