# -*- coding: utf-8 -*-
from io import StringIO
import jwt
import settings
import base64

class CertificateResource(object):

    def load_certificate(self, cert_location: str):
        try:
            content = self.export_certificate(cert_location).replace('\n', '')
            cert_str = StringIO()
            cert_str.write(f"-----BEGIN RSA PRIVATE KEY-----\n")
            cert_str.write(content)
            cert_str.write(f"\n-----END RSA PRIVATE KEY-----")
            return str(cert_str.getvalue())
        except Exception as e:
            raise SystemExit(e)

    def load_certificate_pub(self, cert_location: str):
        try:
            content = self.export_certificate(cert_location).replace('\n', '')
            cert_str = StringIO()
            cert_str.write(content)
            return str(cert_str.getvalue())
        except Exception as e:
            raise SystemExit(e)

    def export_certificate(self, cert_location):
        try:
            with open(cert_location, 'r') as f:
                return f.read()
        except Exception as e:
            raise SystemExit(e)

    def get_private_key(self):
        return self.load_certificate(settings.CERT_LOCATION)

    def get_public_key(self):
        return self.load_certificate_pub(settings.CERT_LOCATION_PUB)


if __name__ == '__main__':
    test = CertificateResource()
    private_key = test.get_private_key()
    encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256")
    public_key = test.get_public_key()
    decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
    print(decoded)
