import os
import shutil

def copy_and_rename_py_files(src_folder, dest_folder, prefix="_backup"):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    for root, _, files in os.walk(src_folder):
        for file_name in files:
            if file_name.endswith(".py"):
                base_name, ext = os.path.splitext(file_name)
                new_name = f"{prefix}{base_name}{ext}"
                src_path = os.path.join(root, file_name)
                dest_path = os.path.join(dest_folder, new_name)
                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} -> {dest_path}")

#Exemplo de uso
source_directory = "./workspaces_DeepSeek-R1/30aws-server-config"  # Substituir pelo caminho da pasta de origem
destination_directory = "./Códigos_DeepSeek-R1" # Substituir pelo caminho da pasta de destino
copy_and_rename_py_files(source_directory, destination_directory, "30_")
