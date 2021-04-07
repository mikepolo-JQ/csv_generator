
$(document).ready(function (){

    let i = 1;
    $("#add_column_button").on("click", function (e){
        e.preventDefault();

        let newСolumn =
           " <article class=\"wrapper\">" +
                "<article class=\"wrapper_column\">"+
                    "<label for=\"column_name_input_\">Column name</label>" +

                    "<article class=\"column__info ready_column\">" +
                        "<input id=\"column_name_input\" type=\"text\" name=\"column_name\" value=\"colname\">" +
                        "<select id='select_" + i + "' class='sel'>"+
                            "<option value=\"\">----</option>" +
                            "<option value=\"name\">Full name</option>" +
                            "<option value=\"int\">Integer</option>" +
                            "<option value=\"company\">Company</option>" +
                            "<option value=\"job\">Job</option>" +
                            "<option value=\"date\">Date</option>" +
                        "</select>" +
                    "</article>"+
                "</article>" +
                "<span id='range_from_" + i + "' class=\"int_range\">" +
                    "<label for=\"input_from\">From</label>" +
                    "<input id=\"input_from\" type=\"number\" min=\"1\" max=\"100\">" +
                "</span>" +
                "<span id='range_to_" + i + "' class=\"int_range\">" +
                    "<label for=\"input_to\">To</label>" +
                    "<input id=\"input_to\" type=\"number\" min=\"1\" max=\"100\">" +
                "</span>"+

                "<article class='int_range active_grid'>" +
                    "<lable for='order_input'>Order</lable>" +
                    "<input id='order_input' class='order_input' type='number' min='1' max='1'>" +
                "</article>" +

                "<article id='delete_" + i + "' onclick='deleteColumn(this);' class='delete_but'>Delete</article>"

        i += 1;
        document.getElementById("select_" + (i-1)).id = "select_" + i;
        document.getElementById("range_from_" + (i-1)).id = "range_from_" + i;
        document.getElementById("range_to_" + (i-1)).id = "range_to_" + i;

        let art = document.createElement("article");
        art.classList = "form_item column";
        art.id = "column_" + (i-1);
        art.innerHTML = newСolumn;
        document.querySelector("#columns").append(art);

        if (i > 1){
            elems = document.getElementsByClassName("order_input");
            for (let j = 0; j < elems.length; ++j){
                elems[j].max = i-1;
            }
        }

        $('select').change(function(e){

            let data= $(this).val();

            let re = /\d+/g;
            let str = this.id;
            let id = str.match(re);
            let rangeFrom = document.getElementById("range_from_" + id);
            let rangeTo = document.getElementById("range_to_" + id);

            if(data === "int"){
                rangeFrom.classList.add("active_grid");
                rangeTo.classList.add("active_grid");
            }else{
                rangeFrom.classList.remove("active_grid");
                rangeTo.classList.remove("active_grid");
            }

        });
    })
})

let deleteColumn = function (elem){
    let re = /\d+/g;
    let str = elem.id;
    let id = parseInt(str.match(re)[0]);

    let columns = document.querySelector("#columns");
    let columnToDel = document.getElementById("column_" + id)
    columns.removeChild(columnToDel);
    console.log(id);
}
