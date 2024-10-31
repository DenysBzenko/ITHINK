import speech_recognition as sr
import pygame
pygame.mixer.init()

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
            play_audio_response("audio/tesp.mp3")
        except sr.RequestError as e:
            print(f"Помилка сервісу: {e}")
            play_audio_response("audio/tesp.mp3")

def play_audio_response(file_path):

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def dialog_flow(user_input):
    # Ключові слова для різних сценаріїв
    positive_keywords = [
        "не надо блокировать", "согласен", "да", "конечно", "буду пользоваться",
        "не блокируйте", "продлевать", "продлевайте", "нет планирую",
        "не пользуюсь", "хорошо", "планирую", "планируем", "буду пользоваться дальше",
        "планируется", "он мне нужен"
    ]

    more_info_keywords = [
        "не хочу торопиться с решением", "больше узнать", "больше информации", "разъясните",
        "объясните", "уточните", "расскажите подробнее", "хотелось бы понять", "нужна дополнительная информация",
        "не спешу с выбором", "можно больше деталей", "хочу разобраться", "какие есть варианты",
        "дайте полную информацию", "объясните по пунктам", "как это работает", "что нужно учитывать",
        "дайте рекомендации", "хочу подумать", "дайте время подумать", "могу обсудить позже",
        "надо подумать над решением", "какой договор", "какое продление"
    ]

    no_notification_keywords = [
        "проинформирован заранее", "проинформирован", "уведомление", "уведомить", "смска",
        "смс", "не сообщили", "предупреждать", "не предупредили", "не было информации", "оповещение",
        "как узнать заранее", "где уведомление", "мне не сообщили", "предупреждение", "сообщите заранее",
        "можно ли получить уведомление", "хочу получить информацию", "как уведомить", "когда будет сообщение",
        "есть ли способ уведомить"
    ]

    visit_office_keywords = [
        "я поеду в отделение", "надо ехать в отделение", "я заеду к вам", "я приеду к вам", "я поеду к вам",
        "в отделение", "собираюсь посетить отделение", "планирую приехать", "хочу заехать", "мне нужно в отделение",
        "когда могу приехать", "когда открыто отделение", "какие часы работы", "как доехать до отделения", "адрес отделения",
        "можно ли приехать", "я на пути к вам", "нужно зайти в отделение", "как долго там буду", "могу ли записаться на время",
        "есть ли очередь", "какие документы взять", "нужна ли предварительная запись"
    ]

    no_use_keywords = [
        "не пользуюсь", "номер не актуальный", "не нуждаюсь", "это не нужно", "больше не использую",
        "устаревший номер", "номер не верный", "не могу использовать", "не подходит", "не актуально",
        "это не работает", "больше не требуется", "не собираюсь пользоваться", "номер недоступен",
        "это не полезно", "это лишнее", "не планирую использовать"
    ]

    deactivate_keywords = [
        "не согласен", "деактивируйте", "блокируйте", "не буду пользоваться", "не надо", "отмените", "уберите",
        "не хочу этого", "это не подходит", "не принимаю", "не согласна", "закройте", "не нужно", "достаточно",
        "не вижу смысла", "это лишнее", "не принимаю решение", "не буду выполнять", "не согласен с условиями",
        "не устраивает", "уберите это"
    ]

    inconvenient_keywords = [
        "не могу говорить", "занят", "наберите через минуту", "подождите минуточку", "перезвоню", "перезвоните",
        "не могу сейчас", "на работе", "за рулем", "давайте позже", "сделаем позже", "давайте потом",
        "сейчас надо", "отложить", "отложим", "отложите", "занята", "до свидания", "сейчас неудобно",
        "перезвоните позже", "в следующем звонке", "позже свяжусь", "не готов говорить", "у меня встреча",
        "немного занят", "не могу говорить долго", "позже обсудим", "у меня дела", "не отвлекайте",
        "сейчас не время", "просто занят", "могу ответить позже", "в другой раз"
    ]

    explanation_keywords = [
        "что значит продлить", "в смысле блокировать", "зачем блокировать", "как это работает", "какие последствия",
        "для чего это нужно", "что за условия", "как избежать блокировки", "в чем причина блокировки", "как узнать",
        "что делать при блокировке", "какие шаги предпринять", "на сколько времени блокируется", "что означает продлить"
    ]

    suspicion_keywords = [
        "почему оператор звонит с неизвестного номера", "номер странный", "непонятно", "странно",
        "что-то здесь не так", "вызываете сомнения", "ощущение некомфорта", "не уверен", "это вызывает подозрение",
        "неясно", "это странное поведение", "нужно проверить"
    ]

    repeat_keywords = [
        "уже звонили", "уже продлевал", "уже был у вас", "уже делал", "уже ездил", "уже была консультация",
        "продлевал в приложении", "продлеваю в приложении", "как продлить"
    ]

    verification_keywords = [
        "докажите что вы сотрудник мтс", "вы с мтс", "вы из компании мтс", "вы не оператор",
        "вы не представляете мтс", "я не верю", "это подозрительно", "подтвердите", "откуда звоните",
        "кто звонит", "как зовут", "представьтесь", "с кем я разговариваю"
    ]

    fraud_keywords = [
        "ваш колега лохотронщик уже звонил", "мошенники", "аферисты", "скам", "развод",
        "обман", "лохотрон", "мошенник", "вы мошенник", "жульё", "придурок", "идиот",
        "не буду говорить", "всё, хватит, закончили"
    ]

    not_present_keywords = [
        "человек нет рядом", "он ушел", "он уехал", "она отошла", "её нет", "он не на месте",
        "человек отсутствует", "я передам сообщение", "я могу передать", "я сообщу",
        "это чужой телефон", "нет владельца", "владелец отошел"
    ]

    if any(keyword in user_input for keyword in positive_keywords):
        play_audio_response("audio/ANSWER YES.mp3")
        return "Позитивна відповідь оброблена"

    elif any(keyword in user_input for keyword in more_info_keywords):
        play_audio_response("audio/I NEED MORE INFORMATION .mp3")
        return "Запит додаткової інформації"

    # elif any(keyword in user_input for keyword in no_notification_keywords):
    #     play_audio_response("audio/tesp.mp3")
    #     return "Запит на попередження"
    #
    # elif any(keyword in user_input for keyword in visit_office_keywords):
    #     play_audio_response("audio/tesp.mp3")
    #     return "Запит на візит до відділення"

    elif any(keyword in user_input for keyword in no_use_keywords):
        play_audio_response("audio/tesp.mp3")
        return "Невикористання номера"

    elif any(keyword in user_input for keyword in deactivate_keywords):
        play_audio_response("audio/DEAKTIVATE .mp3")
        return "Запит на деактивацію"

    elif any(keyword in user_input for keyword in inconvenient_keywords):
        play_audio_response("audio/CANT SPEAK.mp3")
        return "Перенесення розмови"

    # elif any(keyword in user_input for keyword in explanation_keywords):
    #     play_audio_response("audio/tesp.mp3")
    #     return "Пояснення процесу"
    #
    # elif any(keyword in user_input for keyword in suspicion_keywords):
    #     play_audio_response("audio/tesp.mp3")
    #     return "Виникли підозри"
    #
    # elif any(keyword in user_input for keyword in repeat_keywords):
    #     play_audio_response("audio/tesp.mp3")
    #     return "Повторення питання"
    #
    # elif any(keyword in user_input for keyword in verification_keywords):
    #     play_audio_response("audio/tesp.mp3")
    #     return "Підтвердження оператора"

    elif any(keyword in user_input for keyword in fraud_keywords):
        play_audio_response("audio/SCAM COLEGA.mp3")
        return "Запит про шахрайство"

    elif any(keyword in user_input for keyword in not_present_keywords):
        play_audio_response("audio/THE HUMAN NOT HERE .mp3")
        return "Немає абонента на місці"

    else:
        play_audio_response("audio/QUESTION X.mp3")
        return "Невідома відповідь"

def main():
    play_audio_response("audio/SOUND 1 .mp3")

    user_input = recognize_speech()

    if user_input:
        result = dialog_flow(user_input)
        print("Результат: ", result)


if __name__ == "__main__":
    main()