import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 300
    page.window_resizable = False

    txt = ft.Text(value="Hello, Flet!", size=30)

    dropdown1 = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("Option 1"),
            ft.dropdown.Option("Option 2"),
            ft.dropdown.Option("Option 3"),
        ],
    )

    dropdown2 = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("Choice A"),
            ft.dropdown.Option("Choice B"),
            ft.dropdown.Option("Choice C"),
        ],
    )

    page.controls.append(txt)
    page.controls.append(dropdown1)
    page.controls.append(dropdown2)

    page.update()

ft.app(target=main)