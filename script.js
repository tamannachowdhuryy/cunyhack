function getSelectedOptions() {
    var selectElement = document.getElementById('pluralism_course-insertion');
    var selectedOptions = selectElement.selectedOptions;

    var selectedValues = Array.from(selectedOptions).map(option => option.value);

    // Now 'selectedValues' is an array containing the values of the selected options
    console.log(selectedValues);
}
function submit() {
    // Get values from the form
    var csCourse = document.getElementById('cs_course-insertion').value;
    var mathCourse = document.getElementById('math_course-insertion').value;
  


    // Construct the payload
    var payload = {
        "cs_course": csCourse,
        "math_course": mathCourse,
        
    };

   
}
