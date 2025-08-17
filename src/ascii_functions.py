def make_ascii_of_monster_back(filename):
    return remove_right_white_space_of_back(filename)

def make_ascii_of_monster_front(filename):
    return remove_right_white_space_of_front(filename)

def remove_row_white_space(filename):
    lines = filename.splitlines()
    return [line.rstrip("\n") for line in lines if line.strip() != ""]

def remove_left_white_space_of_back(filename):
    lines = remove_row_white_space(filename)
    current_low = min(len(line) - len(line.lstrip(" ")) for line in lines)
    return [line[current_low:] for line in lines]

def remove_left_white_space_of_front(filename):
    lines = remove_row_white_space(filename)
    current_low = min(len(line) - len(line.lstrip(" ")) for line in lines)
    return [line[current_low:] for line in lines]

def remove_right_white_space_of_back(filename):
    lines = remove_left_white_space_of_back(filename)
    return [line.rstrip(" ") for line in lines]

def remove_right_white_space_of_front(filename):
    lines = remove_left_white_space_of_front(filename)
    return [line.rstrip(" ") for line in lines]


# def remove_row_white_space(filename):
#     lines = filename.splitlines()
#     lines = [line.rstrip("\n") for line in lines if line.strip() != ""]
#     return lines

# def remove_left_white_space_of_back(filename):
#     lines = remove_row_white_space(filename)
#     current_low = float("inf")
    
#     for line in lines:
#         count = 0
#         for char in line:
#             if char == " ":
#                 count += 1
#             elif char != " ":
#                 if current_low > count:
#                     current_low = count
#                     break
#                 break
#     for i in range(len(lines)):
#         lines[i] = lines[i][max(current_low - 2, 0):]
#     return lines

# def remove_left_white_space_of_front(filename):
#     lines = remove_row_white_space(filename)
#     current_low = float("inf")
    
#     for line in lines:
#         count = 0
#         for char in line:
#             if char == " ":
#                 count += 1
#             elif char != " ":
#                 if current_low > count:
#                     current_low = count
#                     break
#                 break
#     for i in range(len(lines)):
#         lines[i] = lines[i][current_low:]
#     return lines

# def remove_right_white_space_of_back(filename):
#     lines = remove_left_white_space_of_back(filename)
#     current_low = float("inf")

#     for line in lines:
#         count = 0
#         for char in reversed(line):
#             if char == " ":
#                 count += 1
#             elif char != " ":
#                 if current_low > count:
#                     current_low = count
#                     break
#                 break
#     for i in range(len(lines)):
#         if current_low > 0:
#             lines[i] = lines[i][:-current_low]
#     return lines

# def remove_right_white_space_of_front(filename):
#     lines = remove_left_white_space_of_front(filename)
#     current_low = float("inf")

#     for line in lines:
#         count = 0
#         for char in reversed(line):
#             if char == " ":
#                 count += 1
#             elif char != " ":
#                 if current_low > count:
#                     current_low = count
#                     break
#                 break
#     for i in range(len(lines)):
    
#         if current_low > 0:
#             lines[i] = lines[i][:-current_low]
#     return lines
       