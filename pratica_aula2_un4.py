from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp

KV = '''
<CalculatorApp>
    orientation: 'vertical'
    MDTextField:
        id: input_field
        hint_text: "Insira um número"
        helper_text_mode: "on_focus"
        input_filter: "float"
    GridLayout:
        cols: 4
        spacing: dp(10)
        MDRaisedButton:
            text: "1"
            on_press: app.on_number_press(1)
        MDRaisedButton:
            text: "2"
            on_press: app.on_number_press(2)
        MDRaisedButton:
            text: "3"
            on_press: app.on_number_press(3)
        MDRaisedButton:
            text: "+"
            md_bg_color: 0.2, 0.7, 0.3, 1
            on_press: app.on_operator_press("+")
        MDRaisedButton:
            text: "4"
            on_press: app.on_number_press(4)
        MDRaisedButton:
            text: "5"
            on_press: app.on_number_press(5)
        MDRaisedButton:
            text: "6"
            on_press: app.on_number_press(6)
        MDRaisedButton:
            text: "-"
            on_press: app.on_operator_press("-")
        MDRaisedButton:
            text: "7"
            on_press: app.on_number_press(7)
        MDRaisedButton:
            text: "8"
            on_press: app.on_number_press(8)
        MDRaisedButton:
            text: "9"
            on_press: app.on_number_press(9)
        MDRaisedButton:
            text: "*"
            on_press: app.on_operator_press("*")
        MDRaisedButton:
            text: "c"
            on_press: app.clear_input()
        MDRaisedButton:
            text: "0"
            on_press: app.on_number_press(0)
        MDRaisedButton:
            text: "="
            on_press: app.calculate_result()
        MDRaisedButton:
            text: "/"
            on_press: app.on_operator_press("/")        
'''

#Definindo a classe CalculatorApp que herda de BoxLayout
class CalculatorApp(BoxLayout):
    #Mé_todo chamado quando um número é pressionado
    def on_number_press(self, number):
        current_text = self.ids.input_field.text
        new_text = f"{current_text}{number}"
        self.ids.input_field.text = new_text

    #Mé_todo chamado quando um operador é pressionado
    def on_operator_press(self, operator):
        current_text = self.ids.input_field.text
        new_text = f"{current_text}{operator}"
        self.ids.input_field.text = new_text

    #Mé_todo chamado para limpar a entrada
    def clear_input(self):
        self.ids.input_field.text = ""

    #Mé_todo chamado para calcular o resultado da expressão
    def calculate_result(self):
        try:
            result = eval(self.ids.input_field.text)
            self.ids.input_field.text = str(result)
        except Exception as e:
            self.ids.input_field.text = "Erro"

#Definindo a classe CalculatorMDApp que herda de MDApp
class CalculatorMDApp(MDApp):
    #Mé_todo chamado para construir o app
    def build(self):
        return CalculatorApp()

    #Métodos chamados para interagir com a instância de CalculatorApp
    def on_number_press(self, number):
        self.root.on_number_press(number)

    def on_operator_press(self, operator):
        self.root.on_operator_press(operator)

    def clear_input(self):
        self.root.clear_input()

    def calculate_result(self):
        self.root.calculate_result()

#Verificando se o script está sendo executado diretamente
if __name__ == '__main__':
    #Carregando a string KV usando Builder
    Builder.load_string(KV)
    #Iniciando o aplicativo MD
    CalculatorMDApp().run()