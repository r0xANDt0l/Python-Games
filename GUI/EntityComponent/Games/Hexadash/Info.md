Hexadash es un juego de ritmo en el que tu eres un hexagono, y tienes que moverte entre 3 casillas en las que vienen notas y pulsar una tecla para activarla. Hay 2 tipos de notas:
1) De toque:
       - Aqui solo hay que estar en el slot y pulsar una vez
1) De mantenimiento:
        - Aqui hay que estar en el slot y mantener la tecla pulsada hasta que la nota se acabe.

Las teclas aqui son muy parecidas al Piano Tiles o al Osu!Mania, pero para que se puedas tocar la tecla, tienes que estar en la casilla

Un ejemplo de un mapa sería este (O = Jugador, - = tecla):
```
    |   ----            -       ----     -  
 O  | -         ---       -   -     --  -   ----------
    |       --              -          -
```
Depende de la precisión del toque, podras obtener:
- 300 Puntos (Perfecto)
- 100 Puntos 
- 50 Puntos
- 0 Puntos (Fallado)

Cada nota tambien añadirá 1 al contador de combo, que hara que multiplique el valor del toque por la cantidad de combo (Asi que por ejemplo, si haces un toque de 100 y tienes un combo de 20, obtendras 2000 puntos).

Al final de cada mapa, se te dará una nota con una letra, que se calculará usando un ratio

- SS: Todas las toques han dado 300 puntos
- S : No has hecho ningun toque de 0 y mas de la mitad de toques han sido de 300
- A : Menos de 5% de toques han sido 0
- B : Menos de 15% de toques han sido 0
- C : Menos de un 25% de toques han sido 0
- D : Mas de un 25% de toques han sido 0