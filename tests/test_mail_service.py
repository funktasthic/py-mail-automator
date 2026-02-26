from src.mail_service import MailService

def test_render_body_injection():
    """Check if placeholders in HTML are correctly replaced."""
    service = MailService()
    context = {
        "recipient_name": "Alice",
        "main_content": "Testing Jinja2",
        "sender_name": "Bob",
        "sender_email": "bob@test.com"
    }
    # Note: Ensure you have an 'email_template.html' in your templates folder
    html = service.render_body("email_template.html", **context)
    
    assert "Alice" in html
    assert "Testing Jinja2" in html
    assert "{{ recipient_name }}" not in html