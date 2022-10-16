import string
import secrets


def get_key():
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for _ in range(30))
    return key


if __name__ == '__main__':
    result = get_key()
    print(result)
    