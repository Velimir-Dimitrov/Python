article_title = input()
article_content = input()
comment = input()
comments = []
while comment != "end of comments":
    comments.append(comment)
    comment = input()

print(f"<h1>\n   {article_title}\n</h1>")
print(f"<article>\n   {article_content}\n</article>")
for comment in comments:
    print(f"<div>\n   {comment}\n</div>")
