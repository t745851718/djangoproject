from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from .views_functions import check_topic_owner


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    ts = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {
        'topics': ts
    }
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    t = Topic.objects.get(id=topic_id)
    if not check_topic_owner(request, t):
        raise Http404
    entries = t.entry_set.order_by('-date_added')
    context = {
        'topic': t,
        'entries': entries,
        'topic_id': topic_id
    }
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            tp = form.save(commit=False)
            tp.owner = request.user
            tp.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    tp = Topic.objects.get(id=topic_id)
    if not check_topic_owner(request, tp):
        raise Http404
    topic_text = tp.text
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_en = form.save(commit=False)
            new_en.topic = tp
            new_en.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=(topic_id,)))

    context = {
        'form': form,
        'topic_id': topic_id,
        'topic_text': topic_text
    }
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    tp = entry.topic
    if not check_topic_owner(request, tp):
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=(tp.id,)))
    context = {
        'entry': entry,
        'topic': tp,
        'form': form
    }
    return render(request, 'learning_logs/edit_entry.html', context)
