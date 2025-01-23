import base64

username = "admin"
password = "nimda"

def encode(text):
    encoded_bytes = text.encode('utf-8')

    for i in range(20):
        encoded_bytes = base64.b64encode(encoded_bytes)


    encoded_bytes = encoded_bytes.decode()

    encoded_bytes = encoded_bytes.replace("1","!")
    encoded_bytes = encoded_bytes.replace("2","@")
    encoded_bytes = encoded_bytes.replace("3","$")
    encoded_bytes = encoded_bytes.replace("4","^")
    encoded_bytes = encoded_bytes.replace("5","&")
    encoded_bytes = encoded_bytes.replace("6","*")
    encoded_bytes = encoded_bytes.replace("7","(")
    encoded_bytes = encoded_bytes.replace("8",")")

    return encoded_bytes

if __name__ == "__main__":
    f = open("encoded.txt","w")
    f.write("USERNAME\n")
    f.write(encode(username) + "\n\n\n")
    f.write("PASSWORD\n")
    f.write(encode(password))


    