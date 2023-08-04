# local_api/views.py
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MovieReviewClassifier

# Replace this with the path to your fine-tuned model
model_path = "/home/maxem/Downloads/tuned_multiclass_classification_actual"
classifier = MovieReviewClassifier()

@api_view(['POST'])
def predict_rating(request):
    data = request.data
    review_text = data.get('review_text')
    predicted_rating = int(classifier.predict(review_text))
    print(Response({'predicted_rating': predicted_rating}))
    return Response({'predicted_rating': predicted_rating})
