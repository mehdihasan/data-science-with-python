# pip install PyJWT==1.7.1 ibm_watson wget

from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

from ibm_watson import LanguageTranslatorV3


### SPEECH TO TEXT

# wget -O PolynomialRegressionandPipelines.mp3  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3


url_s2t = ""
iam_apikey_s2t = ""


with open('misc/speech-to-text-api-key.txt', 'r') as file:
    lines = file.readlines() 
    url_s2t = lines[5].strip()
    iam_apikey_s2t = lines[3].strip()

print(url_s2t)
print(iam_apikey_s2t)

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

filename='resources/oroni1.mp3'

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

print(response.result)

json_normalize(response.result['results'],"alternatives")

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)


### LANGUAGE TRANSLATOR

url_lt='https://gateway.watsonplatform.net/language-translator/api'
apikey_lt=''


with open('misc/language-translator-api-key.txt', 'r') as file:
    lines = file.readlines() 
    apikey_lt = lines[3].strip()
    url_lt = lines[5].strip()


print(apikey_lt)
print(url_lt)

version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator


print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))

translation_response = language_translator.translate(text=recognized_text, model_id='en-es')
print(translation_response)

translation=translation_response.get_result()
print(translation)

spanish_translation =translation['translations'][0]['translation']
print(spanish_translation)

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
translation_eng=translation_new['translations'][0]['translation']
print(translation_eng)