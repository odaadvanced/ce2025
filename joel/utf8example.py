text = "Hello € 😀"
encoded = text.encode("utf-8")
print(encoded)   # b'Hello \\xe2\\x82\\xac \\xf0\\x9f\\x98\\x80'
decoded = encoded.decode("utf-8")
print(decoded)  # Write your code here :-)
