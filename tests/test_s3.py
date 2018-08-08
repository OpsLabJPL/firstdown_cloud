import sys
import StringIO
import unittest

from moto import mock_s3

from firstdown_cloud.s3 import get_client, list_buckets, list_objects, read_object, main


class S3TestCase(unittest.TestCase):

    def setUp(self):
        self.bucket = 'static'
        self.key = 'style.css'
        self.value = 'value'

    @mock_s3
    def __moto_setup(self):
        s3 = get_client()
        s3.create_bucket(Bucket=self.bucket)
        s3.put_object(Bucket=self.bucket, Key=self.key, Body=self.value)

    def test_get_client(self):
        s3 = get_client()
        self.assertEqual(s3._endpoint.host, 'https://s3.us-gov-west-1.amazonaws.com')

    @mock_s3
    def test_list_buckets(self):
        self.__moto_setup()
        buckets = [b for b in list_buckets()]
        self.assertTrue(self.bucket in buckets)

    @mock_s3
    def test_list_objects(self):
        self.__moto_setup()
        objects = [o for o in list_objects(self.bucket)]
        self.assertTrue(self.key in objects)

    @mock_s3
    def test_read_object(self):
        self.__moto_setup()
        content = read_object(self.bucket, self.key)
        self.assertTrue(self.value == content)

    @mock_s3
    def test_main(self):
        self.__moto_setup()
        sys.stdout = mystdout = StringIO.StringIO()
        main()
        content = mystdout.getvalue()
        self.assertTrue('[ {} ]'.format(self.bucket) in content)
        self.assertTrue('=> {}'.format(self.key) in content)
