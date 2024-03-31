# scaricata la libreria flet tramite il comando "pip install flet"
import flet as ft
from Classes.Message import Message
from Functions.functions import items_style


# FUNZIONE DI ESEMPIO PER COMPRENDERE COME AVVIARE L'APPLICAZIONE DESKTOP
"""
def main(page:  ft.Page):
    page.add(ft.Text(value='Hello world!'))
"""

def main(page:  ft.Page):
    page.title = "Live chat App"
    
    #
    def on_message(msg : Message):
        #ft.Text(f"{msg.user}: {msg.text}")
        messages.controls.append(items_style(msg))
        page.update()
        
    page.pubsub.subscribe(on_message)
    
    def send_click(e):
        page.pubsub.send_all(Message(user=page.session_id,text= message.value))
        message.value = ""
        page.update()
   
   
    # Definizione del contenitore per i singoli messaggi + expand=True fa in modo che il contenitore prenda tutto lo spazio restante
    message = ft.TextField(hint_text="Inserisci il messaggio...",expand=True)
    
    # Definizione del contenitore per i singoli messaggi
    messages = ft.Column(adaptive=True)
    
     # Definizione del contenitore per il nome dell'utente
    #####user = ft.TextField(hint_text="Inserisci il nome...",width=150)
    
    send = ft.ElevatedButton(text="Invia",on_click=send_click)
    
    page.add(messages,ft.Row(controls=[message,send]))
  
  
# per essere richiamata come webApp utilizzare il parametro ,view=ft.AppView.WEB_BROWSER
ft.app(target=main,view=ft.AppView.WEB_BROWSER)

