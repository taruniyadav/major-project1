import os
import random

def generate_image(keyword, interest="technology"):

    folder_path = f"assets/visuals/{interest.lower()}"

    if not os.path.exists(folder_path):
        folder_path = "assets/visuals/technology"

    files = os.listdir(folder_path)

    if not files:
        return None

    keyword = keyword.lower()

    # 🔥 better matching (split filename words)
    for file in files:
        name = file.lower().replace("_", " ").replace("-", " ")

        if keyword in name:
            return os.path.join(folder_path, file)

    # 🎯 fallback
    return os.path.join(folder_path, random.choice(files))
