// main_app/static/js/article-animations.js

// Article card hover effects
document.querySelectorAll('.article-card').forEach(card => {
  card.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-10px)';
    this.style.boxShadow = '0 10px 20px rgba(0,188,212,0.2)';
  });
  
  card.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0)';
    this.style.boxShadow = 'none';
  });
});

// Progressive loading animation
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const articleObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      articleObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.article-card').forEach(article => {
  articleObserver.observe(article);
});

// Reading progress bar
const createProgressBar = () => {
  const progressBar = document.createElement('div');
  progressBar.className = 'reading-progress';
  document.body.appendChild(progressBar);

  window.addEventListener('scroll', () => {
    const winScroll = document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    progressBar.style.width = scrolled + '%';
  });
};

document.addEventListener('DOMContentLoaded', createProgressBar);
