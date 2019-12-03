// Materialize Framework JQuery Iniitialisations  
 
$(document).ready(function() {
    $('select').material_select();
    $('.collapsible').collapsible();
    $('.button-collapse').sideNav();
    $('.tooltipped').tooltip();
    $('.carousel').carousel();
  });
  
function checkDelete(){
   return confirm("Are you sure you want to delete this?");
}


// Add / Edit  Form - Fill 'Image Url' input box with default value
    $('#add-default-url').click(function() {
        $('#img_url').val("http://glutenfreedelivers.com/template/images/white/glutenfree4.jpg").focus();
    });    

