from pathlib import Path

def load_template(template_name: str) -> str:
    """Load a template file from the templates directory."""
    template_dir = Path(__file__).parent / 'templates'
    template_path = template_dir / template_name
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()