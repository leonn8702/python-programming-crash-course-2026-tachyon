import matplotlib.pyplot as plt
import time

def animated_progress():
    plt.ion() # Turn on interactive mode
    fig, ax = plt.subplots(figsize=(8, 1))
    
    for i in range(101):
        ax.clear() # Clear previous frame
        
        # Formatting
        ax.set_xlim(0, 100)
        ax.set_yticks([])
        ax.set_title(f"Downloading Update... {i}%")
        
        # Draw background and progress
        ax.barh(0, 100, color='#f0f0f0')
        ax.barh(0, i, color='skyblue')
        
        plt.pause(0.05) # Small delay to simulate work
        
    plt.ioff() # Turn off interactive mode
    plt.show()

animated_progress()