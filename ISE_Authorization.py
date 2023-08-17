import base64

username = "admin"
password = "Ringnet01!"
auth_string = f"{username}:{password}"
encoded_bytes = base64.b64encode(auth_string.encode('utf-8'))
encodedAuth = encoded_bytes.decode('utf-8')

print(encodedAuth)