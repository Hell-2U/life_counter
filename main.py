from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class LifeCounter(MDApp):
    def build(self):
        return MDLabel(text="Hello", halign="center")


LifeCounter().run()
