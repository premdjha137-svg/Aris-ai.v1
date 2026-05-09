import wikipedia, random, time

while True:
    print("hlo sir I am aris your personal system")
    print("I can help you with basic calculations,wikipedia search and later lot more things")

    a = input("calculate or search or exit or time: ")

    if a == "calculate":

        num1 = int(input("Any number: "))
        num2 = int(input("Any number: "))

        choose = input("Choose (+, -, *, /, %): ")

        if choose == "+":
            print(num1 + num2)

        elif choose == "-":
            print(num1 - num2)

        elif choose == "*":
            print(num1 * num2)

        elif choose == "/":
            print(num1 / num2)

        elif choose == "%":
            print(num1 % num2)

    elif a == "search":

        topic = input("so what is your topic == ")

        result = wikipedia.summary(topic)

        print(result)

    elif a == "time":

        b = time.ctime()

        print(b)

    elif a == "exit":

        print("bye")

        break
     