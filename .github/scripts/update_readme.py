import feedparser
import re

def update_readme_with_blog_posts():
    feed = feedparser.parse("https://bellringstar.tistory.com/rss")

    latest_posts = []
    for entry in feed.entries[:3]:  # Get the latest 3 posts
        post = f"- [{entry.title}]({entry.link}) - {entry.published[:10]}"
        latest_posts.append(post)

    with open("README.md", "r", encoding="utf-8") as file:
        readme = file.read()

    # Update the README with new blog posts
    start_marker = "<!-- BLOG-POST-LIST:START -->"
    end_marker = "<!-- BLOG-POST-LIST:END -->"
    pattern = f"{start_marker}[\\s\\S]*{end_marker}"

    new_content = f"{start_marker}\n" + "\n".join(latest_posts) + f"\n{end_marker}"
    updated_readme = re.sub(pattern, new_content, readme)

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated_readme)

if __name__ == "__main__":
    update_readme_with_blog_posts()