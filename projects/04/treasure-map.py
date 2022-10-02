row1 = ["💼", "💼", "💼"]
row2 = ["💼", "💼", "💼"]
row3 = ["💼", "💼", "💼"]
map = [row1, row2, row3]

print(f"\n{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treasure?\n(00, 01, 02, 10, 11, 12, 20, 21, 22):\n")

row = int(position[0])
col = int(position[1])

map[row][col] = "💰"

print(f"\n{row1}\n{row2}\n{row3}\n")
