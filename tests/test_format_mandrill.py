import unittest
import email_sender

class FormatMandrillTests(unittest.TestCase):

    # This function is called after validate_inputs so a lot
    # of the usual test cases won't apply.

    def testFormatMandrill(self):
        data = {
            "to": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }
        response = email_sender.format_mandrill(data, '123')
        self.assertEqual(response['key'], '123')
        self.assertEqual(response['message']['to'][0]['email'], "calvinlsliang@gmail.com")
        self.assertEqual(response['message']['to'][0]['name'], "Calvin")
        self.assertEqual(response['message']['to'][0]['type'], "to")
        self.assertEqual(response['message']['from_email'], "calvinlsliang2@gmail.com")
        self.assertEqual(response['message']['from_name'], "Calvin2")
        self.assertEqual(response['message']['subject'], "Hello")
        self.assertEqual(response['message']['text'], "World!")

    def testFormatMandrillBadKeys(self):
        data = {
            "bad": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }
        self.failIf(email_sender.format_mandrill(data, '123'))

def main():
    unittest.main()

if __name__ == '__main__':
    main()