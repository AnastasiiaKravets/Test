import unittest
from pywinauto.application import Application
import time
import utilities

class TestSuite(unittest.TestCase):

    def setUp(self):
        self.app = Application(backend="win32").start(
            r"c:\Users\an.kravets\Downloads\PDFRedirect\PDFRedirect.exe")
        self.main_window = self.app.PDFRedirect

    def tearDown(self):
        print(self._testMethodName)
        while True:
            if self.app.is_process_running() == True:
                self.app.top_window().close()
            else:
                break

    #@unittest.skip('pass')
    def test_1_first_launch(self):
        #self.main_window.print_control_identifiers()
        utilities.set_default_reader(self.main_window)
        utilities.input_text_pattern(self.main_window, 'MetaData')
        #time.sleep(2)

    #@unittest.skip('pass')
    def test_send_an_error_report(self):
        utilities.send_an_error_report(self.app, 'Description error message')
        time.sleep(1)

    def test_set_printers_settings(self):
        utilities.change_dropdown_list(self.main_window)

    def test_0close_ALT_F4(self):
        self.main_window.edit.type_keys('%({F4})')
        assert self.app.is_process_running() is False




if __name__ == "__main__":
    unittest.main()

