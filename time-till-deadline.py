import datetime

user_input = input("Please, enter your goal with a deadline, separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))
print(type(datetime.datetime.strptime(deadline, "%d.%m.%Y")))