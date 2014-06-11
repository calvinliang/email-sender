import unittest
import email_sender

class CleanBodyTests(unittest.TestCase):

    def testCleanBody(self):
        s = '<h1>Hello</h1>'
        self.assertEqual(email_sender.clean_body(s), 'Hello')

    def testCleanBodyRegularString(self):
        s = 'Hello'
        self.assertEqual(email_sender.clean_body(s), 'Hello')

    def testCleanBodyConsecutiveHTMLTags(self):
        s = '<a><b><c>Hello</a></b></c>'
        self.assertEqual(email_sender.clean_body(s), 'Hello')

    def testCleanBodyHrefAttributes(self):
        s = '<a id="foo">Hello</a>'
        self.assertEqual(email_sender.clean_body(s), 'Hello')

    def testCleanBodyRandomString(self):
        s = '<<<<<<<<<<<<<<>Hello'
        self.assertEqual(email_sender.clean_body(s), 'Hello')

    def testCleanBodyRandomString2(self):
        s = '<script<script>>alert("Hi!")<</script>/script>'
        self.assertEqual(email_sender.clean_body(s), '>alert("Hi!")/script>')

def main():
    unittest.main()

if __name__ == '__main__':
    main()