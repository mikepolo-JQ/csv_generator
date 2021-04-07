
$(document).ready(function (){

    $("#submit_but").on("click", function (e){
        let name = $("#id_schema_name").val();
        let sep = $("#id_column_sep").val();
        let character = $("#id_character").val();

        let data = {};
        data['name'] = name;
        data['sep'] = sep;
        data['char'] = character;


        let child = $("#columns").children();

        let columnName = "";
        let columnType = "";
        let columnFrom = 0;
        let columnTo = 0;
        let columnOrder = 0;
        let columns = [];

        for(let i = 0; i < child.length; ++i){
            columnName = child[i].querySelector(".column__info input").value;
            columnType = child[i].querySelector(".column__info select").value;
            columnFrom = child[i].querySelector("#input_from").value;
            columnTo = child[i].querySelector("#input_to").value;
            columnOrder = child[i].querySelector("#order_input").value;
            let column = {};

            column["name"] = columnName;
            column["type"] = columnType;
            column["order"] = columnOrder;
            if(columnType==="int"){
                column["from"] = columnFrom;
                column["to"] = columnTo;
            }
            columns.push(column);

        }

        data['columns'] = columns;
        let json = JSON.stringify(data);
        console.log(json);

        let xhr = new XMLHttpRequest();
        let url = "/g/s/";
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(json);
        xhr.onreadystatechange = function () {
            if (xhr.status === 200) {
                location.href = "/";
            }
        };


    });

    let i = 1;
    $("#add_column_button").on("click", function (e){
        e.preventDefault();

        let selTypeVal = document.getElementById("select_" + i).value;
        let columnName = document.getElementById("column_name_input_"+i).value;
        let fromVal = document.getElementById("range_from_" + i).lastElementChild.value || 1;
        let toVal = document.getElementById("range_to_" + i).lastElementChild.value || 100;

        console.log(fromVal + " = " + toVal);


        let newСolumn =
           " <article class=\"wrapper\">" +
                "<article class=\"wrapper_column\">"+
                    "<label for=\"column_name_input_"+i+"\">Column name</label>" +

                    "<article class=\"column__info ready_column\">" +
                        "<input id=\"column_name_input_" + i + "\" type=\"text\" name=\"column_name\" value='" + columnName + "'>" +
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
                    "<input id=\"input_from\" type=\"number\" min=\"1\" max=\"100\" value='" + fromVal + "'>" +
                "</span>" +
                "<span id='range_to_" + i + "' class=\"int_range\">" +
                    "<label for=\"input_to\">To</label>" +
                    "<input id=\"input_to\" type=\"number\" min=\"1\" max=\"100\" value='" + toVal + "'>" +
                "</span>"+

                "<article class='int_range active_grid'>" +
                    "<lable for='order_input'>Order</lable>" +
                    "<input id='order_input' class='order_input' type='number' min='1' max='1' value='"+ i +"'>" +
                "</article>" +

                "<article id='delete_" + i + "' onclick='deleteColumn(this);' class='delete_but'>Delete</article>"

        i += 1;
        document.getElementById("select_" + (i-1)).id = "select_" + i;
        document.getElementById("range_from_" + (i-1)).id = "range_from_" + i;
        document.getElementById("range_to_" + (i-1)).id = "range_to_" + i;
        document.getElementById("column_name_input_" + (i-1)).id = "column_name_input_" + i;

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

        intRangeOpen();

        setActiveGrid((i-1), selTypeVal)
        document.getElementById("select_"+ (i - 1)).value = selTypeVal;

        smoothScroll();

    })
})

let setActiveGrid = function (id, data){

    let rangeFrom = document.getElementById("range_from_" + id);
    let rangeTo = document.getElementById("range_to_" + id);

    if(data === "int"){
        rangeFrom.classList.add("active_grid");
        rangeTo.classList.add("active_grid");
    }else{
        rangeFrom.classList.remove("active_grid") || console.log();
        rangeTo.classList.remove("active_grid") || console.log();
    }
}

let deleteColumn = function (elem){
    let re = /\d+/g;
    let str = elem.id;
    let id = parseInt(str.match(re)[0]);

    let columns = document.querySelector("#columns");
    let columnToDel = document.getElementById("column_" + id)
    columns.removeChild(columnToDel);
}

let intRangeOpen = function (){
    $('select.sel').change(function(e){

        let data= $(this).val();

        let re = /\d+/g;
        let str = this.id;
        let id = str.match(re);

        setActiveGrid(id, data);
    });
}

let smoothScroll = function (){
    let top = $("#add_column_button").offset().top;
    $("html, body").animate({
        scrollTop: top
    }, 1000)
}

intRangeOpen();
