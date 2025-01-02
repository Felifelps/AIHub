import flet as ft
from ui.view import View


class ReadmeGeneratorPage(View):
    title = 'ReadmeGenerator'

    def build(self):
        self.content = [
            ft.Text('Teste')
        ]
        return super().build()
