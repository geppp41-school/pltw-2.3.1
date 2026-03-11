import random

file = open("40641-Dancing-Skeletons.gif", "r+")
file_data = file.buffer.read()
shift = random.randint(1, 7)
encoded_string = []
message = input("What is the message you would like to encode \n>>> ")

def int_to_binary_string(numb):
    output = ""
    for i in range(8):
        if(numb >= 2**(8-(i+1))):
            output += "1"
            numb -= 2**(8-(i+1))
        else:
            output += "0"
    return output

def custom_binary_shift_left(binary, shift_amount = 1):
    output_array = ["0", "0", "0", "0", "0", "0", "0", "0"]
    output = ""
    zero_index = 8 - shift_amount
    index = zero_index
    for i in range(8):
        output_array[index] = binary[i]
        index += 1
        if(index == 8):
            index = 0
    for i in range(8):
        output += output_array[i]
    return output


for i in range(len(message)):   
     encoded_string.append(int(str(custom_binary_shift_left(int_to_binary_string(str.encode(message[i])[0]), shift)), 2))
print(encoded_string)
encoded_string.append(int(int_to_binary_string(shift), 2))

print(bytes(encoded_string))
file_data += bytes(encoded_string) #type: ignore

with open("encoded.gif", "w") as File:
    File.buffer.write(file_data)
    File.close()
    file.close()