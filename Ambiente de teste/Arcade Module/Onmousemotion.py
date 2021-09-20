import symbol
import arcade
from math import sqrt

class Mygame2(arcade.Window):
    '''Def init standard do arcade'''
    def __init__(self,largura,altura,titulo):

        super(Mygame2,self).__init__(largura,altura,titulo,resizable=True)
        self.set_location(250,200)

        arcade.set_background_color(arcade.color.ICEBERG)
        self.green_x = 100
        self.green_y = 100

        self.blue_x = 300
        self.blue_y = 300

        self.yellow_x = 500
        self.yellow_y = 500

        self.vel_x = 0
        self.vel_y = 0

        #self.txt_x = 300
        #self.txt_y = 150


    def on_draw(self):
        ''' Responsavel por desenhar na tela no momento
        está sendo desenhado um circulo e o start render
        diz para começar a desenhar qualquer coisa
        depois do comando'''
        arcade.start_render()

        arcade.draw_circle_filled(self.green_x, self.green_y, 50, arcade.color.GREEN, 20)
        arcade.draw_circle_filled(self.blue_x, self.blue_y, 50, arcade.color.BLUE, 20)
        arcade.draw_circle_outline(self.yellow_x, self.yellow_y, 50, arcade.color.YELLOW, 2, 20)
        #arcade.draw_text(text='2020', start_x=self.txt_x, start_y=self.txt_y, color=arcade.color.RED)



    def update(self, delta_time):
        self.move_yellow_circle()

    def on_mouse_press(self, x, y, button, modifiers):
        if button  == arcade.MOUSE_BUTTON_LEFT:
            '''self.txt_x = x
            self.txt_y = y'''
            self.green_x = x
            self.green_y = y

        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.blue_x = x
            self.blue_y = y

    def on_mouse_motion(self, x, y, dx, dy):
        self.vel_x = x
        self.vel_y = y

    def move_yellow_circle(self):
        x_dist = self.vel_x - self.yellow_x
        y_dist = self.vel_y - self.yellow_y

        distance = pow(x_dist * x_dist + y_dist * y_dist, 0.5)
        #distance = sqrt(x_dist * x_dist + y_dist * y_dist )

        if distance > 1:
            self.yellow_x += x_dist * 0.1
            self.yellow_y += y_dist * 0.1




Mygame2(800,600,'Just a prank bro')
arcade.run()