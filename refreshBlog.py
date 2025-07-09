
import json
def main():
    with open("blogposts.json", 'r') as f:
        config = json.load(f)
    articles=""
    for(post) in config["posts"]:
        #<article>
        #    <h2>First Blog Post</h2>
        #    <p>Posted on July 7, 2025</p>            
        #   <a href="https://drive.google.com/thumbnail?id=1bxcsEqXO2i8MmKbMtdrxCLQUa5en1sjW&sz=w3840">
        #       <img src="https://drive.google.com/thumbnail?id=1bxcsEqXO2i8MmKbMtdrxCLQUa5en1sjW&sz=w1080" alt="Initial Sketch" title="Screenshot of Project One" id="image-preview">
        #   </a>
        #    <p>This is the content of my first blog post. It's about static websites.</p>
        #</article>
        articles+=f"""<article>
            <h2>{post["title"]}</h2>
            <p>Posted on {post["date"]}</p>"""
        for(component) in post["body"]:
            if(component["type"]=="image"):
                articles+=f"""
                <a href="{component["fullres"]}">
                    <img src="{component["thumbnail"]}" alt="{component["title"]}" title="{component["title"].replace("\"","&quot;")}" id="image-preview">
                </a>
                """
            elif(component["type"]=="text"):
                articles+=f"""
                <p>{component["content"]}</p>
                """
        articles+="</article>"
    return articles


if __name__ == "__main__":
    bodyhtml=main()
    fullhtml=f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="blog.html" class="active">Blog</a>
        <a href="portfolio.html">Portfolio</a>
    </nav>

    <div class="container">
        <h1>My Blog</h1>
        <p>Here are my latest thoughts and articles.</p>
        
        {bodyhtml}
    </div>

    <script src="script.js"></script>
</body>
</html>"""
    with open("blog.html", 'w') as f:
        f.write(fullhtml)