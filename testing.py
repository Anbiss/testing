# Task 1

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def get_visits_in_country(geo_logs, country='Россия'):
    return [geo for dictionary in geo_logs for _, geo in dictionary.items() if geo[1] == country]


# Task 2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35], }

def get_unique_ids(ids):
    return list(set(sum for number in ids.values() for sum in number))


# Task 3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

def get_search_queries_stats(queries):
    a = len(queries)
    rez = {}

    for request in queries:
        word = len(request.split())
        if rez.get(word):
            rez[word] += 1
        else:
            rez[word] = 1

    return {f'Поисковых запросов из {x} слов(а)': round((y * 100) / a) for x, y in sorted(rez.items())}