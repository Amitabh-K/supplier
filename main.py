import datetime

user_input = input("enter goal\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%y")

today_date = datetime.datetime.today()

print(deadline_date - today_date)
