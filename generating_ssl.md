Generating a self-signed certificate pair (PEM):

Openssl
Windows binaries for Openssl are available online
openssl req -newkey rsa:2048 -sha256 -nodes -keyout YOURPRIVATE.key -x509 -days 365 -out YOURPUBLIC.pem -subj "/C=US/ST=New York/L=Brooklyn/O=Example Brooklyn Company/CN=YOURDOMAIN.EXAMPLE"

YOURPUBLIC.pem has to be used as input for setting the self-signed webhook.

You can inspect the generated certificate with:
openssl x509 -text -noout -in YOURPUBLIC.pem

Converting from a previously generated DER:
openssl x509 -inform der -in YOURDER.der -out YOURPEM.pem

Converting from a previously generated PKCS12:
openssl pkcs12 -in YOURPKCS.p12 -out YOURPEM.pem

More information: https://www.openssl.org/