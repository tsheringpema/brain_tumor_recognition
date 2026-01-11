# Brain Tumour Recognition
Druk Brain Tumor Recognition
## Aim
The aim of this project is to develop a web-based application capable of accurately distinguishing different types of brain tumors from MRI scan images using deep learning techniques.
## Project Overview
This project is a Brain Tumor Detection Web Application developed using Django and a Convolutional Neural Network (CNN) trained on MRI images. The system automatically classifies brain MRI scans into four categories:
- Glioma
- Meningioma
- Pituitary
- No Tumor
  
The application provides a simple and user-friendly interface where users can upload MRI images. Once uploaded, the image is preprocessed and analyzed by the trained model, which then predicts the tumor type along with its confidence score.
## Dataset
The dataset consists of 7,203 MRI images sourced from Kaggle, labeled as:
- Glioma
- Meningioma
- Pituitary
- No Tumor
  
🔧 Preprocessing Steps
- Images resized to 224 × 224
- Pixel values normalized
- Data augmentation applied using:
     - Brightness adjustment
     - Zoom
     - Rotation
## Model Summary
A transfer learning model (VGG26) was used for training. The model was trained for 5 epochs with a batch size of 20, using:
Optimizer: Adam
Loss Function: Sparse Categorical Crossentropy
Evaluation Metric: Accuracy
The model demonstrated excellent performance on the test dataset, achieving:
- Accuracy: 96%
- Precision: 96%
- Recall: 96%
- F1-score: 96%
  
These results confirm the model’s reliability and effectiveness in brain tumor classification.
## Interface Preview
Below are screenshots of the application ran locally:
### Home Page
<img width="1834" height="921" alt="Screenshot 2026-01-11 194053" src="https://github.com/user-attachments/assets/a1f5143c-54a0-414b-a33d-15d8187ad5b3" />

### Team Page
<img width="1837" height="915" alt="Screenshot 2026-01-11 194113" src="https://github.com/user-attachments/assets/6167cdfb-c913-473c-a6c9-8b0873cb75cb" />

### Prediction Page
<img width="1826" height="918" alt="Screenshot 2026-01-11 194223" src="https://github.com/user-attachments/assets/4407c774-d8b5-4fd5-868d-2a344fe40846" />
<img width="1827" height="906" alt="Screenshot 2026-01-11 194201" src="https://github.com/user-attachments/assets/4ede6ed7-0a52-4696-a202-0bca6c6fd6dc" />

Workflow:
Users upload an MRI image → the image is preprocessed → passed to the trained model → the system predicts the tumor type along with confidence.
