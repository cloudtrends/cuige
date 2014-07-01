from django.contrib import admin


from polls.models import Question

#admin.site.register(Question)

from polls.models import Choice

#admin.site.register(Choice)



#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3




class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'] , 'classes': ['collapse'] }),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)





# Register your models here.
