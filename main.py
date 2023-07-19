# Import für die App
from kivy.app import App

# Import Layout (Grid, Box, ...)
from kivy.uix.gridlayout import GridLayout

# Import Testfenster
from kivy.uix.label import Label

# Import Fenster zum reinschreiben
from kivy.uix.textinput import TextInput

# Import Knöppe
from kivy.uix.button import Button


# App-Klasse (Alles was vor App steht, so heißt später das Hauptfenster
class GeldumrechnerApp(App):

    # Def für den Aufbau des Hauptfensters
    def build(self):
        self.window = GridLayout()

        # legt bei GridLayout die Spaltenzahl fest
        self.window.cols = 1

        # Größe der Fensterinhalte
        self.window.size_hint = (0.6, 0.7)

        # Position der Fensterinhalte
        self.window.pos_hint = {
            'center_x': 0.5,
            'center_y': 0.5
        }

        # Text für das Textfenster
        self.greeting = Label(text='Wie ist dein Name?', font_size=52, color='#33cccc')
        self.window.add_widget(self.greeting)

        # Texteingabefeld für den Benutzer
        self.user = TextInput(multiline=False, padding_y=(40, 40), size_hint=(1, 0.5))
        self.window.add_widget(self.user)

        # baut einen Knopf, der beim Drücken was macht
        self.entrance_button = Button(text='Eintreten', size_hint=(1, 0.5), bold=True, background_color='#33cccc')
        self.window.add_widget(self.entrance_button)
        self.entrance_button.bind(on_press=self.entrance_button_behaviour)

        # gibt das Fenster mit seinen gebauten inhalten aus
        return self.window

    # Def für den Knopf: Schreibt "Herzlich willkommen," in das Textfenster und holt sich die Benutzereingabe
    # aus dem Eingabefeld dazu
    def entrance_button_behaviour(self, *args):
        self.greeting.text = f'Herzlich Willkommen, {self.user.text}.'


pass

# sorgt dafür, dass das Programm überhaupt erst startet
if __name__ == "__main__":
    app = GeldumrechnerApp()
    app.run()
