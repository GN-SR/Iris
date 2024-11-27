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
        width: window.innerWidth * 0.8,
        height: 200,
        style: "ios9",
        frequency: 4,
        amplitude: 2,
        speed: 0.2,
        autostart: true,
        color: '#BB86FC',
    });


      //siri message animation
      $('.siri-message').textillate({
        loop: true,
        in: {
            effect: "fadeInUp",
            delayScale: 1.5,
            delay: 30,
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            delayScale: 1.5,
            delay: 30,
            sync: true,
        },
    });


    // Mic Button Script
    $("#MicBtn").click(function (e) { 
        eel.playAssistantSound1()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });
});