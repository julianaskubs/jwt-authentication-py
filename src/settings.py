# -*- coding: utf-8 -*-
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REPO_PATH = os.path.join(BASE_DIR, 'repository')

CERT_LOCATION = os.path.join(REPO_PATH, 'pvt_certificate.txt')

CERT_LOCATION_PUB = os.path.join(REPO_PATH, 'pub_certificate.txt')
