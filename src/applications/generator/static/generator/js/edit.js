
$(document).ready(

    $("#edit_but").on("click", function (e) {

        let delete_url = document.getElementById('delete_url').className;

        let json = getJSON()

        if(json){
            $.ajax({
                type: "POST",
                url: "/g/s/",
                data: json,
                success: function (data) {
                    $.ajax({
                        type: "POST",
                        url: delete_url,
                        data: "",
                        success: function () {
                            location.replace('/');
                        }
                    });
                }
            });
        }else{
            alert("Please, check the entered data!");
        }
    })
);