# Digital Ad Agency Website - Setup Guide (Windows)

## Your System
- Windows 11
- Python 3.10, 3.11, 3.12 installed
- **We'll use Python 3.11** (most stable for Django 4.2)

## Step-by-Step Setup

### 1. Extract Files
Extract the agency_project folder to a location like:
```
C:\Users\YourName\Projects\agency_project
```

### 2. Open Command Prompt
- Press `Windows Key + R`
- Type `cmd` and press Enter
- Navigate to your project:
```bash
cd C:\Users\YourName\Projects\agency_project
```

### 3. Create Virtual Environment (Using Python 3.11)
```bash
py -3.11 -m venv venv
```

**If that doesn't work, try:**
```bash
python -m venv venv
```

### 4. Activate Virtual Environment
```bash
venv\Scripts\activate
```

**You should see (venv) at the start of your command line**

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Create Database
```bash
python manage.py migrate
```

### 7. Create Admin User
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account

### 8. Run Development Server
```bash
python manage.py runserver
```

### 9. Open in Browser
Go to: `http://127.0.0.1:8000`

Admin panel: `http://127.0.0.1:8000/admin`

## Troubleshooting

### "py -3.11 not recognized"
Find your Python 3.11 installation path:
```bash
where python
```
Use the full path:
```bash
C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe -m venv venv
```

### "pip is not recognized"
After activating venv:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Port Already in Use
```bash
python manage.py runserver 8080
```
Then visit: `http://127.0.0.1:8080`

## Next Steps After Setup

1. Customize the homepage content
2. Add your services
3. Configure contact form email settings
4. Add blog posts through admin panel
5. Update site branding and colors

## Project Structure
```
agency_project/
├── venv/                  # Virtual environment (you'll create this)
├── adagency/             # Main Django project
│   ├── settings.py       # Configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # Production server config
├── core/                 # Main website app
│   ├── templates/        # HTML templates
│   ├── static/           # CSS, JS, images
│   └── views.py          # Page logic
├── blog/                 # Blog functionality
├── contact/              # Contact form
├── manage.py             # Django management script
└── requirements.txt      # Python packages
```

## Need Help?
If you get stuck at any step, just let me know which step and what error message you see!
