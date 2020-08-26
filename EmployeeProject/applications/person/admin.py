from django.contrib import admin

from  .models import Employee, Skills


admin.site.register(Skills)

class EmployeeAdmin(admin.ModelAdmin):
    list_display= (
        'first_name',
        'last_name',
        'department',
        'job',
        'full_name',
        'id',
    )

    def full_name(self,obj):
        # obj nos muestra cada registro que se esta listando o iterando en nuestro admin de django
        print(obj.first_name , obj.last_name)
        return obj.first_name + ' ' +  obj.last_name


    search_fields= ('first_name',)
    list_filter=('department','job','skills',)
    #
    filter_horizontal= ('skills',)

admin.site.register(Employee, EmployeeAdmin)