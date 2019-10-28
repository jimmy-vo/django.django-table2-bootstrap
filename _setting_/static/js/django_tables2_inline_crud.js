class CrudTable {
    constructor(json_config, url_delete, url_update) {
        this.json_config = json_config;
        this.url_delete = url_delete;
        this.url_update = url_update;

        this.delete = (id, target) => {
            $.ajax({
                url: this.url_delete,
                data: {
                    "id": id
                },
                dataType: "json",
                success: function (data) {
                    if (data.result) {
                        let $parent = $(target).parent().parent();
                        $parent.hide('slow', function () {
                            $parent.remove();
                        });
                    } else {
                        alert("cannot delete row " + id + " .");
                    }
                }
            });
        };

        this.edit = (id, target) => {
            let $parent = $(target).parent().parent();
            let tds = $parent.find("td");

            if ($(target).text() === "Edit") {
                for (let key in this.json_config)
                    if (this.json_config[key]["editable"] === true)
                        if (this.json_config[key]["type"] === "input") {
                            let text = $(tds[this.json_config[key]["order"]]).text();
                            $(tds[this.json_config[key]["order"]]).html("<input value=\"" + text + "\"/>");
                        } else if (this.json_config[key]["type"] === "select") {
                            let removal = this.json_config[key]["href"];
                            let text = $($(tds[this.json_config[key]["order"]]).find('a')[0]).attr('href').replace(removal, '');
                            text = text.substring(0, text.length - 1);
                            $(tds[this.json_config[key]["order"]]).html($(this.json_config[key]["object"]).clone());
                            $($(tds[this.json_config[key]["order"]]).find('select')[0]).val(text);
                        }
                $(target).text("Save");
            } else {
                let input_data = {"id": id};
                for (let key in this.json_config)
                    if (this.json_config[key]["editable"] === true)
                        if (this.json_config[key]["type"] !== "none")
                            input_data[key] = $($(tds[this.json_config[key]["order"]]).find(
                                this.json_config[key]["type"])[0]).val();
                let config = this.json_config;

                $.ajax({
                    url: this.url_update,
                    data: input_data,
                    dataType: "json",
                    success: function (data) {
                        if (data['result'] === true) {
                            data = data['data'];
                            let tds = $parent.find("td");
                            for (let key in config)
                                if (config[key]["editable"] === true)
                                    if (config[key]["type"] === "input")
                                        $(tds[config[key]["order"]]).html(data[key]);
                                    else if (config[key]["type"] === "select") {
                                        let href = config[key]["href"];
                                        let label = $(config[key]["object"]).find('option[value="' + data[key] + '"]').html();
                                        $(tds[config[key]["order"]]).html("<a href=\'" + href + data[key] + "\'/></a>");
                                        $(tds[config[key]["order"]]).find('a').html(label)
                                    }
                        } else {
                            alert(data['result'])
                        }
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ": " + errorThrown)
                    }
                });
                $(target).text("Edit");
            }
        };

        this.create = (id, target) => {
            // collect fields from the created row on the table
            // and send the information back to the server via ajax
        };

        this.add = (id, target) => {
            // add new row on the table
            // assign this.create function to the save button of that row
        }
    }
}

