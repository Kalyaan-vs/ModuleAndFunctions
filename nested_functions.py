def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(f'The ID of `greeting` in `greet_pythons` is {id(greeting)}: {greeting}')
    print(f'local namespace in `greet_pythons`(1): {locals()}')

    def make_greeting(item: str) -> str:
        print(f'local namespace in `make_greeting`(0): {locals()}')
        nonlocal greeting
        print(f'local namespace in `make_greeting`(1): {locals()}')
        print(f'The ID of `greeting` in `make_greeting` is {id(greeting)}: {greeting}')
        print("#" * 100)
        greeting = 'Hi'
        print(f'The ID of `greeting` in `make_greeting` is {id(greeting)}: {greeting}')
        print(f'local namespace in `make_greeting`(2): {locals()}')
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons, `greeting` is {greeting}')
    print(f'The ID of `greeting` in `greet_pythons` is {id(greeting)}: {greeting}')
    print(f'local namespace in `greet_pythons`(2): {locals()}')


names = ["Kalyaan"]  # , "Harish", "Santhosh", "Suganth", "Deepak", "Amrin"]

greet_pythons(names)

print("****************************************************************************" * 2)


# def greet_python(items: list) -> None:
#     greeting = "Hello"
#     print(f"The ID of greeting in greet_python is {id(greeting)}: {greeting}")
#     print(f"Local namespace in greet_python1(1): {locals()}")
#
#     def hello_greeting(item1: str) -> str:
#         nonlocal greeting
#         print(f"Local namespace in hello_greeting(1): {locals()}")
#         greeting = "Hi"
#         print(f"The ID of greeting in hello_greeting is {id(greeting)}: {greeting}")
#         print(f"Local namespace in hello_greeting(2): {locals()}")
#         print(f"{greeting} {item}")
#
#     for item in items:
#         hello_greeting(item)
#     print(f"The ID of greeting in great_python is {id(greeting)}: {greeting}")
#     print(f"Local namespace in greet_python1(2): {locals()}")
#
#
# names = ["Kalyaan"]  # , "Harish", "Santhosh", "Suganth", "Deepak", "Amrin"]
#
# greet_python(names)