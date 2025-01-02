import flet as ft
from ui.drawer import Drawer
from ui.view import View


class ReadmeGeneratorPage(View):
    title = 'ReadmeGenerator'

    def build(self):
        self.drawer = Drawer()
        self.content = [
            ft.Text('Teste')
        ]
        return super().build()
