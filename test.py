import unittest
import os
from pywinauto.application import Application
import time
import utilities
from pywinauto.base_wrapper import ElementNotEnabled as Error
from win32gui import GetForegroundWindow
from pywinauto.findwindows import ElementNotFoundError


class TestSuite_settings(unittest.TestCase):
    meta_data = 'Вулиці Вінниці'
    printer_xps = 'Microsoft XPS Document Writer'
    printer_pdf = 'Microsoft Print to PDF'
    printer_fax = 'Fax'
    pdf_reader = 'FoxitReaderPortable'



    def setUp(self):
        self.app = Application(backend="win32").start(
            r"c:\Users\an.kravets\Downloads\PDFRedirect\PDFRedirect.exe")
        self.main_window = self.app.PDFRedirect

    #TODO screenshot for fail
    def tearDown(self):
        #if _______]:
            #self.app.top_window().capture_as_image().save(self.id()+'.png')
        while True:
            if self.app.is_process_running() == True:
                self.app.top_window().close()
            else:
                break


    #@unittest.skip('pass')
    def test_0_default_view_first_launch(self):
        utilities.default_view(self.main_window)

    #TODO close reader window
    #@unittest.skip('pass')
    def test_set_pdf_reader(self):
        first_element = 0
        utilities.set_default_reader(self.main_window, self.app)
        try:
            handle = GetForegroundWindow()
            temporary_app = Application().connect(handle=handle)
            time.sleep(2)
            temporary_app.top_window().close()
        except :
            pass
        assert self.main_window['Name:Edit'].texts()[first_element] == self.pdf_reader

    #@unittest.skip('pass')
    def test_select_printers_settings(self):
        utilities.select_printer(self.main_window, self.printer_fax)
        assert self.main_window['Printer name:ComboBox'].SelectedText() in self.printer_fax
        utilities.select_paper_format(self.main_window, 'A6')
        assert self.main_window['Paper format:ComboBox'].SelectedText() in 'A6'
        utilities.select_duplex(self.main_window, 'Vertical')
        assert self.main_window['Duplex:ComboBox'].SelectedText() in 'Vertical'
        #time.sleep(3)


    #@unittest.skip('pass')
    def test_matching_paper_and_printer_settings(self):
        utilities.match_printer_settings(self.main_window)


    #@unittest.skip('pass')
    def test_apply_setting_without_pdf_reader(self):
        utilities.input_text_pattern(self.main_window, self.meta_data)
        try:
            self.main_window.Apply.verify_actionable()
            self.fail('The Apply button is active')
        except Error:
            pass


    #@unittest.skip('pass')
    def test_apply_settings_without_text_pattern(self):
        utilities.set_default_reader(self.main_window, self.app)
        try:
            self.main_window.Apply.verify_actionable()
            self.fail('The Apply button is active')
        except Error:
            pass



    #@unittest.skip('pass')
    def test_za_apply_settings(self):
        #self.main_window.print_control_identifiers()
        utilities.set_default_reader(self.main_window, self.app)
        utilities.input_text_pattern(self.main_window, self.meta_data)
        utilities.select_printer(self.main_window, self.printer_pdf)
        utilities.select_paper_format(self.main_window, 'A4')
        utilities.select_duplex(self.main_window, 'Default')
        utilities.apply_settings(self.main_window)

        self.app = Application(backend="win32").start(
            r"c:\Users\an.kravets\Downloads\PDFRedirect\PDFRedirect.exe")
        self.main_window = self.app.PDFRedirect
        utilities.default_view(self.main_window, self.pdf_reader, self.meta_data, self.printer_pdf, 'A4', '',
                               'Default')


    #@unittest.skip('pass')
    def test_send_an_error_report(self):
        utilities.type_an_error_report(self.app, 'Test ')
        #self.app['Description Error'].Send.click()
        #utilities.send_error_confirmation_message(self.app)


    #@unittest.skip('pass')
    def test_send_an_empty_error_report(self):
        utilities.type_an_error_report(self.app)
        #self.app['Description Error'].Send.click()
        #utilities.send_error_confirmation_message(self.app)





    # TODO scroll test
    @unittest.skip('pass')
    def test_scrolling_error_report(self):
        utilities.type_an_error_report(self.app, 'Test '*120)



    #@unittest.skip('pass')
    def test_close_ALT_F4(self):
        self.main_window.close_alt_f4()
        assert self.app.is_process_running() is False



class TestSuite_opening_file(unittest.TestCase):

    def setUp(self):
        self.app = None
        print(self.id())

    def tearDown(self):
        self.app.top_window().close()

    def _zb_open_metadata_file(self):
        os.popen(r'c:\Users\an.kravets\Desktop\MetaData_File.pdf')
        time.sleep(0.5)
        handle = GetForegroundWindow()
        self.app = Application().connect(handle = handle)
        time.sleep(2)
        first_element = 0
        assert self.app.top_window().texts()[first_element] in 'Печать'
        assert self.app.top_window()['&Имя:ComboBox'].SelectedText()[first_element] in 'Microsoft Print to PDF'
        #app.Dialog.Button0.click()
        #time.sleep(3)
        #app.top_window().print_control_identifiers()



    def _zc_open_file_without_metadata(self):
        os.popen(r'c:\Users\an.kravets\Desktop\File.pdf')
        time.sleep(1)
        handle = GetForegroundWindow()
        self.app = Application().connect(handle=handle)
        time.sleep(3)
        first_element = 0
        assert self.app.top_window().texts()[first_element] in 'File.pdf - Foxit Reader'









if __name__ == "__main__":

    unittest.main()