import os
import numpy as np
import json
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

DATA_PATH = "data/processed_frames"
SEQUENCE_LENGTH = 30

def load_data():
    gestures = sorted(os.listdir(DATA_PATH))
    X, y = [], []
    label_map = {gesture: idx for idx, gesture in enumerate(gestures)}
    
    stats = {}
    
    for gesture in gestures:
        gesture_path = os.path.join(DATA_PATH, gesture)
        files = os.listdir(gesture_path)
        valid_files = []
        
        for file in files:
            seq = np.load(os.path.join(gesture_path, file))
            if seq.shape == (SEQUENCE_LENGTH, 21, 3):
                X.append(seq)
                y.append(label_map[gesture])
                valid_files.append(file)
        
        stats[gesture] = {
            "total_files": len(files),
            "valid_files": len(valid_files),
            "samples": len(valid_files)
        }
    
    X = np.array(X)
    y = to_categorical(y, num_classes=len(gestures))
    
    # Save statistics
    stats["total_samples"] = len(X)
    stats["gesture_classes"] = len(gestures)
    stats["sequence_length"] = SEQUENCE_LENGTH
    
    with open("assets/dataset_stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    
    return X, y, gestures, stats

if __name__ == "__main__":
    X, y, gestures, stats = load_data()
    print("Dataset Loaded")
    print(f"Total samples: {stats['total_samples']}")
    print(f"Classes: {gestures}")
    print("Stats saved to assets/dataset_stats.json")