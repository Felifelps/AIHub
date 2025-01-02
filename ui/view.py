import flet as ft


class View(ft.View):

    title = ''
    content = []
    _loading = ft.ProgressRing(
        width=25,
        height=25,
        stroke_width=4,
        visible=False
    )

    def build(self):
        return ft.Column(
            expand=True,
            controls=[
                ft.Row(
                    controls=[
                        ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem(
                                    text="CodeCorrector",
                                    checked=self.title == "CodeCorrector",
                                    on_click=lambda e: e.page.go("/corrector")
                                ),
                                ft.PopupMenuItem(
                                    text="ReadmeGenerator",
                                    checked=self.title == "ReadmeGenerator",
                                    on_click=lambda e: e.page.go("/readme")
                                ),
                            ]
                        ),
                        ft.Text(
                            self.title,
                            expand=True,
                            size=35,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                ),
                ft.Row(
                    controls=[self._loading],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Column(
                    expand=True,
                    controls=self.content,
                ),
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
