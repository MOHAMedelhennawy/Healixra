document.addEventListener('DOMContentLoaded', function() {
    const doctorId = document.getElementById('doctor-id').value;
    const daySelector = document.getElementById('day-selector');
    const appointmentTime = document.getElementById('appointment-time');
    const selectedDate = document.getElementById('selected-date');
    const appointmentList = document.getElementById('appointment-list');

    daySelector.addEventListener('change', function() {
        const selectedDay = daySelector.value;
        selectedDate.value = selectedDay;
        fetch(`/doctor/${doctorId}/appointments/${selectedDay}`)
            .then(response => response.json())
            .then(data => {
                appointmentTime.innerHTML = '<option value="" disabled selected>Select a time</option>';
                if (data.valid_appointments.length > 0) {
                    data.valid_appointments.forEach(time => {
                        const option = document.createElement('option');
                        option.value = time;
                        option.textContent = time;
                        appointmentTime.appendChild(option);
                    });
                } else {
                    appointmentTime.innerHTML = '<option value="" disabled selected>No available appointments</option>';
                }
            });
    });
});
