from training.prepare_data import load_data
from models.lstm_model import build_lstm
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping, CSVLogger
import json
import matplotlib.pyplot as plt
import os

def plot_training_history(history):
    """Plot and save training history"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Accuracy plot
    ax1.plot(history.history['accuracy'], label='Training Accuracy')
    ax1.plot(history.history['val_accuracy'], label='Validation Accuracy')
    ax1.set_title('Model Accuracy')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy')
    ax1.legend()
    ax1.grid(True)
    
    # Loss plot
    ax2.plot(history.history['loss'], label='Training Loss')
    ax2.plot(history.history['val_loss'], label='Validation Loss')
    ax2.set_title('Model Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('assets/graphs/training_history.png', dpi=100, bbox_inches='tight')
    plt.close()
    
    # Save history as JSON
    history_dict = {
        'accuracy': history.history['accuracy'],
        'val_accuracy': history.history['val_accuracy'],
        'loss': history.history['loss'],
        'val_loss': history.history['val_loss']
    }
    
    with open('assets/graphs/training_history.json', 'w') as f:
        json.dump(history_dict, f)

def train():
    os.makedirs('assets/graphs', exist_ok=True)
    
    X, y, gestures, stats = load_data()
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    model = build_lstm(num_classes=len(gestures))
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    early_stop = EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    )
    
    csv_logger = CSVLogger('assets/graphs/training_log.csv')
    
    history = model.fit(
        X_train, y_train,
        epochs=50,
        batch_size=16,
        validation_data=(X_test, y_test),
        callbacks=[early_stop, csv_logger]
    )
    
    plot_training_history(history)
    
    # Evaluate and save test metrics
    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
    
    metrics = {
        'test_accuracy': float(test_accuracy),
        'test_loss': float(test_loss),
        'best_val_accuracy': float(max(history.history['val_accuracy'])),
        'best_val_loss': float(min(history.history['val_loss']))
    }
    
    with open('assets/graphs/test_metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)
    
    model.save_weights("models/gesture_model.weights.h5")
    print(f"Model saved! Test Accuracy: {test_accuracy:.2%}")

if __name__ == "__main__":
    train()