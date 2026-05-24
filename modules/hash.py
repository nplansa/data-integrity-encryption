import hashlib


# text = "Hello World!"
# hash_object = hashlib.sha256(text.encode())
# hash_digest = hash_object.hexdigest()
# print(f"The SHA  of {text} is {hash_digest}")
# print(f"The SHA  of {text} is {hash_object.hexdigest()}")

def hash_file(file_path):
    h = hashlib.new("SHA256")
    with open(file_path,"rb") as file:
        while True:
            chunk = file.read(1024)
            if chunk == b"" :
                break
            h.update(chunk)
        return h.hexdigest()
    
def verify_integrity(file_1,file_2):
    hash1 = hash_file(file_1)
    hash2 = hash_file(file_2)
    print(hash1) 
    print(hash2)
    if hash1 == hash2 :
        return "The file is intact. No changes has been made."
    else:
        return "The file has been tampered."    


if __name__ == "__main__":
    print("The SHA hash of the files are:", hash_file(r"N:\Shared\python\projects\crypto\sample_files\sample2.text"),hash_file(r"N:\Shared\python\projects\crypto\sample_files\sample.text"))
    print(verify_integrity(r"N:\Shared\python\projects\crypto\sample_files\sample2.text",r"N:\Shared\python\projects\crypto\sample_files\sample.text"))