from kivy.app import App
from kivy.uix.boxlayout import BoxLaypout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operators = ["/", '*', "+", "-"]

if __name__ == "__main__":
    app = MainApp()
    app.run()