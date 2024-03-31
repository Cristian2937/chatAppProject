import flet as ft

def items_style(message):
    
    return ft.Container(
        content=ft.Text(value= f"{message.user}: {message.text}"),
        alignment=ft.alignment.center_right,
        height= 100,
        bgcolor=ft.colors.GREEN_100,
        border_radius= ft.border_radius.all(5),
    )
