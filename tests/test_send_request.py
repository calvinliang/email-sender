import unittest
import email_sender

class SendRequestTests(unittest.TestCase):

    # This test is hacky in that it uses your current config settings
    # to run its tests. If you have incorrect configs it will fail.

    def testSendRequestMailgun(self):
        data = {
            "to": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }
        response = email_sender.send_request(data, 'mailgun')
        self.failUnless(response)

    def testSendRequestMailgunBadKey(self):
        data = {
            "too": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }
        response = email_sender.send_request(data, 'mailgun')
        self.failIf(response)

    def testSendRequestMailgunBadDataRemovedField(self):
        data = {
            "too": "calvinlsliang@gmail.com",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }
        response = email_sender.send_request(data, 'mailgun')
        self.failIf(response)

    def testSendRequestMandrill(self):
        data = {
            "to": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }
        response = email_sender.send_request(data, 'mandrill')
        self.failUnless(response)

    def testSendRequestMandrillBadKey(self):
        data = {
            "tooo": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }
        response = email_sender.send_request(data, 'mandrill')
        self.failIf(response)

    def testSendRequestMandrillRemovedField(self):
        data = {
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "<h1>World!</h1>",
            "subject": "Hello"
        }
        response = email_sender.send_request(data, 'mandrill')
        self.failIf(response)

def main():
    unittest.main()

if __name__ == '__main__':
    main()