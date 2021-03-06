"""
Forum urls for the django_comment_client.
"""
from django.conf.urls import patterns, url

from .views import DiscussionBoardFragmentView

urlpatterns = patterns(
    'discussion.views',

    url(r'users/(?P<user_id>\w+)/followed$', 'followed_threads', name='followed_threads'),
    url(r'users/(?P<user_id>\w+)$', 'user_profile', name='user_profile'),
    url(r'^(?P<discussion_id>[\w\-.]+)/threads/(?P<thread_id>\w+)$', 'single_thread', name='single_thread'),
    url(r'^(?P<discussion_id>[\w\-.]+)/inline$', 'inline_discussion', name='inline_discussion'),
    url(
        r'discussion_board_fragment_view$',
        DiscussionBoardFragmentView.as_view(),
        name='discussion_board_fragment_view'
    ),
    url(r'', 'forum_form_discussion', name='forum_form_discussion'),
)
