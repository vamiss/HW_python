def answer(question):
    question = question.lower()
    question_tren = question.find('трен')
    question_rasp = question.find('расп')
    question_oplat = question.find('оплат')
    if question_tren != -1:
        print('Контакты тренера:\nТелефон: +32282281337\nну и так далее, дальше лень придумывать.')
    elif question_rasp != -1:
        print('Текущее расписание:\nСЕССИЯ БЛИЗКО.\nБЕГИ. БЕГИ. БЕГИ.')
    elif question_oplat != -1:
        print('Сумма к оплате:\n3 бутылки прокисшего общажного молока.')
    else:
        print('Ты слишком тупой, чтобы работать с моим автоответчиком.')