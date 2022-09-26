def run():
    
    print("Funciona Maldita sea!!!")
    
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Ivan", "lastname": "Vargas"}

    super_list = [
        {"firstname": "Ivan", "lastname": "Vargas"},
        {"firstname": "Luisa", "lastname": "Ortiz"},
        {"firstname": "Angel", "lastname": "Diaz"},
        {"firstname": "Lucia", "lastname": "Carmona"},
        {"firstname": "Maria", "lastname": "Suarez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.3]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for item in super_list:
        print(item["firstname"], "-", item["lastname"])

    for i in super_list:
        print(i.items())

if __name__ == '__main__':
    run()