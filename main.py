from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

from hungarian_algorithm.main import Munkres

Builder.load_file('view/app.kv')

matrixSizeY = 0
matrixSizeY = 0

# temp
costs = [
    [30, 25, 10],
    [15, 10, 20],
    [25, 20, 15],
]

costsValues = None
costsSum = None

class MenuScreen(Screen):
    
    def onCreateMatrixClick(self):
        global matrixSizeX 
        matrixSizeX = self.ids.sizeX.text
        global matrixSizeY
        matrixSizeY = self.ids.sizeY.text
        sm.current = 'matrix'

class MatrixScreen(Screen):
    
    def onCalculateClick(self):
        global costsSum
        costsSum = Munkres(costs)
        sm.current = 'result'

class ResultScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MatrixScreen(name='matrix'))
sm.add_widget(ResultScreen(name='result'))

class HungarianAlgorithmApp(App):

    def build(self):
        return sm

if __name__ == "__main__":
    HungarianAlgorithmApp().run()

# def main():
#     costs = [
#         [30, 25, 10],
#         [15, 10, 20],
#         [25, 20, 15],
#     ]

#     costs = Munkres(costs)
#     print(costs.getMinCostsValues())
    
# main()

