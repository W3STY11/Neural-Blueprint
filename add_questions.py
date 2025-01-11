import os
from pathlib import Path

def create_question_files(question_path):
    """Create results.json and sources.md in a question folder"""
    os.makedirs(question_path, exist_ok=True)
    
    # Create results.json
    with open(os.path.join(question_path, "results.json"), "w", encoding='utf-8') as f:
        f.write('{\n    "search_results": []\n}')
    
    # Create sources.md
    with open(os.path.join(question_path, "sources.md"), "w", encoding='utf-8') as f:
        f.write("""# Sources

## Academic Papers
1. [Paper 1](link)
2. [Paper 2](link)

## Articles and Guides
1. [Article 1](link)
2. [Article 2](link)

## Tools and Resources
1. [Resource 1](link)
2. [Resource 2](link)
""")

def main():
    base_path = Path.cwd()
    
    # Process each category folder
    for folder in os.listdir(base_path):
        if folder.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            category_path = base_path / folder
            if category_path.is_dir():
                print(f"Processing: {folder}")
                
                # Create Questions folder
                questions_path = category_path / "Questions"
                os.makedirs(questions_path, exist_ok=True)
                
                # Create three question folders
                for i in range(1, 4):
                    question_path = questions_path / f"Question_{i}"
                    create_question_files(question_path)

    print("\nAdding changes to git...")
    os.system('git add .')
    os.system('git commit -m "Add Questions structure with results.json and sources.md"')
    os.system('git push origin main')
    
    print("\n✅ Questions structure added successfully!")

if __name__ == "__main__":
    main()