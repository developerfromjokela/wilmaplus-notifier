# Wilma Plus Notifier
Django-powered notifier backend listens when the app will request a notification check, which will get saved and current exams, lesson notes and announcements, and compare them. If new one, perhaps deleted or exam got its grade, push notification will be sent back to the client

# REST API

(Check the Wiki for more detailed guide)
Endpoints:

*POST* `/api/v1/push` - Check for new items to push
