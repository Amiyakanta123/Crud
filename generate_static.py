#!/usr/bin/env python3
"""
Static Site Generator for PyWebApp
Generates static HTML files from FastAPI templates for optimal performance
"""

import os
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

class StaticGenerator:
    def __init__(self):
        self.template_dir = Path("templates")
        self.output_dir = Path("static/generated")
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_index(self):
        """Generate the index/home page"""
        template = self.env.get_template("index.html")
        
        tasks = [
            {
                "id": 1,
                "title": "Build FastAPI Application",
                "description": "Create a modern web app with FastAPI",
                "completed": True
            },
            {
                "id": 2,
                "title": "Design Beautiful UI",
                "description": "Implement responsive design with Tailwind CSS",
                "completed": True
            },
            {
                "id": 3,
                "title": "Add API Endpoints",
                "description": "Create RESTful API with CRUD operations",
                "completed": False
            },
            {
                "id": 4,
                "title": "Deploy to Production",
                "description": "Deploy the application for public access",
                "completed": False
            }
        ]
        
        stats = {
            "total_tasks": 4,
            "completed_tasks": 2,
            "pending_tasks": 2,
            "completion_rate": 50.0
        }
        
        html = template.render(
            request={"url": "/"},
            tasks=tasks,
            stats=stats,
            current_year=datetime.now().year
        )
        
        output_file = self.output_dir / "index.html"
        output_file.write_text(html, encoding="utf-8")
        print(f"✓ Generated: {output_file}")
    
    def generate_about(self):
        """Generate the about page"""
        template = self.env.get_template("about.html")
        
        html = template.render(
            request={"url": "/about"},
            current_year=datetime.now().year
        )
        
        output_file = self.output_dir / "about.html"
        output_file.write_text(html, encoding="utf-8")
        print(f"✓ Generated: {output_file}")
    
    def generate_all(self):
        """Generate all static pages"""
        print("Starting static site generation...")
        print("-" * 50)
        
        self.generate_index()
        self.generate_about()
        
        print("-" * 50)
        print(f"✓ Static site generation complete!")
        print(f"✓ Files saved to: {self.output_dir.absolute()}")
        print("\nYou can now:")
        print("  1. Open the HTML files directly in a browser")
        print("  2. Serve them with any static file server")
        print("  3. Deploy to any static hosting platform")

def main():
    try:
        generator = StaticGenerator()
        generator.generate_all()
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
