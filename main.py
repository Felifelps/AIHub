import flet as ft
from main_page import MainPage


def main(page: ft.Page):
    page.title = "CodeCorrector"
    page.theme_mode = 'dark'
    page.auto_scroll = True

    page.views.extend([
        MainPage(route='/'),
    ])

    def on_route_change(e):
        page.views.sort(key=lambda view: view.route == page.route)
        page.update()

    page.on_route_change = on_route_change
    page.go('/')


if __name__ == "__main__":
    ft.app(
        name="",
        target=main,
        port=8000,
        view=ft.AppView.FLET_APP_WEB
    )
