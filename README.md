# Py-Mail Automator 📧

Py-Mail Automator is a high-performance, modular Python service designed for secure and personalized mass email distribution. By combining Pydantic for rigorous data validation, Jinja2 for dynamic templating, and Pandas for efficient data handling, this tool ensures that automated communication is professional, traceable, and error-free.

## 🌟 Key Features

- **Personalization:** Uses Jinja2 to inject Excel data into HTML/Text templates, allowing for unique messages per recipient.

- **Data Validation:** Powered by Pydantic, the system validates email formats and data types before execution, following a "Fail-Fast" approach.

- **Security:** Implements pydantic-settings to manage SMTP credentials via environmental variables (.env), keeping secrets out of the source code.

- **Modular Architecture:** Designed with a clear separation of concerns (Config, Models, Services, and Readers) for maximum maintainability.

- **Testing:** Includes a suite of unit tests using Pytest to ensure core logic and data integrity.

## 🛠️ Technologies

- **Python 3.10+**

- **Poetry**: Dependency manager and packaging.

- **Pandas & Openpyxl:** High-speed spreadsheet processing.

- **Pydantic:** Data validation and settings management.

- **Jinja2:** Professional-grade logic-based templating.

- **Pytest:** Testing framework.

## 📜 Requirements

- [Visual Studio Code](https://code.visualstudio.com/) or any modern IDE.
- **Python 3.10 or higher** installed on your system.

## 🚀 Installation & Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/funktasthic/py-mail-automator.git
    cd py-mail-automator
    ```

2. **Install Poetry (if not already installed):**
    Follow the official instructions [Poetry](https://python-poetry.org/docs/#installation).

3. **Install dependencies and setup environment:**
    Poetry will automatically create a virtual environment and install all listed dependencies:

    ```bash
    poetry install
    ```

4. **Environment Setup:**
Create a `.env` file in the root directory:

    ```bash
    EMAIL_USER=your_email@gmail.com
    EMAIL_PASSWORD=your_google_token
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    ```

## 📈 Usage

1. **Prepare your data:** on `data/contacts.xlsx`.

2. **Customize your message:** in `template/email_template.html`.

3. **Run the automation:**
You can run the script directly through Poetry:

    ```bash
    poetry run python main.py
    ```

*Or activate the virtual environment shell first with `poetry shell` and then run `python main.py`*.

## Authors

- **[@funktasthic](https://www.github.com/funktasthic)** - Ignacio Avendaño Ramírez
