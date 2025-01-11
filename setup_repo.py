import os
import subprocess
from pathlib import Path

# Define the folder structure
folders = [
    "01_General_Prioritization_and_Strategy",
    "02_Deep_Dive_into_Core_Foundations",
    "03_Practical_Application_of_Machine_Learning",
    "04_Exploration_of_Deep_Learning",
    "05_Specialized_Areas",
    "06_NLP_and_Computer_Vision",
    "07_MLOps_and_Deployment",
    "08_Theoretical_Foundations",
    "09_Ethics_Fairness_and_Safety",
    "10_AI_Research_and_Development",
    "11_Advanced_Topics",
    "12_Abstract_Thinking_and_Problem_Solving",
    "13_Community_and_Collaboration",
    "14_General_Search_Strategy",
    "15_Refining_Search_Techniques",
    "16_Targeting_Specific_Subfields",
    "17_Leveraging_Educational_Resources",
    "18_Exploring_Professional_Standards_and_Research",
    "19_Search_for_Exhaustive_Knowledge",
    "20_Visual_Knowledge_Maps",
    "21_Expanding_Searches",
    "22_Foundations_of_AI",
    "23_Core_AI_Concepts",
    "24_Machine_Learning_and_Deep_Learning",
    "25_AI_Applications",
    "26_Interdisciplinary_Connections",
    "27_Frameworks_Tools_and_Infrastructure",
    "28_Abstract_and_Philosophical_Thinking",
    "29_Challenges_and_Future_Directions",
    "30_AI_and_Broader_Contexts",
    "31_Lifelong_Learning_for_AI",
    "32_Metacognition_and_Meta-Learning",
    "33_Intelligence_in_its_Broadest_Sense",
    "34_Advanced_Cognitive_Science_and_AI",
    "35_Ethical_Political_and_Societal_Dimensions",
    "36_Theoretical_AI_and_Abstraction",
    "37_Cutting-Edge_AI_Research_and_Techniques",
    "38_Metaphysical_and_Extinction_Questions",
    "39_Ultimate_Framework_for_Thought",
    "40_Beyond_the_Next_Frontiers",
    "41_Philosophical_Meta-Themes",
    "42_Business_and_AI",
    "43_The_Internet_and_AI",
    "44_Big_Tech_and_AI",
    "45_Compute_and_AI",
    "46_AI_in_the_Macro_Economy",
    "47_AI_in_the_Physical_World",
    "48_AI_in_the_Human_Experience",
    "49_Cross-Sectional_and_Strategic_Questions",
    "50_Knowledge_Unique_to_AI_Practitioners",
    "51_Deepening_the_Understanding_of_AI_Complexity",
    "52_Emerging_Paradigms",
    "53_AI_in_the_Broader_Tech_Ecosystem",
    "54_Expanding_the_Human-AI_Connection",
    "55_Philosophical_and_Spiritual_Dimensions",
    "56_AI_for_Self-Discovery",
    "57_Societal_Evolution",
    "58_The_Future_of_AI_Knowledge",
    "59_The_Unfathomable_Depth_of_AI_Expertise",
    "60_Advanced_Knowledge_and_Skills",
    "61_Mental_Frameworks",
    "62_Rare_Cognitive_Skills",
    "63_Hidden_Infrastructure",
    "64_Research_Frontiers",
    "65_Ethical_Frontiers",
    "66_Bridging_Knowledge_Gaps",
    "67_Barriers_to_Accessibility",
]

# Create base directory and README files
base_path = os.getcwd()
print(f"Creating folder structure in: {base_path}")

# Create folders and README files
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    # Create subfolders
    for subfolder in ['questions', 'resources', 'examples']:
        os.makedirs(os.path.join(folder_path, subfolder), exist_ok=True)
    
    # Create README.md in each folder
    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {folder.replace('_', ' ')}\n\nThis section contains research and resources about {folder.replace('_', ' ')}.")

print("Folder structure created successfully!")

# Git commands
try:
    # Add all files
    subprocess.run(["git", "add", "."], check=True)
    
    # Commit changes
    subprocess.run(["git", "commit", "-m", "Add folder structure"], check=True)
    
    # Push to GitHub
    subprocess.run(["git", "push", "origin", "main"], check=True)
    
    print("Changes pushed to GitHub successfully!")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")