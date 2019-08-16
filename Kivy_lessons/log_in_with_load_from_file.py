from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class MyApp(App):
    def update_label(self):
        self.lbl.text = self.data.readline()

    def load_from_file(self, instance):
        self.data = open('C:\\Petryk\\Kivy_lessons\\data.txt')
        self.update_label()

    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', size_hint=[.6, .6])
        # чтобы задать размер напрямую в пикселях: сначала установим size_hint=[None, None], а потом size=[300, 200]
        self.lbl = Label(text='LABEL 1', font_size=30, halign='left', valign='center', size_hint=[1, .3],
                         text_size=(400 * .6, 500 * .6 * .3))
        bl.add_widget(self.lbl)
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text='log in'))
        bl.add_widget(Button(text='load from file', on_press=self.load_from_file))
        al.add_widget(bl)
        return al


if __name__ == '__main__':
    MyApp().run()
