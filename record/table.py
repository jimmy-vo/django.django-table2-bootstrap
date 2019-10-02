import django_tables2 as tables

from .models import Country, Person

delete_script = """
<button type='button' class='btn' id='delete-{{record.id}}' onclick='(function(e){
    $.ajax({
        url: "/ajax_delete/",
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
})(event)'>Delete</button>    
"""

edit_script = """
let tds =  $this.parent().parent().find("td");
$(tds).pop();
tds.each(function(column, td) {
    $(td).text("dsad");

});
"""

update_script = """
<button type='button' class='btn' id='update-{{record.id}}' onclick='(function(e){
    let $this = $("#update-{{record.id}}");
    let $parent = $this.parent().parent();
    let tds =  $parent.find("td");
    if ($this.text() === "Edit") {
        for (let i = 1; i < tds.length - 3; i++){
            let text = $(tds[i]).text();
            $(tds[i]).replaceWith("<td><input value=\\"" + text +  "\\"/></td>");
        }
        $this.text("Save");
    } else {
        let id = $(tds[0]).text();
        let inputs =  $parent.find("input");
        $.ajax({
            url: "/ajax_update/",
            data: {
                "id": id,
                "fullname": $(inputs[0]).val(),
                "height": $(inputs[1]).val(),
            },
            dataType: "json",
            success: function (data) {
                let new_data = [data.id, data.fullname, data.height, data.country]        
                for (let i = 0; i < tds.length - 2; i++){
                    $(tds[i]).replaceWith("<td>" + new_data[i] + "</td>");
                }
            },
            error: function (jqXHR, textStatus, errorThrown) { 
                alert("error occurs.")
            }
        }); 
        $this.text("Edit");
    }
})(event)'>Edit</button>
"""


class PersonTable(tables.Table):
    country = tables.Column(linkify=True)
    update = tables.TemplateColumn(update_script)
    delete = tables.TemplateColumn(delete_script)

    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
