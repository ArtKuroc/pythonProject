def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')

    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>')

    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>')


send_email('Hello', 'ArtKuroc@yandex.ru', 'university.help@gmail.com')
send_email('Hello', 'ArtKuroc@yandex.ru', 'university.fan@gmail.com')
send_email('Hello', 'ArtKuroc@yandex.ru', 'university.help@gmail.ua')
send_email('Hello', 'ArtKuroc_yandex.ru', 'university.help@gmail.com')
send_email('Hello', 'university.help@gmail.com', 'university.help@gmail.com')