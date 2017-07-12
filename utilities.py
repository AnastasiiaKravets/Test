import time


def default_view(window, name_edit='',
                 text_edit='',
                 printer_name_list='Microsoft XPS Document Writer',
                 paper_format_list='Letter',
                 paper_source_list='Автовыбор',
                 duplex_list='Simplex'):
    settings_static = 'Settings'
    default_pdf_program_static = 'Default PDF program'
    name_static = 'Name:'
    open_button_text = '...'
    text_pattern_static = 'Text pattern'
    text_static = 'Text:'
    printer_settings_static = 'Printer settings'
    printer_name_static = 'Printer name:'
    paper_format_static = 'Paper format:'
    paper_source_static = 'Paper source:'
    duplex_static = 'Duplex:'
    first_element = 0
    send_error_button = window.Button
    send_error_button_text = 'Send an error report'
    apply_button = window.Button2
    apply_button_text = 'Apply'
    open_button = window.Button3

    assert window.Settings.texts()[first_element] in settings_static
    assert window['Default PDF program'].texts()[first_element] in default_pdf_program_static
    assert window['Name:Static'].texts()[first_element] in name_static
    assert window['Name:Edit'].texts()[first_element] == name_edit
    assert open_button.texts()[first_element] in open_button_text
    assert window['Text pattern'].texts()[first_element] in text_pattern_static
    assert window['Text:Static'].texts()[first_element] in text_static
    assert window['Text:Edit'].texts()[first_element] == text_edit
    assert window['Printer settings'].texts()[first_element] in printer_settings_static
    assert window['Printer name:Static'].texts()[first_element] in printer_name_static
    assert window['Printer name:ComboBox'].SelectedText() in printer_name_list
    assert window['Paper format:Static'].texts()[first_element] in paper_format_static
    assert window['Paper format:ComboBox'].SelectedText() in paper_format_list
    assert window['Paper source:Static'].texts()[first_element] in paper_source_static
    assert window['Paper source:ComboBox'].SelectedText() in paper_source_list
    assert window['Duplex:Static'].texts()[first_element] in duplex_static
    assert window['Duplex:ComboBox'].SelectedText() in duplex_list
    assert apply_button.texts()[first_element] in apply_button_text
    assert send_error_button.texts()[first_element] in send_error_button_text
    send_error_button.verify_actionable()
    apply_button.verify_visible()
    open_button.verify_actionable()


def description_error_view(window):
    descr_err_window = window['Description Error']
    send_button = descr_err_window.Button
    text_static = 'Text'
    text_edit = ''
    send_button_text = 'Send'

    assert descr_err_window.TextStatic.texts() in text_static
    assert descr_err_window.Edit.texts() in text_edit
    assert descr_err_window.Button.texts() in send_button_text
    send_button.verify_actionable()


def set_default_reader(window):
    window['...Button'].click()
    # TODO opening file


def input_text_pattern(window, text=''):
    text_field = window.edit
    text_field.type_keys(text, with_spaces=True)
    index = 0
    assert text_field.texts()[index] in text


def input_text_pattern_ctrl_c(window, text=''):
    text_field = window.edit
    text_field.type_keys(text, with_spaces=True)
    text_field.type_keys('^(a)^(c)')
    text_field.type_keys('Text should be shifted')
    text_field.type_keys('^(a)^(v)')
    # print(text_field.texts())
    index = 0
    assert text_field.texts()[index] in text


# TODO raise exception if the program still runing
def apply_settings(window):
    window.Apply.wait('active').click()
    if window.is_process_running()is False:
        print('Something wrong')


def type_an_error_report(window, error_text=''):
    window.PDFRedirect.Button.click()
    descr_error_window = window['Description Error']
    descr_error_window.edit.type_keys(error_text, with_spaces=True)


# TODO asserting confirmation message
def send_error_confirmation_message(window):
    confirm_msg = window.top_window()
    first_element = 0
    assert confirm_msg.Static.texts()[first_element] in 'Message sent'
    assert confirm_msg.Button.texts()[first_element] in 'OK'


def change_dropdown_list(window):
    print(window['Printer name:ComboBox'].ItemCount())
    print(window['Printer name:ComboBox'].ItemTexts())
    print(window['Printer name:ComboBox'].SelectedText())
    window['Printer name:ComboBox'].Select('Fax')
    # time.sleep(2)
    assert window['Printer name:ComboBox'].SelectedText() in 'Fax'
