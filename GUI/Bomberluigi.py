import arcade
from arcade import key
from random import uniform

    #A game where you're a knockoff Luigi, and you plant bombs to collect coins

class bomberLuigi(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        # declare variables

        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/2, self.height/2)

        self.bomb = arcade.Sprite("Assets/")

        self.camPos = [0 , 0]

        self.speed = 1
        self.gravity = -0.5

        self.velX = 0
        self.velY = 0
        self.jumpForce = 10

        self.jump = False
        self.pixelRatio = 100

        self.coinAmt = 20
        self.coins = [arcade.Sprite("Assets/coin.png", 0.5) for i in range(self.coinAmt)]

        self.yRange = self.height / self.pixelRatio
        self.xRange = self.width / self.pixelRatio
        self.coinsPos = [(uniform(self.xRange/2 + 1, self.xRange * 2)  , uniform(-self.yRange/2, self.yRange)) for i in range(self.coinAmt)]


    def on_update(self, delta_time: float):
        #Save Position

        y = self.player.position[1]

        #Change Position

        if self.jump:
            self.velY = self.jumpForce
            self.jump = False

        

        self.velY += self.gravity

    
        y += self.velY

        # Check if it's inbounds
        if y < self.player.height/2 :
            y = self.player.height/2 # Bottom side

        #Return Position

        self.camPos[0] += self.speed * delta_time
        self.player.set_position(self.width/2, y)
        self.checkCol()

    def checkCol(self):
        for i in range(self.coinAmt):
            if self.player.collides_with_sprite(self.coins[i]):
                pos = (self.camPos[0] + uniform(self.xRange/2 + 1, self.xRange * 2),
                       uniform(-self.yRange/2, self.yRange))
                self.coinsPos[i] = pos    
                 
    def on_draw(self):
        arcade.start_render()
        for i in range(self.coinAmt):
            coinPixelPoint = (self.width/2 + (self.coinsPos[i][0] - self.camPos[0]) * self.pixelRatio, 
                          self.height/2 + (self.coinsPos[i][1] - self.camPos[1]) * self.pixelRatio )
            self.coins[i].position = coinPixelPoint 
            self.coins[i].draw()
        self.player.draw()
        

    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W or symbol == key.SPACE:
            self.jump = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == key.W or symbol == key.SPACE:
            self.jump = False

bomberLuigi()

arcade.run()