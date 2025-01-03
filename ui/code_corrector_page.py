import flet as ft
from constants import LANGUAGES
from ai.code_corrector_agent import CodeCorrectorAgent
from ui.view import View


class CodeCorrectorPage(View):
    title = 'CodeCorrector'
    __agent = CodeCorrectorAgent()
    __question = ft.TextField(
        hint_text="Digite sua Questão",
        multiline=True,
        expand_loose=True,
        max_lines=3,
    )
    __language = ft.Dropdown(
        value=LANGUAGES[0],
        options=[ft.dropdown.Option(language) for language in LANGUAGES],
        max_menu_height=200
    )
    __answer = ft.TextField(
        hint_text="Digite sua Resposta",
        multiline=True,
        max_lines=7,
    )
    __correction = ft.TextField(
        hint_text='Sua correção aparecerá aqui...',
        read_only=True,
        multiline=True,
        max_lines=5,
    )

    def build(self):
        self.content = [
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
        return super().build()

    def __get_response(self, _):
        self._loading.visible = True

        self.page.update()

        self.__correction.value = self.__agent.run(
            language=self.__language.value,
            question=self.__question.value,
            answer=self.__answer.value
        )

        self._loading.visible = False

        self.page.update()

    def __clear_correction(self, _):
        self.__correction.value = ""
        self.page.update()
