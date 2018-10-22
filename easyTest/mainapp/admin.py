from django.contrib import admin
from .models import Keyword,Question,Answer,TestCategory,Test
# Register your models here.
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword_name', 'active', 'sort')
admin.site.register(Keyword,KeywordAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_keys', 'active', 'sort')
admin.site.register(Question,QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'question', 'is_correct', 'active', 'sort')
admin.site.register(Answer,AnswerAdmin)

class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'active', 'sort')
admin.site.register(TestCategory,TestCategoryAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','questions',  'category', 'max_questions', 'required_correct_answers', 'active', 'sort')
admin.site.register(Test,TestAdmin)