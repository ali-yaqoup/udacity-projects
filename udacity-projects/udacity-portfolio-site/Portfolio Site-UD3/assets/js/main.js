// Main JavaScript file for portfolio website
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initNavigation();
    initScrollEffects();
    initProjectFilter();
    initContactForm();
    initBackToTop();
    initScrollReveal();
    initSmoothScrolling();
});

// Navigation functionality
function initNavigation() {
    const header = document.querySelector('.header');
    const menuToggle = document.querySelector('.header__menu-toggle');
    const mobileNav = document.querySelector('.header__mobile-nav');
    const navLinks = document.querySelectorAll('.header__nav-link, .header__mobile-nav-link');
    
    // Toggle mobile menu
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            const isOpen = header.classList.toggle('header--menu-open');
            menuToggle.setAttribute('aria-expanded', isOpen);
        });
    }
    
    // Close mobile menu when clicking on links
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            header.classList.remove('header--menu-open');
            menuToggle.setAttribute('aria-expanded', 'false');
        });
    });
    
    // Update active navigation link based on scroll position
    updateActiveNavLink();
    window.addEventListener('scroll', updateActiveNavLink);
}

function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.header__nav-link');
    
    let currentSection = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        const sectionHeight = section.offsetHeight;
        
        if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
            currentSection = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('header__nav-link--active');
        if (link.getAttribute('href') === `#${currentSection}`) {
            link.classList.add('header__nav-link--active');
        }
    });
}

// Scroll effects
function initScrollEffects() {
    const header = document.querySelector('.header');
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', function() {
        const currentScrollY = window.scrollY;
        
        // Header scroll effect
        if (currentScrollY > 50) {
            header.classList.add('header--scrolled');
        } else {
            header.classList.remove('header--scrolled');
        }
        
        lastScrollY = currentScrollY;
    });
}

// Project filter functionality
function initProjectFilter() {
    const filterButtons = document.querySelectorAll('.projects__filter-button');
    const projectCards = document.querySelectorAll('.projects__card');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('projects__filter-button--active'));
            this.classList.add('projects__filter-button--active');
            
            // Filter projects
            projectCards.forEach(card => {
                if (filter === 'all' || card.getAttribute('data-category') === filter) {
                    card.style.display = 'block';
                    // Add animation
                    card.style.animation = 'fadeIn 0.5s ease-in-out';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

// Contact form functionality
function initContactForm() {
    const form = document.querySelector('.contact__form');
    if (!form) return;
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Reset previous errors
        clearFormErrors();
        
        // Validate form
        if (validateForm()) {
            // Show loading state
            const submitButton = form.querySelector('.contact__form-button');
            const originalText = submitButton.textContent;
            submitButton.innerHTML = '<span class="contact__form-loading"></span>Sending...';
            submitButton.disabled = true;
            
            // Simulate form submission (replace with actual submission)
            setTimeout(() => {
                // Show success message
                const successMessage = form.querySelector('.contact__form-success');
                successMessage.style.display = 'block';
                
                // Reset form
                form.reset();
                submitButton.textContent = originalText;
                submitButton.disabled = false;
                
                // Hide success message after 5 seconds
                setTimeout(() => {
                    successMessage.style.display = 'none';
                }, 5000);
            }, 2000);
        }
    });
    
    // Real-time validation
    const inputs = form.querySelectorAll('.contact__form-input, .contact__form-textarea');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            clearFieldError(this);
        });
    });
}

function validateForm() {
    const form = document.querySelector('.contact__form');
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(field => {
        if (!validateField(field)) {
            isValid = false;
        }
    });
    
    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    let isValid = true;
    let errorMessage = '';
    
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        errorMessage = `${fieldName.charAt(0).toUpperCase() + fieldName.slice(1)} is required`;
    } else if (field.type === 'email' && value && !isValidEmail(value)) {
        isValid = false;
        errorMessage = 'Please enter a valid email address';
    } else if (field.name === 'message' && value && value.length < 10) {
        isValid = false;
        errorMessage = 'Message must be at least 10 characters long';
    }
    
    if (!isValid) {
        showFieldError(field, errorMessage);
    }
    
    return isValid;
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function showFieldError(field, message) {
    const errorElement = field.parentElement.querySelector('.contact__form-error');
    if (errorElement) {
        errorElement.textContent = message;
        field.setAttribute('aria-invalid', 'true');
        field.setAttribute('aria-describedby', errorElement.id || `error-${field.name}`);
    }
}

function clearFieldError(field) {
    const errorElement = field.parentElement.querySelector('.contact__form-error');
    if (errorElement) {
        errorElement.textContent = '';
        field.removeAttribute('aria-invalid');
        field.removeAttribute('aria-describedby');
    }
}

function clearFormErrors() {
    const errorElements = document.querySelectorAll('.contact__form-error');
    errorElements.forEach(element => {
        element.textContent = '';
    });
    
    const inputs = document.querySelectorAll('.contact__form-input, .contact__form-textarea');
    inputs.forEach(input => {
        input.removeAttribute('aria-invalid');
        input.removeAttribute('aria-describedby');
    });
}

// Back to top functionality
function initBackToTop() {
    const backToTopButton = document.querySelector('.footer__back-to-top');
    if (!backToTopButton) return;
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTopButton.classList.add('footer__back-to-top--visible');
        } else {
            backToTopButton.classList.remove('footer__back-to-top--visible');
        }
    });
    
    backToTopButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Scroll reveal animation
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.scroll-reveal');
    
    const revealOnScroll = function() {
        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight - 100) {
                element.classList.add('scroll-reveal--visible');
            }
        });
    };
    
    // Initial check
    revealOnScroll();
    
    // Check on scroll
    window.addEventListener('scroll', revealOnScroll);
}

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Skip if it's just "#"
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Update focus for accessibility
                target.setAttribute('tabindex', '-1');
                target.focus();
            }
        });
    });
}

// Utility function to debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debounce to scroll events
window.addEventListener('scroll', debounce(function() {
    // Add any scroll-debounced functionality here
}, 100));

// Keyboard navigation enhancement
document.addEventListener('keydown', function(e) {
    // Escape key closes mobile menu
    if (e.key === 'Escape') {
        const header = document.querySelector('.header');
        const menuToggle = document.querySelector('.header__menu-toggle');
        
        if (header.classList.contains('header--menu-open')) {
            header.classList.remove('header--menu-open');
            menuToggle.setAttribute('aria-expanded', 'false');
            menuToggle.focus();
        }
    }
});

// Add focus trap for mobile menu
function initFocusTrap() {
    const mobileNav = document.querySelector('.header__mobile-nav');
    const menuToggle = document.querySelector('.header__menu-toggle');
    const focusableElements = mobileNav.querySelectorAll(
        'a, button, input, textarea, select, [tabindex]:not([tabindex="-1"])'
    );
    
    if (focusableElements.length === 0) return;
    
    const firstFocusable = focusableElements[0];
    const lastFocusable = focusableElements[focusableElements.length - 1];
    
    mobileNav.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            if (e.shiftKey) {
                if (document.activeElement === firstFocusable) {
                    e.preventDefault();
                    lastFocusable.focus();
                }
            } else {
                if (document.activeElement === lastFocusable) {
                    e.preventDefault();
                    firstFocusable.focus();
                }
            }
        }
    });
}

// Initialize focus trap when DOM is ready
document.addEventListener('DOMContentLoaded', initFocusTrap);
