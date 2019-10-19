 // Materialize Framework JQuery Iniitialisations  
 
$(document).ready(function() {
     $('select').material_select();
     $(".collapsible").collapsible();
     $(".button-collapse").sideNav();
     $(".tooltipped").tooltip();
});    


 function changeFavourite() {
   const element = document.getElementById("favourite");
   if (element.innerText == "ON") {
       element.innerText = "Favourite";
   }
   else {
       element.style.display = "none";
   }
} 

changeFavourite();
 