
from ursina import *


def reset():
    pelotita.x = 0
    pelotita.z = -.2


def update():
    global dx, dz, puntaje_A, puntaje_B
    paleta_2.x = paleta_2.x + held_keys['right arrow'] * time.dt
    paleta_2.x = paleta_2.x - held_keys['left arrow'] * time.dt
    paleta_1.x = paleta_1.x + held_keys['d'] * time.dt
    paleta_1.x = paleta_1.x - held_keys['a'] * time.dt
    pelotita.x = pelotita.x + time.dt * dx
    pelotita.z = pelotita.z + time.dt * dz

    # comprobando limite de izquierda y derecha
    if abs(pelotita.x) > .4:
        dx = -dx

    # comprobando limite de arriba y abajo
    if pelotita.z > .25:
        puntaje_B += 1
        Audio('sounds/whistle.wav')
        print_on_screen(f'Player A: Player B = {puntaje_A}:{puntaje_B}', position=(-.85, .45), scale=2, duration=2)
        reset()

    if pelotita.z < -.65:
        puntaje_A += 1
        Audio('sounds/whistle.wav')
        print_on_screen(f'Player A : Player B = {puntaje_A}:{puntaje_B}', position=(-.85, .45), scale=2, duration=2)
        reset()

    # colisiones
    hit_info = pelotita.intersects()
    if hit_info.hit:
        if hit_info.entity == paleta_1 or hit_info.entity == paleta_2:
            Audio('sounds/pong sound.wav')
            dz = -dz


app = Ursina()

window.color = color.orange

mesa = Entity(model="cube", color=color.green, scale=(10, .5, 14), position=(0, 0, 0), texture="white_cube")

paleta_1 = Entity(parent=mesa, color=color.black, model="cube", scale=(.2, .3, .05), position=(0, 3.7, .22),
                  collider="box")
paleta_2 = duplicate(paleta_1, z=-.62)

camera.position = (0, 15, -26)
camera.rotation_x = 30

Text(text="Gamer A", scale=2, position=(-.1, .32))
Text(text="Gamer B", scale=2, position=(-.1, -.4))

linea_central = Entity(parent=mesa, model="quad", scale=(.88, .2, .1), position=(0, 3.5, -.2))
pelotita = Entity(parent=mesa, model="sphere", color=color.red, scale=.05, position=(0, 3.71, -.2), collider="box")
dx = .1
dz = .2

puntaje_A = 0
puntaje_B = 0

app.run()
