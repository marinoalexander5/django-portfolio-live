const bgVideo = document.getElementById("bg-video");
const btnPlay = document.getElementById("btn-play");
const btnPause = document.getElementById("btn-pause");

const videos = ["coral_reef", "forest", "road", "bird"]; 
const radioBtns =  document.getElementsByName("btnradio");

const preloader = document.querySelector(".preloader");

// Play and Pause
btnPause.addEventListener("click", function() {
    bgVideo.pause();
});

btnPlay.addEventListener("click", function() {
    bgVideo.play();
});

// Video switch
radioBtns.forEach((btn) => {
    btn.addEventListener("change", changeVideo);
});

function changeVideo() {
    for (let i = 0; i < radioBtns.length; i++) {
        if (radioBtns[i].checked) {
            bgVideo.pause();
            document.getElementsByTagName("source")[0].src = "/static/jsprojects/videos/" + videos[i] + ".mp4";     
            bgVideo.load();
            bgVideo.play();
        }    
    }
}

// Preloader
bgVideo.addEventListener("loadstart", function(){
    preloader.classList.remove("hide");
})

bgVideo.addEventListener("loadeddata", function(){
    preloader.classList.add("hide");
})


