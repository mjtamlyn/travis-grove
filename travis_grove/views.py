import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import requests

from .models import Project, User


class Main(TemplateView):
    template_name = 'home.html'

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        print 'Received post request from travis'
        print 'data: %s' % request.body
        data = json.loads(request.body)

        # get project or go away
        try:
            project = Project.objects.get(github_url=data['respository']['url'])
        except Project.DoesNotExist:
            return HttpResponseBadRequest('No project for name {name}'.format(data['respository']['url']))

        print 'project identified as %s' % project

        # set up user
        author_name = data['author_name']
        try:
            user = User.objects.get(name=author_name).grove_nick
        except User.DoesNotExist:
            user = author_name

        # build message
        pass_message = '{user}: Your build on {project} passes!'
        fail_message = '{user}: Your build on {project} FAILED!'
        message = pass_message if data['status_message'] == 'Passed' else fail_message
        message = message.format(**{'user': user, 'project': project.github_url})

        print 'sending message "%s" to grove' % message
        # send message
        requests.post(
                'https://grove.io/api/notice/{0}/'.format(project.token),
                data={
                    'service': 'TravisCI',
                    'message': message,
                    'image_url': 'https://secure.gravatar.com/avatar/eaafec56c36c18928c31d7c5d7126d10',
                }
        )
        print 'all done'
        print 'data: %s' % request.body

        return HttpResponse('ok')
