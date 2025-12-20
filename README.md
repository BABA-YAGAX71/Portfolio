# Portfolio Website - Python Flask Application

A modern, responsive portfolio website built with Python and Flask. Features a clean design with sections for projects, skills, achievements, and contact information.

## Project Structure

```
Portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── index.html        # Home page
│   ├── about.html        # About page with skills
│   ├── projects.html     # Projects showcase
│   └── contact.html      # Contact information
├── static/
│   ├── images/
│   │   └── profile.jpg   # Profile photo
│   └── css/              # Custom CSS (optional)
└── Md Shahriar Rashid Rahi - Resume.pdf
```

## Features

- 📱 **Fully Responsive Design** - Mobile-friendly layout using Tailwind CSS
- 🎨 **Modern UI** - Clean, professional dark theme with blue accents
- 📝 **Multiple Pages** - Home, About, Projects, and Contact pages
- 🖼️ **Profile Section** - Integrated profile photo from your image
- 💼 **Project Showcase** - Display your work with tech stack details
- 🏆 **Achievements** - Highlight your competitive programming and accomplishments
- 📊 **Skills Display** - Organized skill categories
- 📧 **Contact Integration** - Easy email and social media links

## Installation

1. Install Python 3.8 or higher

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated

2. Run the Flask app:
```bash
python app.py
```

3. Open your browser and go to:
```
http://localhost:5000
```

## Customization

Edit `app.py` to customize:
- Your profile information (name, email, phone, location)
- Social media links
- Skills and skill categories
- Projects and their descriptions
- Achievements
- Competitive programming statistics

## Pages

- **Home (`/`)** - Landing page with hero section, featured skills, and projects
- **About (`/about`)** - Detailed about section with full skill list and achievements
- **Projects (`/projects`)** - All projects with descriptions and tech stacks
- **Contact (`/contact`)** - Contact information and ways to get in touch

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, Tailwind CSS
- **Templating**: Jinja2
- **Design**: Responsive design with mobile-first approach

## Resume Integration

Your resume PDF is included in the project. You can:
- Share it directly from the portfolio folder
- Embed it on a dedicated resume page (enhancement option)
- Link to it from your portfolio

## Profile Photo

Your profile photo (IMG_1470.JPG) is automatically copied to `static/images/profile.jpg` and displayed throughout the site.

## Future Enhancements

- Blog section for technical articles
- Dark/Light mode toggle
- Form submission for contact messages
- Resume PDF embed
- Animation effects
- Analytics integration

---

Built with ❤️ using Python & Flask
