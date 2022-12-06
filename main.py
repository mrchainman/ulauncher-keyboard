from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

import subprocess


class KeyboardLayoutChange(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_query().strip()
        if query == extension.preferences['kus']:
            subprocess.Popen(['setxkbmap', 'us', '-option', 'caps:escape'])
        if query == extension.preferences['kde']:
            subprocess.Popen(['setxkbmap', 'de', '-option', 'caps:escape'])
        if query == extension.preferences['kit']:
            subprocess.Popen(['setxkbmap', 'it', '-option', 'caps:escape'])
        return HideWindowAction()
        

if __name__ == '__main__':
    KeyboardLayoutChange().run()
