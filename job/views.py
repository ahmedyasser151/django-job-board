from pickle import FALSE
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job, Category
from .form import ApplyForm

# Create your views here.

def jobs_list(request):
    job_list = Job.objects.all()
    categories = Category.objects.all()
    
    paginator = Paginator(job_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'job/jobs_list.html',{'jobs':page_obj, 'categories':categories})

def job_details(request, slug):
    
    job_details = Job.objects.get(slug=slug)
    
    if request.method=='POST':
        
        apply = ApplyForm(request.POST, request.FILES)
                
        if apply.is_valid():
            
        #    apply.job = job_details \ i use it when exclude job field from applyform
           
           apply.save()
         
    else:
        apply = ApplyForm() 
    return render(request, 'job/job_details.html', {'job':job_details , 'applyform':apply})
