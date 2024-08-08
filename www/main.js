$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceInLeft",
        },
        out: {
            effect: "bounceOutRight",
        },

    });
    // Siri Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        frequency: 4,
        amplitude: "1",
        speed: "0.250",
        autostart: true
      });

      //siri message animation
      $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true
        },
        out: {
            effect: "fadeOutUp",
            sync:true
        },

    });

    // Mic Button Script
    $("#MicBtn").click(function (e) { 
        eel.playAssistantSound1()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
    });
});