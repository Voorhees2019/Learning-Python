from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

from kivy.config import Config  # устанавливает статический размер окна
Config.set('graphics', 'resizable', '0')  # окно не может менять размер
Config.set('graphics', 'width', '640')  # устанавливает ширину окна
Config.set('graphics', 'height', '480')  # устанавливает высоту окна
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter  # изменение виджетов внутри, как двумя пальцами на андроиде(android touch)


class MyApp(App):
    def build(self):
        # return CodeInput(lexer=HtmlLexer())
        s = Scatter()
        fl = FloatLayout(size=(300, 300))
        s.add_widget(fl)
        fl.add_widget(Button(text='This is my first button.', font_size=18, on_press=self.btn_press,
                      background_color=[0, 0, 1, 1], background_normal='',
                             size_hint=(.5, .25), pos=(640/4, 480/2-(480*.25/2))))  # size_hint(.5=50%, .25=25%)
        return s

    def btn_press(self, instance):
        print('Button is pressed!')
        instance.text = 'already pressed button'


if __name__ == '__main__':
    MyApp().run()

