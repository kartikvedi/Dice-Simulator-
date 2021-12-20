import random
again=True
while again:
    print(random.randint(1,6))
    another_one=input("Want to roll the die again ?(y/n):")
    if another_one.lower() == 'y':
        continue
    else:
        break

