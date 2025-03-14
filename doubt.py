def greet_pythons(items: list) -> None:
    greeting = ['Hello']
    print(
        f'Inside the enclosing function: {greeting[0]} - ID (list): {id(greeting)}, ID (specific index): {id(greeting[0])}')

    def make_greeting(item: str) -> str:
        nonlocal greeting
        greeting = ['Hola']
        global_list.append(greeting)  # <--
        return f'{greeting[0]}, {item}! - ID (list): {id(greeting)}, ID (specific index): {id(greeting[0])}'

    for item in items:
        print(make_greeting(item))
    print(
        f'Inside the enclosing function: {greeting[0]} - ID (list): {id(greeting)}, ID (specific index): {id(greeting[0])}')


names = ['John', 'Terry', 'Graham', 'Michael', 'other Terry', 'Eric', 'Fred']
global_list = []  # <--

greet_pythons(names)