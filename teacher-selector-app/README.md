# Teacher Selector App

This is a Flask web application designed to help users select teachers for meetings. The application features a user-friendly interface that allows users to add or remove teacher names, specify how many teachers to select, and display the selected teachers' names.

## Project Structure

```
teacher-selector-app
├── app.py                # Main application file for the Flask web app
├── requirements.txt      # Lists dependencies required for the project
├── templates
│   └── index.html       # HTML structure for the user interface
├── static
│   └── style.css        # CSS styles for the application
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd teacher-selector-app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app.py
   ```

5. **Open your web browser and go to:**
   ```
   http://127.0.0.1:5000
   ```

## Usage

- Use the comboboxes to add or remove teacher names.
- Specify the number of teachers you want to select.
- Click the "Select Teacher" button to display the selected teachers' names.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the application.

## License

This project is licensed under the MIT License.