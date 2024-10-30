document.addEventListener('DOMContentLoaded', function() {
    const cvElements = document.querySelectorAll('.fade-in');
    
    window.addEventListener('scroll', function() {
        cvElements.forEach(function(element) {
            const rect = element.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom >= 0) {
                element.classList.add('visible');
            }
        });
    });

    // Trigger fade-in on page load
    cvElements.forEach(function(element) {
        const rect = element.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom >= 0) {
            element.classList.add('visible');
        }
    });
});
