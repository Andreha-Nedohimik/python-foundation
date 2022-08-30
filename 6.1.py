from itertools import  cycle
from time import sleep

class TratticLight:
    __color = [["red", [7, 31]], ["yellow", [2,33]], ["green", [7,32]], ["yellow", [2, 33]]]

    def runnning(self):
        for light in cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            sleep(light[1][0])


TratticLight_1 = TratticLight()
TratticLight_1.runnning()