$(
    function () {
        $('#search').keyup(function () {
            $.ajax({
                type: "POST",
                url: "/all/search/",
                data: {
                    'search_text': $('#search').val(),
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
                },
                success: searchSucess,
                dataType: 'html'
            })

        });


    }
);

function searchSucess(data, textStatus, jqXHR) {
    $('#search-results').html(data);
}
