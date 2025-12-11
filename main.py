import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt = ft.Text(value="Hello, Flet!", size=30)
    page.controls.append(txt)

    page.update()

ft.app(target=main)
