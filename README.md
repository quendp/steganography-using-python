# Super Secure Steganography using Python

---

## 📝 Code Flowchart

<img width="5500px" src="./code-flowchart.png" />
<br><br>

## ❓ What the software does?

- Selects a Program Mode, can either be encrypt or decrypt.
- Loading and Saving Image Data - gets the image's rgb data in per pixel that will either be encrypted or decrypted based on the program mode.

In encrypt mode: <br>

- Encrypting the Message using a given Key.
- Translate Key and Message from String to Binary.
- Adding the Key and Message Binary to the Image.

In decrypt mode: <br>

- Extract Key and Message Binary from Image Data.
- Translate Key and Message from Binary to String.
- Decrypt the Message using a Given Key.
- Save Decrypted Message to Text File

See a more detailed demonstration in the flowchart below.

<br><br>

## 📝 Description

“Steganography includes the concealment of information within computer files. In digital steganography, electronic
communications may include steganographic coding inside of a transport layer, such as a document file, image file,
program, or protocol. Media files are ideal for steganographic transmission because of their large size.”

- <a href="https://en.wikipedia.org/wiki/Steganography">Wikipedia on Steganography</a>

<br><br>

## 🗓️ Date Finished

February, 2022

<br><br>

## ⌛ Time Spent

1 month

<br><br>

## ⚙️ Tools and Languages

- Python
- Pillow Library
