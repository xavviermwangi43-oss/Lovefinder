from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=dp(24), spacing=dp(16))
        layout.add_widget(Label(text="❤️ Love Finder", font_size="32sp"))
        layout.add_widget(Label(text="Connect • Chat • Meet", font_size="20sp"))
        btn = Button(text="Open Chat", size_hint_y=None, height=dp(55))
        btn.bind(on_release=lambda *_: setattr(self.manager, "current", "chat"))
        layout.add_widget(btn)
        self.add_widget(layout)


class ChatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(12))
        layout.add_widget(Label(text="💬 Love Finder Chat", font_size="26sp", size_hint_y=None, height=dp(50)))
        self.output = Label(text="No messages yet.", halign="left", valign="top")
        self.output.bind(size=self.output.setter("text_size"))
        layout.add_widget(self.output)
        row = BoxLayout(size_hint_y=None, height=dp(55), spacing=dp(8))
        self.message = TextInput(hint_text="Write a message...", multiline=False)
        send = Button(text="Send", size_hint_x=None, width=dp(90))
        send.bind(on_release=self.send_message)
        row.add_widget(self.message)
        row.add_widget(send)
        layout.add_widget(row)
        back = Button(text="Back", size_hint_y=None, height=dp(50))
        back.bind(on_release=lambda *_: setattr(self.manager, "current", "home"))
        layout.add_widget(back)
        self.add_widget(layout)

    def send_message(self, *_):
        text = self.message.text.strip()
        if text:
            if self.output.text == "No messages yet.":
                self.output.text = "You: " + text
            else:
                self.output.text += "\nYou: " + text
            self.message.text = ""


class LoveFinderApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ChatScreen(name="chat"))
        return sm


if __name__ == "__main__":
    LoveFinderApp().run()
