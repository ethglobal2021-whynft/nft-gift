from django.test import TestCase

from web.tasks import send_email


class EmailTestCase(TestCase):
    # def setUp(self):
    #     RawNewsText(**TEST_NEWS).save()
    def test_email_send(self):
        send_email()
