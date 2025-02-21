city = ["chittagong", "dhaka", "chandpur"]
country=["Bangladesh","China","Russia"]


def display(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")



display(city)
display(country)
print_list(city)
print_list(country)