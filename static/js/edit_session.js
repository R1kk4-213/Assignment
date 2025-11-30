// Edit Session UI Logic

document.addEventListener('DOMContentLoaded', function() {
    // Modal elements
    const createModal = document.getElementById('createSessionModal');
    const rescheduleModal = document.getElementById('rescheduleSessionModal');
    const createBtn = document.getElementById('create-session-btn');
    const closeBtns = document.querySelectorAll('.close');

    // Open create session modal
    createBtn.addEventListener('click', function() {
        createModal.style.display = 'block';
    });

    // Close modals
    closeBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            createModal.style.display = 'none';
            rescheduleModal.style.display = 'none';
        });
    });

    // Close modal when clicking outside
    window.addEventListener('click', function(event) {
        if (event.target === createModal) {
            createModal.style.display = 'none';
        }
        if (event.target === rescheduleModal) {
            rescheduleModal.style.display = 'none';
        }
    });

    // Handle create session form submission
    document.getElementById('createSessionForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const studentSelect = document.getElementById('student_id');
        const selectedOption = studentSelect.options[studentSelect.selectedIndex];
        
        const sessionData = {
            student_id: document.getElementById('student_id').value,
            student_name: selectedOption.getAttribute('data-name'),
            subject: document.getElementById('subject').value,
            date: document.getElementById('date').value,
            time: document.getElementById('time').value,
            duration: document.getElementById('duration').value,
            location: document.getElementById('location').value
        };

        fetch('/api/sessions/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(sessionData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Session created successfully!');
                location.reload();
            } else {
                alert('Error creating session');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error creating session');
        });
    });

    // Handle reschedule button clicks
    document.querySelectorAll('.reschedule-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const sessionId = this.getAttribute('data-session-id');
            const row = this.closest('tr');
            
            document.getElementById('reschedule_session_id').value = sessionId;
            document.getElementById('reschedule_date').value = row.querySelector('.session-date').textContent;
            document.getElementById('reschedule_time').value = row.querySelector('.session-time').textContent;
            document.getElementById('reschedule_location').value = row.querySelector('.session-location').textContent;
            
            rescheduleModal.style.display = 'block';
        });
    });

    // Handle reschedule form submission
    document.getElementById('rescheduleSessionForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const sessionId = document.getElementById('reschedule_session_id').value;
        const rescheduleData = {
            date: document.getElementById('reschedule_date').value,
            time: document.getElementById('reschedule_time').value,
            location: document.getElementById('reschedule_location').value
        };

        fetch(`/api/sessions/${sessionId}/reschedule`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(rescheduleData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Session rescheduled successfully!');
                location.reload();
            } else {
                alert('Error rescheduling session');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error rescheduling session');
        });
    });

    // Handle cancel button clicks
    document.querySelectorAll('.cancel-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            if (confirm('Are you sure you want to cancel this session?')) {
                const sessionId = this.getAttribute('data-session-id');
                
                fetch(`/api/sessions/${sessionId}/cancel`, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('Session cancelled successfully!');
                        location.reload();
                    } else {
                        alert('Error cancelling session');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error cancelling session');
                });
            }
        });
    });
});

