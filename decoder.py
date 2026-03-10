file = input("What is the file you would like to decode\n>>> ")
original_end = 468878
line_index = 0
message = []
for line in file:
    line_index += 1
    # doesn't work, needs editing
    if line_index > original_end:
        message.append(line)