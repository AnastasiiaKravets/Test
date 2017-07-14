from pywinauto.application import Application
import time
from win32gui import GetForegroundWindow
from pywinauto.timings import WaitUntilPasses
import unittest



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
    window_widght = 448
    window_height = 359

    assert window.rectangle().width() == window_widght
    assert window.rectangle().height() == window_height
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
    #assert window['Paper source:ComboBox'].SelectedText() in paper_source_list
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


def apply_settings(window):
    window.Apply.wait('enabled').click()


def type_an_error_report(window, error_text=''):
    window.PDFRedirect.Button.click()
    descr_error_window = window['Description Error']
    descr_error_window.edit.type_keys(error_text, with_spaces=True)


def send_error_confirmation_message(window):
    confirm_msg = window.top_window()
    first_element = 0
    assert confirm_msg.Static2.texts()[first_element] in 'Message sent.'
    assert confirm_msg.Button.texts()[first_element]in 'ОК'
    confirm_msg.Button.click()


def select_printer(window, printer_name):
    window['Printer name:ComboBox'].Select(printer_name)


def select_paper_format(window, paper_format):
    window['Paper format:ComboBox'].Select(paper_format)


def select_duplex(window, duplex):
    window['Duplex:ComboBox'].Select(duplex)


def match_printer_settings(window):
    xps_writer_items = ['Letter', 'Letter Small', 'Таблоид']
    pdf_items = ['Letter', 'Таблоид', 'Legal']
    fax_items = ['Letter', 'Letter Small', 'Legal']
    xps_writer_amount = 107
    pdf_amount = 10
    fax_amount = 69

    select_printer(window, 'Microsoft XPS Document Writer')
    if window['Printer name:ComboBox'].SelectedText() == 'Microsoft XPS Document Writer':
        iteration = 0
        for element in window['Paper format:ComboBox'].ItemTexts():
            assert element in xps_writer_items
            iteration += 1
            if iteration == 3:
                break
        assert window['Paper format:ComboBox'].ItemCount() == xps_writer_amount
        assert window['Paper source:ComboBox'].SelectedText() in 'Автовыбор'

    select_printer(window, 'Microsoft Print to PDF')
    if window['Printer name:ComboBox'].SelectedText() == 'Microsoft Print to PDF':
        iteration = 0
        for element in window['Paper format:ComboBox'].ItemTexts():
            assert element in pdf_items
            iteration += 1
            if iteration == 3:
                break
        assert window['Paper format:ComboBox'].ItemCount() == pdf_amount
        #window['Paper source:ComboBox'].SelectedText()

    select_printer(window, 'Fax')
    if window['Printer name:ComboBox'].SelectedText() == 'Fax':
        iteration = 0
        for element in window['Paper format:ComboBox'].ItemTexts():
            assert element in fax_items
            iteration += 1
            if iteration == 3:
                break
        assert window['Paper format:ComboBox'].ItemCount() == fax_amount
        assert window['Paper source:ComboBox'].SelectedText() in 'По умолчанию'



def set_default_reader(window, app):
    window['...Button'].click()
    WaitUntilPasses(10, 0.5, lambda: app.window_(title=u'Select application'))
    select_app = app['Select application']
    path = "c:\Adobe\AcrobatReaderDC\Reader\AcroRd32.exe"
    select_app.edit.type_keys(path, with_spaces=True)
    select_app.OpenButton.click()

    handle_pdf_redirect = GetForegroundWindow()
    first_element = 0
    time.sleep(1)
    handle_reader = GetForegroundWindow()
    if handle_reader != handle_pdf_redirect:
        try:
            temporary_app = Application().connect(handle=handle_reader)
            if temporary_app.top_window().texts()[first_element] == 'Adobe Acrobat Reader DC':
                temporary_app.top_window().close()
        except:
            pass

