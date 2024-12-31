import os

def generate_markdown(directory, github_repo_url):
    total_files = 0
    markdown_content = "# PROMPT HUB\n\n"
    
    # Get all folders and sort them
    folders = [f for f in os.listdir(directory) 
              if os.path.isdir(os.path.join(directory, f)) 
              and not f.startswith(('.', '_'))]
    folders.sort()
    
    # Create Table of Contents
    markdown_content += "## Table of Contents\n\n"
    toc = ""
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        files = [f for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f)) 
                and not f.startswith(('.', '_'))]
        file_count = len(files)
        toc += f"- [{folder}](#{folder.replace(' ', '-').lower()}) ({file_count} prompts)\n"
    markdown_content += toc + "\n---\n\n"

    # Generate sections for each folder
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        files = [f for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f)) 
                and not f.startswith(('.', '_'))]
        files.sort()  # Sort files alphabetically
        file_count = len(files)
        total_files += file_count
        
        # Add collapsible section for folder
        markdown_content += f"## {folder} ({file_count} prompts)\n"
        markdown_content += f"<details>\n  <summary>Click to expand the list</summary>\n\n"
        
        if files:
            markdown_content += f"#### Files in {folder}:\n\n"
            for file in files:
                file_link = f"{github_repo_url}/{folder}/{file}"
                formatted_file_name = file.replace('-', ' ').replace('.md', '')
                markdown_content += f"- [{formatted_file_name}]({file_link})\n"

        else:
            markdown_content += "No files found in this folder.\n"
        
        markdown_content += "\n</details>\n\n"

    # Add total file count at the beginning
    markdown_content = markdown_content.replace(
        "# PROMPT HUB\n\n",
        f"# PROMPT HUB\n\nTotal number of prompts: {total_files}\n\n"
    )

    # Remove extra lines at the end
    markdown_content = markdown_content.rstrip() + "\n"

    # Save the markdown file
    with open('README-index.md', 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)

# Define the directory and repo URL
current_directory = os.getcwd()
github_repo_url = "https://github.com/LucasDitchun/Prompt-Hub/blob/main"

# Generate the README
generate_markdown(current_directory, github_repo_url)
