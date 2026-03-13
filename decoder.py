# file = input("What is the file you would like to decode\n>>> ")
# original_end = 468878
# line_index = 0
# message = []
# for line in file:
#     line_index += 1
#     # doesn't work, needs editing
#     if line_index > original_end:
#         message.append(line)

file = open("encoded.gif", "r+")

file.seek(468879)
data = bytes(file.buffer.read())
shift = data[len(data)-1]

def int_to_binary_string(numb):
    output = ""
    for i in range(8):
        if(numb >= 2**(8-(i+1))):
            output += "1"
            numb -= 2**(8-(i+1))
        else:
            output += "0"
    return output

def custom_binary_shift_right(binary, shift_amount = 1):
    output_array = ["0", "0", "0", "0", "0", "0", "0", "0"]
    output = ""
    zero_index = 0 + shift_amount
    index = zero_index
    for i in range(8):
        output_array[index] = binary[i]
        index += 1
        if(index == 8):
            index = 0
    for i in range(8):
        output += output_array[i]
    return output

output = ""
for i in range(len(data) -1):
    output += chr(int(custom_binary_shift_right(int_to_binary_string(data[i]), shift), 2))

print(f"the encoded message was: {output}")