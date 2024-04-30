from django.shortcuts import render
from .models import data
import pdfkit
from django.template import loader

from django.http import HttpResponse


# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        work = request.POST.get("work", "")
        skills = request.POST.get("skills", "")

        object = data(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            work=work,
            skills=skills,
        )

        object.save()

    return render(request, "cvgenerate/accept.html")


def resume(request, id):
    val = data.objects.get(pk=id)
    template = loader.get_template("cvgenerate/resume.html")
    html = template.render({"user": val})

    options = {
        "page-size": "Letter",
        "encoding": "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachment"
    filename = "resume.pdf"

    return response


def list(request):
    val = data.objects.all()
    return render(request, "cvgenerate/list.html", {"users": val})
