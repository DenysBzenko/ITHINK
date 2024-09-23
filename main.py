  import speech_recognition as sr
import pyttsx3

# Функція для розпізнавання голосу
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажіть щось...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="uk-UA")
            print("Ви сказали: ", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Не вдалося розпізнати голос.")
        except sr.RequestError as e:
            print(f"Помилка сервісу; {e}")

# Функція для озвучування тексту
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Основна функція
def main():
    user_input = recognize_speech()
    if user_input:
        # Перевіряємо, чи є в тексті певні питання
        if "як справи" in user_input:
            response = "Добре"
        elif "скільки тобі років" in user_input:
            response = "Мені 100 років"
        elif "як тебе звати" in user_input:
            response = "Мене звати Андрій"
        else:
            response = "Я не знаю як відповісти на це питання"
        
        print("Відповідь: ", response)
        speak_text(response)

if __name__ == "__main__":
    main()
