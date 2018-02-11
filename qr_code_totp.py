#!/usr/bin/python

import pyotp
import os.path
import qrcode
from qrcode.image.pure import PymagingImage

b32secretFile = "otpsecret.file"
key = None

if os.path.exists(b32secretFile):
    print "load secret from %s" % b32secretFile
    with open(b32secretFile, 'rb') as fdesc:
        key = fdesc.read();
else:
    # Generate a base32 Secret Key compatible with Google 
    # Authenticator and other OTP apps
     print "create a new secret key" 
     key = pyotp.random_base32()
     with open(b32secretFile, 'wb') as fdesc:
        fdesc.write(key)
        print "secret key saved in %s" % b32secretFile

uri = pyotp.totp.TOTP(key).provisioning_uri("alice@et.esiea.fr", issuer_name="ALN App")
img = qrcode.make(uri, image_factory=PymagingImage)
