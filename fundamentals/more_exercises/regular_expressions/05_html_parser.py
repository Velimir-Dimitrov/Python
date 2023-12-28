import re

text = input()

title_pattern = r"(?<=<title>).+(?=<\/title>)"
body_pattern = r"(?<=<body>)(.*?)(?=</body>)"
tags_pattern = r"<(.|\n)*?>"
n_pattern = r"\\n"

body_text = re.findall(body_pattern, text)
removed_tags = re.sub(tags_pattern, "", body_text[0])
extracted_content = re.sub(n_pattern, "", removed_tags)
title_list = re.findall(title_pattern, text)
extracted_title = title_list[0]

print(f"Title: {extracted_title}")
print(f"Content: {extracted_content}")
