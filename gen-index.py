import os

def generate_markdown(directory):
    markdown_content = "# PROMPT HUB\n\n## Directory and Files Index\n\n"
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        
        # Verificar se é uma pasta e não começa com '.' ou '_'
        if os.path.isdir(folder_path) and not folder.startswith(('.', '_')):
            markdown_content += f"### {folder}/\n"
            
            # Listar arquivos dentro da pasta
            files = os.listdir(folder_path)
            if files:
                markdown_content += f"#### Files in {folder}:\n"
                for file in files:
                    file_path = os.path.join(folder_path, file)
                    if os.path.isfile(file_path) and not file.startswith(('.', '_')):
                        markdown_content += f"- {file}\n"
            else:
                markdown_content += "No files found in this folder.\n"
            
            markdown_content += "\n"

    with open('README-index.md', 'w') as md_file:
        md_file.write(markdown_content)

current_directory = os.getcwd()
generate_markdown(current_directory)
