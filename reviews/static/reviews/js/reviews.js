
$('#id_rating').on('change', function(){

    // get the current rating
    let selectedRating = this.value;

    // empty all child elements
    $('#review-stars').empty();

    // add new elemnts reflecting the selected score
    for (let i=0; i<5; i++){
        if(i < selectedRating){
            $('#review-stars').append('<div class="pt-3"><i class="fas fa-star golden-star"></i></div>');
        }else{
            $('#review-stars').append('<div class="pt-3"><i class="far fa-star"></i></div>');
        };
    }
});