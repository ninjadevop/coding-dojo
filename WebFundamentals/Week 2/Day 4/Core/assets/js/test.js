var h1Text = document.getElementById("myH1").textContent;
        var container = document.getElementById("myH1");
        container.textContent = "";
        for (var i = 0; i < h1Text.length; i++) {
    setTimeout(function (i) {
        return function () {
        container.textContent += h1Text[i];
        };
      }(i), i * 350); 
    }