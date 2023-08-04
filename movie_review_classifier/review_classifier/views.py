# review_classifier/views.py

from django.shortcuts import render
from .models import MovieReviewClassifier
from .forms import ReviewForm

def predict_rating(request):
    predicted_rating = None

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = form.cleaned_data['review_text']
            model_path = "path/to/your/fine_tuned_model"  # Update this with your actual model path

            classifier = MovieReviewClassifier()
            predicted_rating = int(classifier.predict(review_text))
            mapping = {1: "very negative", 2: "very negative", 3: "negative", 4: "rather negative", 7:"rather positive", 8: "positive", 9: "positive", 10:"very positive"}
            outcome = mapping[predicted_rating]
            predicted_rating = f"{predicted_rating} out of 10. We think this review is {outcome}."

    else:
        form = ReviewForm()

    context = {
        'form': form,
        'predicted_rating': predicted_rating,
    }
    return render(request, 'predict_rating.html', context)
