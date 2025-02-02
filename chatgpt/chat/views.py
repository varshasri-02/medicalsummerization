from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat

# Create your views here.
def index(request):
    return render(request, 'index.html')

def response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')  # Get the user's message from the form
        
        # Simulate AI response (for now, just return a placeholder response)
        answer = "Received: " + message  # Placeholder response
        
        # Save the user's message and the simulated response to the database
        new_chat = Chat(message=message, response=answer)
        new_chat.save()
        
        # Return the response as a JsonResponse
        return JsonResponse({'response': answer})

    return JsonResponse({'response': 'Invalid request'}, status=400)
