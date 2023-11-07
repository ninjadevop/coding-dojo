var clip = document.querySelector(".video")

clip.addEventListener("mouseover", function (e) {
    clip.play();
})

clip.addEventListener("mouseout", function (e) {
    clip.pause();
})