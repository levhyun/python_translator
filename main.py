import googletrans
import time

translator = googletrans.Translator()

lang = ["ko", "en"]

while True:
    print("[입력 언어 설정]\n1.한국어\n2.영어\n3.일본어")
    input_lang = int(input("번호를 입력하세요>"))
    print("[출력 언어 설정]\n1.한국어\n2.영어\n3.일본어")
    output_lang = int(input("번호를 입력하세요>"))

    input_str = input("번역할 글을 입력하세요>")

    output_str = translator.translate(input_str, dest = lang[output_lang-1], src = lang[input_lang-1])

    print(f"번역 후>{output_str.text}")

    time.sleep(1000)