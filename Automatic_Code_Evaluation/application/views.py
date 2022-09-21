from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')


# File handling
from .forms import MyfileUploadForm
from .models import file_upload




def submit_code(request):
    if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)


        print(form.as_p)
        
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']

            file_upload(file_name=name, my_file=the_files).save()
            
            return HttpResponse("file uploaded")
        else:
            return HttpResponse('error')

    else:
        
        context = {
            'form':MyfileUploadForm()
        }      
        
        return render(request, 'submit_code.html', context)
        



def show_file(request):
    # this for testing 
    all_data = file_upload.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'view.html', context)
    

