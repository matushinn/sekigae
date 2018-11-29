import random

import random


def seat_shuffle():
    with  open("members.txt", mode="r") as f:

        members_list = f.read()
        members = members_list.split("\n")

        shuffle1 = random.sample(members, 6)
        for i in range(0, len(shuffle1)):
            members.remove(shuffle1[i])

        shuffle2= random.sample(members, 5)

        for i in range(0, len(shuffle2)):
            members.remove(shuffle2[i])

        shuffle3 = members

        print(f"table1 :{shuffle1}\n"
              f"table2 :{shuffle2}\n"
              f"table3 :{shuffle3}"
              )




if __name__ == "__main__":
    seat_shuffle()