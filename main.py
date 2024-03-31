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
        if msg.message_type == "chat_message":
            messages.controls.append(items_style(msg))
        elif msg.message_type == "login_message":
            messages.controls.append(
                ft.Text(value=msg.text, italic=True, color=ft.colors.BLACK45, size=12),
            )
        page.update()
        
    page.pubsub.subscribe(on_message)
    
    def send_click(e):
        page.pubsub.send_all(Message(user= page.session.get("user_name"),text= message.value,message_type="chat_message"))
        message.value = ""
        page.update()
        
        
    def join_click(e):
       if not user_name.value:
           user_name.error_text = "Devi inserire un nome!"
           user_name.update()
       else:
           page.session.set("user_name",user_name.value)
           page.dialog.open = False
           page.pubsub.send_all(Message(user=user_name.value, text=f"{user_name.value} has joined the chat.", message_type="login_message"))
           page.update()
           
           
    
   
    # Definizione del contenitore per i singoli messaggi + expand=True fa in modo che il contenitore prenda tutto lo spazio restante
    message = ft.TextField(hint_text="Inserisci il messaggio...",expand=True)
    
    # Definizione del contenitore per i singoli messaggi
    messages = ft.Column(adaptive=True)
    
     # Definizione del contenitore per il nome dell'utente
    #user = ft.TextField(hint_text="Inserisci il nome...",width=150)
    
    
    # Definizione della modale che prenderà il nome dell'utente come input
    user_name = ft.TextField(label="Inserisci il tuo nome...")
    
    page.dialog = ft.AlertDialog(
        open=True,
        modal= True,
        title= ft.Text(value="Benvenuto!"),
        content=ft.Column(controls=[user_name],tight=True),
        actions=[ft.ElevatedButton(text="Unisciti alla chat",on_click=join_click)]
    )
    
    send = ft.ElevatedButton(text="Invia",on_click=send_click)
    
    page.add(messages,ft.Row(controls=[message,send]))
  
  
# per essere richiamata come webApp utilizzare il parametro ,view=ft.AppView.WEB_BROWSER
ft.app(target=main,view=ft.AppView.WEB_BROWSER)

