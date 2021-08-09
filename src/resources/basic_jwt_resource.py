# -*- coding: utf-8 -*-
import jwt
import json

# HS256 algorithm

class BasicJWT:

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
            return False
        except Exception as e:
            raise SystemExit(e)


if __name__ == '__main__':
    payload = {
        'appKey': 'testappkey'
    }
    tr = BasicJWT()
    token = tr.create_token(payload)
    print(token)
    print(tr.validate_jwt(token))
    print(tr.validate_jwt(f'{token}123'))
