import pytest
import testing

def test_get_visits_in_country():
    assert testing.get_visits_in_country(testing.geo_logs, 'Россия') == [
        ['Москва', 'Россия'],
        ['Владимир', 'Россия'],
        ['Тула', 'Россия'],
        ['Тула', 'Россия'],
        ['Курск', 'Россия'],
        ['Архангельск', 'Россия']
    ]

def test_get_unique_ids():
    assert sorted(testing.get_unique_ids(testing.ids)) == sorted([213, 15, 54, 119, 98, 35])

def test_get_search_queries_stats():
    assert testing.get_search_queries_stats(testing.queries) == {'Поисковых запросов из 2 слов(а)': 43, 'Поисковых запросов из 3 слов(а)': 57}

