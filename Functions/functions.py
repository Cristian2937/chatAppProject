import flet as ft
import numpy as np
import random

# Funzione per definire lo styling dell'applicazione
def items_style(message):
    
    return ft.Container(
        content=ft.Text(value= f"{message.user}: {message.text}",
                        color= ft.colors.WHITE ),
        alignment=ft.alignment.center_right,
        width= 300,
        height= 70,
        bgcolor=ft.colors.DEEP_PURPLE,
        padding= ft.padding.all(10),
        border_radius= ft.border_radius.all(5),
        )
    