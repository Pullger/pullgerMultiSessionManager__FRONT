from django.shortcuts import render
from pullgerMultisessionManager_FRONT import tt


def about(request):

    tt.test()

    # manager

    # listJobs = reglament_app.scheduler.get_jobs()
    # return http.HttpResponse('about')
    return render(request, 'about.html')