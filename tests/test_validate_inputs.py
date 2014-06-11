import unittest
import email_sender

class ValidateInputTests(unittest.TestCase):

    def testValidateInputs(self):
        data = {
            "to": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "Hello!",
            "subject": "Test"
        }
        self.failUnless(email_sender.validate_inputs(data))

    def testValidateInputsInvalidValue(self):
        data = {
            "to": "calvinlslianggmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "Hello!",
            "subject": "Test"
        }
        self.failIf(email_sender.validate_inputs(data))

    def testValidateInputsWithInteger(self):
        data = {
            "to": "calvinlsliang@gmail.com",
            "to_name": 1,
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "Hello!",
            "subject": "Test"
        }
        self.failUnless(email_sender.validate_inputs(data))

    def testValidateInputsInvalidKey(self):
        data = {
            "too": "calvinlslianggmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "Hello!",
            "subject": "Test"
        }
        self.failIf(email_sender.validate_inputs(data))

    def testValidateInputsMissingOneParameter(self):
        data = {
            "to": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "subject": "Test"
        }
        self.failIf(email_sender.validate_inputs(data))

    def testValidateInputsExtraParameters(self):
        data = {
            "to": "calvinlsliang@gmail.com",
            "to_name": "Calvin",
            "from": "calvinlsliang2@gmail.com",
            "from_name": "Calvin2",
            "body": "Hello!",
            "derp": "derp",
            "subject": "Test"
        }
        self.failUnless(email_sender.validate_inputs(data))

def main():
    unittest.main()

if __name__ == '__main__':
    main()