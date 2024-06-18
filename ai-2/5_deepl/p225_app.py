import deepl
import os

input_path = "./data/어린왕자_영어_원본.docx"
output_path = "./data/어린왕자_한국어_번역.docx"

auth_key = os.environ["DEEPL_AUTH_KEY"]

translator = deepl.Translator(auth_key)

result = translator.translate_document_from_filepath(input_path, output_path,
target_lang="KO")

print(result.done)