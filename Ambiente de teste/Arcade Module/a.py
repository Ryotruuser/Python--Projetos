import arcade

class Mygame(arcade.Window):
    def __init__(self,largura, altura, titulo):
        super(Mygame, self).__init__(largura, altura, titulo)
        cor = arcade.color.WHITE_SMOKE
        cor2 = arcade.color.YELLOW_GREEN

        arcade.draw_text(font_name=('Arial'),font_size=35,start_x=220,start_y=500,color=cor,text='FELIZ ANO NOVO')
        arcade.draw_text(font_name=('MingLiU-ExtB'), font_size=35, start_x=350, start_y=450, color=cor2, text='2020')
        #self. set_location(400, 200)

Mygame(800,600,'Teste do Teste')
arcade.run()