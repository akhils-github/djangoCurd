from django.shortcuts import get_object_or_404, render, redirect
from .models import Data

# from .forms import detailsform
from django.contrib import messages


# Create your views here.
def retrieve(request):
    data = Data.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        si_no = request.POST.get("SINO")
        detail = Data(name=name, desc=desc, SINO=si_no)
        detail.save()
        messages.info(request, "Data added successfully")
    context = {"data_list": data}

    return render(request, "retrieve.html", context)


# def create(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         desc = request.POST.get("desc")
#         si_no = request.POST.get("SINO")
#         detail = Data(name=name, desc=desc, SINO=si_no)
#         detail.save()
#     return render(request, "retrieve.html")


def update(request, id):
    data = get_object_or_404(Data, id=id)

    # data = Data.objects.get(id=id)
    # form = detailsform(request.POST or None, request.FILES, instance=data)
    # if data.is_valid():
    #     name = request.POST.get("name")
    #     desc = request.POST.get("desc")
    #     si_no = request.POST.get("SINO")
    #     data = Data(name=name, desc=desc, SINO=si_no)
    #     data.save()
    if request.method == "POST":
        if (
            request.POST.get("name")
            and request.POST.get("desc")
            and request.POST.get("SINO")
        ):
            Data.objects.filter(id=id).update(
                name=request.POST.get("name"),
                desc=request.POST.get("desc"),
                SINO=request.POST.get("SINO"),
            )
        return redirect("/")
    messages.success(request, "The item was successfully updated")
    return render(request, "update.html", {"data": data})


def delete(request, id):
    if request.method == "POST":
        data = Data.objects.get(id=id)
        data.delete()
        return redirect("/")
    return render(request, "delete.html")


# ef editpost(request, id):
#         postobj= get_object_or_404(Post, id=id)

#         if request.method == 'POST':
#             if request.POST.get('title') and request.POST.get('content'):
#                 Post.objects.filter(id = id).update(title= request.POST.get('title'), content= request.POST.get('content'))

# 		messages.success(request, "The post was successfully updated")

#                 context={'postobj': postobj}


#                 return render(request, 'posts/edit.html')


#         else:
#                 context={'postobj': postobj,
# 			 'error': 'The post was not successfully updated. The title and content must be filled out.'}
#                 return render(request,'posts/edit.html', context)
