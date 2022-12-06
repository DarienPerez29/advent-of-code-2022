stream = input()

for c_index in range(len(stream) - 3):
    new_charset = ''
    is_start_of_packet = True

    for i in range(14):
        my_char = stream[c_index + i]
        if my_char not in new_charset:
            new_charset += my_char
        else:
            is_start_of_packet = False
            break

    if is_start_of_packet:
        start_of_message_marker_pos = c_index + 14
        break


print(start_of_message_marker_pos)
