import os

def generate_markdown(directory, github_repo_url):
    markdown_content = "# PROMPT HUB\n\n## Directory and Files Index\n\n"
    
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        
        if os.path.isdir(folder_path) and not folder.startswith(('.', '_')):
            markdown_content += f"### {folder}/\n"
            
            files = os.listdir(folder_path)
            if files:
                markdown_content += f"#### Files in {folder}:\n"
                for file in files:
                    file_path = os.path.join(folder_path, file)
                    
                    if os.path.isfile(file_path) and not file.startswith(('.', '_')):
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
