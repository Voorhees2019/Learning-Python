from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget  # empty widget class
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class CalculatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if self.formula[-1] != instance.text:
            self.formula += str(instance.text)
        self.update_label()

    def equal(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = str(eval(self.lbl.text))

    def clean(self, instance):
        self.formula = '0'
        self.update_label()

    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation='vertical', padding=10)
        gl = GridLayout(cols=4, spacing=3, size_hint=[1, .6])

        self.lbl = Label(text='0', font_size=40, halign='right', valign='center',
                            size_hint=[1, .4], text_size=(400-20, 500*.4-20))
        bl.add_widget(self.lbl)
        # text_size - задает размер текстуры текста внутри виджета лейбла

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='*', on_press=self.add_operation))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operation))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_operation))

        gl.add_widget(Button(text='C', on_press=self.clean))
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='.', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.equal))

        bl.add_widget(gl)
        return bl


if __name__ == '__main__':
    CalculatorApp().run()
