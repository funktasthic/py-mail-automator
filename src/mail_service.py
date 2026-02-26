from jinja2 import Environment, FileSystemLoader, select_autoescape

class MailService:
    """
    Handles email body rendering using templates.
    """
    def __init__(self, template_dir: str = 'templates'):
        # Setup the template loader to look into templates folder
        self.jinja_env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def render_body(self, template_name: str, **context) -> str:
        """
        Takes an HTML template and injects variables
        Returns the final HTML string.
        """
        try:
            template = self.jinja_env.get_template(template_name)
            return template.render(**context)
        except Exception as e:
            raise RuntimeError(f"Template rendering failed: {e}")