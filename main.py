import json
from src.reader import load_contacts
from src.mail_service import MailService
from src.config import settings

def main():
    # Load profile data and template configuration
    try:
        with open("data/mail_config.json", "r", encoding="utf-8") as f:
            mail_config = json.load(f)
    except FileNotFoundError:
        print("Config error: data/mail_config.json not found.")
        return

    contacts = load_contacts("data/contacts.xlsx")
    if not contacts:
        return

    mailer = MailService()
    
    for contact in contacts:
        content = {
            **mail_config,
            "recipient_name": contact.name,
            "sender_email": settings.email_user,
            "main_content": mail_config["main_content_template"].format(company=contact.company)
        }
        
        try:
            html = mailer.render_body("email_template.html", **content)
            
            mailer.send_email(
                recipient_email=contact.email,
                subject=f"Inquiry for {contact.company}",
                html_body=html
            )
            print(f"Delivered: {contact.email} (via {settings.email_user})")
        except Exception as e:
            print(f"Failed: {contact.email} | Error: {e}")

if __name__ == "__main__":
    main()