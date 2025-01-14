# Streamlit Document to Markdown Converter

A Streamlit web application that converts various document formats (DOCX, PDF, HTML, etc.) to Markdown using Microsoft's markitdown library.

## Features

- Support for multiple document formats:
  - Microsoft Word (DOCX)
  - PDF Documents
  - HTML Files
  - Text Files
  - Rich Text Format (RTF)
- Live Markdown preview
- One-click download of converted files
- Clean and intuitive user interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/travis-burmaster/streamlit-doc-to-md.git
cd streamlit-doc-to-md
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file:
```bash
cp .env.example .env
```

5. Configure your environment variables in the .env file:
```env
# Example environment variables
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
MAX_UPLOAD_SIZE=5
```

## Usage

1. Ensure your virtual environment is activated:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to `http://localhost:8501` (or whatever port you configured)

4. Upload a document and convert it to Markdown!

## Environment Variables

The following environment variables can be configured in your `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| STREAMLIT_SERVER_PORT | Port for the Streamlit server | 8501 |
| STREAMLIT_SERVER_ADDRESS | Server address | localhost |
| MAX_UPLOAD_SIZE | Maximum upload size in MB | 5 |

## Project Structure

```
streamlit-doc-to-md/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment variables
├── .env               # Local environment variables (git-ignored)
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Microsoft's markitdown library](https://github.com/microsoft/markitdown)
- [Streamlit](https://streamlit.io/)