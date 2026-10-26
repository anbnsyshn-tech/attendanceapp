import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import urllib.request

class AttendanceApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text='نظام تسجيل الحضور والغياب', font_size=20))
        
        self.user_id_input = TextInput(hint_text='رقم المستخدم', multiline=False)
        layout.add_widget(self.user_id_input)
        
        self.password_input = TextInput(hint_text='كلمة المرور', password=True, multiline=False)
        layout.add_widget(self.password_input)
        
        self.date_input = TextInput(hint_text='التاريخ', multiline=False)
        layout.add_widget(self.date_input)
        
        self.status_input = TextInput(hint_text='الحالة حضور أو غياب', multiline=False)
        layout.add_widget(self.status_input)
        
        self.variable_state_input = TextInput(hint_text='الحالة المتغيرة', multiline=False)
        layout.add_widget(self.variable_state_input)
        
        submit_btn = Button(text='إرسال البيانات')
        submit_btn.bind(on_press=self.send_data)
        layout.add_widget(submit_btn)
        
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)
        
        return layout

    def send_data(self, instance):
        url = 'http://10.58.199.45:5000/sync'
        try:
            data = {
                'user_id': int(self.user_id_input.text),
                'password': self.password_input.text,
                'date': self.date_input.text,
                'status': self.status_input.text,
                'variable_state': self.variable_state_input.text
            }
            req = urllib.request.Request(url, headers={'Content-Type': 'application/json'})
            response = urllib.request.urlopen(req, data=json.dumps(data).encode('utf-8'))
            self.result_label.text = 'تمت المزامنة بنجاح'
        except Exception as err:
            self.result_label.text = 'فشل الاتصال بالسيرفر'

if __name__ == '__main__':
    AttendanceApp().run()
