with open("encryption_text.txt", mode='r') as f:
    print(len(f.read().encode("utf8")))