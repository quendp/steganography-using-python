

def char_to_ascii(data_list):
    ascii_values= []
    for value in data_list:
        converted_value = ''
        ### Do not modify anything above this line ###
        # insert your code here #
        converted_value = ord(value)
        ### Do not modify anything below this line ###
        ascii_values.append(converted_value)
    return ascii_values
    
def ascii_to_binary(data_list):
    binary_values= []
    for value in data_list:
        converted_value = ''
        ### Do not modify anything above this line ###
        # insert your code here #
        converted_value = bin(value)[2:]
        ### Do not modify anything below this line ###
        binary_values.append(converted_value)
    return binary_values

if __name__ == "__main__":
    word = input()
    ascii_data = char_to_ascii(word)
    binary_data = ascii_to_binary(ascii_data)
    for character, ascii, binary in zip(word, ascii_data, binary_data):
        print('{}: {} - {}'.format(character, ascii, binary))