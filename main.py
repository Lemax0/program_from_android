from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.lang import Builder



class Container(BoxLayout):

    def get_result(self):
        try:
            self.res_one.text = str(round(float(self.one_now.text.replace(',','.')) - float(self.one_max.text.replace(',','.')),1))
            self.res_two.text = str(round(float(self.two_now.text.replace(',','.')) - float(self.two_max.text.replace(',','.')), 1))
            self.res_three.text = str(round(float(self.three_now.text.replace(',','.')) - float(self.three_max.text.replace(',','.')), 1))
            self.res_four.text = str(round(float(self.four_now.text.replace(',','.')) - float(self.four_max.text.replace(',','.')), 1))
            self.res_five.text = str(round(float(self.five_now.text.replace(',','.')) - float(self.five_max.text.replace(',','.')), 1))
            self.res_six.text = str(round(float(self.six_now.text.replace(',','.')) - float(self.six_max.text.replace(',','.')), 1))
            self.res_seven.text = str(round(float(self.seven_now.text.replace(',','.')) - float(self.seven_max.text.replace(',','.')), 1))
            self.res_eight.text = str(round(float(self.eight_now.text.replace(',','.')) - float(self.eight_max.text.replace(',','.')), 1))
            self.res_nine.text = str(round(float(self.nine_now.text.replace(',','.')) - float(self.nine_max.text.replace(',','.')), 1))
            self.res_ten.text = str(round(float(self.ten_now.text.replace(',','.')) - float(self.ten_max.text.replace(',','.')), 1))
            self.debug.text = ''
        except ValueError:
            self.debug.text = 'Пожалуйста, только цифры!'
        except Exception as ex:
            self.debug.text = str(ex)

class WorkApp(App):
    def build(self):
        return Container()
 
if __name__ == '__main__':
    WorkApp().run()
