name = input("What is your name? ")
business = input("What is the name of your business? ")
tagline = input("One-line description of your business: ")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{business}</title>
  <style>
    body {{
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #0e0e0e;
      font-family: monospace;
      color: #e0e0e0;
    }}
    .card {{
      border: 1px solid #333;
      border-radius: 12px;
      padding: 48px 64px;
      text-align: center;
      background: #1a1a1a;
    }}
    .business {{ font-size: 2rem; font-weight: bold; color: #ffffff; margin-bottom: 8px; }}
    .tagline {{ font-size: 1rem; font-style: italic; color: #bbb; margin-bottom: 12px; }}
    .name {{ font-size: 1rem; color: #888; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="business">{business}</div>
    <div class="tagline">{tagline}</div>
    <div class="name">{name}</div>
  </div>
</body>
</html>"""

output_path = "week2/business_card.html"
with open(output_path, "w") as f:
    f.write(html)

print(f"Business card saved to {output_path}")
