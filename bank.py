greeting = input("Приветствие: ")

if greeting.startswith("здравствуйте"):
    print("$0")
elif greeting.startswith("з") and not greeting.startswith("здравствуйте"):
    print("$20")
else:
    print("$100")
