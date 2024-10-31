// main_app/static/js/hobbies-animations.js

// Gallery masonry layout and animations
class GalleryManager {
  constructor() {
    this.gallery = document.querySelector('.hobby-gallery');
    this.items = document.querySelectorAll('.gallery-item');
    this.modal = document.querySelector('.gallery-modal');
    
    this.init();
  }

  init() {
    this.setupMasonry();
    this.setupLightbox();
    this.setupFilters();
  }

  setupMasonry() {
    const masonry = new Masonry(this.gallery, {
      itemSelector: '.gallery-item',
      columnWidth: '.gallery-sizer',
      percentPosition: true,
      gutter: 20
    });

    imagesLoaded(this.gallery).on('progress', () => {
      masonry.layout();
    });
  }

  setupLightbox() {
    this.items.forEach(item => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        this.openLightbox(item);
      });
    });
  }

  setupFilters() {
    const filters = document.querySelectorAll('.hobby-filter');
    filters.forEach(filter => {
      filter.addEventListener('click', () => {
        const category = filter.dataset.category;
        this.filterGallery(category);
      });
    });
  }

  openLightbox(item) {
    const image = item.querySelector('img');
    const modalImage = this.modal.querySelector('.modal-image');
    modalImage.src = image.src;
    this.modal.classList.add('active');
  }

  filterGallery(category) {
    this.items.forEach(item => {
      if (category === 'all' || item.dataset.category === category) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
    
    this.gallery.masonry.layout();
  }
}

// Initialize gallery
document.addEventListener('DOMContentLoaded', () => {
  new GalleryManager();
});

// Hobby card hover animations
document.querySelectorAll('.hobby-card').forEach(card => {
  card.addEventListener('mouseenter', function() {
    this.classList.add('hover');
  });
  
  card.addEventListener('mouseleave', function() {
    this.classList.remove('hover');
  });
});

// Parallax effect for hobby headers
document.addEventListener('scroll', () => {
  const headers = document.querySelectorAll('.hobby-header');
  headers.forEach(header => {
    const speed = header.dataset.speed || 0.5;
    const yPos = -(window.pageYOffset * speed);
    header.style.transform = `translateY(${yPos}px)`;
  });
});
