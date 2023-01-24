# Keygen

A keygen which generates a new key each time and adds it to a new line in a text file. 

Also checks for the same key in the file so will never create duplicate.

# How to run:

- Download or clone git. 
- Open Command Prompt or Terminal and navigate to project folder
- Type 'python keygen.py' and press enter

### Example Usage:
```
key = LicenseKey()
keyValue = key.generateKey()
print(keyValue)
```
>>Emgvk-Zpbbt-vLH4W-PbN9j-GYNjb

### Customised Usage:
```
key = LicenseKey(3,8,"--")
keyValue = key.generateKey()
print(keyValue)
```
>>Emg--Zpb--vLH--PbN--GYN--bBt--6Sd--2bV
