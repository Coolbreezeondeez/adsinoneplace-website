# Ads in One Place - Digital Marketing Agency Website

A professional Django-based website for a digital marketing agency, featuring blog functionality, contact forms, and service showcases.

## Features

### Phase 1 (Current)
- ✅ Homepage with hero section and service preview
- ✅ About page
- ✅ Services page with detailed offerings
- ✅ Blog with categories and pagination
- ✅ Contact form with email notifications
- ✅ Responsive Bootstrap 5 design
- ✅ Admin panel for content management
- ✅ Rich text editor for blog posts

### Phase 2 (Coming Soon)
- 🔄 User authentication system
- 🔄 Client dashboard
- 🔄 Project management

### Phase 3 (Future)
- 🔄 Ad platform API integrations (Meta, Google, TikTok)
- 🔄 Campaign reporting dashboards
- 🔄 Analytics and visualization

## Tech Stack

- **Backend:** Django 4.2
- **Database:** SQLite (development) / PostgreSQL (production)
- **Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript
- **Editor:** CKEditor for blog posts
- **Forms:** Django Crispy Forms with Bootstrap 5

## Quick Start (Windows)

### Prerequisites
- Python 3.11 (recommended)
- Git (optional)

### Installation

1. **Extract the project files**
   ```
   Extract agency_project folder to C:\Users\YourName\Projects\
   ```

2. **Open Command Prompt**
   ```bash
   cd C:\Users\YourName\Projects\agency_project
   ```

3. **Create virtual environment**
   ```bash
   py -3.11 -m venv venv
   ```

4. **Activate virtual environment**
   ```bash
   venv\Scripts\activate
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the website**
   - Homepage: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

## Usage

### Adding Blog Posts

1. Go to http://127.0.0.1:8000/admin
2. Log in with your superuser credentials
3. Click "Posts" under "Blog"
4. Click "Add Post"
5. Fill in the details (title, content, category, etc.)
6. Change status to "Published" and set "Published at" date
7. Save

### Managing Contact Messages

1. Go to admin panel
2. Click "Contact messages" under "Contact"
3. View submissions and update their status
4. Add internal notes if needed

### Customizing Content

- **Homepage:** Edit `templates/core/home.html`
- **Services:** Modify the services list in `core/views.py`
- **Styling:** Update `static/css/style.css`
- **Colors:** Change Bootstrap classes in templates or update CSS variables

## Project Structure

```
agency_project/
├── adagency/              # Main project settings
│   ├── settings.py        # Django configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config
├── core/                 # Main website app
│   ├── views.py          # Page views
│   └── urls.py           # URL patterns
├── blog/                 # Blog functionality
│   ├── models.py         # Blog data models
│   ├── views.py          # Blog views
│   ├── admin.py          # Admin config
│   └── urls.py           # Blog URLs
├── contact/              # Contact form
│   ├── models.py         # Contact message model
│   ├── forms.py          # Contact form
│   ├── views.py          # Contact view
│   └── urls.py           # Contact URLs
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── core/             # Core app templates
│   ├── blog/             # Blog templates
│   └── contact/          # Contact templates
├── static/               # Static files (CSS, JS, images)
│   └── css/
│       └── style.css     # Custom styles
├── media/                # User uploads
├── venv/                 # Virtual environment
├── requirements.txt      # Python dependencies
├── manage.py             # Django management script
└── README.md            # This file
```

## Common Commands

```bash
# Start server
python manage.py runserver

# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic

# Run tests
python manage.py test
```

## Email Configuration

By default, emails from the contact form print to the console. To send real emails:

1. Open `adagency/settings.py`
2. Find the email configuration section
3. Uncomment and configure SMTP settings:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-app-password'
   ```

## Deployment

For production deployment:

1. Change `DEBUG = False` in settings.py
2. Set `ALLOWED_HOSTS` in settings.py
3. Use PostgreSQL instead of SQLite
4. Set up environment variables for sensitive data
5. Run `python manage.py collectstatic`
6. Use a production WSGI server (Gunicorn, uWSGI)
7. Set up a reverse proxy (Nginx, Apache)

## Support

For issues or questions, refer to:
- Django Documentation: https://docs.djangoproject.com/
- Bootstrap 5 Docs: https://getbootstrap.com/docs/5.3/
- Project setup guide: SETUP_WINDOWS.md

## License

This project is proprietary. All rights reserved.
