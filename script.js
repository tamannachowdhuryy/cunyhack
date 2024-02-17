function getSelectedOptions() {
    var selectElement = document.getElementById('pluralism_course-insertion');
    var selectedOptions = selectElement.selectedOptions;
    var hunter_course = document.getElementById('hunter_course').value;

    var selectedValues = Array.from(selectedOptions).map(option => option.value);

    // Now 'selectedValues' is an array containing the values of the selected options
    console.log(selectedValues);
}
function submitForm() {
    // Get values from the form
    var csCourse = document.getElementById('cs_course-insertion').value;
    var mathCourse = document.getElementById('math_course-insertion').value;

    // Get selected values from the hunter_course-insertion select element
    var hunterCoursesSelect = document.getElementById('hunter_course-insertion');
    var selectedHunterCourses = Array.from(hunterCoursesSelect.selectedOptions).map(option => option.value);

    // Construct the payload
    var payload = {
        "cs_course": csCourse,
        "math_course": mathCourse,
        "hunter_courses": selectedHunterCourses
    };

    // Make the POST request
    fetch('http://localhost:8000', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    
}

// calancer
function updateSchedule(calendarInfo) {
    console.log('Received calendarInfo:', calendarInfo);
    var eventTitle = calendarInfo.event_title;
    var eventDate = calendarInfo.event_date;
    var eventDescription = calendarInfo.event_description;

    console.log('Updating schedule for event:', eventTitle, 'on', eventDate);

    // Find the appropriate cell in the schedule based on the eventDate and update its content
    var cell = document.querySelector(`[data-cell][data-day="${eventDate}"]`);
    if (cell) {
        cell.textContent = `${eventTitle}: ${eventDescription}`;
        console.log('Schedule updated successfully.');
    } else {
        console.error('Could not find the appropriate cell for the event date:', eventDate);
    }
}

