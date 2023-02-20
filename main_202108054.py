from PIL import Image

# PART 1

# Main Function
def main():
    while True:
        # Select mode
        while True:
            mode = input('Select program mode: (encrypt/decrypt/exit):')
            if mode == 'encrypt' or mode == 'decrypt':
                break
            elif mode== 'exit':
                print('Thank you for using this program!')
                quit()
            else:
                print ('Invalid input, choose a different item!')

        # Asks the user for a valid filename
        while True:
            filename = input('Enter image filename:')
            try:
                Image.open(filename)
            except:
                print ('Invalid image file.')
            else:
                if filename[-4:] == "jpeg" or filename[-3:] == "jpg" :
                    break
                else:
                    print ('Invalid image file.')

        # Gets image dimension as tuple and image data as list of tuples
        image_dimension, image_data = load_image_data(filename)
        
        # If the user chose to encrypt
        if mode == 'encrypt':

            # Get the key and message from the user
            key, text = get_data_to_encrypt(image_dimension) 

            # Encrypt the message and convert encrypted message and key to binary
            encrypted_message = encrypt_text(text,key)
            bin_encrypted_mes = ascii_to_binary(char_to_ascii(encrypted_message))
            bin_key = ascii_to_binary(char_to_ascii(key))

            # Encode the message and key to the image and save the image
            modified_image_data = encode_message(image_data, bin_key, bin_encrypted_mes)
            f_name = filename.split("/")
            save_path = "output/modified_"+ f_name[-1]
            save_image_to_file(save_path, image_dimension, modified_image_data)

        # If the user chose to decrypt
        else:

            try:
                decode_message(image_data)
            except:
                print('Error: cannot decode message!')
            else:
                # Get the key and decrypted message
                binary_key, binary_encrypted_message = decode_message(image_data)
                key = binary_to_ascii_string(binary_key)
                encrypted_message = binary_to_ascii_string(binary_encrypted_message)
                decrypted_message = decrypt_text(encrypted_message,key)

                # Check the constraints in key and message
                size = image_dimension[0]*image_dimension[1]
                input_size = (6+(8*(len(key) + len(decrypted_message)))/3)
                # Secret key contains only ‘u’ or ‘d’ characters.
                for i in key:
                    if i == 'u' or i == 'd':
                        a = True
                    else:
                        a = False
                        break

                # Secret key length should be at least 3 and at most 20 characters.
                if len(key) >= 3 and len(key) <= 20:
                    b = True
                else:
                    b = False

                # Message contain characters from the ASCII table with values between 32 and 126.
                for i in decrypted_message:
                    if ord(i) >= 32 and ord(i) <= 126:
                        c = True
                    else:
                        c = False
                        break

                # Message length should be at least 10 and at most 1000 characters.
                if len(decrypted_message) >= 10 and len(decrypted_message) <= 1000:
                    d = True
                else:
                    d = False

                # Key and message fits in the image
                if size >= input_size:
                    e = True
                else:
                    e = False

                # Validity Checking
                if a == True and b == True and c == True and d == True and e == True:
                    f_name_0 = filename.split("/")
                    f_name = f_name_0[-1].split(".")
                    decrypt_filename = "output/" + f_name[0] + "_decoded_message.txt"
                    save_file(decrypt_filename,decrypted_message)

                else:
                    print('Error: cannot decode message!')

# PART 2

# Returns image_dimension and image_data
def load_image_data(filename):
    file = Image.open(filename)
    image_dimension = file.size
    image_data = list(file.getdata())
    file.close()
    return image_dimension, image_data

# Save image after encryption
def save_image_to_file(filename, image_dimension, image_data):
    file = Image.new('RGB', image_dimension, (0,0,0))
    file.putdata(image_data)
    file.save(filename, format = "png")
    file.close()

# PART 3

# 3.0 Returns secret_key and message
def get_data_to_encrypt(image_size):

    while True:

        # Variables
        secret_key = input('Enter Key:')
        message = input ('Enter Message:')
        key_len, mes_len = len(secret_key), len(message)
        size = image_size[0]*image_size[1]
        input_size = (6+(8*(key_len + mes_len))/3)

        # Secret key contains only ‘u’ or ‘d’ characters.
        for i in secret_key:
            if i == 'u' or i == 'd':
                a = True
            else:
                a = False
                break

        # Secret key length should be at least 3 and at most 20 characters.
        if key_len >= 3 and key_len <= 20:
            b = True
        else:
            b = False

        # Message contain characters from the ASCII table with values between 32 and 126.
        for i in message:
            if ord(i) >= 32 and ord(i) <= 126:
                c = True
            else:
                c = False
                break

        # Message length should be at least 10 and at most 1000 characters.
        if mes_len >= 10 and mes_len <= 1000:
            d = True
        else:
            d = False

        # Key and message fits in the image
        if size >= input_size:
            e = True
        else:
            e = False

        # Validity Checking
        if a == True and b == True and c == True and d == True and e == True:
            return secret_key, message
        elif a == False or b == False or c == False or d == False:
            print('Invalid Key/Message. Please Try again.')
        else:
            print('Message and Key cannot fit in the image.')
        

