from django.contrib import admin
from .models import Question, Choice

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_txt']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_txt']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    # list_display = ['question_txt', 'pub_date']
    list_display = ('question_txt', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)