import unittest
import email_sender

class ValidateEmailTests(unittest.TestCase):
    def testValidateEmail(self):
        email = "calvinlsliang@gmail.com"
        self.failUnless(email_sender.validate_email(email))

    def testValidateEmailMultipleAt(self):
        email = "calvin@lsliang@gmail.com"
        self.failIf(email_sender.validate_email(email))

    def testValidateEmailNoAt(self):
        email = "calvinlslianggmail.com"
        self.failIf(email_sender.validate_email(email))

    def testValidateEmailConsecutivePeriods(self):
        email = "calvinlsliang@gmail..com"
        self.failIf(email_sender.validate_email(email))

    def testValidateEmailWithInteger(self):
        email = 1
        self.failIf(email_sender.validate_email(email))

def main():
    unittest.main()

if __name__ == '__main__':
    main()