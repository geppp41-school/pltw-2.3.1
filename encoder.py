
_REQUIRED_FILE_TYPE = "GIF89a"
file = open("40641-Dancing-Skeletons.gif", "r+")

### use file.buffer.read to read the file
file_type = str(file.buffer.read(6))[2:8]

print(file_type)

def read_packed_feild():
    
    pass

if(file_type == _REQUIRED_FILE_TYPE):
    width = int.from_bytes(file.buffer.read(2), "little")
    height = int.from_bytes(file.buffer.read(2), "little")
    packed_feild = file.buffer.read(1)[0]
    global_color_table_flag = packed_feild & 128
    color_resolution = (packed_feild & 112) >> 4
    table_size_i_think = 2**(color_resolution+1)
    sort_flag = (packed_feild & 8) >> 3  # if this is 1 then colors are sorted most used to least used
    global_color_table_size = packed_feild & 7 #number of actual colors i think
    background_color_index = file.buffer.read(1)[0]
    file.buffer.read(1)#skipping a byte
    
    
else:
    print("file type is not GIF")


