import random

guests = {}
food_menu = ["Curry", "Fish", "Beef", "Chicken", "Steak", "Ragu"]


def read_guestlist(file_name):
    text_file = open(file_name, "r")
    n = None
    while True:
        if n is not None:
            line_data = n.strip().split(",")
        else:
            line_data = text_file.readline().strip().split(",")

        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        n = yield name, age


guest_generator = read_guestlist("guest_list.txt")

i = 0
for guest in guest_generator:
    if i < 10:
        print(guest)
        i += 1
    else:
        break

print(guest_generator.send("Jane, 35"))

# Checkpoint 4
# Define a generator expression
# that will use the guests dictionary to retrieve a generator
# of names of all guests who are 21 and over
names_generator = (name for name, age in guests.items() if age >= 21)


for name in names_generator:
    print(name)


# Checkpoint 5
def table_1():
    food = random.choice(food_menu)
    table = 1
    for i in range(1, 6):
        seat = i
        yield food, table, seat


def table_2():
    food = random.choice(food_menu)
    table = 2
    for i in range(1, 6):
        seat = i
        yield food, table, seat


def table_3():
    food = random.choice(food_menu)
    table = 3
    for i in range(1, 6):
        seat = i
        yield food, table, seat


def generate_tables():
    yield from table_1()
    yield from table_2()
    yield from table_3()


tables = generate_tables()

# -----by generator function-----------
# def table_assigner(guests, generate_tables):
#   for guest, table in zip(guests, generate_tables):
#       yield guest, table

# assign = table_assigner(guests, tables)
# print(next(assign))
# print(next(assign))
# print(next(assign))


# By generator expression
assign = ((guest, table) for guest, table in zip(guests, tables))
for _ in range(13):
    print(next(assign))
