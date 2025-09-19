print("Hello World")
my_list = []
count = 0
while True:
    my_input = input("Enter input or complete to end loop: ")
    if my_input == "complete":
        break
    else:
        my_list.append(int(my_input))
for i in my_list:
    count += 1
print(" ")
print(my_list, count)
