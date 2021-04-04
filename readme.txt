referance link:
https://studygyaan.com/django/how-to-add-social-login-to-django

//Installation of Django Social Auth App ( social-auth-app-django )

    >>pip install social-auth-app-django

//Change to settings.py file
    INSTALLED_APPS = [
        ..............
        'social_django',  # <-- Here social-auth-app-django
    ]

// run command
    >>python manage.py migrate
//Add settigs.py file
    MIDDLEWARE_CLASSES = [
        ...................
        
        'social_django.middleware.SocialAuthExceptionMiddleware',  # <-- Here
    ]

    'context_processors': [
        'django.template.context_processors.debug',
        
        'social_django.context_processors.backends',  # <-- Here
        'social_django.context_processors.login_redirect', # <-- Here
    ],

//Add all code to settns.py file
    AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    )

// Add code into main urls.py 
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here

SOCIAL_AUTH_FACEBOOK_KEY = '985292215170699'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '7b8483ff422109a7c17b3f7a03966bbf'  # App Secret

// go to facebook site and  create appID and App Secret ID
https://developers.facebook.com/

    >>MyApps >> add app name and create appID
    >>Sttings >>Basic
    >>apps Domains "Localhost" // add platform click select website
    >>site url "http://localhost:8000/" // Savechanges click go back
    
//Add to code in login.html
     <p><strong>-- OR --</strong></p>
    <a href="{% url 'social:begin' 'facebook' %}">Login with Facebook</a>






