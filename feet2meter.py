def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
	# Здесь будет ваш код
    # Удаляем 'ft' из строки и преобразуем в число
    feet = float(v[:-2])
    # Переводим футы в метры (1 фут = 0.3048 метра)
    meters = feet * 0.3048
    return meters
main()