# 3.1 Encrypting the Message using a given Key
def encrypt_text(text,key):

    # Setting the conditions (for week 4 building block)
    if key == "":
        return text
    for i in key:
            if i == 'u' or i == 'd':
                a = True
            else:
                a = False
                break
    if a == False or text == "":
        return text
    else: 
        # Variables
        shift = len(key)
        key_loop = list(key)

        # Loop key if key is shorter than text
        if len(text) > len(key):
            for i in range (len(text) - len(key_loop)):
                key_loop.append(key_loop[i])
        
        # Convert the text characters to decimal
        decimal_list = []
        for j in text:
            decimal_list.append(ord(j))

        # Apply the shift in the decimal values
        encrypted_text = []
        for k in range(len(text)):
            if key_loop[k] == 'u':
                limit = decimal_list[k] + shift
                if limit > 126:
                    encrypted_text.append((limit - 126) + 31)
                else:
                    encrypted_text.append(limit)

            else: 
                limit = decimal_list[k] - shift
                if limit < 32:
                    encrypted_text.append(127 - (32 - limit))
                else:
                    encrypted_text.append(limit)
        
        # Convert decimal back to characters
        encrypted_char = []
        for l in encrypted_text:
            char = chr(l)
            encrypted_char.append(char)
        encrypted_message = ''.join(str(i) for i in encrypted_char)
        return encrypted_message

# 3.2 Translate Key and Message from String to Binary
def char_to_ascii(word):
    ascii_values= []
    for i in word:
        converted_value = ord(i)
        ascii_values.append(converted_value)
    return ascii_values

def ascii_to_binary(ascii_values):
    binary_values= []
    for value in ascii_values:
        converted_value = bin(value)[2:]
        if len(converted_value) < 8:
            diff = 8 - len(converted_value)
            converted_value = diff*'0' + converted_value
        binary_values.append(converted_value)
    return binary_values

# 3.3 Adding the Key and Message Binary to the Image
def encode_message(image_data, binary_key, binary_encrypted_message):
    
    # Variables
    delimiter = ['11111111']
    binary_list = [binary_key , delimiter , binary_encrypted_message, delimiter]

    # Combine every binary in a single list
    binary = []
    for i in binary_list:
        for j in i:
            for k in j:
                binary.append(k)

    # Combine each RGB Value in a single list            
    rgb = []
    for i in image_data:
        for j in i:
            rgb.append(j)

    # Add or subtract 1 from the RGB Values
    limit = list(range(0,len(binary)))
    index = limit[0]
    encoded = []
    for i in rgb[0:len(binary)]:
        if i%2 == 0 and binary[index] == '0':
            value = i
            encoded.append(value)
        if i%2 == 0 and binary[index] == '1':
            value = i+1
            encoded.append(value)
        if i%2 != 0 and binary[index] == '0':
            value = i-1
            encoded.append(value)
        if i%2 != 0 and binary[index] == '1':
            value = i
            encoded.append(value)
        index += 1

    # RGB Values that was not affected    
    excess = rgb[len(binary):]
    for i in excess:
        encoded.append(i)
    
    # Convert list into tuple 
    encoded_tuple = tuple(encoded)

    # Makes a list of tuples of RGB Values
    modified_image_data = []
    for i in range(0,len(encoded_tuple),3):
        modified_image_data.append((encoded_tuple[i:i+3]))
    return (modified_image_data)

# PART 4

# 4.1 Extract Key and Message Binary from Image Data
def decode_message(image_data):

    # Put RGB values in a list
    rgb = []
    for i in image_data:
        for j in i:
            rgb.append(j)

    # Turn RGB Values into binary
    binary = []
    for k in rgb:
        if k%2 == 0:
            binary.append('0')
        else:
            binary.append('1')

    # Convert binary list into tuple and make a lsit of all binary values
    binary_tuple = tuple(binary)
    binary_1 = []
    for i in range(0,len(binary_tuple),8):
        binary_1.append((binary_tuple[i:i+8]))
    
    # Find the delimeter in the list as well as the binary key and binary message
    delimiter = ('1', '1', '1', '1', '1', '1', '1', '1')
    index = [i for i, j in enumerate(binary_1) if j == delimiter]
    binary_key_0 = binary_1[0:index[0]]
    binary_encrypted_message_0 = binary_1[index[0]+1:index[1]]

    # Remove the apostrophes and the return value
    binary_key = [''.join(x) for x in binary_key_0]
    binary_encrypted_message = [''.join(x) for x in binary_encrypted_message_0]
    return binary_key , binary_encrypted_message

#4.2 Translate Key and Message from Binary to String
def binary_to_ascii_string(binary_values):
    string = ''.join([chr(int(i, 2)) for i in binary_values])
    return string

# 4.3 Decrypt the Message using a Given Key
def decrypt_text(encrypted_text,key):

    # Setting the conditions (for week 4 building block)
    if key == "":
        return encrypted_text
    for i in key:
            if i == 'u' or i == 'd':
                a = True
            else:
                a = False
                break
    if a == False or encrypted_text == "":
        return encrypted_text
    else: 

        # Variables
        shift = len(key)
        key_loop = list(key)

        # Loop key if key is shorter than text
        if len(encrypted_text) > len(key):
            for i in range (len(encrypted_text) - len(key_loop)):
                key_loop.append(key_loop[i])

        # Convert the text characters to decimal
        decimal_list = []
        for j in encrypted_text:
            decimal_list.append(ord(j))

        # Apply the shift in the decimal values
        decrypted_text = []
        for k in range(len(encrypted_text)):
            if key_loop[k] == 'd':
                limit = decimal_list[k] + shift
                if limit > 126:
                    decrypted_text.append((limit - 126) + 31)
                else:
                    decrypted_text.append(limit)

            else: 
                limit = decimal_list[k] - shift
                if limit < 32:
                    decrypted_text.append(127 - (32 - limit))
                else:
                    decrypted_text.append(limit)
        
        # Convert decimal back to characters
        decrypted_char = []
        for l in decrypted_text:
            x = chr(l)
            decrypted_char.append(x)
        decrypted_message = ''.join((i) for i in decrypted_char)
        return decrypted_message

# 4.4 Save Decrypted Message to Text File
def save_file(filename,text):
    with open(filename, 'w') as file:
        file.write(text)

if __name__ == '__main__':
    main()