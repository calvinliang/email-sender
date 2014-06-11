import unittest
import email_sender

class FormatMailgunTests(unittest.TestCase):

    # This function is called after validate_inputs so a lot
    # of the usual test cases won't apply.

    def testFormatMailgun(self):
        data = {
            "to": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }
        response = email_sender.format_mailgun(data)
        self.assertEqual(response['to'], "Calvin <calvinlsliang@gmail.com>")
        self.assertEqual(response['from'], "Calvin2 <calvinlsliang2@gmail.com>")
        self.assertEqual(response['text'], "World!")
        self.assertEqual(response['subject'], "Hello")

    def testFormatMailgunBadKeys(self):
        data = {
            "bad": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }

        self.failIf(email_sender.format_mailgun(data))



def main():
    unittest.main()

if __name__ == '__main__':
    main()