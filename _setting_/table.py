import django_tables2 as tables


update_button = tables.TemplateColumn(
    "<button type='button' class='btn' onclick='(function(e){ajax.edit({{record.id}}, $(e.target));})(event)'>" \
    "Edit" \
    "</button>",
    verbose_name=""
)

delete_button = tables.TemplateColumn(
    "<button type='button' class='btn' onclick='(function(e){ajax.delete({{record.id}}, $(e.target));})(event)'>" \
    "Delete" \
    "</button>",
    verbose_name=""
)


class CrudTable(tables.Table):
    update = update_button
    delete = delete_button

    class Meta:
        model = None
        template_name = "django_tables2/bootstrap.html"
        sequence = ['id', 'name', 'symbol']
