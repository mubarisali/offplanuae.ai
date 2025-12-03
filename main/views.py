# offplanuae/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Property
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    """Render the home page"""
    offplan = Property.objects.order_by('-low_price')[:8]
    context = {
        'offplan':offplan,
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
    """Render the blog page with all blog posts"""
    # Demo blog posts data
    blog_posts = [
        {
            'id': 1,
            'title': 'Top 10 Off-Plan Developments in Dubai 2025',
            'excerpt': 'Explore the most promising off-plan projects launching this year in Dubai\'s thriving real estate market. Discover exclusive opportunities.',
            'date': 'Nov 20, 2025',
            'author': 'Sarah Ahmed',
            'image': 'img/hero.avif',
            'content': '''
                <p>Dubai's real estate market continues to flourish with groundbreaking off-plan developments that redefine luxury living. In this comprehensive guide, we explore the top 10 projects that are set to transform the emirate's skyline in 2025.</p>
                
                <h3>1. Palm Residences - Nakheel</h3>
                <p>Located on the iconic Palm Jumeirah, this development offers unparalleled beachfront living with world-class amenities and stunning Arabian Gulf views.</p>
                
                <h3>2. Downtown Villas - Damac Properties</h3>
                <p>Experience urban sophistication in the heart of Downtown Dubai with these premium villas featuring contemporary design and smart home technology.</p>
                
                <h3>3. Marina Heights - Emaar Properties</h3>
                <p>Rising high in Dubai Marina, these luxury apartments offer breathtaking views and direct access to the finest dining and entertainment venues.</p>
                
                <p>Each of these developments represents the pinnacle of modern architecture and lifestyle convenience, making them excellent investment opportunities for both end-users and investors.</p>
            '''
        },
        {
            'id': 2,
            'title': 'How AI is Transforming Property Investment',
            'excerpt': 'Discover how artificial intelligence is revolutionizing the way investors find and evaluate real estate opportunities in the UAE market.',
            'date': 'Nov 18, 2025',
            'author': 'Michael Johnson',
            'image': 'img/hero.avif',
            'content': '''
                <p>Artificial Intelligence is reshaping the real estate industry, bringing unprecedented efficiency and insights to property investment decisions.</p>
                
                <h3>Predictive Analytics</h3>
                <p>AI algorithms analyze vast amounts of market data to predict price trends, helping investors make informed decisions about when and where to invest.</p>
                
                <h3>Property Valuation</h3>
                <p>Machine learning models can accurately assess property values by considering multiple factors including location, amenities, market trends, and historical data.</p>
                
                <h3>Personalized Recommendations</h3>
                <p>AI-powered platforms like OffPlanUAE.ai can match investors with properties that perfectly align with their investment goals and preferences.</p>
            '''
        },
        {
            'id': 3,
            'title': 'Understanding UAE Real Estate Laws',
            'excerpt': 'A comprehensive guide to navigating property ownership regulations and legal requirements in the United Arab Emirates.',
            'date': 'Nov 15, 2025',
            'author': 'Fatima Al-Mansoori',
            'image': 'img/hero.avif',
            'content': '''
                <p>Understanding the legal framework governing real estate in the UAE is crucial for any investor or homebuyer looking to enter this dynamic market.</p>
                
                <h3>Freehold vs Leasehold</h3>
                <p>Learn the difference between freehold areas where foreigners can own property outright and leasehold areas with long-term lease agreements.</p>
                
                <h3>Registration Process</h3>
                <p>All property transactions must be registered with the Dubai Land Department or relevant authority to ensure legal ownership.</p>
                
                <h3>RERA Regulations</h3>
                <p>The Real Estate Regulatory Agency (RERA) oversees all real estate activities, protecting both buyers and sellers in transactions.</p>
            '''
        },
        {
            'id': 4,
            'title': 'Investment Tips for First-Time Buyers',
            'excerpt': 'Essential advice and strategies for those entering the UAE property market for the first time.',
            'date': 'Nov 12, 2025',
            'author': 'John Smith',
            'image': 'img/hero.avif',
            'content': '''
                <p>Entering the real estate market for the first time can be overwhelming. Here are key tips to help you make smart investment decisions.</p>
                
                <h3>Set a Realistic Budget</h3>
                <p>Calculate your budget including down payment, monthly installments, maintenance fees, and additional costs like registration and agency fees.</p>
                
                <h3>Location is Key</h3>
                <p>Choose locations with strong growth potential, good infrastructure, and proximity to key amenities like schools, hospitals, and transportation.</p>
                
                <h3>Research the Developer</h3>
                <p>Invest with reputable developers who have a proven track record of delivering quality projects on time.</p>
            '''
        },
        {
            'id': 5,
            'title': 'Abu Dhabi\'s Emerging Property Hotspots',
            'excerpt': 'Explore the up-and-coming areas in Abu Dhabi that offer excellent investment potential and quality of life.',
            'date': 'Nov 10, 2025',
            'author': 'Ahmed Hassan',
            'image': 'img/hero.avif',
            'content': '''
                <p>Abu Dhabi is experiencing rapid development with several emerging neighborhoods becoming prime investment destinations.</p>
                
                <h3>Yas Island</h3>
                <p>Home to world-class entertainment and leisure facilities, Yas Island continues to attract investors with its diverse residential offerings.</p>
                
                <h3>Saadiyat Island</h3>
                <p>Known as the cultural district of Abu Dhabi, Saadiyat Island offers luxury living combined with art, culture, and natural beauty.</p>
                
                <h3>Reem Island</h3>
                <p>This modern development offers a perfect blend of residential, commercial, and recreational facilities with stunning waterfront views.</p>
            '''
        },
        {
            'id': 6,
            'title': 'Financing Your Off-Plan Property Purchase',
            'excerpt': 'Understanding mortgage options, payment plans, and financial strategies for off-plan property investments.',
            'date': 'Nov 8, 2025',
            'author': 'Lisa Chen',
            'image': 'img/hero.avif',
            'content': '''
                <p>Financing an off-plan property requires careful planning and understanding of available options to make the most of your investment.</p>
                
                <h3>Developer Payment Plans</h3>
                <p>Many developers offer flexible payment plans allowing you to pay in installments during the construction period, typically with minimal or no interest.</p>
                
                <h3>Mortgage Options</h3>
                <p>UAE banks offer competitive mortgage rates for off-plan properties, usually requiring 20-25% down payment for expatriates.</p>
                
                <h3>Investment Returns</h3>
                <p>Off-plan properties often offer better ROI compared to ready properties, with potential for capital appreciation and rental income.</p>
            '''
        },
    ]
    
    context = {
        'page_title': 'Blog - Off Plan UAE',
        'meta_description': 'Latest news and insights about UAE real estate',
        'blog_posts': blog_posts
    }
    return render(request, 'main/blog.html', context)


def blog_detail(request, blog_id):
    """Render individual blog post detail page"""
    # Demo blog posts data (same as above)
    blog_posts = [
        {
            'id': 1,
            'title': 'Top 10 Off-Plan Developments in Dubai 2025',
            'excerpt': 'Explore the most promising off-plan projects launching this year in Dubai\'s thriving real estate market. Discover exclusive opportunities.',
            'date': 'Nov 20, 2025',
            'author': 'Sarah Ahmed',
            'image': 'img/hero.avif',
            'content': '''
                <p>Dubai's real estate market continues to flourish with groundbreaking off-plan developments that redefine luxury living. In this comprehensive guide, we explore the top 10 projects that are set to transform the emirate's skyline in 2025.</p>
                
                <h3>1. Palm Residences - Nakheel</h3>
                <p>Located on the iconic Palm Jumeirah, this development offers unparalleled beachfront living with world-class amenities and stunning Arabian Gulf views.</p>
                
                <h3>2. Downtown Villas - Damac Properties</h3>
                <p>Experience urban sophistication in the heart of Downtown Dubai with these premium villas featuring contemporary design and smart home technology.</p>
                
                <h3>3. Marina Heights - Emaar Properties</h3>
                <p>Rising high in Dubai Marina, these luxury apartments offer breathtaking views and direct access to the finest dining and entertainment venues.</p>
                
                <p>Each of these developments represents the pinnacle of modern architecture and lifestyle convenience, making them excellent investment opportunities for both end-users and investors.</p>
            '''
        },
        {
            'id': 2,
            'title': 'How AI is Transforming Property Investment',
            'excerpt': 'Discover how artificial intelligence is revolutionizing the way investors find and evaluate real estate opportunities in the UAE market.',
            'date': 'Nov 18, 2025',
            'author': 'Michael Johnson',
            'image': 'img/hero.avif',
            'content': '''
                <p>Artificial Intelligence is reshaping the real estate industry, bringing unprecedented efficiency and insights to property investment decisions.</p>
                
                <h3>Predictive Analytics</h3>
                <p>AI algorithms analyze vast amounts of market data to predict price trends, helping investors make informed decisions about when and where to invest.</p>
                
                <h3>Property Valuation</h3>
                <p>Machine learning models can accurately assess property values by considering multiple factors including location, amenities, market trends, and historical data.</p>
                
                <h3>Personalized Recommendations</h3>
                <p>AI-powered platforms like OffPlanUAE.ai can match investors with properties that perfectly align with their investment goals and preferences.</p>
            '''
        },
        {
            'id': 3,
            'title': 'Understanding UAE Real Estate Laws',
            'excerpt': 'A comprehensive guide to navigating property ownership regulations and legal requirements in the United Arab Emirates.',
            'date': 'Nov 15, 2025',
            'author': 'Fatima Al-Mansoori',
            'image': 'img/hero.avif',
            'content': '''
                <p>Understanding the legal framework governing real estate in the UAE is crucial for any investor or homebuyer looking to enter this dynamic market.</p>
                
                <h3>Freehold vs Leasehold</h3>
                <p>Learn the difference between freehold areas where foreigners can own property outright and leasehold areas with long-term lease agreements.</p>
                
                <h3>Registration Process</h3>
                <p>All property transactions must be registered with the Dubai Land Department or relevant authority to ensure legal ownership.</p>
                
                <h3>RERA Regulations</h3>
                <p>The Real Estate Regulatory Agency (RERA) oversees all real estate activities, protecting both buyers and sellers in transactions.</p>
            '''
        },
        {
            'id': 4,
            'title': 'Investment Tips for First-Time Buyers',
            'excerpt': 'Essential advice and strategies for those entering the UAE property market for the first time.',
            'date': 'Nov 12, 2025',
            'author': 'John Smith',
            'image': 'img/hero.avif',
            'content': '''
                <p>Entering the real estate market for the first time can be overwhelming. Here are key tips to help you make smart investment decisions.</p>
                
                <h3>Set a Realistic Budget</h3>
                <p>Calculate your budget including down payment, monthly installments, maintenance fees, and additional costs like registration and agency fees.</p>
                
                <h3>Location is Key</h3>
                <p>Choose locations with strong growth potential, good infrastructure, and proximity to key amenities like schools, hospitals, and transportation.</p>
                
                <h3>Research the Developer</h3>
                <p>Invest with reputable developers who have a proven track record of delivering quality projects on time.</p>
            '''
        },
        {
            'id': 5,
            'title': 'Abu Dhabi\'s Emerging Property Hotspots',
            'excerpt': 'Explore the up-and-coming areas in Abu Dhabi that offer excellent investment potential and quality of life.',
            'date': 'Nov 10, 2025',
            'author': 'Ahmed Hassan',
            'image': 'img/hero.avif',
            'content': '''
                <p>Abu Dhabi is experiencing rapid development with several emerging neighborhoods becoming prime investment destinations.</p>
                
                <h3>Yas Island</h3>
                <p>Home to world-class entertainment and leisure facilities, Yas Island continues to attract investors with its diverse residential offerings.</p>
                
                <h3>Saadiyat Island</h3>
                <p>Known as the cultural district of Abu Dhabi, Saadiyat Island offers luxury living combined with art, culture, and natural beauty.</p>
                
                <h3>Reem Island</h3>
                <p>This modern development offers a perfect blend of residential, commercial, and recreational facilities with stunning waterfront views.</p>
            '''
        },
        {
            'id': 6,
            'title': 'Financing Your Off-Plan Property Purchase',
            'excerpt': 'Understanding mortgage options, payment plans, and financial strategies for off-plan property investments.',
            'date': 'Nov 8, 2025',
            'author': 'Lisa Chen',
            'image': 'img/hero.avif',
            'content': '''
                <p>Financing an off-plan property requires careful planning and understanding of available options to make the most of your investment.</p>
                
                <h3>Developer Payment Plans</h3>
                <p>Many developers offer flexible payment plans allowing you to pay in installments during the construction period, typically with minimal or no interest.</p>
                
                <h3>Mortgage Options</h3>
                <p>UAE banks offer competitive mortgage rates for off-plan properties, usually requiring 20-25% down payment for expatriates.</p>
                
                <h3>Investment Returns</h3>
                <p>Off-plan properties often offer better ROI compared to ready properties, with potential for capital appreciation and rental income.</p>
            '''
        },
    ]
    
    # Find the blog post with matching ID
    blog_post = None
    for post in blog_posts:
        if post['id'] == blog_id:
            blog_post = post
            break
    
    # If blog post not found, redirect to blog page
    if not blog_post:
        messages.error(request, 'Blog post not found.')
        return redirect('main:blog')
    
    # Get related posts (exclude current post)
    related_posts = [post for post in blog_posts if post['id'] != blog_id][:3]
    
    context = {
        'page_title': f'{blog_post["title"]} - Blog',
        'meta_description': blog_post['excerpt'],
        'blog_post': blog_post,
        'related_posts': related_posts,
    }
    return render(request, 'main/blog_detail.html', context)


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

def properties_detail(request, property_id=None):
    """Render the property detail page with demo data if no property_id"""
    
    # If property_id provided and Property model exists, try to load from database
    if property_id and Property:
        try:
            property_obj = Property.objects.get(id=property_id)
            
            # Handle contact form submission
            if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                message = request.POST.get('message')
                
                messages.success(request, 'Thank you for your inquiry! We will contact you soon.')
                return redirect('main:properties_detail', property_id=property_id)
            
            context = {
                'property': property_obj,
                'page_title': f'{property_obj.name} - Property Details',
                'meta_description': f'{property_obj.description[:160]}',
            }
            return render(request, 'main/properties_detail.html', context)
        except:
            pass
    
    # Demo data structure matching the model
    class DemoObject:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
        
        def all(self):
            return getattr(self, '_items', [])
    
    # Create demo developer
    demo_developer = DemoObject(
        name="Emaar Properties",
        logo=DemoObject(url="{% static 'img/emaar.png' %}")
    )
    
    # Create demo unit details
    demo_units = [
        DemoObject(
            unit_type="Apartment",
            rooms=1,
            size=508,
            price=853879
        ),
        DemoObject(
            unit_type="Apartment",
            rooms=2,
            size=1126,
            price=1833874
        ),
        DemoObject(
            unit_type="Apartment",
            rooms=3,
            size=2672,
            price=4040459
        ),
    ]
    
    # Create demo amenities
    demo_amenities = [
        DemoObject(name="Swimming Pool", icon="fa-swimming-pool"),
        DemoObject(name="Fitness Center", icon="fa-dumbbell"),
        DemoObject(name="Covered Parking", icon="fa-car"),
        DemoObject(name="24/7 Security", icon="fa-shield-alt"),
        DemoObject(name="Landscaped Gardens", icon="fa-tree"),
        DemoObject(name="Retail Outlets", icon="fa-shopping-bag"),
        DemoObject(name="Business Center", icon="fa-building"),
        DemoObject(name="High-Speed Internet", icon="fa-wifi"),
    ]
    
    # Create demo gallery
    demo_gallery = [
        DemoObject(image=DemoObject(url="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&auto=format&fit=crop")),
        DemoObject(image=DemoObject(url="https://images.unsplash.com/photo-1502672260066-6bc35f0a9e7c?w=800&auto=format&fit=crop")),
        DemoObject(image=DemoObject(url="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&auto=format&fit=crop")),
        DemoObject(image=DemoObject(url="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&auto=format&fit=crop")),
    ]
    
    # Create demo property
    demo_property = DemoObject(
        name="Marina Heights",
        developer=demo_developer,
        location="Dubai Marina",
        bedrooms=2,
        size=1450,
        price=2450000,
        description="Experience luxury living at its finest in this stunning 2-bedroom apartment located in the heart of Dubai Marina. Featuring breathtaking views, premium finishes, and world-class amenities.",
        image=DemoObject(url="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&auto=format&fit=crop"),
        video_url="https://www.youtube.com/embed/dQw4w9WgXcQ",
        map_embed_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3623.9997!2d55.136169!3d25.080373!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5f6d8e12345!2sDubai%20Marina!5e0!3m2!1sen!2sae!4v1634071196899!5m2!1sen!2sae",
        unit_details=DemoObject(_items=demo_units),
        amenities=DemoObject(_items=demo_amenities),
        gallery=DemoObject(_items=demo_gallery),
    )
    
    # Handle demo contact form submission
    if request.method == 'POST':
        messages.success(request, 'Thank you for your inquiry! We will contact you soon.')
        return redirect('main:properties_detail')
    
    context = {
        'property': demo_property,
        'page_title': 'Marina Heights - Property Details',
        'meta_description': 'Experience luxury living at its finest in this stunning 2-bedroom apartment',
    }
    return render(request, 'main/properties_detail.html', context)