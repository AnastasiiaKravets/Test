import time


def set_default_reader(window):
    window['...Button'].click()
    # TODO opening file


def input_text_pattern(window, text = ''):
    text_field = window.edit
    text_field.type_keys(text, with_spaces=True)
    index = 0
    assert text_field.texts()[index] in text

def input_text_pattern_CTRL_C(window, text = ''):
    text_field = window.edit
    text_field.type_keys(text, with_spaces=True)
    text_field.type_keys('^(a)^(c)')
    text_field.type_keys('Text should be shifted')
    text_field.type_keys('^(a)^(v)')
    #print(text_field.texts())
    index = 0
    assert text_field.texts()[index] in text

def applying_settings(window):
    window.Apply.wait('active').click()



def send_an_error_report(window, error_text = ''):
    window.PDFRedirect.Button.click()
    descr_error_window = window['Description Error']
    descr_error_window.edit.type_keys(error_text, with_spaces=True)
    #descr_error_window.Send.click()
    #TODO asserting confirmation message

def change_dropdown_list(window):
    print(window['Printer name:ComboBox'].ItemCount())
    print(window['Printer name:ComboBox'].ItemTexts())
    print(window['Printer name:ComboBox'].SelectedText())
    window['Printer name:ComboBox'].Select('Fax')
    #time.sleep(2)
    assert window['Printer name:ComboBox'].SelectedText() in 'Fax'