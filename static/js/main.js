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
