from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrow

def draw_activity_diagram():
    fig, ax = plt.subplots(figsize=(12, 10))

    # Start Node
    ax.text(0.5, 0.95, "Start", fontsize=12, ha='center', bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='circle'))
    
    # Choose Feature
    ax.text(0.5, 0.85, "Choose Feature", fontsize=12, ha='center', bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.3'))
    
    # Feature Branches
    ax.text(0.1, 0.75, "Disease First Aid", fontsize=10, ha='center', bbox=dict(facecolor='lightgrey', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.text(0.5, 0.75, "BMI Calculator", fontsize=10, ha='center', bbox=dict(facecolor='lightgrey', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.text(0.9, 0.75, "Doctor Information", fontsize=10, ha='center', bbox=dict(facecolor='lightgrey', edgecolor='black', boxstyle='round,pad=0.3'))
    
    ax.text(0.1, 0.65, "Emergency Services", fontsize=10, ha='center', bbox=dict(facecolor='lightgrey', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.text(0.5, 0.65, "Health Articles", fontsize=10, ha='center', bbox=dict(facecolor='lightgrey', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.text(0.9, 0.65, "Symptom Tracker", fontsize=10, ha='center', bbox=dict(facecolor='lightgrey', edgecolor='black', boxstyle='round,pad=0.3'))
    
    # End Nodes for each branch
    ax.text(0.1, 0.55, "Show First Aid", fontsize=10, ha='center', bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.text(0.5, 0.55, "Show BMI & Exercise", fontsize=10, ha='center', bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.text(0.9, 0.55, "Show Doctors", fontsize=10, ha='center', bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.3'))
    
    ax.text(0.1, 0.45, "Show Nearby Hospital", fontsize=10, ha='center', bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.text(0.5, 0.45, "Show Articles & News", fontsize=10, ha='center', bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.text(0.9, 0.45, "Show Possible Diseases", fontsize=10, ha='center', bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.3'))
    
    # End Node
    ax.text(0.5, 0.35, "End", fontsize=12, ha='center', bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='circle'))
    
    # Arrows for flow
    ax.annotate('', xy=(0.5, 0.92), xytext=(0.5, 0.87), arrowprops=dict(facecolor='black', shrink=0.05))
    
    ax.annotate('', xy=(0.15, 0.77), xytext=(0.5, 0.82), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(0.5, 0.77), xytext=(0.5, 0.82), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(0.85, 0.77), xytext=(0.5, 0.82), arrowprops=dict(facecolor='black', shrink=0.05))
    
    ax.annotate('', xy=(0.15, 0.67), xytext=(0.1, 0.73), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(0.5, 0.67), xytext=(0.5, 0.73), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(0.85, 0.67), xytext=(0.9, 0.73), arrowprops=dict(facecolor='black', shrink=0.05))
    
    ax.annotate('', xy=(0.15, 0.57), xytext=(0.1, 0.63), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(0.5, 0.57), xytext=(0.5, 0.63), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(0.85, 0.57), xytext=(0.9, 0.63), arrowprops=dict(facecolor='black', shrink=0.05))
    
    ax.annotate('', xy=(0.15, 0.47), xytext=(0.1, 0.53), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(0.5, 0.47), xytext=(0.5, 0.53), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(0.85, 0.47), xytext=(0.9, 0.53), arrowprops=dict(facecolor='black', shrink=0.05))
    
    ax.annotate('', xy=(0.5, 0.37), xytext=(0.5, 0.42), arrowprops=dict(facecolor='black', shrink=0.05))

    # Set axis limits and hide axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.show()

draw_activity_diagram()
