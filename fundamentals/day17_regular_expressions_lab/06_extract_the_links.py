import re
text = input()
while text:

    pattern = r"(www.[A-Za-z0-9]+(\-*[a-z0-9]+)*(\.[a-z]+)(\.?([a-z]))+)"
    # (w{3}\.[A-Za-z0-9-\.]+\.[a-z]+)
    extracted_links = re.findall(pattern, text)
    if extracted_links:
        [print(link[0]) for link in extracted_links]
    text = input()

