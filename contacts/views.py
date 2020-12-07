from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response


class ContactCreateView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = request.data

        send_mail(
            data['subject'],

                    'Name: ' +  data['name']
            + '\n' +'Email: ' + data['email']
            + '\n' + 'Message:'
            + '\n' +            data['message'],

            'bobsmith228322@yandex.ru',
            fail_silently=False,
            recipient_list=['bobsmith228322@yandex.ru']
            )

        contact = Contact(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
        contact.save()
        return Response({'success': 'Message sent successfully'})

