import matplotlib.pyplot as plt
import numpy as np

def create_placeholder_image(filename, text="Placeholder"):
    plt.figure(figsize=(10, 6))
    plt.text(0.5, 0.5, text, ha='center', va='center', fontsize=20)
    plt.axis('off')
    plt.savefig(f'main/static/main/images/{filename}.jpg')
    plt.close()

# Create placeholder images
create_placeholder_image('ai-header', 'AI Header Image')
create_placeholder_image('ai-ml', 'Machine Learning')
create_placeholder_image('ai-robotics', 'AI Robotics')
create_placeholder_image('ai-ethics', 'AI Ethics')
create_placeholder_image('ai-future', 'Future of AI')
