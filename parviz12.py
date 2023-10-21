user_name = input("Enter your name please: ")
desired_salary_input = input("Enter your desired salary level: ")

if desired_salary_input.isdigit():
    desired_salary = int(desired_salary_input)
    tax_level = desired_salary * 0.2
    print(f"{user_name}, the tax level you will pay with the salary {desired_salary} is {tax_level}")
else:
    print(f"{user_name}, please enter your desired salary as a digit.")

    # Определение лямбда-функций для арифметических операций
    operations = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: x / y, lambda x, y: x ** y]

    # Вывод доступных операций
    print("Please choose the task you want to perform:")
    for i, operation in enumerate(["Addition", "Multiplication", "Division", "Exponentiation"], 1):
        print(f"{i}. {operation}")

    choice = int(input("User Input: "))

    numbers = input("Please enter two numbers, comma separated: ").split(',')
    x, y = float(numbers[0]), float(numbers[1])

    result = operations[choice - 1](x, y)
    print(result)

n = int(input("Please enter the length of the Fibonacci sequence: "))
fib_sequence = [1, 1]

while len(fib_sequence) < n:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

print(f"The Fibonacci sequence for {n} is:")
print(', '.join(map(str, fib_sequence)))

unique_items = set()
non_unique_items = []
task = 1

while task == 1:
    items_input = input("Please enter items separated by a comma: ")
    items = items_input.split(', ')

    for item in items:
        if items.count(item) > 1:
            non_unique_items.append((item, items.count(item)))
        else:
            unique_items.add(item)

    print("Items are saved")
    print("Unique items:", unique_items)
    print("Non-unique items:", tuple(non_unique_items))

    task = int(input("1. Enter items\n2. Exit\nUser Input: "))





