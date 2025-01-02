import flet as ft
from constants import LANGUAGES
from view import View


class MainPage(View):
    def __init__(self, **kwargs):
        self.__question = ft.TextField(
            hint_text="Digite sua Questão",
            multiline=True,
            expand_loose=True,
            max_lines=3,
        )
        self.__language = ft.Dropdown(
            value=LANGUAGES[0],
            options=[ft.dropdown.Option(language) for language in LANGUAGES],
            max_menu_height=200
        )
        self.__answer = ft.TextField(
            hint_text="Digite sua Resposta",
            multiline=True,
            min_lines=9,
            max_lines=9
        )
        self.__correction = ft.TextField(
            value='Sua correção aparecerá aqui...',
            hint_text='Correção',
            read_only=True,
            multiline=True,
            min_lines=5,
            max_lines=5,
        )
        controls = [
            self.__question,
            self.__language,
            self.__answer,
            ft.Row(
                controls=[
                    ft.OutlinedButton(
                        'Limpar',
                        on_click=self.__clear_correction
                    ),
                    ft.FilledButton(
                        'Corrigir',
                        width=90,
                        on_click=self.__get_response
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            self.__correction
        ]
        super().__init__(*controls, **kwargs)

    def __get_response(self, e):
        question = self.__question.value
        answer = self.__answer.value
        language = self.__language.value

        self._loading.visible = True

        self.page.update()

        correction = self._agent.run(
            language, question, answer
        )

        self.__correction.value = correction

        self._loading.visible = False

        self.page.update()

    def __clear_correction(self, e):
        self.__correction.value = ""
        self.page.update()
