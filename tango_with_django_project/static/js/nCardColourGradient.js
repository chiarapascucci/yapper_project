
/**
 * Javascript to apply a colour accorss multiple UI elements from white -> target colour. 
 * The effect is a colour gradient accross multiple sequential elements.
 * 
 * Class hardcoded for now
 */

// Get elements and number of elements
var numCards = document.getElementsByClassName("card flex-md-row mb-4 box-shadow h-md-250").length;
var cards = document.getElementsByClassName("card flex-md-row mb-4 box-shadow h-md-250");

// Set target colour (alice blue here so white -> aliceblue)
var t_r = 240
var t_g = 248
var t_b = 255

// Call function to apply colours
applyGradientOnCards(t_r, t_g, t_b, numCards, cards)

function applyGradientOnCards(t_r, t_g, t_b, numCards, cards) {

    // Starting from white always (will always need to decrement too)
    var r = 255;
    var g = 255;
    var b = 255;

    // Get decrement values
    dr = (r - t_r) / numCards;
    dg = (g - t_g) / numCards;
    db = (b - t_b) / numCards;

    var i;
    for (i = 0; i < numCards; i++) {

        // Set background colour from white to a solid colour
        cards[i].style.backgroundColor = "rgb(" + r + "," + g + "," + b + ")";

        // Decrement the rgb values to step towards target colour
        r = r - dr;
        g = g - dg;
        b = b - db;
    }
}   