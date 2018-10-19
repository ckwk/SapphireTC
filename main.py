from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.tabbedpanel import TabbedPanel


class MoveScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MoveScreen, self).__init__(**kwargs)
        self.cols = 5
        self.add_widget(Label(text='User Name'))
        self.username = Button(text='Button')
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = Button(text='Button')
        self.add_widget(self.password)


class PokeTCApp(App):

    def build(self):
        return MoveScreen()


if __name__ == '__main__':
    PokeTCApp().run()