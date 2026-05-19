from django.shortcuts import render, redirect
from .models import Item

def home(request):
    query = request.GET.get('q')
    
    # Homepage Rule: Only display Active 'Lost' or 'Found' items to regular users.
    # This automatically hides 'Claimed' items from the public feed!
    if query:
        items = Item.objects.filter(title__icontains=query, status__in=['Lost', 'Found']).order_by('-created_at')
    else:
        items = Item.objects.filter(status__in=['Lost', 'Found']).order_by('-created_at')
        
    return render(request, 'home.html', {'items': items, 'query': query})


def add_item(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        contact = request.POST['contact']
        image = request.FILES.get('image') # Capture the uploaded image file safely

        Item.objects.create(
            title=title,
            description=description,
            status=status,
            contact=contact,
            image=image
        )
        return redirect('home')

    return render(request, 'add_item.html')