import flet as ft
from agent import Agent


class View(ft.View):

    _agent = Agent() 

    def __init__(self, *controls, **kwargs):
        super().__init__(**kwargs)
        self._loading = ft.ProgressRing(
            width=25,
            height=25,
            stroke_width=4,
            visible=False
        )
        self.controls = [
            ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                'CodeCorrector',
                                size=40,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls=[self._loading],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    *controls,
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
        ]
