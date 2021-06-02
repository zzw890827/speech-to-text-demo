from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Todo (Zhao, 2021/06/01): Implement other cloud service (e.g. GCP, AZ, AWS)
class IBMConverter(object):
    def __init__(self, api_url, access_key, source):
        self.__api_url = api_url
        self.__access_key = access_key
        self.__source = source

    @property
    def transcript(self):
        authenticator = IAMAuthenticator(self.__access_key)
        service = SpeechToTextV1(authenticator=authenticator)
        service.set_service_url(self.__api_url)

        result = service.recognize(model='ja-JP_BroadbandModel',
                                   audio=self.__source,
                                   content_type='audio/wav',
                                   timestamps=True,
                                   word_confidence=True).get_result()
        return result['results'][0]['alternatives'][0]['transcript']
