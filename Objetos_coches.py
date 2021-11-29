import persistencia_pickle as pp
import car_class
import random as rd
FILE = "Coches_obj.txt"

lista_coches = pp.retrive(FILE)
if lista_coches == None:
    lista_coches = []
while True:
    marca = input("Marca :")
    if marca == 'fin':
        break
    modelo = input("Modelo :")
    combustible = input("Combustible :")
    cilindrada = input("Cilindrda :")
    ancho = input("Ancho de la rueda :")
    rodadura = input("Rodadura :")
    diametro = input("Diametro :")

    wheel = car_class.wheel (ancho, rodadura, diametro)
    coches = car_class.car(marca, modelo, combustible, cilindrada, wheel)

    lista_coches.append(coches)

    coches.wheel.set_presure(input("Presion deseada :"))

    coches.move_to(rd.random()*100, rd.random()*600)
    print("Position:", coches.get_pos)
    coches.move_inc(rd.random()*10, rd.random()*60)
    print("Position: ", coches.get_pos)
    del (coches)
    del (wheel)

pp.store(lista_coches, FILE)
lista_coches = []
print(lista_coches)

lista_coches = pp.retrive(FILE)
for car in lista_coches:
    print("marca, modelo, combustible, cilindrada:",
          car.marca, car.modelo, car.combustible, car.cilindrada)
    print("ancho, rodadura, diametro, presion:",
          car.wheel.print_info())
    print("Posicion", car.get_pos(), '\n')

