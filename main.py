from configparser import ConfigParser

from speech_to_text import IBMConverter

if __name__ == '__main__':
    cloud = 'IBM'
    config = ConfigParser()
    config.read('credential.cfg')
    api_url = config.get(cloud, 'api_url')
    access_key = config.get(cloud, 'access_key')

    fileName = 'data/publicaudioja-JP_Broadband-sample.wav'

    with open(fileName, 'rb') as audio:
        speech_to_text_result = IBMConverter(api_url, access_key, audio)
        print(speech_to_text_result.transcript)
