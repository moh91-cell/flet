
import flet as ft

def main(page: ft.Page):
    page.title = "My App"
    page.window.width = 390
    page.window.height = 740
    page.window.top= 10
    page.window.left = 600
    page.add(ft.Text("Hello Flet"))

ft.app(
    target=main,
    view=ft.AppView.FLET_APP
)
