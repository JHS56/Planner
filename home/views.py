from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Plan, Object
from .forms import Writing, Checking, GoalForm, Time

def user_is_plan_owner(view_func):
    def _wrapped_view(request, *args, **kwrags):
        plan_id = kwrags.get('plan_id')
        if plan_id:
            plan = get_object_or_404(Plan, id=plan_id)
            if plan.user != request.user:
                return HttpResponseForbidden("권한이 없습니다.")
        return view_func(request, *args, **kwrags)
    
    return _wrapped_view

def user_is_object_owner(view_func):
    def _wrapped_view(request, *args, **kwrags):
        object_id = kwrags.get('object_id')
        if object_id:
            object = get_object_or_404(Object, id=object_id)
            if object.user != request.user:
                return HttpResponseForbidden("권한이 없습니다.")
        return view_func(request, *args, **kwrags)
    
    return _wrapped_view


def home(request):
    planner = Plan.objects.filter(user=request.user).order_by("-title")[:10]
    object = Object.objects.filter(user=request.user).first()
    context = {
        "planner" : planner,
        "object" : object,
    }

    return render(request, "home/home.html", context)

@login_required
@user_is_plan_owner
def detail(request, plan_id):
    prefixes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2]
    suffixes = range(1,7)
    plan = get_object_or_404(Plan, id=plan_id)


    if request.method == 'POST':
        checking_form = Checking(request.POST, instance=plan)
        time_form = Time(request.POST)

        if checking_form.is_valid() and time_form.is_valid():
            checking_form.save()
            for prefix in prefixes:
                for suffix in range(1,7):
                    field_name = f"t{prefix}_{suffix}"
                    if field_name in time_form.cleaned_data:
                        setattr(plan, field_name, time_form.cleaned_data[field_name])
            plan.save()
            
            return redirect('home')
    else:
        checking_form = Checking(instance=plan)
        time_form = Time(instance=plan)
    return render(request,"home/detail.html", {
        "plan" : plan,
        "checking_form": checking_form,
        "time_form": time_form,
        "prefixes": prefixes,
        "suffixes" : suffixes,})


# def edit(request):
#     return render(request, "home/edit.html")


def create(request):
    if request.method == 'POST' :
        form = Writing(request.POST)

        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect("home")
        
    else:
        form = Writing()
        
    return render(request, 'home/form.html', {'form':form})

@login_required
@user_is_plan_owner
def edit(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST' :
        form = Writing(request.POST, instance=plan)


        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
        form = Writing(instance=plan)
        
    return render(request, 'home/form.html', {'form': form})


@login_required
@user_is_plan_owner
def delete(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)


    if request.method == 'POST' :
        plan.delete()
        return redirect('home')
    return render(request, 'home/delete.html', {'plan' : plan})


def goal(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect('home')
        
    else:
        form = GoalForm()   
    
    return render(request, 'goal/create.html', {'form' : form})

@login_required
@user_is_object_owner
def edit_goal(request, object_id):
    object = get_object_or_404(Object, id=object_id)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = GoalForm(instance=object)

    return render(request, 'goal/edit.html', {'form' : form})