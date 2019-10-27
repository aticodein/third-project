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
            
const nav = document.querySelector('#sticky-nav');
const topOfNav = nav.offsetTop;

function fixNav() {
    if (window.scrollY >= topOfNav) {
        document.body.style.paddingTop = '100px';
        document.body.classList.add("navbar-fixed");
    } else {
        document.body.style.paddingTop = 0;
        document.body.classList.remove("navbar-fixed");
    }
}

window.addEventListener('scroll', fixNav);