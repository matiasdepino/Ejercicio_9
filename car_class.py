class car:
    def __init__(self, marca, modelo, combustible, cilindrada, wheel):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.wheel = wheel
        self.pos_x = 0
        self.pos_y = 0

    def move_to(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move_inc(self, x,  y):
        self.pos_x += x
        self.pos_y += y

    def get_pos(self):
        return self.pos_x, self.pos_y

#Ejercicio 9
class wheel:
    def __init__(self, ancho, diametro, rodadura):
        self.ancho = ancho
        self.diametro = diametro
        self.rodadura = rodadura
        self.presion = 0

    def set_presure(self, presion):
        self.presion = presion

    def print_info(self):
        print("Dimensiones de la rueda :", self.ancho, "/", self.diametro, "R", self.rodadura)
        print("Presión deseada :", self.presion)




