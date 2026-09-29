"""
Simulador de lanzamiento de dados

Aplicación de consola que simula el lanzamiento de distintos
tipos de dados (D4, D6, D8, D10, D12 y D20). El usuario elige el tipo de
dado y la cantidad a lanzar con un maximo de 5 dados, se ve una animacion
con rich, y obtiene el resultado de cada dado, junto con el
total y el promedio de la tirada.
"""
import random

from rich.console import Console
from rich.panel import Panel
from rich.live import Live

"Constantes: número de caras de cada tipo de dado disponible"
DADO_D4 = 4
DADO_D6 = 6
DADO_D8 = 8
DADO_D10 = 10
DADO_D12 = 12
DADO_D20 = 20

MAX_DADOS = 5

console = Console()

"Menu principal"

opcion_menu = ""

while opcion_menu != "2":

    console.print(Panel(
        "[bold cyan]1[/bold cyan]. Lanzar dados\n"
        "[bold cyan]2[/bold cyan]. Salir",
    ))

    opcion_menu = input("Elige una opción (1-2): ")

    try:
        opcion_menu_numero = int(opcion_menu)
    except ValueError:
        console.print("[red]Opción no válida. Introduzca uno de los números de las opciones[/red]")
        opcion_menu = ""
        continue
    
    "Menu de tipo de dado que quieres"
    
    if opcion_menu_numero == 1:
        console.print(Panel(
            "[bold cyan]1[/bold cyan]. D4\n"
            "[bold cyan]2[/bold cyan]. D6\n"
            "[bold cyan]3[/bold cyan]. D8\n"
            "[bold cyan]4[/bold cyan]. D10\n"
            "[bold cyan]5[/bold cyan]. D12\n"
            "[bold cyan]6[/bold cyan]. D20",
            title="Elige el tipo de dado",
        ))

        tipo_dado_valido = False

        while not tipo_dado_valido:
            tipo_dado_opcion = input("Que tipo de dado quieres lanzar: ")

            try:
                tipo_dado = int(tipo_dado_opcion)
            except ValueError:
                console.print("[red]Debes introducir un número[/red]")
                continue

            if tipo_dado == 1:
                caras_dados = DADO_D4
                nombre_dado = "D4"
                tipo_dado_valido = True
            elif tipo_dado == 2:
                caras_dados = DADO_D6
                nombre_dado = "D6"
                tipo_dado_valido = True
            elif tipo_dado == 3:
                caras_dados = DADO_D8
                nombre_dado = "D8"
                tipo_dado_valido = True
            elif tipo_dado == 4:
                caras_dados = DADO_D10
                nombre_dado = "D10"
                tipo_dado_valido = True
            elif tipo_dado == 5:
                caras_dados = DADO_D12
                nombre_dado = "D12"
                tipo_dado_valido = True
            elif tipo_dado == 6:
                caras_dados = DADO_D20
                nombre_dado = "D20"
                tipo_dado_valido = True
            else:
                console.print("[red]Elige una opción válida[/red]")