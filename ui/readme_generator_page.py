import flet as ft
import pyperclip
from ai.readme_generator_agent import ReadmeGeneratorAgent
from ui.view import View


class ReadmeGeneratorPage(View):
    title = "ReadmeGenerator"
    __agent = ReadmeGeneratorAgent()
    __repo_name = ft.TextField(
        hint_text="Nome do repositório",
        expand_loose=True,
        helper_text="username/nome do repositório"
    )
    __branch = ft.TextField(
        hint_text="Branch",
        expand_loose=True,
        helper_text="Branch desejado"
    )
    __extensions = ft.TextField(
        hint_text="Extensões",
        expand_loose=True,
        helper_text="Separe por vírgulas, ex: .py, .md, .js."
    )
    __readme = ft.Markdown(
        "Seu readme aparecerá aqui",
        extension_set="gitHubWeb",
        selectable=True
    )

    def build(self):
        self.auto_scroll = True
        self.content = [
            self.__repo_name,
            self.__branch,
            self.__extensions,
            ft.Row(
                controls=[
                    ft.OutlinedButton(
                        "Limpar",
                        on_click=self.__clear_readme
                    ),
                    ft.OutlinedButton(
                        "Copiar",
                        on_click=self.__copy_readme
                    ),
                    ft.FilledButton(
                        "Gerar",
                        width=90,
                        on_click=self.__get_response
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.ListView(
                controls=[self.__readme],
                expand=1,
                spacing=10,
                padding=20,
            )
        ]
        return super().build()

    def __clear_readme(self, e):
        self.__readme.value = ""
        self.page.update()

    def __copy_readme(self, e):
        try:
            pyperclip.copy(self.__readme.value)
            snackbar_text = "Copiado para a área de transferência"
            bgcolor = ft.Colors.ON_PRIMARY_CONTAINER
        except Exception as e:
            snackbar_text = "Erro ao copiar"
            bgcolor = ft.Colors.ERROR
            print(e)

        snackbar = ft.SnackBar(
            content=ft.Text(snackbar_text),
            bgcolor=bgcolor
        )
        self.page.snack_bar = snackbar
        self.page.snack_bar.open = True
        self.page.update()

    def __get_response(self, e):
        self._loading.visible = True
        self.page.update()

        self.__readme.value = self.__agent.run(
            self.__repo_name.value,
            self.__branch.value,
            self.__extensions.value.split(",").replace(" ", "")
        )

        self._loading.visible = False
        self.page.update()
