
$('#id_message').on('change', function(){
    let chosenMessage = this.value;
    $('#banner-message').html(chosenMessage);
});
$('#id_discount').on('change', function(){
    let chosenDiscount = this.value;
    $('#banner-discount').html(chosenDiscount);
});
$('#id_price_threshold').on('change', function(){
    let chosenThreshold = this.value;
    $('#banner-threshold').html(chosenThreshold);
});
$('#id_theme').on('change', function(){
    $('#banner').removeClass();
    let chosenTheme = this.value;
    switch (chosenTheme){
        case 'U':
            $('#banner').addClass('urgent');
            break;
        case 'M':
            $('#banner').addClass('moderate');
            break;
        case 'L':
            $('#banner').addClass('reminder');
            break;
    }
});
