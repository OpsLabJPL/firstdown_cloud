import json
from time import strftime, gmtime
import unittest

from moto import mock_sns

from firstdown_cloud.sns import *


class SNSTestCase(unittest.TestCase):

    @mock_sns
    def __moto_setup(self):
        topic = create_topic("test-topic")
        topic_arn = topic.get("TopicArn")
        return topic_arn


    @mock_sns
    def test_sns_publish(self):
        topic_arn = self.__moto_setup()
        message = "Hello, test world!"
        publish_message(topic_arn, message)


    @mock_sns
    def test_sns_publish_user_notification(self):
        topic_arn = self.__moto_setup()
        payload = {}
        payload["default"] = "Default message, only used when no platform-specific data for the receiver exists."
        message = "Elvis has left the building"
        sound = "default"
        badge = 1
        category = "Celebrity Departure"
        #populate aps dictionary with standard values
        aps = make_apns_payload(alert=message, sound=sound, badge=badge, category=category, thread_id=None)
        #populate aps dictionary with app specific data values
        time = gmtime()
        time_str = strftime("%Y-%M-%dT%H:%M:%S", time)
        aps["time"] = time_str

        self.assertEqual(message, aps["alert"])
        self.assertEqual(category, aps["category"])
        self.assertEqual(sound, aps["sound"])
        self.assertEqual(category, aps["category"])
        self.assertTrue("thread-id" not in aps)

        # for APNS_SANDBOX, replaces APNS with APXS_SANDBOX
        payload["APNS"] = {"aps": aps}

        gcm = make_gcm_payload(title=category, message=message, topic=category)
        gcm["data"]["time"] = time_str

        self.assertEqual(category, gcm["notification"]["title"])
        self.assertEqual(message, gcm["notification"]["body"])

        payload["GCM"] = gcm

        json_str = json.dumps(payload, sort_keys=True, indent=4, separators=(',', ': '))
        publish_message(topic_arn=topic_arn, message=json_str)


    @mock_sns
    def test_sns_publish_silent_notification(self):
        topic_arn = self.__moto_setup()
        payload = {}
        time = gmtime()
        time_str = strftime("%Y-%M-%dT%H:%M:%S", time)
        aps = make_apns_silent_payload()
        aps["time"] = time_str

        self.assertTrue("alert" not in aps)
        self.assertTrue("sound" not in aps)
        self.assertTrue("badge" not in aps)
        self.assertEqual(1, aps["content-available"])

        gcm = make_gcm_silent_payload()
        gcm["data"]["time"] = time_str

        self.assertTrue("data" in gcm)
        self.assertTrue("notification" not in gcm)

        payload["APNS"] = {"aps": aps}
        payload["GCM"] = gcm

        json_str = json.dumps(payload, sort_keys=True, indent=4, separators=(',', ': '))
        publish_message(topic_arn=topic_arn, message=json_str)

