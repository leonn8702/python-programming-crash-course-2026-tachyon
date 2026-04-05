import matplotlib.pyplot as plt

def draw_progress_bar(percent, title="Task Progress"):
    fig, ax = plt.subplots(figsize=(6, 1))
    
    # Create the background bar (gray)
    ax.barh(0, 100, color='#eeeeee', height=0.6)
    
    # Create the progress bar (green)
    ax.barh(0, percent, color='#4CAF50', height=0.6)
    
    # Clean up the UI
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.5, 0.5)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'])
    ax.set_yticks([])  # Hide Y axis
    
    # Add text label in the center
    ax.text(50, 0, f'{percent}%', ha='center', va='center', 
            fontweight='bold', color='black' if percent < 50 else 'white')
    
    plt.title(title)
    plt.tight_layout()
    plt.show()

draw_progress_bar(75)