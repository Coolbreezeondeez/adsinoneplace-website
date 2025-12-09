from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send email notification (optional - currently prints to console in development)
            subject = f"New Contact Form: {contact_message.subject}"
            message = f"""
            New contact form submission:
            
            Name: {contact_message.name}
            Email: {contact_message.email}
            Phone: {contact_message.phone}
            Company: {contact_message.company}
            
            Subject: {contact_message.subject}
            
            Message:
            {contact_message.message}
            """
            
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@adagency.com',
                    ['bbrucker@cbcbconnect.com'],  # Replace with your email
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Thank you for contacting us! We\'ll get back to you soon.')
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
