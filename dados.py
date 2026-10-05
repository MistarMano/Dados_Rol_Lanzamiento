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

#Constantes: número de caras de cada tipo de dado disponible
DADO_D4 = 4
DADO_D6 = 6
DADO_D8 = 8
DADO_D10 = 10
DADO_D12 = 12
DADO_D20 = 20
#Numero máximo de dados que se pueden lanzar a la vez
MAX_DADOS = 5

console = Console()


opcion_menu = ""
#Bucle principal del programa, se repite hasta que el usuario elige salir
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
    
    #Menu de tipo de dado que quieres lanzar y cantidad de dados a lanzar
    
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
            #Determina el tipo de dado y el número de caras según la opción elegida por el usuario
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
                cantidad_valida = False

        while not cantidad_valida:
            cantidad_texto = input(
                "¿Cuántos dados " + nombre_dado + " quieres lanzar? (máximo " + str(MAX_DADOS) + "): "
            )
            try:
                cantidad_dados = int(cantidad_texto)
                if cantidad_dados <= 0:
                    console.print("[red]La cantidad debe ser un número entero positivo.[/red]")
                elif cantidad_dados > MAX_DADOS:
                    console.print(
                        "[red]Solo se pueden lanzar un máximo de " + str(MAX_DADOS) + " dados a la vez.[/red]"
                    )
                else:
                    cantidad_valida = True
            except ValueError:
                console.print("[red]Entrada no válida. Introduce un número entero.[/red]")
                
        #Animacion de los dados al tirarlos que muestra un número aleatorio entre 1 y el número de caras del dado elegido
        with Live(console=console, refresh_per_second=10) as animacion:
            contador_animacion = 0
            while contador_animacion < 12:
                valor_animado = random.randint(1, caras_dados)
                animacion.update(Panel(
                    "[bold yellow]Lanzando " + str(cantidad_dados) + " x " + nombre_dado + "...[/bold yellow]\n"
                    "[white]" + str(valor_animado) + "[/white]",
                    title="Tirando...",
                    border_style="yellow"
                ))
                #Pausa para que la animación se vea durante un tiempo antes de mostrar el resultado final
                contador_espera = 0
                while contador_espera < 3000000:
                    contador_espera = contador_espera + 1

                contador_animacion = contador_animacion + 1
        #Se genera el resultado final de la tirada, mostrando el valor de cada dado, el total y el promedio
        total_tirada = 0
        resultados_texto = ""
        contador_dado = 0

        while contador_dado < cantidad_dados:
            valor_obtenido = random.randint(1, caras_dados)
            total_tirada = total_tirada + valor_obtenido

            if valor_obtenido == caras_dados:
                color_resultado = "green"
            elif valor_obtenido == 1:
                color_resultado = "red"
            else:
                color_resultado = "yellow"

            resultados_texto = (
                resultados_texto
                + "Dado " + str(contador_dado + 1) + ": "
                + "[bold " + color_resultado + "]" + str(valor_obtenido) + "[/bold " + color_resultado + "]\n"
            )

            contador_dado = contador_dado + 1

        promedio_tirada = total_tirada / cantidad_dados

        resultados_texto = (
            resultados_texto
            + "\n[bold white]Total:[/bold white] " + str(total_tirada) + "\n"
            + "[bold white]Promedio:[/bold white] " + str(round(promedio_tirada, 2))
        )

        console.print(Panel(
            resultados_texto,
            title="Resultado de la tirada (" + str(cantidad_dados) + " x " + nombre_dado + ")",
            border_style="green"
        ))

    elif opcion_menu_numero == 2:
        console.print("[bold cyan]Suerte en la siguientes tiradas[/bold cyan]")
        opcion_menu = "2"

    else:
        console.print("[red]Opción no válida. Elige 1 o 2.[/red]")