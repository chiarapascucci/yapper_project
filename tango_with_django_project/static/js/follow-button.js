$(document).ready(function() {

    $('#fllw_btn').click(function() {
        var breedIdVar;
        breedIdVar = $(this).attr('data-breedid');

        $.get('/rango/follow_breed/',
            {'breed_id': breedIdVar},
            function(data) {    
                $('#follow_count').html(data);
                $('#fllw_btn').hide();
                $('#fllw_btn').disabled = true;
            })
            
    });
});