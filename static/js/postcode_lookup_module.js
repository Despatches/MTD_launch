
$( document ).ready(function() {

function change_view(latlng){
map.setView((latlng),14);
};

 $("#show_pc").click(function(){
    $( "#postcode_container" ).toggleClass("hide");
    $( "#hide_postcode" ).toggleClass("hide");
    $( "#show_postcode" ).toggleClass("hide");
});

$("#hide_pc").click(function(){
    $( "#postcode_container" ).toggleClass("hide");
    $( "#hide_postcode" ).toggleClass("hide");
    $( "#show_postcode" ).toggleClass("hide");
    if ($('#map').hasClass('hide')== false){
        $( "#map" ).toggleClass("hide");
    }
});


$("#show_map").click(function(){

    $( "#div_show_map_button" ).toggleClass("hide");
    $( "#show_change_pc" ).toggleClass("hide");

    if ($('#map').hasClass('hide')== true){
    $( "#map" ).toggleClass("hide");
    }

    Initialize_map(49.528423, -10.76418);

    $.ajax({
    async : false,
    data : {postcode:$('#postcode_input').val()},
    type : 'POST',
    url : "/get_post_code_data",
    success: function(data){
        console.log(data);
        var latlng = L.latLng(data.latitude, data.longitude);
        change_view(latlng);
    },
     error: function(error) {
        console.log(error);
    }
    });
});
$("#change_pc").click(function(){
    $.ajax({
    data : {postcode:$('#postcode_input').val()},
    type : 'POST',
    url : "/get_post_code_data",
    success: function(data){
        var latlng = L.latLng(data.latitude, data.longitude);
        change_view(latlng);
    },
    error: function(error) {
        console.log(error);
    }
    });
});
});