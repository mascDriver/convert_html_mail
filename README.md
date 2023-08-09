
# HTML Processor div to tables

This project provides a simple HTML template that allows users to input HTML code, process it on the backend built with Flask, and display both the processed result and a rendered version. The HTML code input and processed result are tables to use in mail template.

## Features

- Input HTML code in a textarea.
- Process the HTML code on the Flask backend.
- Display processed result in a textarea and render it in an iframe.
- Syntax-highlighted HTML code using Prism.js.

## Getting Started

1. Clone this repository to your local machine.

```sh
git clone https://github.com/your-username/html-processor.git
```

```sh
cd convert_html_mail
```

2. Create a virtual environment and install dependencies.

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the Flask app.

```sh
flask run
```

## Flask Backend

The backend of this project is built with Flask, a lightweight Python web framework. The backend code can be found in the `app.py` file.

## Built With

- HTML
- CSS
- Prism.js - For syntax highlighting
- Flask - For the backend

## Note

This project uses Flask for the backend processing logic.

## Credits

- Prism.js: [https://prismjs.com/](https://prismjs.com/)
- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
