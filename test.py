import unittest
from pywinauto.application import Application
import time
import utilities


class TestSuite(unittest.TestCase):

    def setUp(self):
        self.app = Application(backend="win32").start(
            r"c:\Users\an.kravets\Downloads\PDFRedirect\PDFRedirect.exe")
        self.main_window = self.app.PDFRedirect

    #TODO screenshot for fail
    def tearDown(self):
        print(self._testMethodName)
        while True:
            if self.app.is_process_running() == True:
                self.app.top_window().close()
            else:
                break


    @unittest.skip('pass')
    def test_0_default_view_first(self):
        utilities.default_view(self.main_window)

    #@unittest.skip('pass')
    def test_set_pdf_reader(self):
        utilities.set_default_reader(self.main_window)

    #TODO
    @unittest.skip('pass')
    def test_set_printers_settings(self):
        pass

    #TODO
    @unittest.skip('pass')
    def test_matching_paper_and_printer_settings(self):
        pass

    @unittest.skip('pass')
    def test_apply_setting_without_pdf_reader(self):
        pass

    @unittest.skip('pass')
    def test_apply_settings_without_text_pattern(self):
        pass

    @unittest.skip('pass')
    def test_first_launch(self):
        #self.main_window.print_control_identifiers()
        utilities.set_default_reader(self.main_window)
        utilities.input_text_pattern(self.main_window, 'MetaData')
        utilities.apply_settings(self.main_window)
        # time.sleep(2)

    #TODO
    @unittest.skip('pass')
    def test_open_saved_setting(self):
        pass

    @unittest.skip('pass')
    def test_send_an_error_report(self):
        utilities.type_an_error_report(self.app, 'Test ')
        #self.app['Description Error'].Send.click()
        utilities.send_error_confirmation_message(self.app)

    @unittest.skip('pass')
    def test_send_an_empty_error_report(self):
        utilities.type_an_error_report(self.app)
        #self.app['Description Error'].Send.click()
        utilities.send_error_confirmation_message()

    # TODO scroll test
    @unittest.skip('pass')
    def test_scrolling_error_report(self):
        utilities.type_an_error_report(self.app, 'Test '*120)

    @unittest.skip('pass')
    def test_close_ALT_F4(self):
        self.main_window.close_alt_f4()
        assert self.app.is_process_running() is False




if __name__ == "__main__":
    unittest.main()

