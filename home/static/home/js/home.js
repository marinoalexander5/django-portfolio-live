//Carousel
$(document).ready(function(){
    $("#myCarousel").carousel();
});


// Scroll Top Button
const topButton = document.getElementById("topBtn");

window.onscroll = function() {
    scrollFunction()
}

function scrollFunction() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        console.log(document.documentElement.scrollTop)
        topButton.style.display = "block";
    } else {
        topButton.style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}