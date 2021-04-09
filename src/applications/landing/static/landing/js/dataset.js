
$(document).ready(function () {

    startStatus();

    $("#generate_but").on("click", function (e) {

        let elements = document.getElementsByClassName('status');
        for(let i = 0; i < elements.length; ++i){
            makeProcessing(elements[i])
        }

        let rows = $('#rows_input').val()
        let url ="/g/s/" + rows + "/csv/";

        $.ajax({
           type: "POST",
           url: url,
           data: "",
           success: function(data)
           {
               setInterval(startStatus, 2000);

           }
         });
    })
});

let startStatus = function (){
    let url = document.getElementById('start_url').className

    $.ajax({
       type: "POST",
       url: url,
       data: "",
       success: function(data)
       {
           let pks = data['data']
           for(let i = 0; i < pks.length; ++i){
               let elem = document.getElementById('status_' + pks[i]);
               makeReady(elem);
           }

       }
    });
}

let makeReady = function (elem){
    elem.style.backgroundColor = 'limegreen';
    elem.innerText = "Ready";
}
let makeProcessing = function (elem){
    elem.style.backgroundColor = 'darkgrey';
    elem.innerText = "Processing";
}

