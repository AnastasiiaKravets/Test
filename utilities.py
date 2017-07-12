import time

def default_view(window, name_edit = None, text_edit = None, \
                 printer_name_list ='Microsoft XPS Document Writer', \
                 paper_format_list = 'Letter', \
                 paper_source_list = 'Автовыбор', \
                 duplex_list = 'Simplex'):
    settings_static = 'Settings'
    default_pdf_program_static = 'Default PDF program'
    name_static = 'Name:'
    text_pattern_static = 'Text pattern'
    text_static = 'Text:'
    printer_settings_static = 'Printer settings'
    printer_name_static = 'Printer name:'
    paper_format_static = 'Paper format:'
    paper_source_static = 'Paper source:'
    duplex_static = 'Duplex:'
    first_element = 0

    assert window.Settings.texts()[first_element] in settings_static
    assert window['Default PDF program'].texts()[first_element] in default_pdf_program_static
    assert window['Name:Static'].texts()[first_element] in name_static
    #assert window['Name:Edit'].texts()[first_element] == name_edit
    assert window['Text pattern'].texts()[first_element] in text_pattern_static
    assert window['Text:Static'].texts()[first_element] in text_static
    #assert window['Text:Edit'].texts()[first_element] == text_edit
    assert window['Printer settings'].texts()[first_element] in printer_settings_static
    assert window['Printer name:Static'].texts()[first_element] in printer_name_static
    assert window['Printer name:ComboBox'].SelectedText() in printer_name_list
    assert window['Paper format:Static'].texts()[first_element] in paper_format_static
    assert window['Paper format:ComboBox'].SelectedText() in paper_format_list
    assert window['Paper source:Static'].texts()[first_element] in paper_source_static
    assert window['Paper source:ComboBox'].SelectedText() in paper_source_list
    assert window['Duplex:Static'].texts()[first_element] in duplex_static
    assert window['Duplex:ComboBox'].SelectedText() in duplex_list
    window.Button.verify_actionable()   # is Send an error report button active
    window.Button2.verify_visible()     # is Apply button visible
    window.Button3.verify_actionable()  # is ...Button active
    print(window.Button.texts())





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
    # print(text_field.texts())
    index = 0
    assert text_field.texts()[index] in text


def applying_settings(window):
    window.Apply.wait('active').click()


def send_an_error_report(window, error_text = ''):
    window.PDFRedirect.Button.click()
    descr_error_window = window['Description Error']
    descr_error_window.edit.type_keys(error_text, with_spaces=True)
    # descr_error_window.Send.click()
    #TODO asserting confirmation message


def change_dropdown_list(window):
    print(window['Printer name:ComboBox'].ItemCount())
    print(window['Printer name:ComboBox'].ItemTexts())
    print(window['Printer name:ComboBox'].SelectedText())
    window['Printer name:ComboBox'].Select('Fax')
    # time.sleep(2)
    assert window['Printer name:ComboBox'].SelectedText() in 'Fax'