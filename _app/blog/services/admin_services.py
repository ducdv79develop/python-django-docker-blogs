from django.contrib import admin


class PostStatusFilter(admin.SimpleListFilter):
    parameter_name = 'is_status'
    title = 'Filter status'
    STATUS1, STATUS2, STATUS3 = 1, 2, 3

    def lookups(self, request, model_admin):
        return (
            (self.STATUS1, 'status 1'),
            (self.STATUS2, 'status 2'),
            (self.STATUS3, 'status 3'),
        )

    def queryset(self, request, queryset):
        if self.value() == self.STATUS1 or self.value() == self.STATUS2 or self.value() == self.STATUS3:
            print('ahahaha')
            return queryset.filter(status=self.value())

        return queryset

