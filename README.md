🧠 Medical AI Summarizer

Overview
This project introduces an edge-deployable AI system that transforms scanned medical report images into readable summaries and extracts key medical entities such as diseases, symptoms, and medications. 
It addresses the critical gap in healthcare accessibility, especially in rural or low-resource areas, where patients struggle to interpret clinical documents and may lack access to internet-based services.

🔧 Technology Stack
- OCR : [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – Converts scanned medical report images (JPG/PNG) into machine-readable text.
- Summarization : [BART-large-CNN](https://huggingface.co/facebook/bart-large-cnn) – Converts technical medical text into layperson-friendly summaries.
- Deployment : Fully offline-compatible, optimized for edge devices (e.g., Raspberry Pi, local desktop environments).

✅ Key Features
- Offline Capability : Runs without internet access for use in remote or privacy-sensitive environments.
- End-to-End Pipeline : Combines OCR, NER, and summarization in a modular, interpretable workflow.
- Privacy-Preserving : No cloud processing—data stays entirely on the user's device.
- Readable Summaries : Converts clinical jargon into simple, digestible language.

⚙️ Working Requirements

To run this system locally, users should have Python 3.8+, `pip`, and basic dependencies such as `pytesseract`, `transformers`, `torch`, and `opencv-python`. 
Tesseract OCR must be installed and accessible via system path. The NER and summarization models should be either downloaded from Hugging Face or stored locally for offline inference. 
The application is lightweight and can be deployed on devices with moderate hardware, such as mid-range laptops with 4GB+ RAM.


🚀 How to Run the Project

Follow the steps below to run the project locally:

1. Clone the Repository
   git clone https://github.com/your-username/ai-medical-summarizer.git
   cd ai-medical-summarizer
   
2. Create and Activate Virtual Environment (Optional but Recommended)
   python3 -m venv venv
   source venv/bin/activate
   On Windows: venv\Scripts\activate

4. Install Python Dependencies
   pip install -r requirements.txt

5. Install Tesseract OCR Engine
   - Linux: `sudo apt install tesseract-ocr`
   - Windows: [Download installer](https://github.com/tesseract-ocr/tesseract/wiki)

6. Download Required Models
   - Place BART-large-CNN model in the `models/` directory as described in documentation.

7. Run the Application
   python app.py

8. Upload a Medical Report Image
   - Use the interface to upload a scanned medical report (JPG/PNG).
   - View the extracted summary and identified medical terms.
