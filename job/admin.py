from django.contrib import admin
from .models import Job, JobQuestion, JobInvite, Proposal, JobRating


admin.site.register(Job)
admin.site.register(JobQuestion)
admin.site.register(JobInvite)
admin.site.register(Proposal)
admin.site.register(JobRating)
