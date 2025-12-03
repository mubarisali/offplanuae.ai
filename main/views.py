# offplanuae/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    """Render the home page"""
    context = {
        'page_title': 'Home - Off Plan UAE',
        'meta_description': 'Discover premium off-plan properties in UAE',
    }
    return render(request, 'main/home.html', context)

def about(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Save to database or send to email service
        messages.success(request, 'Thank you for subscribing!')
        return redirect('about')
    
    context = {
        'page_title': 'About Us - OffPlanUAE.ai',
        'meta_description': 'Learn about OffPlanUAE.ai - transforming property discovery in UAE with AI technology.',
    }
    return render(request, 'main/about.html', context)

def blog(request):
    """Render the blog page"""
    context = {
        'page_title': 'Blog - Off Plan UAE',
        'meta_description': 'Latest news and insights about UAE real estate',
        'blog_posts': [
            {
                'title': 'Top 10 Off-Plan Projects in Dubai 2024',
                'excerpt': 'Discover the most promising off-plan developments...',
                'date': '2024-11-15',
                'image': '/static/images/blog1.jpg'
            },
            {
                'title': 'Investment Guide: Abu Dhabi Real Estate',
                'excerpt': 'Everything you need to know about investing...',
                'date': '2024-11-10',
                'image': '/static/images/blog2.jpg'
            },
        ]
    }
    return render(request, 'main/blog.html', context)



@csrf_exempt
def contact(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            phone = data.get('phone', '').strip()
            subject = data.get('subject', '').strip()
            message = data.get('message', '').strip()
            
            # Basic validation
            errors = {}
            if not name:
                errors['name'] = 'Name is required'
            if not email or '@' not in email:
                errors['email'] = 'Valid email is required'
            if not phone:
                errors['phone'] = 'Phone number is required'
            if not subject:
                errors['subject'] = 'Subject is required'
            if not message:
                errors['message'] = 'Message is required'
            
            if errors:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Please fill all required fields',
                    'errors': errors
                }, status=400)
            
            # Here you can add:
            # 1. Save to database
            # 2. Send email notification
            # 3. Send to CRM
            
            # Example: Save to database (you'll need to create a Contact model)
            # Contact.objects.create(
            #     name=name,
            #     email=email,
            #     phone=phone,
            #     subject=subject,
            #     message=message
            # )
            
            # Example: Send email
            # from django.core.mail import send_mail
            # send_mail(
            #     f'New Contact Form: {subject}',
            #     f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}',
            #     'noreply@offplanuae.ai',
            #     ['info@offplanuae.ai'],
            #     fail_silently=False,
            # )
            
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you for contacting us! We will get back to you within 24 hours.'
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid request format'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'An error occurred. Please try again later.'
            }, status=500)
    
    context = {
        'page_title': 'Contact Us - Off Plan UAE',
        'meta_description': 'Get in touch with Off Plan UAE for property inquiries',
    }
    return render(request, 'main/contact.html', context)

def properties(request):
    return render(request, 'main/properties.html')
