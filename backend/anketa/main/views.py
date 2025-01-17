from django.http import JsonResponse

def main_page_data(request):
    data = {
        "welcome_message": "Салам алейкум",
        "articles": [
            {"id": 1, "title": "Первая статья"},
            {"id": 2, "title": "Вторая статья"},
        ] 
    }
    return JsonResponse(data)