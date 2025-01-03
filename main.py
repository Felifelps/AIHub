import flet as ft
from ui.code_corrector_page import CodeCorrectorPage
from ui.readme_generator_page import ReadmeGeneratorPage


def main(page: ft.Page):
    page.title = "CodeCorrector"
    page.theme_mode = 'dark'
    page.auto_scroll = True

    views = {view.route: view for view in [
        CodeCorrectorPage(route='/corrector'),
        ReadmeGeneratorPage(route='/readme'),
    ]}

    page.views.append(views['/corrector'])

    def on_route_change(e):
        page.views[0] = views[page.route]
        page.update()

    page.on_route_change = on_route_change
    page.go('/corrector')


if __name__ == "__main__":
    ft.app(
        name="",
        target=main,
        port=8000,
        view=ft.AppView.FLET_APP_WEB
    )
