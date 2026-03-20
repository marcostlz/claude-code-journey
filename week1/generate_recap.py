commands = [
    ("pwd", "Shows where you are"),
    ("ls", "Lists files in current folder"),
    ("cd folder", "Goes into a folder"),
    ("cd ..", "Goes up one level"),
    ("mkdir name", "Creates a folder"),
    ("touch file", "Creates a file"),
    ("mv", "Moves or renames a file"),
    ("cp", "Copies a file"),
    ("rm", "Deletes a file"),
]

concepts = [
    ("variables", "Store information: name = 'Marco'"),
    ("print()", "Output text to the screen"),
    ("input()", "Ask the user a question"),
    ("if/else", "Make decisions based on conditions"),
    ("for loop", "Repeat an action for each item in a list"),
    ("functions", "Reusable blocks of code with def"),
]

def generate_row(cols):
    return "<tr>" + "".join("<td>" + c + "</td>" for c in cols) + "</tr>"

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Day 1 Recap</title>
<style>
  body { font-family: monospace; background: #0e0e0e; color: #e8e4dc; padding: 40px; }
  h1 { color: #c8a96e; margin-bottom: 8px; }
  h2 { color: #7eb8a4; margin-top: 40px; }
  table { border-collapse: collapse; width: 100%; margin-top: 16px; }
  td { border: 1px solid #2a2a2a; padding: 10px 16px; }
  tr:first-child td { color: #c8a96e; font-weight: bold; }
</style>
</head>
<body>
<h1>Claude Code Journey — Day 1 Recap</h1>
<p>Built by Marco · Week 1 · Terminal + Python basics</p>
<h2>Terminal Commands</h2>
<table>
  <tr><td>Command</td><td>What it does</td></tr>
"""

for c in commands:
    html += generate_row(c) + "\n"

html += """</table>
<h2>Python Concepts</h2>
<table>
  <tr><td>Concept</td><td>What it does</td></tr>
"""

for c in concepts:
    html += generate_row(c) + "\n"

html += """</table>
</body>
</html>"""

with open("week1/recap_day1.html", "w") as f:
    f.write(html)

print("Recap generated! Open week1/recap_day1.html in your browser.")