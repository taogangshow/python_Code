def creatNum():
    print("---start---")
    a,b = 0,1
    for i in range(10):
        yield b
        a,b = b,a+b
    print("---stop---")

