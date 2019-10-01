import django_tables2 as tables

from .models import Country, Person

delete_script = """
<button type='button' class='btn' id='update-{{record.id}}' onclick='(function(e){
    $.ajax({
        url: "/validate_delete/",
        data: {
            "id": {{record.id}}
        },
        dataType: "json",
        success: function (data) {
            if (data.result) {
                alert("row {{record.id}} was deleted.");
            } else {
                alert("cannot delete row {{record.id}}.");
            }
        }
    }); 
})(event)'>Edit</button>    
"""

update_script = """
<button type='button' class='btn' id='delete-{{record.id}}' onclick='(function(e){
    var $this = $("#update-{{record.id}}");
    if ($this.text() === "Edit") {
        $this.text("Save");
    } else {
        $this.text("Edit");
    }
})(event)'>Remove</button>
"""

class PersonTable(tables.Table):
    country = tables.Column(linkify=True)
    edit = tables.TemplateColumn(update_script)
    delete = tables.TemplateColumn(delete_script)

    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
