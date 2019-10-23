alert("only main js loaded trogh base"); 
 
 
 // Materialize Framework JQuery Iniitialisations  
 
$(document).ready(function() {
     $('select').material_select();
     $(".collapsible").collapsible();
     $(".button-collapse").sideNav();
     $(".tooltipped").tooltip();
});

function checkDelete(){
   return confirm("Are you sure you want to delete this?");
}   
            
 