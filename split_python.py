print("Hello World")
my_list = []
while True:
    my_input = input("Enter input or complete to end loop: ")
    if my_input == "complete":
        break
    else:
        my_list.append(int(my_input))
print(my_list)