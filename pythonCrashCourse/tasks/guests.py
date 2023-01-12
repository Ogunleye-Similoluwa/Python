my_list = ["simi", "seun", "adeola", "henry"]
my_list.insert(0, "glory")
my_list.insert(2, "saheed")
my_list.append("samuelshola")
another_list = [my_list[2:]]
print(len(my_list))


print("\33[94mI can  only invite two people")

for name in my_list:
    print(name + " you are invited to a dinner")


for names in another_list:
    for name in names:
        print("It's no problem if you would not come ", name)

for num in my_list[2:]:
    my_list.remove(num)

print(my_list)
