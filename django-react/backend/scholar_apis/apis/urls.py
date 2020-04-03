from django.urls import path

from . import views

urlpatterns = [
    # all author-specific api paths
    path('authors/all', views.AllAuthors),
    path('authors/id=<int:ID>', views.AuthorsById),
    path('authors/name=<str:name>', views.AuthorsByName),
    path('authors/name=<str:name>/affiliation=<str:affiliation>', views.AuthorsByNameAffiliation),
    # all article specfic api paths
    path('articles/all', views.AllArticles),
    path('articles/id=<int:ID>', views.ArticlesById),
    path('articles/name=<str:name>', views.ArticlesByName),
    path('articles/name=<str:name>/affiliation=<str:affiliation>', views.ArticlesByNameAffiliation),
    path('articles/journal=<str:journal>', views.ArticlesByJournal),
    # create author, article
    path('authors/add', views.AddAuthor),
    path('articles/add', views.AddArticle),
    # update article
    path('articles/update', views.UpdateArticle),
    #@TODO: update author necessary?

    # delete article, author
    path('authors/delete', views.DeleteAuthor),
    path('articles/delete', views.DeleteArticle),

    # get all the article info for a certain topic
    path('topics/topic=<str:topic>',views.TopicDetailByName),

]

