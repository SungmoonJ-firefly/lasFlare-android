from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class LasFlareApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="lasFlare",
            font_size="32sp"
        )

        start_button = Button(
            text="검색 시작",
            font_size="24sp"
        )

        stop_button = Button(
            text="검색 중지",
            font_size="24sp"
        )

        result = Label(
            text="검색 결과 없음",
            font_size="20sp"
        )

        layout.add_widget(title)
        layout.add_widget(start_button)
        layout.add_widget(stop_button)
        layout.add_widget(result)

        return layout


if __name__ == "__main__":
    LasFlareApp().run()