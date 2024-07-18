// Update the count down every 1 second
var x = setInterval(function() {
    // Get all appointment datetime elements
    var datetimeElements = document.querySelectorAll('input[id^="appointment-datetime-"]');
    
    datetimeElements.forEach(function(element) {
        var index = element.id.split('-')[2];
        var dateTimeStr = element.value;
        var countDownDate = new Date(dateTimeStr).getTime();

        // Get today's date and time
        var now = new Date().getTime();
        
        // Find the distance between now and the count down date
        var distance = countDownDate - now;
        
        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        // Output the result in an element with id="demo-[index]"
        var demoElement = document.getElementById("demo-" + index);
        if (demoElement) {
            demoElement.innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
            
            // If the count down is over, write some text 
            if (distance < 0) {
                clearInterval(x);
                demoElement.innerHTML = "EXPIRED";
            }
        }
    });
}, 1000);
