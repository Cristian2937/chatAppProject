# scaricata la libreria flet tramite il comando "pip install flet"
import flet as ft


# FUNZIONE DI ESEMPIO PER COMPRENDERE COME AVVIARE L'APPLICAZIONE DESKTOP
"""
def main(page:  ft.Page):
    page.add(ft.Text(value='Hello world!'))
"""

def main(page:  ft.Page):
    page.title = "Live chat App"
    
    #
    def on_message(msg):
        messages.controls.append(ft.Text(msg))
        page.update()
        
    page.pubsub.subscribe(on_message)
    
    def send_click(e):
        page.pubsub.send_all(f"{user.value}: {message.value}")
        message.value = ""
        page.update()
   
    
    # Definizione del contenitore per i singoli messaggi
    messages = ft.Column()
     # Definizione del contenitore per il nome dell'utente
    user = ft.TextField(hint_text="Inserisci il nome...",width=150)
    # Definizione del contenitore per i singoli messaggi + expand=True fa in modo che il contenitore prenda tutto lo spazio restante
    message = ft.TextField(hint_text="Inserisci il messaggio...",expand=True)
    send = ft.ElevatedButton(text="Invia",on_click=send_click)
    
    page.add(messages,ft.Row(controls=[user,message,send]))
    
ft.app(target=main,view=ft.AppView.WEB_BROWSER)

