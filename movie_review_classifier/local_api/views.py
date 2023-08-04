# local_api/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from your_model_module import MovieReviewClassifier

# Replace this with the path to your fine-tuned model
model_path = "/home/maxem/Downloads/tuned_multiclass_classification_actual"
classifier = MovieReviewClassifier(model_path)

@api_view(['POST'])
def predict_rating(request):
    data = request.data
    review_text = data.get('review_text')
    predicted_rating = classifier.predict(review_text)
    return Response({'predicted_rating': predicted_rating})
