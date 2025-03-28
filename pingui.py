from vpython import *
import math

# Crear la escena
scene = canvas()

# Cabeza del pingüino
cabeza = sphere(color=color.cyan, pos=vector(0,8,0), radius=7)

# Ojos
ojo1 = sphere(color=color.yellow, pos=vector(-4,7,5), radius=2.5)
ojo2 = sphere(color=color.yellow, pos=vector(4,7,5), radius=2.5)

# Sombrero estilo Michael Jackson (hecho con cilindros)
sombrero_base = cylinder(color=color.white, pos=vector(0,14.5,0), axis=vector(-10,-65,5), radius=6, length=1)  # base del sombrero
sombrero_top = cylinder(color=color.white, pos=vector(0,15.5,0), axis=vector(10,65,5), radius=4, length=3)  # parte superior del sombrero

# Pico del pingüino
pico = cylinder(color=color.yellow, pos=vector(-0.3,5,7.5))
pico.radius1 = 3  # base del cono
pico.radius2 = 0  # punta del cono

# Cuerpo del pingüino
cuerpo1 = sphere(color=color.cyan, pos=vector(0,-5 ,0), radius=10)
cuerpo2 = sphere(color=color.white, pos=vector(0,-5.7,5), radius=7)

# Alas (esferas aplanadas)
ala_izquierda = ellipsoid(color=color.cyan, pos=vector(-10,-4,2), length=14, height=2, width=7)
ala_derecha = ellipsoid(color=color.cyan, pos=vector(10,-4,2), length=14, height=2, width=7)

# Patas (cilindros)
pata_izquierda = cylinder(pos=vector(-3,-16,2), axis=vector(0, 1, 0), radius=2.5, length=10, color=color.orange)
pata_derecha = cylinder(pos=vector(3,-16,2), axis=vector(0, 1, 0), radius=2.5, length=10, color=color.orange)

# Colocar las alas, las patas, los ojos y el pico como hijos del cuerpo
ala_izquierda.pos = cuerpo1.pos + vector(-10,1,2)
ala_derecha.pos = cuerpo1.pos + vector(10,1,2)

pata_izquierda.pos = cuerpo1.pos + vector(-3,-11,2)
pata_derecha.pos = cuerpo1.pos + vector(3,-11,2)

ojo1.pos = cabeza.pos + vector(-4,7,5)
ojo2.pos = cabeza.pos + vector(4,7,5)

pico.pos = cabeza.pos + vector(-0.3,5,7.5)

# Parámetros para la animación
amplitud = 25  # Ángulo máximo de inclinación
frecuencia = 0.1  # Control de la velocidad del balanceo
tiempo = 0
radio = 20  # Radio de la trayectoria circular
velocidad_angular = 0.01  # Velocidad de avance en el círculo
angulo_circular = 0  # Ángulo de movimiento circular

# Variable para controlar el giro gradual de la cabeza
rotacion = 0  # Comienza sin rotación

while True:
    rate(30)  # Controla la velocidad de la animación
    
    # El movimiento circular sobre el eje XZ (horizontal)
    angulo = amplitud * math.sin(frecuencia * tiempo)
    angulo_circular += velocidad_angular
    cabeza.pos = vector(radio * math.cos(angulo_circular), 8, radio * math.sin(angulo_circular))
    cuerpo1.pos = vector(radio * math.cos(angulo_circular), -5, radio * math.sin(angulo_circular))
    cuerpo2.pos = vector(radio * math.cos(angulo_circular), -5.7, radio * math.sin(angulo_circular))

    # Movimiento de las alas (giro de las alas siguiendo la cabeza)
    ala_izquierda.pos = cuerpo1.pos + vector(10,0,2)
    ala_derecha.pos = cuerpo1.pos + vector(-10,0,2)

    # Las alas giran con la cabeza (giran igual que los ojos)
    ala_izquierda.pos = cuerpo1.pos + vector(10,0,2)
    ala_derecha.pos = cuerpo1.pos + vector(-10,0,2)
    ala_izquierda.rotate(angle=math.radians(angulo), axis=vector(0,1,0), origin=ala_izquierda.pos)
    ala_derecha.rotate(angle=math.radians(angulo), axis=vector(0,-1,0), origin=ala_derecha.pos)
    
    # Movimiento de las patas (sincronizado con el cuerpo)
    pata_izquierda.pos = cuerpo1.pos + vector(-3,-11,2)
    pata_derecha.pos = cuerpo1.pos + vector(3,-11,2)
    pata_izquierda.rotate(angle=math.radians(angulo), axis=vector(0,1,0), origin=cuerpo1.pos)
    pata_derecha.rotate(angle=math.radians(angulo), axis=vector(0,1,0), origin=cuerpo1.pos)
    
    # Movimiento del sombrero
    sombrero_base.pos = cabeza.pos + vector(0,7,0)  # Sombrero sigue la cabeza
    sombrero_top.pos = cabeza.pos + vector(0,7.5,0)  # Sombrero sigue la cabeza
    
    # Movimiento de los ojos (sincronizado con la cabeza)
    ojo1.pos = cabeza.pos + vector(-4,2,4)
    ojo2.pos = cabeza.pos + vector(4,2,4)

    # Movimiento del pico (sincronizado con la cabeza)
    pico.pos = cabeza.pos + vector(-0.3,0.7,7.5)

    # Hacer que la cabeza gire con respecto al movimiento circular
    # Calcular la dirección del movimiento (hacia donde apunta la cabeza)
    direccion = vector(-math.sin(angulo_circular), 0, math.cos(angulo_circular))
    
    # Rotar la cabeza para que siempre esté orientada hacia el movimiento
    cabeza.up = direccion
    tiempo += 1

    # Lógica para la rotación gradual de la cabeza al llegar a la parte posterior del círculo
    if angulo_circular < math.pi * 0.6:
        # Interpolamos el giro suavemente entre 0 y pi a medida que avanzamos
        rotacion = min(rotacion + 0.03, math.pi)  # Incrementa la rotación gradualmente hasta pi
    
        # Aplicamos la rotación gradual en la cabeza, los ojos y el pico
    cabeza.rotate(angle=math.radians(angulo), axis=vector(0,-1,0), origin=cabeza.pos)
    ojo1.rotate(angle=math.radians(angulo), axis=vector(0,-1,0), origin=cabeza.pos)
    ojo2.rotate(angle=math.radians(angulo), axis=vector(0,-1,0), origin=cabeza.pos)
    pico.rotate(angle=math.radians(angulo), axis=vector(0,-0.5,0), origin=cabeza.pos)
    cuerpo1.rotate(angle=math.radians(angulo), axis=vector(0,-1,0), origin=cuerpo1.pos)
        #ala_izquierda.rotate(angle=rotacion, axis=vector(0,-1,0), origin=ala_izquierda.pos)
        #ala_derecha.rotate(angle=rotacion, axis=vector(0,-1,0), origin=ala_derecha.pos)'''


    # Actualizamos el tiempo
   
