import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Project, Task


@login_required
def dashboard(request):
    projects = Project.objects.filter(owner=request.user)
    tasks = Task.objects.filter(project__owner=request.user)

    total_projects = projects.count()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='Completed').count()
    pending_tasks = tasks.exclude(status='Completed').count()

    return render(request, 'tasks/dashboard.html', {
        'projects': projects,
        'tasks': tasks,
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks
    })


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'tasks/register.html', {
                'error': 'Passwords do not match.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'tasks/register.html', {
                'error': 'Username already exists.'
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'tasks/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'tasks/login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'tasks/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def create_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        Project.objects.create(
            name=name,
            description=description,
            owner=request.user
        )

        return redirect('projects')

    return render(request, 'tasks/create_project.html')


@login_required
def projects(request):
    projects = Project.objects.filter(
        owner=request.user
    ).order_by('-id')

    return render(request, 'tasks/projects.html', {
        'projects': projects
    })


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(
        Project,
        id=project_id,
        owner=request.user
    )

    if request.method == 'POST':
        project.name = request.POST['name']
        project.description = request.POST['description']
        project.save()

        return redirect('projects')

    return render(request, 'tasks/edit_project.html', {
        'project': project
    })


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(
        Project,
        id=project_id,
        owner=request.user
    )

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'tasks/delete_project.html', {
        'project': project
    })


@login_required
def create_task(request):
    projects = Project.objects.filter(owner=request.user)
    users = User.objects.all()

    if request.method == 'POST':
        project_id = request.POST['project']
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        status = request.POST['status']
        assigned_to = request.POST['assigned_to']

        project = get_object_or_404(
            Project,
            id=project_id,
            owner=request.user
        )

        Task.objects.create(
            project=project,
            title=title,
            description=description,
            due_date=due_date or None,
            status=status,
            assigned_to_id=assigned_to or None
        )

        return redirect('task_list')

    return render(request, 'tasks/create_task.html', {
        'projects': projects,
        'users': users
    })


@login_required
def task_list(request):
    tasks = Task.objects.filter(
        project__owner=request.user
    ).order_by('-id')

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks
    })


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        project__owner=request.user
    )

    projects = Project.objects.filter(owner=request.user)
    users = User.objects.all()

    if request.method == 'POST':
        project_id = request.POST['project']

        project = get_object_or_404(
            Project,
            id=project_id,
            owner=request.user
        )

        task.title = request.POST['title']
        task.description = request.POST['description']
        task.project = project
        task.due_date = request.POST['due_date'] or None
        task.status = request.POST['status']

        assigned_to = request.POST['assigned_to']
        task.assigned_to_id = assigned_to or None

        task.save()

        return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {
        'task': task,
        'projects': projects,
        'users': users
    })


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        project__owner=request.user
    )

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/delete_task.html', {
        'task': task
    })


@login_required
def settings_view(request):
    return render(request, 'tasks/settings.html')


@login_required
def profile(request):

    # User projects
    projects = Project.objects.filter(
        owner=request.user
    )

    # User tasks
    tasks = Task.objects.filter(
        project__owner=request.user
    )

    # Total counts
    total_projects = projects.count()
    total_tasks = tasks.count()

    # Task status counts
    todo_tasks = tasks.filter(
        status='To Do'
    ).count()

    in_progress_tasks = tasks.filter(
        status='In Progress'
    ).count()

    completed_tasks = tasks.filter(
        status='Completed'
    ).count()

    # Project names
    project_names = []

    # Task count for every project
    project_task_counts = []

    for project in projects:

        project_names.append(project.name)

        task_count = Task.objects.filter(
            project=project
        ).count()

        project_task_counts.append(task_count)

    # Convert Python lists into JSON
    # so JavaScript/Chart.js can read them correctly
    project_names_json = json.dumps(project_names)
    project_task_counts_json = json.dumps(project_task_counts)

    return render(
        request,
        'tasks/profile.html',
        {
            'total_projects': total_projects,
            'total_tasks': total_tasks,

            'todo_tasks': todo_tasks,
            'in_progress_tasks': in_progress_tasks,
            'completed_tasks': completed_tasks,

            'project_names': project_names_json,
            'project_task_counts': project_task_counts_json,
        }
    )