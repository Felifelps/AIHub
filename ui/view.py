import flet as ft
from ai.gemini_agent import GeminiAgent


class View(ft.View):

    title = ''
    content = []
    _agent = GeminiAgent()
    _loading = ft.ProgressRing(
        width=25,
        height=25,
        stroke_width=4,
        visible=False
    )

    def build(self):
        return ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.MENU,
                            on_click=lambda e: e.page.open(self.drawer) and e.page.update()
                        ),
                        ft.Text(
                            self.title,
                            size=40,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[self._loading],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                *self.content,
                ft.Row(
                    controls=[
                        ft.TextButton(
                            content=ft.Text(
                                'Github/@Felifelps',
                                text_align=ft.TextAlign.CENTER,
                            ),
                            url="https://github.com/Felifelps/",
                            style=ft.ButtonStyle(overlay_color=ft.colors.BACKGROUND),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            '© 2025 por Felifelps. Todos os direitos reservados.',
                            text_align=ft.TextAlign.CENTER,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ]
        )
