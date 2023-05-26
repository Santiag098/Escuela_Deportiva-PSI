from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',views.inicio),
    path('',views.landing, name='Home'),
    path('projects/',views.listProjects, name='projects.list'),
    path('pay/',views.pay_list, name='pay_list'),
    path('projects-create/',views.showFormCreateProject, name='projects.create'),
    path('projects-store/',views.storeProject, name='projects.store'),
    path('projects-edit/<int:project_id>',views.showFormEditProject, name ='projects.edit'),
    path('projects-update/<int:project_id>',views.updateProject, name ='projects.update'),
    path('projects-delete/<int:project_id>',views.showConfirmDelete, name='projects.delete'),
    path('projescts-destroy/<int:project_id>',views.destroyProject, name='projects.destroy'),
    path('projescts-detail/<int:project_id>',views.detailOfProject,name='projects.detail'),
    path('pay/',views.pay, name="pay.list"),
    path('pay-create/',views.showCreatePayForm, name="pay.create"),
    path('pay-store/',views.storePay, name="pay.store"),
    path('pay-edit/<int:pay_id>/',views.showUpdatePayForm, name="pay.edit"),
    path('pay-update/<int:pay_id>/',views.updatePay, name="pay.update"),
    path('pay-delete/<int:pay_id>/',views.confirmDeletePay, name="pay.delete"),
    path('pay-destroy/<int:pay_id>/',views.destroyPay, name="pay.destroy"),
    path('signup-form/',views.showSignupForm, name='signup-form'),
    path('signup/',views.signup, name='signup'),
    path('login-form/',views.showLoginForm, name='login-form'),
    path('start-session',views.startSession, name='start'),
    path('logout/',views.finishSession, name='logout')
]