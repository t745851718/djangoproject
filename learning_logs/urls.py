"""定义learning_logs的url模式"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path(r'', views.index, name='index'),

    # 显示所有的主题
    path(r'topics/', views.topics, name='topics'),

    # 特定主题的详细页面
    path(r'topics/<topic_id>/', views.topic, name='topic'),

    # 用于添加新主题的网页
    path(r'new_topic/', views.new_topic, name='new_topic'),

    # 用于添加新条目的网页
    path(r'new_entry/<topic_id>/', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    path(r'edit_entry/<entry_id>/', views.edit_entry, name='edit_entry')
]
