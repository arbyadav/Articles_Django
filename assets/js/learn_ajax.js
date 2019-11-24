// function loadDoc() {
//     var x
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function () {
//         if (this.readyState == 4 && this.status == 200) {
//             document.getElementById("demo").innerHTML =
//                 this.responseText;
//         }
//     };
//     xhttp.open("GET", "/assets/ajax_info.txt", true);
//     xhttp.send();
// }

$(
    function () {
        $('#demo').onclick(function () {
            $.ajax({
                type: "POST",
                url: "/learn1/",
                data: {
                    'ajax_data': 'AMIT',
                },
                success: loadDoc,
                dataType: 'html'
            })

        });
    }
);

function loadDoc(data, textStatus, jqXHR) {
    $('#fetched_data').html(data);
}

