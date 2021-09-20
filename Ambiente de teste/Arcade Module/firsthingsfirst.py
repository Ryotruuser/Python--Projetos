import symbol

import arcade

class Mygame2(arcade.Window):
    '''Def init standard do arcade'''
    def __init__(self,largura,altura,titulo):
        super(Mygame2,self).__init__(largura,altura,titulo,resizable=True)
        self.set_location(250,200)

        arcade.set_background_color(arcade.color.ICEBERG)

        ''' Define o angulo e a velocidade da bolinha
        tela'''
        self.c_x = 100
        self.c_y = 100
        self.x_speed = 300
        self.y_speed = 300

        '''Variaveis para mover um circulo com teclado'''
        self.player_x = 100
        self.player_y = 200
        self.player_speed = 250
        self.right = False
        self.left = False
        self.up = False
        self.down = False


    def on_draw(self):
        ''' Responsavel por desenhar na tela no momento
        está sendo desenhado um circulo e o start render
        diz para começar a desenhar qualquer coisa
        depois do comando'''
        arcade.start_render()
        arcade.draw_circle_filled(self.c_x, self.c_y, 50, arcade.color.GREEN, 20)
        arcade.draw_circle_outline(self.player_x, self.player_y, 50, arcade.color.BLUE, 2, 20)


    def update(self, delta_time):
        '''Trabalha em tempo real com os
        objetos que estão sendo renderizados na tela
        administrando ou comandandos eles da maneira
        que forem programados '''
        self.c_x += self.x_speed  * delta_time
        self.c_y += self.y_speed  * delta_time

        if self.c_x > 800 - 50 or self.c_x < 0 + 50:
            self.x_speed *= -1
        if self.c_y > 600 - 50 or self.c_y < 0 + 50:
            self.y_speed *= -1
        '''so um toque de fluidez'''
        if self.right:
            self.player_x += self.player_speed * delta_time
        if self.left:
            self.player_x -= self.player_speed * delta_time
        if self.up:
            self.player_y += self.player_speed * delta_time
        if self.down:
            self.player_y -= self.player_speed * delta_time

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

    def on_key_release(self, symbol, modifiers):
        '''Reseta a posição das teclas para
        que outras possam apertadas afinal se
        você definiu as teclas on press para True
        elas ficaram ligadas para sempre se não definires
        nada aqui correto!!!'''
        if symbol == arcade.key.RIGHT:
            self.right = False
        if symbol == arcade.key.LEFT:
            self.left = False
        if symbol == arcade.key.UP:
            self.up = False
        if symbol == arcade.key.DOWN:
            self.down = False



Mygame2(800,600,'Just a prank bro')
arcade.run()