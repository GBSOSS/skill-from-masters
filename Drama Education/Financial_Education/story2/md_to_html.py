import markdown
import os

# CSS to make it look nice (GitHub-like style)
CSS_STYLE = """
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        line-height: 1.6;
        color: #24292e;
        max-width: 900px;
        margin: 0 auto;
        padding: 40px 20px;
        background-color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6 {
        margin-top: 24px;
        margin-bottom: 16px;
        font-weight: 600;
        line-height: 1.25;
    }
    h1 { font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    h3 { font-size: 1.25em; }
    p { margin-top: 0; margin-bottom: 16px; }
    a { color: #0366d6; text-decoration: none; }
    a:hover { text-decoration: underline; }
    ul, ol { padding-left: 2em; margin-bottom: 16px; }
    blockquote {
        padding: 0 1em;
        color: #6a737d;
        border-left: 0.25em solid #dfe2e5;
        margin: 0 0 16px 0;
    }
    code {
        padding: 0.2em 0.4em;
        margin: 0;
        font-size: 85%;
        background-color: rgba(27,31,35,0.05);
        border-radius: 3px;
        font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
    }
    pre {
        padding: 16px;
        overflow: auto;
        font-size: 85%;
        line-height: 1.45;
        background-color: #f6f8fa;
        border-radius: 3px;
    }
    pre code {
        display: inline;
        padding: 0;
        margin: 0;
        overflow: visible;
        line-height: inherit;
        word-wrap: normal;
        background-color: transparent;
        border: 0;
    }
    table {
        border-spacing: 0;
        border-collapse: collapse;
        display: block;
        width: 100%;
        width: -webkit-max-content;
        width: -moz-max-content;
        width: max-content;
        max-width: 100%;
        overflow: auto;
        margin-bottom: 16px;
    }
    table th, table td {
        padding: 6px 13px;
        border: 1px solid #dfe2e5;
    }
    table tr:nth-child(2n) {
        background-color: #f6f8fa;
    }
    hr {
        height: 0.25em;
        padding: 0;
        margin: 24px 0;
        background-color: #e1e4e8;
        border: 0;
    }
    .container {
        border: 1px solid #e1e4e8;
        padding: 40px;
        border-radius: 6px;
        background-color: #fff;
    }
    @media (max-width: 768px) {
        body { padding: 20px 15px; }
        .container { padding: 20px; border: none; }
    }
    
    /* Attachments Styling */
    .certificate {
        border: 4px double #333;
        padding: 40px;
        background-color: #fffcf5;
        font-family: "Georgia", "Times New Roman", serif;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        position: relative;
    }
    .certificate-header {
        font-size: 2.2em;
        font-weight: bold;
        letter-spacing: 3px;
        margin-bottom: 10px;
        border-bottom: 2px solid #333;
        display: inline-block;
        padding-bottom: 5px;
    }
    .certificate-body {
        font-size: 1.1em;
        line-height: 1.8;
        margin: 20px 0;
        text-align: left;
    }
    .certificate-signature {
        display: flex;
        justify-content: space-between;
        margin-top: 50px;
        padding-top: 10px;
    }
    .sig-block {
        border-top: 1px solid #333;
        width: 40%;
        text-align: center;
        padding-top: 5px;
    }
    .seal {
        width: 100px;
        height: 100px;
        border: 2px solid #c0392b;
        border-radius: 50%;
        color: #c0392b;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        transform: rotate(-15deg);
        position: absolute;
        bottom: 30px;
        right: 45%;
        opacity: 0.8;
        font-size: 14px;
        text-align: center;
    }

    .newspaper {
        background-color: #fdfdfd;
        padding: 20px;
        border: 1px solid #ddd;
        margin: 30px 0;
        font-family: "Times New Roman", serif;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .news-masthead {
        border-bottom: 3px double #2c3e50;
        margin-bottom: 15px;
        padding-bottom: 5px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
    }
    .news-paper-name {
        font-weight: 900;
        font-size: 1.2em;
        text-transform: uppercase;
        color: #555;
    }
    .news-date {
        font-style: italic;
        font-size: 0.9em;
        color: #777;
    }
    .news-headline {
        font-size: 1.8em;
        font-weight: bold;
        line-height: 1.2;
        margin: 10px 0;
        color: #111;
    }
    .news-subhead {
        font-style: italic;
        color: #555;
        margin-bottom: 15px;
        font-weight: bold;
    }
    .news-content {
        column-count: 2;
        column-gap: 30px;
        column-rule: 1px solid #eee;
        text-align: justify;
        font-size: 1.05em;
    }
    .news-tag {
        background: #2c3e50;
        color: #fff;
        padding: 2px 6px;
        font-size: 0.8em;
        text-transform: uppercase;
        margin-right: 10px;
        vertical-align: middle;
    }
    @media (max-width: 600px) {
        .news-content { column-count: 1; }
    }

    /* Pedagogical Note (Maister's Voice) */
    .maister-note {
        background-color: #f0f7fb;
        border-left: 5px solid #3498db;
        padding: 15px 20px;
        margin: 25px 0;
        border-radius: 0 4px 4px 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        color: #2c3e50;
    }
    .maister-note strong {
        color: #2980b9;
        font-size: 1.05em;
    }
    .maister-note em {
        font-family: "Georgia", serif;
        color: #555;
    }
</style>
"""

def convert_md_to_html(source_file, target_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(text, extensions=['tables', 'fenced_code', 'nl2br'])

    # Wrap in HTML structure
    html_template = f"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>活動二：虹港 (Rainbow Port)</title>
    {CSS_STYLE}
</head>
<body>
    <div class="container">
        {html_content}
    </div>
</body>
</html>
"""

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"File saved to {target_file}")

if __name__ == "__main__":
    source = "lesson_plan_activity2_rainbow_port.md"
    target = "index.html"
    convert_md_to_html(source, target)
