from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Resume
from django.template import loader
from django.conf import settings
import pdfkit
import os
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        job = request.POST.get('job')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        university = request.POST.get('university')
        about = request.POST.get('about')
        skills = ("||".join(request.POST.getlist('skills')))
        experience = ("||".join(request.POST.getlist('experience')))
        experience_title = ("||".join(request.POST.getlist('experience_title')))
        new_resume = Resume(name=name, job=job, email=email, phone=phone, university=university,
                            about=about, skills=skills, experience=experience, experience_title=experience_title)
        new_resume.save()
        return redirect("resume/{}".format(new_resume.id))
    return render(request, "resume/index.html")


def resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    # compute how many times to display the ul tag to match the template
    skills_count = len(resume.skills_as_list())
    if skills_count % 3 == 0:
        skills_count = skills_count / 3
    else:
        skills_count = skills_count//3 + 1
    return render(request, "resume/resume.html", {'resume': resume, 'range': range(int(skills_count))})


def download_link(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    skills_count = len(resume.skills_as_list())
    if skills_count % 3 == 0:
        skills_count = skills_count / 3
    else:
        skills_count = skills_count//3 + 1

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'enable-local-file-access': None,

    }
    template = loader.get_template("resume/resume.html")
    html = template.render({'resume': resume, 'range': range(int(skills_count))})
    html = html[:html.find('<h3><a id="pdf"')] + html[html.find('Download PDF</a></h3>')+21:]

    css = os.path.join(settings.STATICFILES_DIRS[0] + '/resume/css/resume.css')
    pdf = pdfkit.from_string(html, False, options, css=css)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Transfer-Encoding'] = 'binary'
    filename = resume.name+".pdf"
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
