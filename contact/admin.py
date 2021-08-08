from django.contrib import admin

from .models import ContactModel, WebSite, BackgroundContact

admin.site.register(ContactModel)
admin.site.register(WebSite)
admin.site.register(BackgroundContact)

#готово покажи по быстрому все фаллы где писал форму
# создал модельку / затем сделал форму / затем вьюшка ну и вывел в шаблон

