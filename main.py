from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>My Custom Page</title>
        </head>
        <body>
            <h1>Welcome to My Custom Page!</h1>
            <p>This is a paragraph with some <strong>bold</strong> text.</p>
            <p>Here's a list:</p>
            <ul>
                <li>First item</li>
                <li>Second item</li>
                <li>Third item</li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
