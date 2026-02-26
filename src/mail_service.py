import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader, select_autoescape
from src.config import settings

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
    """
    Takes an HTML template
    Returns the final HTML string.
    """
    def render_body(self, template_name: str, **context) -> str:

        template = self.jinja_env.get_template(template_name)
        return template.render(**context)

    """
    Injects the environment variables
    
    """
    def send_email(self, recipient_email: str, subject: str, html_body: str):
        message = MIMEMultipart()
        
        # Use the enviroment variables
        message['From'] = settings.email_user 
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(html_body, 'html'))

        with smtplib.SMTP(settings.smtp_server, settings.smtp_port) as server:
            server.starttls()
            server.login(settings.email_user, settings.email_pass)
            server.send_message(message)