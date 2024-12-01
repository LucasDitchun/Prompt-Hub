import os

def generate_markdown(directory, github_repo_url):
    total_files = 0
    markdown_content = "# PROMPT HUB\n\n"
    
    # Get all folders and sort them
    folders = [f for f in os.listdir(directory) 
              if os.path.isdir(os.path.join(directory, f)) 
              and not f.startswith(('.', '_'))]
    folders.sort()
    
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        files = [f for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f)) 
                and not f.startswith(('.', '_'))]
        files.sort()  # Sort files alphabetically
        total_files += len(files)
    
    markdown_content += f"Total number of prompts: {total_files}\n\n"
    markdown_content += "## Directory and Files prompts\n\n"
    
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        markdown_content += f"### {folder}/\n"
        
        files = [f for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f)) 
                and not f.startswith(('.', '_'))]
        files.sort()  # Sort files alphabetically
        
        if files:
            markdown_content += f"#### Files in {folder}:\n"
            for file in files:
                file_path = os.path.join(folder_path, file)
                file_link = f"{github_repo_url}/{folder}/{file}"
                markdown_content += f"- [{file}]({file_link})\n"
        else:
            markdown_content += "No files found in this folder.\n"
        
        markdown_content += "\n"

    with open('README-index.md', 'w') as md_file:
        md_file.write(markdown_content)

current_directory = os.getcwd()
github_repo_url = "https://github.com/LucasDitchun/Prompt-Hub/blob/main"

generate_markdown(current_directory, github_repo_url)
