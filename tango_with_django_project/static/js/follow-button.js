$(document).ready(function() {

    // Breed follow button
    $('#fllw_btnb').click(function() {
        var breedIdVar;
        breedIdVar = $(this).attr('data-breedid');

        $.get('/rango/follow_breed/',
            {'breed_id': breedIdVar},
            function(data) {    
                $('#follow_countb').html(data);
                $('#fllw_btnb').hide();
            })     
    });

    // Dog follow button
    $('#fllw_btnd').click(function() {
        var dogIdVar;
        dogIdVar = $(this).attr('data-dogid');

        $.get('/rango/follow_dog/',
            {'dog_id': dogIdVar},
            function(data) {    
                $('#follow_countd').html(data);
                $('#fllw_btnd').hide();
            })     
    });

    // Sport follow button
    $('#fllw_btns').click(function() {
        var sportIdVar;
        sportIdVar = $(this).attr('data-sportid');

        $.get('/rango/follow_sport/',
            {'sport_id': sportIdVar},
            function(data) {    
                $('#follow_counts').html(data);
                $('#fllw_btns').hide();
            })     
    });

});