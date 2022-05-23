from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from Introduction import *


class LandingPage(MDScreen):
    pass


class PythonCore(MDScreen):
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(LandingPage(name="LandingPage"))
screen_manager.add_widget(PythonCore(name="PythonCore"))
screen_manager.add_widget(Welcome(name="Welcome"))
screen_manager.add_widget(WhatIsProgramming(name="WhatIsProgramming"))
screen_manager.add_widget(HistoryOfProgramming(name="HistoryOfProgramming"))
screen_manager.add_widget(GenerationsOfProgramming(name="GenerationsOfProgramming"))


class TASProgramApp(MDApp):
    def __init__(self):
        super(TASProgramApp, self).__init__()
        self.title = "TAS Program"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        self.ScreenManager = screen_manager
        self.root = Builder.load_file("Core.kv")

    def build(self):
        return LandingPage()


if __name__ == "__main__":
    TASProgramApp().run()
