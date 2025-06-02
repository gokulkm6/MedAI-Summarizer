from flask import Flask, request, render_template_string
from services.llm_engine import generate_summary
from services.ocr_module import extract_text_from_image
from services.ner_module import extract_medical_entities

import os


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>🧠 Medical Report AI</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h2 class="mb-4 text-center">🩻 Medical AI Summarizer</h2>
        <form method="POST" enctype="multipart/form-data" class="card p-4 shadow-sm bg-white">
            <div class="mb-3">
                <label for="file" class="form-label">Upload Image (JPG / PNG)</label>
                <input type="file" class="form-control" name="file" accept=".jpg,.jpeg,.png" required>
            </div>
            <button type="submit" class="btn btn-primary">Analyze</button>
        </form>
        
        {% if summary %}
        <div class="mt-4 p-4 bg-success text-white rounded">
            <h5>📝 AI-Generated Summary:</h5>
            <p>{{ summary }}</p>
        </div>
        <div class="mt-3 p-3 bg-info text-dark rounded">
            <h5>🧬 Detected Conditions:</h5>
            <ul>
                {% for disease in diseases %}
                <li>{{ disease }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    diseases = []
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            extracted_text = extract_text_from_image(filepath)
            summary = generate_summary(extracted_text)
            diseases = extract_medical_entities(extracted_text)
    
    return render_template_string(HTML_TEMPLATE, summary=summary, diseases=diseases)

if __name__ == "__main__":
    app.run(debug=True)