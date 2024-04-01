# scaricata la libreria flet tramite il comando "pip install flet"
import flet as ft
from Classes.Message import Message
from Functions.functions import items_style
from Classes.ChatMessage import ChatMessage


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
            # instanzio la classe ChatMessage creata e passo msg all'oggetto
            chat = ChatMessage(msg)
        elif msg.message_type == "login_message":
            chat = ft.Text(value=f"{user_name.value} has joined the chat", italic=True, color=ft.colors.BLACK45, size=12)
            
        messages.controls.append(chat)
        page.update()
        
    page.pubsub.subscribe(on_message)
    
    def send_click(e):
        if not message.value:
            message.error_text = "Devi inserire un messaggio!"
        else:
            page.pubsub.send_all(
                Message(
                    user= page.session.get("user_name"),
                    text= message.value,
                    message_type="chat_message"
                )
            )
            message.value = ""
        page.update()
        
        
    def join_click(e):
       if not user_name.value:
           user_name.error_text = "Devi inserire un nome!"
           user_name.update()
       else:
           page.session.set("user_name",user_name.value)
           page.dialog.open = False
           page.pubsub.send_all(
               Message(
                   user=user_name.value,
                   text=f"{user_name.value} has joined the chat.",
                   message_type="login_message"
                )
            )
           page.update()
           
    def change_color(e):
        send.content = ft.Row([
                    ft.Icon(
                        name=ft.icons.SEND,
                        color=ft.colors.WHITE
                    )
                ])
        send.on_hover = ft.colors.BLACK45
        send.color = ft.colors.WHITE
        send.bgcolor = ft.colors.BLACK45
        send.update()
           
           
    
   
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
        content=ft.Column(
            controls=[user_name],
            tight=True
        ),
        actions=[
            ft.ElevatedButton(
                text="Unisciti alla chat",
                on_click=join_click
                )
        ]
    )
        
    send = ft.ElevatedButton(
        on_click=send_click,
        content=ft.Row([
            ft.Icon(
                name=ft.icons.SEND
                )
            ]),
        on_hover= change_color
    )
    
    page.add(
            messages,
            ft.Row(controls=[message,send]),
        )
  
  
# per essere richiamata come webApp utilizzare il parametro ,view=ft.AppView.WEB_BROWSER
ft.app(
        port=8080,
        target=main,
        assets_dir="assets",
    )

