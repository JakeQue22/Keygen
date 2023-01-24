from licensekeygenerator import LicenseKey

file_path = "generated-keys.txt"
key = LicenseKey(5,5,"-")
keyValue = key.generateKey()

if keyValue in file_path:
	keyValue = key.generateKey()
	print(keyValue)
else:
	print(keyValue)


with open(file_path, 'a') as file:
    file.write(keyValue + "\n")
