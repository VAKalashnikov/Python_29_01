from time import sleep


class TraficLight:
    __color = ["red", "yellow", "green"]

    def running(self):
        color_index = 0
        while color_index != 3:
            print(TraficLight.__color[color_index])
            if color_index == 0:
                sleep(7)
            elif color_index == 1:
                sleep(2)
            elif color_index == 2:
                sleep(10)
            color_index += 1


obj = TraficLight()
obj.running()
