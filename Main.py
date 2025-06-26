from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale=0.5, collider='box')
camera.parent = player
camera.position = (0, 10, -20)
camera.rotation_x = 30

walls = []
for z in range(10):
    for x in range(10):
        if (x, z) not in [(0,0), (9,9), (4,5), (5,5), (6,5), (7,5)] and (x % 2 == 0 or z % 2 == 0):
            walls.append(Entity(model='cube', color=color.gray, position=(x,0,z), collider='box'))

goal = Entity(model='cube', color=color.green, position=(9,0,9), scale=0.5)

def update():
    speed = 5 * time.dt
    if held_keys['w']: player.z += speed
    if held_keys['s']: player.z -= speed
    if held_keys['a']: player.x -= speed
    if held_keys['d']: player.x += speed

    # Colisión con meta
    if distance(player.position, goal.position) < 0.75:
        print('¡Ganaste!')
        application.quit()

app.run()
