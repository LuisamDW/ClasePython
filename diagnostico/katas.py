"""Sesión 1 — Prueba diagnóstica (45 min). Implemente cada función y ejecute:

    uv run pytest diagnostico -q

Mide: tipado, colecciones, comprensiones, funciones de orden superior, generadores,
manejo de errores, dataclasses y context managers. No requiere librerías externas.
"""

from __future__ import annotations

import string


# 1. Comprensiones -----------------------------------------------------------
def palabras_por_longitud(texto: str) -> dict[int, list[str]]:
    """Agrupa palabras únicas (minúsculas, sin puntuación) por longitud, ordenadas."""

    text = texto.lower()
    regla = str.maketrans("", "", string.punctuation)
    text = text.translate(regla)
    text = text.split()
    text = set(text)

    listado = {}

    for text in text:
        longitud = len(text)

        if longitud not in listado:
            listado[longitud] = []

        listado[longitud].append(text)

    return sorted(listado.items())


# 2. Colecciones -------------------------------------------------------------
def top_n(frecuencias: Iterable[str], n: int) -> list[tuple[str, int]]:
    """Los n elementos más frecuentes; empate → orden alfabético."""

    contador = {}
    resultado = {}

    for palabra in frecuencias:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    for letra, Frenc in contador.items():
        if Frenc == n:
            resultado[letra] = Frenc

    return sorted(resultado.items())


# 3. Funciones de orden superior / closures ----------------------------------
def reintentar(veces: int) -> Callable[[Callable[..., object]], Callable[..., object]]:
    """Decorador: reintenta la función hasta `veces` si lanza excepción; luego la propaga."""
    raise NotImplementedError


print(palabras_por_longitud("El sol, el mar y la sal."))
print(top_n(["b", "a", "b", "c", "a", "d"], 2))
