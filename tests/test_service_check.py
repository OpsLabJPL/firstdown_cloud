import getpass
from unittest import TestCase
from firstdown_cloud import service_check
from moto import mock_s3
from firstdown_cloud.s3 import get_client, list_objects

class TestServiceCheck(TestCase):

    def setUp(self):
        self.bucket = 'nsytinfo'
        self.key = 'status.json'
        self.username = getpass.getuser()

    @mock_s3
    def __moto_setup(self):
        s3 = get_client()
        s3.create_bucket(Bucket=self.bucket)


    def test_expected_output_is_present(self):
        self.outputIsThere = service_check.expected_output_is_present(["echo $USER"], self.username)
        self.assertTrue(self.outputIsThere)


    @mock_s3
    def test_upload_service_status(self):
        self.__moto_setup()
        service_check.upload_service_status(["echo $USER"], self.username, self.bucket, self.key)
        objects = [o for o in list_objects(self.bucket)]
        self.assertTrue(self.key in objects)

