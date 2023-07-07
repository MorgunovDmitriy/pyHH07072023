from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Vacancy,Company
from .forms import VacancyForm, VacancyEditForm,CompanyForm,CompanyEditForm

# Create your views here.
def homepage(request):
    return render(request=request, template_name="index.html")

def about(request):
    return HttpResponse('Найдите работу или работника мечты!')

def contact_view(request):
    return HttpResponse('''
        <div>
            Phone: +3874628734 <br>
            Email: kaium@gmail.com
        </div>
    ''')

def address(request):
    return HttpResponse('''
        <ul>
            <li>г. Бишкек, 7 м-н, 26/1</li>
            <li>г. Ош, Черёмушка, дом 235</li>
        </ul>
    ''')
def company_add_django_form(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_company = form.save()
            return redirect(f'/companys/')
    company_form = CompanyForm()
    return render(
        request,
        'company/company_django_form.html',
        {"company_form": company_form}
    )

def company_edit_df(request, id):
    company_object = Company.objects.get(id=id)

    if request.method == "GET":
        form = CompanyEditForm(instance=company_object)
        return render(request, "company/company_edit.html", {"form": form})

    elif request.method == "POST":
        form = CompanyEditForm(data=request.POST, instance=company_object)
        if form.is_valid():
            obj = form.save()
            return redirect(company, id=obj.id)
        else:
            return HttpResponse("Форма не валидна")

def company(request):
    companys = Company.objects.all() #SElect в Django ORM
    context={"companys":companys}
    return render(request, 'company/companys.html',context)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()  # в Django ORM "SELECT * FROM Vacancies"
    context = {"vacancies": vacancies}  # context data для jinja2
    context["example"] = "hello"
    return render(request, 'vacancies.html', context)


def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)  # 1
    candidates = vacancy_object.candidate.all()  # list
    context = {
        'vacancy': vacancy_object,
        'candidates_list': candidates,
    }
    return render(request, 'vacancy/vacancy_page.html', context)


def search(request):
    word = request.GET["keyword"]
    vacancy_list = Vacancy.objects.filter(title__contains=word)
    context = {"vacancies": vacancy_list}
    return render(request, 'vacancies.html', context)

def reg_view(request):
    if request.method == "POST":
        user = User(
            username=request.POST["username"]
        )
        user.save()
        user.set_password(request.POST["password"])
        user.save()
        return HttpResponse("Готово")

    return render(
        request,
        "auth/registr.html"
    )


def vacancy_add(request):
    if request.method == "POST":
        new_vacancy = Vacancy(
            title=request.POST["title"],
            salary=int(request.POST["salary"]),
            description=request.POST["description"],
            email=request.POST["email"],
            contacts=request.POST["contacts"],
        )
        new_vacancy.save()
        return redirect(f'/vacancy/{new_vacancy.id}/')
    return render(request, 'vacancy/vacancy_form.html')

def vacancy_add_via_django_form(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')
    vacancy_form = VacancyForm()
    return render(
        request,
        'vacancy/vacancy_django_form.html',
        {"vacancy_form": vacancy_form}
    )

def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == "POST":
        vacancy.title = request.POST["title"]
        vacancy.salary = int(request.POST["salary"])
        vacancy.description = request.POST["description"]
        vacancy.email = request.POST["email"]
        vacancy.contacts = request.POST["contacts"]
        vacancy.save()
        return redirect(f'/vacancy/{vacancy.id}/')
    return render(
        request, 'vacancy/vacancy_edit_form.html',
        {"vacancy": vacancy}
    )

def vacancy_edit_df(request, id):
    resume_object = Vacancy.objects.get(id=id)

    if request.method == "GET":
        form = VacancyEditForm(instance=resume_object)
        return render(request, "vacancy/vacancy_edit_form_df.html", {"form": form})

    elif request.method == "POST":
        form = VacancyEditForm(data=request.POST, instance=resume_object)
        if form.is_valid():
            obj = form.save()
            return redirect(vacancy_detail, id=obj.id)
        else:
            return HttpResponse("Форма не валидна")