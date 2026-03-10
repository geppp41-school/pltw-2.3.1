import random
_REQUIRED_FILE_TYPE = "GIF89a"
file = open("40641-Dancing-Skeletons.gif", "r+")


### use file.buffer.read to read the file
file_type = str(file.buffer.read(6))[2:8]
file_end = 468878
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890_-+={[]}\\|;:\'\",<.>/?`~".replace("", " ").split(" ")
message = input("What is the message you would like to encode \n>>> ")
shift = random.randint(1, 7)
encoded_string = [int(str(shift), 2)]
file_data = file.buffer.read(file_end)
print(int(str.encode(chars[1])[0]) << shift)


for i in range(len(message)):
    encoded_string.append(int(str(str.encode(message[i])[0]), 2) << shift)

file_data += bytes(encoded_string) #type: ignore
# with open("encoded.gif", "w") as File:
#     File.write(file_str)
#     File.close()

# print(file_type)

# find end of file
file.seek(file_end, 0)

# print(file.buffer.read(1))
# if(file_type == _REQUIRED_FILE_TYPE):
#     width = int.from_bytes(file.buffer.read(2), "little")
#     height = int.from_bytes(file.buffer.read(2), "little")
#     packed_field = file.buffer.read(1)[0] #type: ignore
#     global_color_table_flag = packed_field & 128
#     color_resolution = (packed_field & 112) >> 4
#     table_size_i_think = 2**(color_resolution+1)
#     sort_flag = (packed_field & 8) >> 3  # if this is 1 then colors are sorted most used to least used
#     global_color_table_size = packed_field & 7 #number of actual colors i think
#     background_color_index = file.buffer.read(1)[0] #type: ignore
#     file.buffer.read(1) #skipping a byte
    
    
# else:
#     print("file type is not GIF")


# get user message input
# shift each char in the message to the left by a random amount through something like print(int(str.encode(chars[1])[0]) << 6)
# add the encoded message to the end of the file with the amount it's shifted by at the start of the encoded message