def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 !=0:
    #         squares.append(i**2)
    # squeares = [i**2 for i in range(1,101) if i % 3 !=0]

    # print(squeares)
    
    # multiplos = [i for i in range(1,10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    # print(multiplos)
    

    dictionary = {"Numero": i for i in range(1,101), "Cubo": i**3 for i in range(1,101)}

if __name__ == '__main__':
    run()