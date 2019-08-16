from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout


class GridApp(App):
    def build(self):
        gl = GridLayout(cols=10, padding=[30], spacing=3)
        for i in range(1, 51):
            gl.add_widget(Button(text='button '+str(i)))

        return gl


if __name__ == '__main__':
    GridApp().run()
