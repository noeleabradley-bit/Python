print("Hello World")

x = 5
y = "John"
z = 87.45678
a, b, c = "Orange", "Banana", "Cherry"
list1 = ["abc", 34, True, 40, "male"]
S1 = " STR,IN,G1 "
L1 = ["STR1", 123, True, 123.456]

print(x, y, type(y), a, b, c)
print(f"Format string int {x}, String {y}, float 3 DP {z:.2f} {type(y)}, {a}, \t {b + ' ' + y}, \n c ")


print(list1)
print("Length = " + str(len(list1)) + ", Type = " + str(type(list1)))
print(f"Length = {len(list1)} ")


print(f" List Vs String: Type = {type(S1)} Vs {type(L1)}, Length = {len(S1)} Vs {len(L1)} ")
print(f"Indexing content, Str 1st to 4th = {S1[:4]}, 4th last to end {S1[-4:]} ")
print(f"Indexing content, List 1st to 4th = {L1[:4]}, 4th last to end {L1[-4:]} ")

print(f"UP = {S1.upper()}, Low = {S1.lower()}, strip = {S1.strip()}, Find IN {S1.find("IN")}, Split = {S1.split(",")}")
print(f"STR1 = {S1}, Replace IN MM, {S1.replace("IN","MM")}")
