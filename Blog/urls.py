from django.urls import path,re_path
from django.conf.urls import url
from Blog import views

app_name = "Blog"

urlpatterns = [
    # re_path(r"^test/(?P<pk>\d+)/$", views.test),
    path("About/",views.About.as_view(),name="About_Page"),
    # url(r"^$", views.index,name = "Main_Page"),
    url(r"^post/(?P<pk>\d+)$", views.PostDetailView.as_view(), name = "Post_Detail_Page"),
    url(r"^post/new/$",views.PostCreateView.as_view(), name="Post_Create_Page"),
    url(r"^post/(?P<pk>\d+)/update/$",views.PostUpdateView.as_view(),name="Post_Update_Page"),
    url(r"^post/(?P<pk>\d+)/delete/$",views.PostDeleteView.as_view(),name="Post_Delete_Page"),
    url(r"^draft/$",views.PostDraftView.as_view(),name="Post_Draft_Page"),
    url(r"^post/(?P<pk>\d+)/comment/$",views.app_comment_to_post,name="Comment_Add_Page"),
    url(r"^comment/(?P<pk>\d+)/approve/$",views.Comment_Approve, name = "Comment_Approve_Page"),
    url(r"^comment/(?P<pk>\d+)/delete/$",views.Comment_Remove,name="Comment_Delete_Page"),
    url(r"^post/(?P<pk>\d+)/publish/$",views.Post_Publish, name="Post_Publish_Page"),
    url(r"^$", views.PostListView.as_view(),name = "Post_List_Page"),
    # url(r"^post/(?P<pk>\d+)/like/$",views.Post_Like,name="Like_Post"),
]
