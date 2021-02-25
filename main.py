from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


Builder.load_string(
    """
<MainLayout>
    
"""
)


class MainLayout(MDBoxLayout):
    pass


class SelfDrivingCarAIApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Green"

    def build(self):
        return MainLayout()

    def on_pause(self):
        return True


if __name__ == "__main__":

    app = SelfDrivingCarAIApp()
    app.run()
