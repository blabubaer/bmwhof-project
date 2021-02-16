from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.forms import forms, modelformset_factory
from .models import Image, Blog
from .forms import ImageForm, BlogForm

def add_blog(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

    if request.method == 'GET':
        blog_form = BlogForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'blog/addblog.html', {"blog_form":blog_form, "formset":formset})
    elif request.method == "POST":
        blog_form = BlogForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)

        if blog_form.is_valid() and formset.is_valid():
            blog_obj = blog_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    Image.objects.create(image=image, blog=blog_obj)
                return redirect('home')
        else:
            print(blog_form.errors, formset.errors)

def blog_view(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog/blog_view.html', {"blog":blog})
