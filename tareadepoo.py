"""Examen del tema 1"""
import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Desafío de Estrategia")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)  # Fondo gris
LIGHT_GRAY = (200, 200, 200)  # Botón activo
DARK_GRAY = (100, 100, 100)  # Botón inactivo

# Fuente
font = pygame.font.Font(None, 36)


def mostrar_texto(texto, x, y, color=BLACK):
    """Función para mostrar texto en la pantalla."""
    text_surface = font.render(texto, True, color)
    screen.blit(text_surface, (x, y))


def dibujar_boton(texto, x, y, ancho, alto, activo):
    """Dibuja un botón y cambia de color si está activo."""
    color = LIGHT_GRAY if activo else WHITE
    pygame.draw.rect(screen, color, (x, y, ancho, alto))
    text_surface = font.render(texto, True, BLACK)
    screen.blit(text_surface,
                (x + (ancho - text_surface.get_width()) // 2, y + (alto - text_surface.get_height()) // 2))


def esperar_continuar(puntos, tiempo):
    """Espera hasta que el jugador haga clic en el botón 'Next' o 'Salir'."""
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        next_activo = WIDTH // 2 - 50 <= mouse_x <= WIDTH // 2 + 50 and HEIGHT // 2 <= mouse_y <= HEIGHT // 2 + 40
        salir_activo = WIDTH // 2 - 50 <= mouse_x <= WIDTH // 2 + 50 and HEIGHT // 2 + 60 <= mouse_y <= HEIGHT // 2 + 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_activo:
                    return "continuar"
                if salir_activo:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "continuar"

        # Dibujar pantalla y botones con interacción
        screen.fill(GRAY)
        mostrar_texto(f"Puntos: {puntos}", 20, 20)
        mostrar_texto(f"Tiempo : {tiempo}", 20, 60)
        dibujar_boton("Next", WIDTH // 2 - 50, HEIGHT // 2, 100, 40, next_activo)
        dibujar_boton("Salir", WIDTH // 2 - 50, HEIGHT // 2 + 60, 100, 40, salir_activo)
        pygame.display.flip()


def mostrar_puntuacion(puntos, tiempo_total):
    """Muestra la puntuación final y el tiempo total."""
    screen.fill(GRAY)
    mostrar_texto(f"Puntuación final: {puntos}", 20, 20)
    mostrar_texto(f"Tiempo total: {tiempo_total:.2f} segundos", 20, 60)
    mostrar_texto("¡Felicidades! Has terminado el juego.", 20, 100)
    dibujar_boton("Salir", WIDTH // 2 - 50, HEIGHT // 2, 100, 40, True)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                pygame.quit()
                sys.exit()


def pedir_nombre():
    """Función para pedir el nombre del jugador."""
    input_text = ""
    while True:
        screen.fill(GRAY)
        mostrar_texto("Introduce tu nombre: " + input_text, 20, 20)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text  # Devuelve el nombre cuando presione Enter
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode


def mostrar_instrucciones(nombre):
    """Muestra las instrucciones del juego."""
    screen.fill(GRAY)
    mostrar_texto(f"Bienvenido {nombre}!", 20, 20)
    mostrar_texto("Este es un juego de desafíos de estrategia.", 20, 60)
    mostrar_texto("Debes resolver varios desafíos para ganar puntos.", 20, 100)
    mostrar_texto("Alcanza 9 puntos para ganar el juego.", 20, 140)
    dibujar_boton("Comenzar", WIDTH // 2 - 50, HEIGHT // 2, 100, 40, True)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                return  # Sale de la pantalla de instrucciones y comienza el juego


def jugar():
    nombre = pedir_nombre()  # Solicitar el nombre del jugador
    mostrar_instrucciones(nombre)  # Mostrar instrucciones con el nombre del jugador
    puntos = 0
    desafios = [("memoria", 1), ("matematicas", 1), ("adivinacion", 1)]  # Ajustar dificultad
    tiempo_total = 0  # Inicializa el tiempo total

    while puntos < 9:  # Mientras que el puntaje sea menor a 9
        for desafio, puntaje in desafios:
            screen.fill(GRAY)

            # Inicializa el temporizador para cada desafío
            tiempo_restante = 0  # Tiempo en segundos, inicia en 0
            inicio_tiempo = pygame.time.get_ticks()  # Tiempo inicial

            mostrar_texto(f"Desafío: {desafio.capitalize()}", 20, 20)

            if desafio == "memoria":
                secuencia = [random.randint(1, 20) for _ in range(random.randint(3, 5))]  # Se ajusta la cantidad para que sea más fácil
                mostrar_texto(f"Recuerda esta secuencia: {secuencia}", 20, 60)
                pygame.display.flip()
                pygame.time.delay(4000)  # Tiempo de visualización
                screen.fill(GRAY)

                # Selecciona un índice aleatorio de la secuencia
                indice_pregunta = random.randint(0, len(secuencia) - 1)
                pregunta = f"¿Cuál fue el número en la posición {indice_pregunta + 1}?"

                mostrar_texto(pregunta, 20, 60)
                input_text = ""
                continuar = True
                while continuar:
                    tiempo_transcurrido = (pygame.time.get_ticks() - inicio_tiempo) / 1000
                    tiempo_restante = max(0, int(tiempo_transcurrido))

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                if input_text.isdigit() and int(input_text) == secuencia[indice_pregunta]:
                                    if 0 <= tiempo_restante <= 10:  # Ajuste de tiempo
                                        puntos += 1
                                continuar = False
                            elif event.key == pygame.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                input_text += event.unicode

                    screen.fill(GRAY)
                    mostrar_texto(f"Desafío: {desafio.capitalize()}", 20, 20)
                    mostrar_texto(pregunta, 20, 60)
                    mostrar_texto("Respuesta: " + input_text, 20, 100)
                    mostrar_texto(f"Tiempo: {tiempo_restante}", WIDTH - 150, 20)
                    dibujar_boton("Next", WIDTH // 2 - 50, HEIGHT // 2, 100, 40, True)
                    pygame.display.flip()

                # Espera el botón "Next"
                esperar_continuar(puntos, tiempo_restante)

            elif desafio == "matematicas":
                num1 = random.randint(1, 10)  # Dificultad ajustada
                num2 = random.randint(1, 10)  # Dificultad ajustada
                operacion = random.choice(["+", "-", "*"])
                if operacion == "+":
                    respuesta = num1 + num2
                    pregunta = f"{num1} + {num2} = ?"
                elif operacion == "-":
                    respuesta = num1 - num2
                    pregunta = f"{num1} - {num2} = ?"
                else:
                    respuesta = num1 * num2
                    pregunta = f"{num1} * {num2} = ?"

                input_text = ""
                continuar = True
                while continuar:
                    tiempo_transcurrido = (pygame.time.get_ticks() - inicio_tiempo) / 1000
                    tiempo_restante = max(0, int(tiempo_transcurrido))

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                if input_text.isdigit() and int(input_text) == respuesta:
                                    if 0 <= tiempo_restante <= 10:  # Ajuste de tiempo
                                        puntos += 1
                                continuar = False
                            elif event.key == pygame.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                input_text += event.unicode

                    screen.fill(GRAY)
                    mostrar_texto(f"Desafío: {desafio.capitalize()}", 20, 20)
                    mostrar_texto(pregunta, 20, 60)
                    mostrar_texto("Respuesta: " + input_text, 20, 100)
                    mostrar_texto(f"Tiempo: {tiempo_restante}", WIDTH - 150, 20)
                    dibujar_boton("Next", WIDTH // 2 - 50, HEIGHT // 2, 100, 40, True)
                    pygame.display.flip()

                # Espera el botón "Next"
                esperar_continuar(puntos, tiempo_restante)

            elif desafio == "adivinacion":
                numero_secreto = random.randint(1, 3)  # Número entre 1 y 3
                input_text = ""
                continuar = True
                while continuar:
                    tiempo_transcurrido = (pygame.time.get_ticks() - inicio_tiempo) / 1000
                    tiempo_restante = max(0, int(tiempo_transcurrido))

                    screen.fill(GRAY)  # Asegurarse de limpiar la pantalla en cada ciclo
                    mostrar_texto("Adivina un número entre 1 y 3:", 20, 60)
                    mostrar_texto("Respuesta: " + input_text, 20, 100)
                    mostrar_texto(f"Tiempo: {tiempo_restante}", WIDTH - 150, 20)
                    dibujar_boton("Next", WIDTH // 2 - 50, HEIGHT // 2, 100, 40, True)  # Botón para continuar
                    pygame.display.flip()  # Actualiza la pantalla

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                if input_text.isdigit() and int(input_text) == numero_secreto:
                                    if 0 <= tiempo_restante <= 10:  # Ajuste de tiempo
                                        puntos += 1
                                continuar = False
                            elif event.key == pygame.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                input_text += event.unicode

                # Espera el botón "Next"
                esperar_continuar(puntos, tiempo_restante)

            tiempo_total += (pygame.time.get_ticks() - inicio_tiempo) / 1000  # Acumula el tiempo total

    mostrar_puntuacion(puntos, tiempo_total)


# Ejecutar el juego
if __name__ == "__main__":
    jugar()

