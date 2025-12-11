import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 300
    page.window_resizable = False

    # Authentication elements
    username = ft.TextField(label="Username", width=200)
    password = ft.TextField(label="Password", password=True, width=200)
    login_button = ft.ElevatedButton("Login", width=200)
    auth_status = ft.Text(size=15, color="red")

    def login_click(e):
        if username.value == "admin" and password.value == "admin":
            auth_status.value = "Login successful!"
            auth_status.color = "green"
            page.update()

            # Clear auth elements and show main content
            page.controls.clear()
            page.controls.append(auth_status)
            page.controls.append(ft.Text(value="Hello, Flet!", size=30))
            page.controls.append(ft.Dropdown(
                width=200,
                options=[
                    ft.dropdown.Option("Option 1"),
                    ft.dropdown.Option("Option 2"),
                    ft.dropdown.Option("Option 3"),
                ],
            ))
            page.controls.append(ft.Dropdown(
                width=200,
                options=[
                    ft.dropdown.Option("Choice A"),
                    ft.dropdown.Option("Choice B"),
                    ft.dropdown.Option("Choice C"),
                ],
            ))
            page.update()
        else:
            auth_status.value = "Invalid credentials!"
            page.update()

    login_button.on_click = login_click

    # Add auth elements to page
    page.controls.append(ft.Text(value="Login", size=24, weight="bold"))
    page.controls.append(username)
    page.controls.append(password)
    page.controls.append(login_button)
    page.controls.append(auth_status)

    page.update()

ft.app(target=main)