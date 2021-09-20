from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from random import randint


class test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        self.label = Label (text='DAMN')
        bot1 = Button(text="Touch me and i'll give you a number",size_hint_y=None,on_press=self.number)
        bot2 = Button(text= 'Same as the douchebag above you',width=10,size_hint_y=None,on_release=self.letter)
        box.add_widget(bot1)
        box.add_widget(self.label)
        box.add_widget(bot2)

        return box
    def number(self,bot1):
        x= randint(1,100)
        self.label.text= str(x)

    def letter(self,bot2):
        x = randint(1,10)
        if x == 1:
            self.label.text = 'Nunca é tão fácil perder-se como quando se julga conhecer o caminho'
        if x == 2:
            self.label.text = 'Jamais se desespere em meio as sombrias aflições de sua vida, pois das nuvens mais negras cai água límpida e fecunda'
        if x == 3:
            self.label.text = 'Positivo, o bagulho e doido e o processo e lento'
        if x == 4:
            self.label.text = 'Agua coca latão pra gringo e mas caro ein'
        if x == 5:
            self.label.text = 'Ih mane olha la o gringo usando a camisa do colegio municipal filma la'
        if x == 6:
            self.label.text = 'i am a different man in the show'
        if x == 7:
            self.label.text = 'Freefas e jogo de maluco '
        if x == 8:
            self.label.text = 'Eu picko udyr independente do matchup'
        if x == 9:
            self.label.text = 'I felt bad '
        if x == 10:
            self.label.text = 'this beat is sicky man this token shit is real lit look at this wow'





test().run()