import flet as ft

def main(page: ft.Page):
    page.title = "Интерактивная страница"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Элементы страницы
    txt = ft.Text(value="Привет, мир!", size=30, color=ft.colors.BLUE)
    btn = ft.ElevatedButton(text="Нажми меня!", on_click=lambda e: toggle_text(e))

    def toggle_text(e):
        if txt.value == "Привет, мир!":
            txt.value = "Текст изменен!"
            txt.color = ft.colors.GREEN
        else:
            txt.value = "Привет, мир!"
            txt.color = ft.colors.BLUE
        page.update()

    # Добавляем элементы на страницу
    page.add(txt, btn)

ft.app(target=main)