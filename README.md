# Wiki Encyclopedia

[This project](https://cs50.harvard.edu/web/2020/projects/1/wiki/) is a part of the CS50 Web Programming with Python and JavaScript course. It is a simple Wiki Encyclopedia built using Django. The application allows users to browse, search, create, edit, and view random encyclopedia entries written in Markdown. The entries are converted to HTML for display. The project also includes Bootstrap 5 for styling, Google Fonts for typography, and a dark mode option. 

## Video Preview

[Video Link](https://youtu.be/o1lEu2gQYtY)

## Features

- **Entry Page**: View the content of an encyclopedia entry.
- **Index Page**: Clickable list of all encyclopedia entries.
- **Search**: Search for encyclopedia entries by name or substring.
- **New Page**: Create new encyclopedia entries with Markdown content.
- **Edit Page**: Edit existing encyclopedia entries.
- **Random Page**: View a random encyclopedia entry.
- **Markdown to HTML Conversion**: Display Markdown content as HTML.
- **Dark Mode**: Toggle between light and dark mode for better readability.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/hiralinda/wiki-encyclopedia.git
    cd wiki-encyclopedia
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Home Page**: Lists all encyclopedia entries. Click on any entry to view its content.
- **Search**: Use the search bar in the sidebar to find entries by name or substring. Matching entries are listed, and clicking on them takes you to the entry page.
- **Create New Page**: Click "Create New Page" in the sidebar to create a new entry. Enter the title and Markdown content, then save.
- **Edit Entry**: On any entry page, click "Edit" to modify the entry. The existing content is pre-populated in a textarea.
- **Random Page**: Click "Random Page" in the sidebar to view a random entry.
- **Dark Mode**: Toggle the dark mode option in the sidebar for a dark-themed interface.

## File Structure

- `encyclopedia/urls.py`: URL configuration for the encyclopedia app.
- `encyclopedia/util.py`: Utility functions for interacting with encyclopedia entries.
- `encyclopedia/views.py`: View functions for handling requests and rendering templates.
- `encyclopedia/templates/encyclopedia/`: HTML templates for the encyclopedia app.
  - `layout.html`: Template for the layout.
  - `index.html`: Template for the index page.
  - `error.html`: Template for pages not found.
  - `entry.html`: Template for individual entry pages.
  - `new_page.html`: Template for creating a new entry.
  - `edit_page.html`: Template for editing an entry.
  - `search_results.html`: Template for displaying search results.
- `static/`: Static files for styling and scripts.
  - `styles.css`: Custom stylesheets.
  - `script.js`: JavaScript files for functionality like dark mode.
- `entries/`: Directory containing Markdown files for each encyclopedia entry.

## Dependencies

- **Django**: Python web framework.
- **markdown2**: Library for converting Markdown to HTML.
- **Bootstrap 5**: Front-end framework for styling.
- **Google Fonts**: Web fonts for typography.

## Customization

- **Styling**: Modify `static/css/styles.css` for custom styles.
- **Templates**: Edit HTML templates in `encyclopedia/templates/encyclopedia/` for custom layouts.
- **JavaScript**: Add or modify JavaScript in `static/js/scripts.js` for custom functionality.

## Future Improvements and Features

- **User Accounts**: Allow users to create accounts, log in, and manage their profiles.
- **Permissions**: Implement different user roles, with varying access to creating, editing, or deleting entries.
- **History and Version Control**: Track changes to entries, allowing users to view and revert to previous versions.
- **Full-Text Search**: Enable searching within the content of entries, not just by title.
- **Search Suggestions**: Provide search suggestions as users type in the search bar.
- **Categories**: Organize entries into categories or topics for easier browsing.
- **Tags**: Implement a tagging system to enable keyword search.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [markdown2 Documentation](https://github.com/trentm/python-markdown2)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Google Fonts](https://fonts.google.com/)

---

*[This project](https://cs50.harvard.edu/web/2020/projects/1/wiki/) is a part of the CS50 Web Programming with Python and JavaScript course.*
