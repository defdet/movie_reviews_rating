# review_classifier/views.py

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

# ... other views ...

def predict_rating(request):
    predicted_rating = None

    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        if review_text:
            # Replace 'http://your-local-ip:8000/predict_rating/' with your local API endpoint
            local_api_url = 'http://127.0.0.1:8000/predict_rating/'
            data = {'review_text': review_text}

            try:
                response = requests.post(local_api_url, json=data)
                if response.status_code == 200:
                    predicted_rating = response.json().get('predicted_rating')
                else:
                    # Handle the case when the local API returns an error
                    pass
            except requests.exceptions.RequestException:
                # Handle connection error to the local API
                pass

    context = {
        'predicted_rating': predicted_rating,
    }
    return render(request, 'predict_rating.html', context)
