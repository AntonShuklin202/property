# в этой функции в качестве аргументов нужно передавать отношение
# которое можно создать с помощью функции set_otn()
def set_property(f, s): 
    first = f
    second = s
    if first == second:
        return f, s
    else:
        print("This property is not correct")
        return False
# фунция создания отношения
# в качестве аргументов требуется любое число
def set_otn(f, s):
    first = f
    second = s
    otn = first/second
    return otn
ont1 = set_otn(3, 4)
ont2 = set_otn(9, 12)
propert = set_property(ont1, ont2)
print(propert)