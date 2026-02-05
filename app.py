from flask import Flask, render_template
from pathlib import Path
import json

app = Flask(__name__)

# Portfolio data extracted from resume
portfolio_data = {
    "profile": {
        "name": "Md Shahriar Rashid Rahi",
        "title": "AI Developer at Softevence, Betopia Group",
        "email": "babayagxrahi123@gmail.com",
        "phone": "01794780059",
        "location": "Chittagong, Bangladesh",
        "summary": "AI Developer at Softevence, Betopia Group, with expertise in artificial intelligence, machine learning, and full-stack development. Skilled in solving complex problems and building intelligent solutions using cutting-edge technologies.",
        "socials": [
            {"platform": "GitHub", "url": "https://github.com/BABA-YAGAX71"},
            {"platform": "LinkedIn", "url": "https://www.linkedin.com/in/md-shahriar-rashid-867008263/"},
            {"platform": "Codeforces", "url": "https://codeforces.com/profile/babayagaxrahi123"},
            {"platform": "Email", "url": "mailto:babayagxrahi123@gmail.com"},
        ]
    },
    "skills": [
        {
            "category": "Languages",
            "skills": ["Python", "Go", "JavaScript", "C++", "SQL"]
        },
        {
            "category": "Web Development",
            "skills": ["Flask", "Django", "HTML/CSS", "React", "REST APIs"]
        },
        {
            "category": "Databases & Tools",
            "skills": ["PostgreSQL", "MongoDB", "Git", "Docker", "Linux"]
        }
    ],
    "projects": [
        {
            "title": "Web Portfolio",
            "description": "Personal portfolio website showcasing projects and skills with responsive design.",
            "tech_stack": "Python, Flask, Tailwind CSS, PostgreSQL",
            "link": "#"
        },
        {
            "title": "Machine Learning Projects",
            "description": "Advanced ML models for classification, regression, and clustering tasks. Includes data preprocessing, feature engineering, and model optimization with scikit-learn, TensorFlow, and PyTorch.",
            "tech_stack": "Python, TensorFlow, PyTorch, scikit-learn, Pandas, NumPy",
            "link": "/projects/ml"
        },
        {
            "title": "RAG (Retrieval-Augmented Generation) System",
            "description": "Intelligent RAG system combining LLMs with vector databases for context-aware responses. Enables retrieval of relevant documents and generation of accurate answers using embeddings and semantic search.",
            "tech_stack": "Python, LangChain, OpenAI, Pinecone, ChromaDB, Transformers",
            "link": "#"
        },
        {
            "title": "Competitive Programming Solutions",
            "description": "Collection of optimized solutions for algorithmic problems from Codeforces, AtCoder, and LeetCode.",
            "tech_stack": "C++, Python, Algorithms",
            "link": "#"
        },
        {
            "title": "Full-Stack Application",
            "description": "Complete web application with backend API and interactive frontend.",
            "tech_stack": "Go, React, PostgreSQL",
            "link": "#"
        }
    ],
    "achievements": [
        {
            "title": "Competitive Programming Contests",
            "description": "Participated in multiple programming contests with consistent rankings"
        },
        {
            "title": "Technical Leadership",
            "description": "Led projects and mentored team members in software development best practices"
        },
        {
            "title": "Open Source Contributions",
            "description": "Contributed to various open-source projects"
        }
    ],
    "certifications": [
        {
            "title": "Machine Learning Specialization",
            "issuer": "Coursera",
            "date": "2024",
            "credential": "View Credential",
            "url": "#"
        },
        {
            "title": "Python for Data Science",
            "issuer": "edX",
            "date": "2024",
            "credential": "View Credential",
            "url": "#"
        },
        {
            "title": "Full Stack Web Development",
            "issuer": "Udemy",
            "date": "2023",
            "credential": "View Credential",
            "url": "#"
        },
        {
            "title": "Deep Learning Specialization",
            "issuer": "Coursera",
            "date": "2023",
            "credential": "View Credential",
            "url": "#"
        }
    ],
    "cp_stats": [
        "700+ Problems Solved",
        "solved many problems in Data Structures & Algorithms",
        "Competitive Rating: 1800+",
        "Active on Codeforces & LeetCode"
    ],
    "coding_platforms": [
        {
            "name": "Codeforces",
            "url": "https://codeforces.com",
            "problems_solved": "400+",
            "rating": "1000",
            "icon": "🟦",
            "description": "Competitive programming contests and algorithmic challenges"
        },
        {
            "name": "LeetCode",
            "url": "https://leetcode.com",
            "problems_solved": "50+",
            "icon": "🟨",
            "description": "Interview preparation and coding challenges"
        },
        {
            "name": "CSES",
            "url": "https://cses.fi/problemset/",
            "problems_solved": "100",
            "icon": "🟪",
            "description": "Algorithmic problem set covering competitive programming topics"
        },
        {
            "name": "Beecrowd",
            "url": "https://www.beecrowd.com.br",
            "problems_solved": "150+",
            "icon": "🟧",
            "description": "Brazilian competitive programming platform with diverse problems"
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=portfolio_data)

@app.route('/projects/ml')
def ml_projects():
    return render_template('ml-projects.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
