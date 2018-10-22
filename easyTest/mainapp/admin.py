from django.contrib import admin
from .models import Keyword,Question,Answer,TestCategory,Test
# Register your models here.
class KeywordAdmin(admin.ModelAdmin):
    fields = ('title', 'active', 'sort')
admin.site.register(Keyword,KeywordAdmin)

class QuestionAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'keyword', 'active', 'sort')
admin.site.register(Question,QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'question', 'is_correct', 'active', 'sort')
admin.site.register(Answer,AnswerAdmin)

class TestCategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'active', 'sort')
admin.site.register(TestCategory,TestCategoryAdmin)

class TestAdmin(admin.ModelAdmin):
    fields = ('title', 'description','questions',  'category', 'max_questions', 'required_correct_answers', 'active', 'sort')
admin.site.register(Test,TestAdmin)