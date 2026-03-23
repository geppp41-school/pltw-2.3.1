file = open("Hard.png", "r")
output = ""


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