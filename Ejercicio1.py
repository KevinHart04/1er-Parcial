# -Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# -funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# -funcion recursiva para listar los superheroes de la lista.



# - Lista de superheroes
superheroes_marvel: list = [
    "Spider-Man",
    "Iron Man",
    "Capitan America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Doctor Strange",
    "Scarlet Witch",
    "Black Panther",
    "Ant-Man",
    "Wolverine",
    "Deadpool",
    "Captain Marvel",
    "Hawkeye",
    "Vision"
]


# - Funcion para buscar y determinar si "Capitan America" esta en la lista

def buscar_capitan_america(superheroes: list, indice: int = 0) -> bool:
    if indice >= len(superheroes):
        return False
    if superheroes[indice] == "Capitan America":
        return True
    return buscar_capitan_america(superheroes, indice + 1)

# - Funcion para listar los superheroes de la lista

def listar_superheroes(superheroes: list, indice: int = 0) -> None:
    if indice < len(superheroes):
        print(superheroes[indice])
        listar_superheroes(superheroes, indice + 1)
        

# - Verificar si "Capitan America" esta en la lista
if buscar_capitan_america(superheroes_marvel):
    print("Capitan America esta en la lista.")
else:
    print("Capitan America no esta en la lista.")

# - Listar todos los superheroes
print("\nLista de Superheroes:")
listar_superheroes(superheroes_marvel)
# - Fin del ejercicio   
