from django.urls import path

# from simple_ajax_app.single_views.userSignUpView import UserSignUpView
# from simple_ajax_app.single_views.validateUsernameView import ValidateUsernameView
from simple_ajax_app.views import UserSignUpView, ValidateUsernameView

urlpatterns = [
    path('simpleAjaxV3/', UserSignUpView.as_view(), name='simple_ajax'),
    path('ajaxV3/validate-username/', ValidateUsernameView.as_view(), name='simple_ajax_validate')
]
