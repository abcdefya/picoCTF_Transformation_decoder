# Encoded string
flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽'

# List to store the decoded values
de_flag = []

# Step 1: Iterate through each character in the encoded string
for i in range(len(flag)):
    x = ord(flag[i])
    
    # Step 2: Get the high 8 bits of the Unicode value
    de_flag.append(ord(flag[i]) >> 8)
    
    x1 = x >> 8
    c = x1 << 8
    
    # Step 3: Get the low 8 bits of the Unicode value and subtract the high 8 bits
    de_flag.append((x - c))

# Print the list of decoded values
print(de_flag)

# Step 4: Convert the integers to ASCII characters
ascii_characters = [chr(num) for num in de_flag]

# Step 5: Join the characters back into a decoded string
ascii_flag = ''.join(ascii_characters)

# Print the decoded string
print(ascii_flag)
