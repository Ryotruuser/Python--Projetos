import symbol
import arcade
from math import sqrt

class Mygame2(arcade.Window):
    '''Def init standard do arcade'''
    def __init__(self,largura,altura,titulo):

        super(Mygame2,self).__init__(largura,altura,titulo,resizable=True)
        self.set_location(150, 250)

        arcade.set_background_color(arcade.color.BLACK)
        self.player_x = 100
        self.player_y = 200
        self.player_speed = 250

        self.sprite1 = arcade.Sprite("imagens/nave.png",center_x=100,center_y=100)

        self.right = False
        self.left = False
        self.up = False
        self.down = False


        self.bala = arcade.Sprite("imagens/yellow.png",center_y=self.player_y, center_x=self.player_x)

    def on_draw(self):
        arcade.start_render()
        self.sprite1.draw()


    def update(self, delta_time):
        if self.right:
            self.player_x += self.player_speed * delta_time
        if self.left:
            self.player_x -= self.player_speed * delta_time
        if self.up:
            self.player_y += self.player_speed * delta_time
        if self.down:
            self.player_y -= self.player_speed * delta_time
        self.sprite1.set_position(self.player_x, self.player_y)


    def on_key_press(self, symbol, modifiers):
        '''Vai permitir utilizar teclas para mover o objeto ao
        longo da tela'''
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True
        if symbol == arcade.key.SPACE:
            self.player_x = 500

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = False
        if symbol == arcade.key.LEFT:
            self.left = False
        if symbol == arcade.key.UP:
            self.up = False
        if symbol == arcade.key.DOWN:
            self.down = False
        if symbol == arcade.key.SPACE:
            self.player_x = 100

Mygame2(1024,720,'waitt for itt')
arcade.run()