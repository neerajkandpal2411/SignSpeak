import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from training.prepare_data import load_data
from models.lstm_model import build_lstm
import json

def generate_confusion_matrix():
    """Generate and save confusion matrix"""
    X, y, gestures, _ = load_data()
    
    model = build_lstm(num_classes=len(gestures))
    model.load_weights("models/gesture_model.weights.h5")
    
    # Get predictions
    y_pred = model.predict(X, verbose=0)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true_classes = np.argmax(y, axis=1)
    
    # Confusion Matrix
    cm = confusion_matrix(y_true_classes, y_pred_classes)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=gestures, yticklabels=gestures)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('assets/graphs/confusion_matrix.png', dpi=100, bbox_inches='tight')
    plt.close()
    
    # Classification Report
    report = classification_report(y_true_classes, y_pred_classes, 
                                   target_names=gestures, output_dict=True)
    
    with open('assets/graphs/classification_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("Confusion matrix and classification report saved!")

if __name__ == "__main__":
    generate_confusion_matrix()