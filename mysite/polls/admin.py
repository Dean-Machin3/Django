from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import Question, Choice

#display choices
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #display the question fields in a particular order
    #with date collapsed initally
    fieldsets = [
        (None,               {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    #display an option to create choices when creating questions
    inlines = [ChoiceInline]

    #change the way quesions are listed in the admin screen
    list_display = ('question_text','pub_date', 'was_published_recently' )

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
