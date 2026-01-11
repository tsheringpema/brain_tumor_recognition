from django.shortcuts import render

# Create your views here.
import os
from django.shortcuts import render
from .forms import ImageUploadForm
from keras.models import load_model
import numpy as np
from PIL import Image
from django.core.files.storage import FileSystemStorage

# Load model once
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, 'tumor_detector', 'brain_tumor_model.h5')
model = load_model(MODEL_PATH)

classes = ['Glioma', 'Meningioma', 'Notumor', 'Pituitary']

def preprocess_image(image_file):
    img = Image.open(image_file).convert('RGB')
    img = img.resize((128, 128))
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def home_view(request):
    return render(request, 'home.html')

def team(request):
    return render(request, 'team.html')

def predict_view(request):
    prediction = None
    confidence = None
    image_url = None
    form = ImageUploadForm()

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            # Save uploaded image to media folder
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)  # relative URL for template

            # Preprocess and predict
            img_array = preprocess_image(fs.path(filename))
            print("img_array.shape:", img_array.shape)  # Add this line for debugging
            preds = model.predict(img_array)

            pred_index = np.argmax(preds)
            prediction = classes[pred_index]
            confidence = float(preds[0][pred_index]) * 100  # as percentage

    return render(request, 'predict.html', {
        'form': form,
        'prediction': prediction,
        'confidence': f"{confidence:.2f}%" if confidence is not None else None,
        'image_url': image_url
    })
