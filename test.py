import unittest
import os
import subprocess

import sys
from pywinauto.application import Application
import time
import utilities
from pywinauto.base_wrapper import ElementNotEnabled as Error
from win32gui import GetForegroundWindow, FindWindow
from pywinauto.application import AppStartError
from pywinauto.timings import WaitUntilPasses


class TestSuite_settings(unittest.TestCase):
    path_to_app = 'c:\\Users\\an.kravets\Downloads\PDFRedirect\PDFRedirect.exe'
    path_to_app_win_7 = 'C:\Test\PDFRedirect\PDFRedirect.exe'
    meta_data = 'Вулиці Вінниці'
    printer_xps = 'Microsoft XPS Document Writer'
    printer_pdf = 'Microsoft Print to PDF'
    printer_fax = 'Fax'
    pdf_reader = 'AcroRd32'


    def setUp(self):
        try:
            #self.app = Application(backend="win32").start(self.path_to_app)
            self.app = Application(backend="win32").start(self.path_to_app_win_7)

        except AppStartError:
            self.fail('The application can not start')
        """if self.app.PDFRedirect.exists(10, 0.5):
            self.main_window = self.app.PDFRedirect
        else:
            self.fail('The application is not visible')"""
        try:
            self.app.PDFRedirect.wait('ready', 20, 0.5)
        except:
            self.fail('The application can not start2')
        self.main_window = self.app.PDFRedirect

        #print(sys.getwindowsversion())
        #print(self.id())

    #TODO screenshot for fail
    def tearDown(self):
        i = 0
        '''while True:
            try:
                    self.app.top_window().close()
            except:
                break
            print(i)
            i += i'''
        self.app.kill()

    #@unittest.skip('pass')
    def test_0_clean_register(self):
        utilities.clean_register()


    #@unittest.skip('pass')
    def test_1_default_view_first_launch(self):
        utilities.default_view(self.main_window)


    #@unittest.skip('pass')
    def test_set_pdf_reader(self):
        first_element = 0
        utilities.set_default_reader(self.main_window, self.app)
        assert self.main_window['Name:Edit'].texts()[first_element] == self.pdf_reader

    #@unittest.skip('pass')
    def test_select_printers_settings(self):
        utilities.select_printer(self.main_window, self.printer_fax)
        assert self.main_window['Printer name:ComboBox'].SelectedText() in self.printer_fax
        utilities.select_paper_format(self.main_window, 'A6')
        assert self.main_window['Paper format:ComboBox'].SelectedText() in 'A6'
        utilities.select_duplex(self.main_window, 'Vertical')
        assert self.main_window['Duplex:ComboBox'].SelectedText() in 'Vertical'


    #@unittest.skip('pass')
    @unittest.skipIf(sys.getwindowsversion()[0]==6, 'Windows version 7')
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
    def test_z_apply_settings(self):
        utilities.set_default_reader(self.main_window, self.app)
        utilities.input_text_pattern(self.main_window, self.meta_data)
        utilities.select_printer(self.main_window, self.printer_fax)
        utilities.select_paper_format(self.main_window, 'A6')
        utilities.select_duplex(self.main_window, 'Vertical')
        utilities.apply_settings(self.main_window)
        """if self.app.is_process_running():
            self.fail('The program should be closed')"""

        #self.app = Application(backend="win32").start(self.path_to_app)
        self.app = Application(backend="win32").start(self.path_to_app_win_7)

        self.main_window = self.app.PDFRedirect
        utilities.default_view(self.main_window, self.pdf_reader, self.meta_data, self.printer_fax, 'A6', 'По умолчанию',
                               'Vertical')


    #@unittest.skip('pass')
    def test_send_an_error_report(self):
        utilities.type_an_error_report(self.app, 'Test ')
        self.app['Description Error'].Send.click()
        time.sleep(1)
        #WaitUntilPasses(10, 0.5, lambda: self.app.window_(title=u'PDFRedirect'))
        utilities.send_error_confirmation_message(self.app)


    #@unittest.skip('pass')
    def test_close_ALT_F4(self):
        self.main_window.close_alt_f4()
        """assert self.app.exists(1, 0.5) is False"""


class TestSuite_z_opening_file(unittest.TestCase):

    path = 'c:\\Users\\an.kravets\\Desktop'
    path_win7 = 'C:\\Users\\root\\Desktop\\'

    def find_window(self, window):
        for i in range(20):
            if FindWindow(window, window) != None:
                return True
            else:
                time.sleep(0.5)
        return False

    def setUp(self):
        self.app = None

    def tearDown(self):
        #self.app.top_window().close()
        self.app.kill()


    #@unittest.skip('pass')
    def test_zb_open_metadata_file(self):
        #os.startfile(self.path + '\MetaData_File.pdf')
        #subprocess.Popen("%s %s" % (TestSuite_settings.path_to_app, self.path+'\MetaData_File.pdf'))
        subprocess.Popen("%s %s" % (TestSuite_settings.path_to_app_win_7, self.path_win7+'\MetaData_File.pdf'))


        time.sleep(2)

        self.find_window('Печать')
        time.sleep(1)
        handle = GetForegroundWindow()
        self.app = Application().connect(handle = handle)
        #time.sleep(1)
        self.app.top_window().wait('ready', 10, 0.5)
        first_element = 0
        assert self.app.top_window().texts()[first_element] in 'Печать'
        assert self.app.top_window()['&Имя:ComboBox'].SelectedText()[first_element] in 'Fax'



    #@unittest.skip('pass')
    def test_zc_open_file_without_metadata(self):
        #subprocess.Popen("%s %s" % (TestSuite_settings.path_to_app, self.path+'\File.pdf'))
        subprocess.Popen("%s %s" % (TestSuite_settings.path_to_app_win_7, self.path_win7+'\File.pdf'))



        self.find_window('File.pdf - Adobe Acrobat Reader DC')
        time.sleep(1)

        handle = GetForegroundWindow()
        self.app = Application().connect(handle=handle)
        #time.sleep(1)
        self.app.top_window().wait('ready', 10, 0.5)
        first_element = 0
        assert self.app.top_window().texts()[first_element] in 'File.pdf - Adobe Acrobat Reader DC'





if __name__ == "__main__":
    unittest.main(verbosity=2)