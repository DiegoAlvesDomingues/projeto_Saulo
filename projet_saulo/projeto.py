from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Line, Rectangle
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Calculadora de Área do Cubo"
            halign: "center"
            font_style: "H5"

        MDTextField:
            id: edge_length
            hint_text: "Digite o comprimento da aresta do cubo (em unidades)"
            helper_text: "Ex: 3"
            helper_text_mode: "on_focus"
            mode: "rectangle"

        MDRectangleFlatButton:
            text: "Calcular Área"
            pos_hint: {"center_x": 0.5}
            on_release: app.calculate_area()

        MDLabel:
            id: result_label
            text: ""
            halign: "center"
            font_style: "H6"

        CubeWidget:
            id: cube_widget
            size_hint: (1, 0.5)
'''

class CubeWidget(FloatLayout):
    def draw_cube(self, edge_length):
        self.canvas.clear()  # Limpa o canvas antes de desenhar

        # Define a cor do cubo
        with self.canvas:
            Color(0, 0, 1, 1)  # Azul
            # Desenha um cubo (representação 2D)
            # (x, y) são as coordenadas do canto inferior esquerdo
            x, y = self.center_x - edge_length / 2, self.center_y - edge_length / 2
            Rectangle(pos=(x, y), size=(edge_length, edge_length))

            # Desenha as linhas para representar o cubo
            Line(points=[x, y, x + edge_length, y, x + edge_length, y + edge_length, x, y + edge_length, x, y], width=2)
            Line(points=[x + edge_length, y, x + edge_length + edge_length / 2, y + edge_length / 2,
                         x + edge_length + edge_length / 2, y + edge_length / 2 + edge_length,
                         x + edge_length, y + edge_length], width=2)
            Line(points=[x, y + edge_length, x + edge_length / 2, y + edge_length / 2 + edge_length,
                         x + edge_length / 2, y + edge_length / 2, x, y + edge_length], width=2)

class MainScreen(Screen):
    pass

class CubeAreaApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def calculate_area(self):
        edge_length = self.root.get_screen('main').ids.edge_length.text
        if edge_length:
            try:
                edge_length = float(edge_length)
                area = 6 * (edge_length ** 2)  # A = 6 * a²
                self.root.get_screen('main').ids.result_label.text = f"Área Total: {area:.2f} unidades²"
                self.root.get_screen('main').ids.cube_widget.draw_cube(edge_length)
            except ValueError:
                self.root.get_screen('main').ids.result_label.text = "Por favor, insira um número válido."
        else:
            self.root.get_screen('main').ids.result_label.text = "Por favor, insira um valor."

if __name__ == '__main__':
    CubeAreaApp().run()