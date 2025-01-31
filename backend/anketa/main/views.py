from django.http import JsonResponse

def main_page_data(request):
    data = {
        "welcome_message": "Салам алейкум",
        "news": [
            {"id": 1, "title": "Первая статья", 'content': 'Описание новости 1'},
            {"id": 2, "title": "Вторая статья",'content': 'Описание новости 2'},
        ], 
        'articles': [
            {'id': 1, 'tiltle': 'Статья 1', 'content': 'Описание статьи 1'},
            {'id': 2, 'tiltle': 'Статья 2', 'content': 'Описание статьи 2'},
        ]
    }
    return JsonResponse(data)