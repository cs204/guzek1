calories_dict = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Grapefruit": 60,
    "Lime":20

}


fruit = input("Фрукт: ")

if fruit in calories_dict:
    calories = calories_dict[fruit]
    print(f"Калории: {calories}")



