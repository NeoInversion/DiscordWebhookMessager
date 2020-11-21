import PySimpleGUI as sg
from discord_webhook import DiscordWebhook, DiscordEmbed

sg.theme('DarkGrey6')

layout = [  
    [sg.Text('Enter webhook URL:'), sg.InputText()],
    [sg.Text('Enter webhook message:'), sg.InputText()],
    [sg.Button('Send'), sg.Button('Exit')] 
]

window = sg.Window('SendToWebhook', layout)

while True:
    event, values = window.read()
    #print(event, values)
    if event in (None, 'Exit'):
        window.close()
        break
    if event in (None, "Send"):
        webhook = DiscordWebhook(url = values[0], content = values[1])
        response = webhook.execute()
