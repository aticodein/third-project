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

// Add / Remove Ingredients
    var num_fields = $('#ingredients-container .ingredient_field').length;
    var min_fields = 1;
    var max_fields = 10;
    var num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

    // Add
    $('#add_ingredient').click(function() {
        if (num_fields < max_fields) {
            $('#ingredients-container').append(
                "<div class='input-field col s4 measure_field'>" +
                "<i class='material-icons prefix'>view_week</i>" +
                "<input id='measure_" + (num_fields + 1) + "' name='measure_" + (num_fields + 1) + "' type='text' class='validate' required>" +
                "<label for='measure_" + (num_fields + 1) + "'>Measure" + num_list[(num_fields)] + "</label>" +
                "<span class='helper-text' data-error='Cannot be empty.' data-success='Passed'></span>" +
                "</div>" +
                "</div>" +
                "<div class='input-field col s4 quantity_field'>" +
                "<i class='material-icons prefix'>vignette</i>" +
                "<input id='quantity_" + (num_fields + 1) + "' name='quantity_" + (num_fields + 1) + "' type='text' class='validate' required>" +
                "<label for='quantity_" + (num_fields + 1) + "'>Quantity" + num_list[(num_fields)] + "</label>" +
                "<span class='helper-text' data-error='Cannot be empty.' data-success='Passed'></span>" +
                "</div>" +
                "</div>" +
                "<div class='input-field col s4 ingredient_field'>" +
                "<i class='material-icons prefix'>reorder</i>" +
                "<input id='ingredient_" + (num_fields + 1) + "' name='ingredient_" + (num_fields + 1) + "' type='text' class='validate' required>" +
                "<label for='ingredient_" + (num_fields + 1) + "'>Ingredient" + num_list[(num_fields)] + "</label>" +
                "<span class='helper-text' data-error='Cannot be empty.' data-success='Passed'></span>" +
                "</div>" +
                "</div>"

            );
            num_fields += 1;
        }
    });

    // Remove
    $('#remove_ingredient').click(function() {
        if (num_fields > min_fields) {
            $('.measure_field').filter(':last').remove();
            $('.ingredient_field').filter(':last').remove();
            $('.quantity_field').filter(':last').remove();
            num_fields -= 1;
        }
    });
    
// Add / Edit Drink Form - Fill 'Image Url' input box with default value
    $('#add-default-url').click(function() {
        $('#img_url').val("http://glutenfreedelivers.com/template/images/white/glutenfree4.jpg").focus();
    });    

