from django.urls import path
from blog_app import views
urlpatterns = [
   path("",views.post_list,name="post_list"),
   path("detail/<int:pk>/",views.post_detail, name="post_detail"),
   path("draft/",views.draft_list,name="draft_list"),
   path("draft-detail/<int:pk>/", views.draft_detail,name="draft_detail"),
   path("draft-publish/<int:pk>/", views.draft_publish,name="draft_publish"),
   path("podt_create/",views.post_create,name="post_create"),
   path("post_update/<int:pk>/", views.post_update,name="post_update"),
   path("post_delete/<int:pk>/", views.post_delete,name="post_delete"),
  
]