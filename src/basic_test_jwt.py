# -*- coding: utf-8 -*-
import jwt
import json
import base64

# HS256 algorithm

class TokenResource:

    def get_security_key(self):
        return 'testsecuritykey'

    def get_application_key(self):
        return 'testappkey'

    def create_token(self, payload):
        key = str(self.get_security_key)
        encoded = jwt.encode(payload, key, algorithm="HS256")
        return encoded

    def validate_jwt(self, encoded):
        try:
            key = str(self.get_security_key)
            decoded = jwt.decode(encoded, key, algorithms="HS256")
            if decoded:
                print(decoded)
                return True
        except Exception as e:
            print(f'Error trying to decode jwt: {e}')
            return False


if __name__ == '__main__':
    payload = {
        'appKey': 'testappkey'
    }
    tr = TokenResource()
    token = tr.create_token(payload)
    print(token)
    decoded = tr.validate_jwt(token)
    print(decoded)
    decoded = tr.validate_jwt(f'{token}123')
    print(decoded)
