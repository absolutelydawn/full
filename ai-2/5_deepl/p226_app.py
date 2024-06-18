import deepl
import os

folder = "./data/"
input_path = folder + "President_Obamas_Farewell_Address_영어_원본.pdf"
output_path = folder + "President_Obamas_Farewell_Address_영어_원본.pdf"

auth_key = os.environ["DEEPL_AUTH_KEY"]

translator = deepl.Translator(auth_key)

result = translator.translate_document_from_filepath(input_path, output_path,
target_lang="KO")

print(result.done)