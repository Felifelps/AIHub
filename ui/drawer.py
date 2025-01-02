import flet as ft

class Drawer(ft.NavigationDrawer):
    def __init__(self, **kwargs):
        super().__init__(
            on_dismiss=self.on_dismiss_function,
            on_change=self.on_change_function,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Item 1",
                    icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
                    label="Item 2",
                    selected_icon=ft.Icons.MAIL,
                ),
            ],
            **kwargs
        )

    def on_dismiss_function(self, e):
        pass

    def on_change_function(self, e):
        e.page.go(e.page.views[self.selected_index].route)
