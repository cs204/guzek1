def camel_to_snake(name):
    result = [name[0].lower()]
    for char in name[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)

camel_case_name = input("Верблюжий стиль: ")
snake_case_name = camel_to_snake(camel_case_name)
print(snake_case_name)
