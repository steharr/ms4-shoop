let context = jQuery.parseJSON($('#homepage-sales-banner-context').text());
let theme = context.theme;

switch(theme){
    case 'U':
        $('#homepage-sales-banner-container').addClass('urgent');
        break;
    case 'M':
        $('#homepage-sales-banner-container').addClass('moderate');
        break;
    case 'L':
        $('#homepage-sales-banner-container').addClass('reminder');
        break;
}