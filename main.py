from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, ObjectProperty
import json


class Lce_InputScreen(Screen):
    input_code_out = ObjectProperty(None)
    vod_text = StringProperty('')

    def check_data_login(self):
        test = self.input_code_out.text
        print(type(test))

        file_name = 'test.json'
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())

        taxi = data[0]["prich_error"]

        vod_text = StringProperty(taxi)

        print("texa", type(taxi), taxi)
        print(type(vod_text), vod_text)

class ScreenManagement(ScreenManager):
    pass

class CustomMenuApp(MDApp):
    def build(self):
        return Builder.load_file("copymain.kv")

if __name__ == "__main__":
    CustomMenuApp().run()