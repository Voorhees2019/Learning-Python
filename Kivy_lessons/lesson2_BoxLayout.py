from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout


class BoxApp(App):
    def build(self):
        bl = BoxLayout(orientation='horizontal', padding=[0, 25, 50, 100], spacing=100)
        # padding - отступ начала виджетов от края окна(слева, сверху, справа, снизу)
        # spacing - расстаяние между виджетами
        bl.add_widget(Button(text='button1'))
        bl.add_widget(Button(text='button2'))
        return bl


if __name__ == '__main__':
    BoxApp().run()
