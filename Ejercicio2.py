
#-Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
#-Listado ordenado de manera ascendente por nombre de los personajes.
#-Determinar en que posicion esta The Thing y Rocket Raccoon.
#-Listar todos los villanos de la lista.
#-Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
#-Listar los superheores que comienzan con  Bl, G, My, y W.
#-Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
#-Listado de superheroes ordenados por fecha de aparación.
#-Modificar el nombre real de Ant Man a Scott Lang.
#-Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
#-Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

import ListLib
from SuperheroesData import superheroes
from colores import color, NEGRITA, ROJO, VERDE, AMARILLO, AZUL, MAGENTA, CIAN
from QueueLib import Queue


# - Se crea una clase Superhero para representar a cada personaje
class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        nombre_coloreado = color(self.name, ROJO) if self.is_villain else color(self.name, VERDE)
        flag_coloreada = color(str(self.is_villain), ROJO) if self.is_villain else color(str(self.is_villain), VERDE)
        return f"{nombre_coloreado}, {self.real_name} - {flag_coloreada}, {self.first_appearance} - {self.short_bio}"

# - Se crea una lista de superheroess
superheroes_list = ListLib.Lista()
for hero in superheroes:
    superheroes_list.append(Superhero(
        name=hero['name'],
        alias=hero['alias'],
        real_name=hero['real_name'],
        short_bio=hero['short_bio'],
        first_appearance=hero['first_appearance'],
        is_villain=hero['is_villain'],
    ))


# - Listado ordenado de manera ascendente por nombre de los personajes:

# - Funcion para determinar el criterio de ordenamiento por nombre
def ordenar_por_nombre(hero):
    return hero.name
# - se agrega el criterio de ordenamiento a la lista
superheroes_list.agregar_criterio("name", ordenar_por_nombre)
# - se ordena la lista por el criterio de nombre
superheroes_list.ordenar_por_criterio("name")


# - Determinar en que posicion esta The Thing y Rocket Raccoon

thething_position = superheroes_list.buscar("The Thing", "name")
rocket_position = superheroes_list.buscar("Rocket Raccoon", "name")
print(f"\n [*] The Thing se encuentra en la posición: {color(thething_position,ROJO)}")
print(f" [*] Rocket Raccoon se encuentra en la posición: {color(rocket_position,ROJO)}")



# - Listar todos los villanos de la lista
def listar_villanos(superheroes: list):
    print(color("\n [*] Villanos de la lista:", AMARILLO))
    for hero in superheroes:
        if hero.is_villain:
            print(hero)

listar_villanos(superheroes_list)

# - Poner villanos en una cola para determinar luego cuales aparecieron antes de 1980

cola_superheroes = Queue()
for hero in superheroes_list:
    if hero.is_villain and hero.first_appearance < 1980:
        cola_superheroes.arrive(hero)

# - Muestra los Villano que aparecieron antes de 1980
print(color("\n [*] Villanos que aparecieron antes de 1980:", MAGENTA))
while cola_superheroes.size() > 0:
    villano = cola_superheroes.attention()
    print(villano)

# - Listar los superheores que comienzan con Bl, G, My, y W

def listar_superheroes_por_prefijo(superheroes: list, prefijos: list):
    prefijos_str = ", ".join(prefijos)
    print(color(f"\n [*] Superheroes que comienzan con los prefijos: {prefijos_str}", AMARILLO))
    
    for hero in superheroes:
        if any(hero.name.startswith(prefijo) for prefijo in prefijos):
            print(hero)


prefijos = ["Bl", "G", "My", "W"]
listar_superheroes_por_prefijo(superheroes_list, prefijos)

# - Listado de personajes ordenado por nombre real de manera ascendente
def ordenar_por_nombre_real(hero):
    return hero.real_name or ""  # - Maneja el caso de nombre real vacío

superheroes_list.agregar_criterio("realname", ordenar_por_nombre_real)
superheroes_list.ordenar_por_criterio("realname")
print(color("\n [*] Listado de personajes ordenado por nombre real:", ROJO))
superheroes_list.mostrar()

# - listado de superheroes ordenados por fecha de aparación
def ordenar_por_fecha_aparicion(hero):
    return hero.first_appearance

superheroes_list.agregar_criterio("first_appearance", ordenar_por_fecha_aparicion)
superheroes_list.ordenar_por_criterio("first_appearance")
print(color("\n [*] Listado de superheroes ordenados por fecha de aparición:", AZUL))
superheroes_list.mostrar()

# - Modificar el nombre real de Ant

ant_position = superheroes_list.buscar("Ant Man", "name")
print(color("\n Nombre de Ant Man antes de modificar:", NEGRITA))
print(superheroes_list[ant_position])  # - Muestra el personaje antes de modificar
if ant_position is not None:
    superheroes_list[ant_position].real_name = "Scott Lang"
print(color("\n Nombre real de Ant modificado", NEGRITA))
print(superheroes_list[ant_position])  # - Muestra el personaje después de modificar

# - Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit

def mostrar_personajes_por_biografia(superheroes: list, palabras_clave: list):
    print(color("\n [*] Personajes con palabras clave en su biografía:", AMARILLO))
    for hero in superheroes:
        bio_resaltada = hero.short_bio
        for palabra in palabras_clave:
            if palabra in bio_resaltada:
                # - Reemplaza la palabra por una versión coloreada
                bio_resaltada = bio_resaltada.replace(palabra, color(palabra, VERDE))
        if bio_resaltada != hero.short_bio:
            print(f"{color(hero.name, CIAN)} - {bio_resaltada}")
            

palabras_clave = ["time-traveling", "suit"]
mostrar_personajes_por_biografia(superheroes_list, palabras_clave)

# - Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista

electro = superheroes_list.eliminar_valor("Electro", "name")
baron_zemo = superheroes_list.eliminar_valor("Baron Zemo", "name")

if electro:
    print(color("\n [!] Electro se encontraba en la lista y ha sido eliminado:", ROJO))
    print(color(f"Información de Electro eliminado: {electro}", ROJO))
if baron_zemo:
    print(color("\n [!] Baron Zemo se encontraba en la lista y ha sido eliminado:", ROJO))
    print(color(f"Información de Baron Zemo eliminado: {baron_zemo}", ROJO))


# - Fin del ejercicio