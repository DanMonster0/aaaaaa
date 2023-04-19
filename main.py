import time
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Stopwatch(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.time_label = Label(text='0.00', font_size=50, size_hint=(1, 0.5))
        self.add_widget(self.time_label)

        self.start_button = Button(text='Start', size_hint=(1, 0.2))
        self.start_button.bind(on_press=self.start_stopwatch)
        self.add_widget(self.start_button)

        self.reset_button = Button(text='Reset', size_hint=(1, 0.2))
        self.reset_button.bind(on_press=self.reset_stopwatch)
        self.add_widget(self.reset_button)

        self.start_time = None
        self.elapsed_time = 0
        self.is_running = False

    def start_stopwatch(self, instance):
        if not self.is_running:
            self.start_time = time.time()
            Clock.schedule_interval(self.update_time, 0.01)
            self.is_running = True

    def reset_stopwatch(self, instance):
        self.elapsed_time = 0
        self.is_running = False
        self.time_label.text = '0.00'
        Clock.unschedule(self.update_time)

    def update_time(self, dt):
        self.elapsed_time = time.time() - self.start_time
        self.time_label.text = '{:.2f}'.format(self.elapsed_time)


class MyApp(App):
    def build(self):
        return Stopwatch()


if __name__ == '__main__':
    MyApp().run()
