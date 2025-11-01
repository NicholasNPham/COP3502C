from pakuri import *
from pakudex import *

def main():

    my_store = Pakudex(5)

    print(my_store.add_pakuri("Pikachu"))
    print(my_store.add_pakuri("Bulbasaur"))
    print(my_store.add_pakuri("Bulbasaur"))
    print(my_store.add_pakuri("Psygoose"))
    print(my_store.add_pakuri("AAAA"))
    print(my_store.add_pakuri("BBBB"))
    print(my_store.add_pakuri("CCCC"))

    # my_store.my_pakudex.append(Pakuri('Pikachu'))
    # my_store.my_pakudex.append(Pakuri('Bulbasaur'))

    for each_pakuri in my_store.my_pakudex:
        print(each_pakuri.get_species(), " ", each_pakuri.get_attack())

    # obj = Pakuri("Pikachu")
    # # print(obj.get_species())
    # # print(obj.get_attack())
    # # print(obj.get_defense())
    # # print(obj.get_speed())
    # obj2 = Pakuri("Bulbasaur")
    # obj3 = Pakuri("Psygoose")
    #
    # pakudex = [obj, obj2, obj3]
    #
    # pakudex.sort()
    #
    # for each_pakuri in pakudex:
    #     print(each_pakuri.get_species(), " ", each_pakuri.get_attack())

if __name__ == "__main__":
    main()
