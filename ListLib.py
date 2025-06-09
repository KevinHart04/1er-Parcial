from typing import Any, Optional

class Lista(list):
    """
    Subclase personalizada de list con métodos para ordenar, buscar, mostrar y eliminar elementos
    usando criterios personalizados.
    """

    FUNCIONES_CRITERIO = {}

    def agregar_criterio(self, clave_criterio: str, funcion) -> None:
        """
        Agrega una función como criterio de orden o búsqueda.

        Parámetros:
            clave_criterio (str): Nombre del criterio.
            funcion (callable): Función que se usará para comparar los elementos.

        Ejemplo:
            lista.agregar_criterio("longitud", len)
        """
        self.FUNCIONES_CRITERIO[clave_criterio] = funcion

    def mostrar(self) -> None:
        """
        Muestra todos los elementos de la lista en consola, uno por línea.

        Ejemplo:
            lista = Lista([1, 2, 3])
            lista.mostrar()  # Imprime 1\n2\n3
        """
        for elemento in self:
            print(elemento)

    def eliminar_valor(self, valor, clave_criterio: str = None) -> Optional[Any]:
        """
        Elimina un valor de la lista usando un criterio de búsqueda binaria si se indica.

        Parámetros:
            valor (Any): Valor a eliminar.
            clave_criterio (str): Clave del criterio a usar para buscar.

        Retorna:
            El valor eliminado o None si no se encontró.

        Ejemplo:
            lista = Lista(["hola", "mundo"])
            lista.agregar_criterio("longitud", len)
            lista.eliminar_valor(5, "longitud")  # Elimina "mundo" si tiene len==5
        """
        indice = self.buscar(valor, clave_criterio)
        return self.pop(indice) if indice is not None else None

    def ordenar_por_criterio(self, clave_criterio: str = None) -> None:
        """
        Ordena la lista usando un criterio personalizado si se indica.

        Parámetros:
            clave_criterio (str): Clave del criterio en FUNCIONES_CRITERIO.

        Ejemplo:
            lista.ordenar_por_criterio("longitud")
        """
        criterio = self.FUNCIONES_CRITERIO.get(clave_criterio)

        if criterio is not None:
            self.sort(key=criterio)
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print("Criterio de orden no encontrado")

    def buscar(self, valor_buscado, clave_criterio: str = None) -> Optional[int]:
        """
        Busca un valor en la lista ordenada por un criterio, usando búsqueda binaria.

        Parámetros:
            valor_buscado (Any): Valor a buscar.
            clave_criterio (str): Criterio de orden/búsqueda.

        Retorna:
            Índice donde se encuentra el valor, o None si no lo encuentra o no se puede comparar.

        Ejemplo:
            lista = Lista(["hola", "mundo", "xd"])
            lista.agregar_criterio("longitud", len)
            lista.buscar(2, "longitud")  # Retorna índice del "xd"
        """
        self.ordenar_por_criterio(clave_criterio)
        inicio = 0
        fin = len(self) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            criterio = self.FUNCIONES_CRITERIO.get(clave_criterio)

            if criterio is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            valor = criterio(self[medio]) if criterio else self[medio]

            if valor == valor_buscado:
                return medio
            elif valor < valor_buscado:
                inicio = medio + 1
            else:
                fin = medio - 1

        return None
