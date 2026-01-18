// Mobile Menu Toggle
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        
        // Animate hamburger menu
        const spans = mobileMenuToggle.querySelectorAll('span');
        if (navMenu.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
        } else {
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });
}

// FAQ Accordion
const faqQuestions = document.querySelectorAll('.faq-question');

faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
        const faqItem = question.parentElement;
        const isActive = faqItem.classList.contains('active');
        
        // Close all FAQ items
        document.querySelectorAll('.faq-item').forEach(item => {
            item.classList.remove('active');
        });
        
        // Open clicked item if it wasn't already open
        if (!isActive) {
            faqItem.classList.add('active');
        }
    });
});

// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        
        if (target) {
            const offsetTop = target.offsetTop - 80; // Account for fixed header
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
            
            // Close mobile menu if open
            navMenu.classList.remove('active');
            const spans = mobileMenuToggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });
});

// Scroll Progress Indicator & Scroll to Top Button
const scrollProgress = document.querySelector('.scroll-progress-bar');
const scrollToTopBtn = document.getElementById('scroll-to-top');

window.addEventListener('scroll', () => {
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const scrollPercent = (scrollTop / (documentHeight - windowHeight)) * 100;

    if (scrollProgress) {
        scrollProgress.style.width = scrollPercent + '%';
    }

    // Show/hide scroll to top button
    if (scrollToTopBtn) {
        if (scrollTop > 500) {
            scrollToTopBtn.classList.add('visible');
        } else {
            scrollToTopBtn.classList.remove('visible');
        }
    }
});

// Scroll to top function
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Header Scroll Effect
let lastScroll = 0;
const header = document.querySelector('.header');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 100) {
        header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    } else {
        header.style.boxShadow = '0 1px 2px 0 rgb(0 0 0 / 0.05)';
    }

    lastScroll = currentScroll;
});

// Lazy Load Animation
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Apply to service cards
document.querySelectorAll('.service-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.5s, transform 0.5s';
    observer.observe(card);
});

// Apply to testimonial cards
document.querySelectorAll('.testimonial-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.5s, transform 0.5s';
    observer.observe(card);
});

// Form Validation (for future quote form)
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    let valid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('error');
            valid = false;
        } else {
            input.classList.remove('error');
        }
    });
    
    return valid;
}

// Add loading state to buttons
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function(e) {
        if (this.getAttribute('href') === '#quote') {
            e.preventDefault();
            this.style.position = 'relative';
            this.innerHTML = '<span style="opacity: 0.5;">Loading...</span>';
            
            // Simulate loading then show message
            setTimeout(() => {
                this.innerHTML = 'Get Free Quote';
                alert('Quote form would open here. For now, please call (323) 555-1234');
            }, 1000);
        }
    });
});

// Counter Animation for Stats (if you add a stats section)
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    
    const timer = setInterval(() => {
        start += increment;
        if (start >= target) {
            element.textContent = target;
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(start);
        }
    }, 16);
}

// Booking System Functions
function openBooking(type) {
    const messages = {
        regular: 'Opening booking system for regular service...',
        assessment: 'Scheduling your free kitchen assessment...',
        footer: 'Loading online booking system...'
    };
    
    // Show loading state
    alert(messages[type] || 'Loading booking system...');
    
    // In production, this would open your actual booking system
    // For now, we'll simulate it
    setTimeout(() => {
        alert('To complete your booking, please call (323) 555-1234 or we\'ll integrate with your preferred booking system.');
    }, 1000);
}

// Quote Calculator Functions
function openQuoteCalculator() {
    const modal = document.getElementById('quote-calculator');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeQuoteCalculator() {
    const modal = document.getElementById('quote-calculator');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';

    // Reset form
    document.getElementById('quote-form').reset();
    document.getElementById('quote-result').style.display = 'none';
}

function calculateQuote() {
    const kitchenSize = document.getElementById('kitchen-size').value;
    const serviceType = document.getElementById('service-type').value;
    const frequency = document.getElementById('frequency').value;

    if (!kitchenSize || !serviceType || !frequency) {
        alert('Please fill in all fields');
        return;
    }

    // Pricing logic
    const basePrices = {
        small: { 'deep-clean': 600, 'hood': 400, 'sanitization': 500, 'emergency': 800 },
        medium: { 'deep-clean': 1200, 'hood': 700, 'sanitization': 900, 'emergency': 1500 },
        large: { 'deep-clean': 2200, 'hood': 1200, 'sanitization': 1600, 'emergency': 2800 }
    };

    const frequencyDiscounts = {
        'one-time': 1.0,
        'monthly': 0.85,
        'biweekly': 0.80,
        'weekly': 0.75
    };

    const basePrice = basePrices[kitchenSize][serviceType];
    const finalPrice = Math.round(basePrice * frequencyDiscounts[frequency]);

    // Display result
    const resultDiv = document.getElementById('quote-result');
    const priceEl = document.getElementById('quote-price');
    const detailsEl = document.getElementById('quote-details');

    priceEl.textContent = '$' + finalPrice.toLocaleString();

    const frequencyText = {
        'one-time': 'One-time service',
        'monthly': 'per month',
        'biweekly': 'bi-weekly',
        'weekly': 'per week'
    };

    detailsEl.textContent = `${frequencyText[frequency]} • Includes all equipment and supplies • 100% satisfaction guaranteed`;

    resultDiv.style.display = 'block';
    resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Close modal when clicking outside
window.addEventListener('click', (e) => {
    const modal = document.getElementById('quote-calculator');
    if (e.target === modal) {
        closeQuoteCalculator();
    }
});

// Chat Widget Functions
function toggleChat() {
    const chatWindow = document.getElementById('chat-window');
    const chatBadge = document.querySelector('.chat-badge');

    if (chatWindow.style.display === 'none' || !chatWindow.style.display) {
        chatWindow.style.display = 'flex';
        if (chatBadge) chatBadge.style.display = 'none';
    } else {
        chatWindow.style.display = 'none';
    }
}

function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();

    if (!message) return;

    const chatMessages = document.querySelector('.chat-messages');

    // Add user message
    const userMsg = document.createElement('div');
    userMsg.className = 'chat-message user-message';
    userMsg.innerHTML = `
        <p>${message}</p>
        <span class="message-time">Just now</span>
    `;
    chatMessages.appendChild(userMsg);

    input.value = '';

    // Simulate bot response
    setTimeout(() => {
        const botMsg = document.createElement('div');
        botMsg.className = 'chat-message bot-message';
        botMsg.innerHTML = `
            <p>Thanks for your message! A team member will respond shortly. For immediate assistance, call us at (323) 555-1234.</p>
            <span class="message-time">Just now</span>
        `;
        chatMessages.appendChild(botMsg);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 1000);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function sendQuickReply(type) {
    const responses = {
        pricing: 'Our pricing starts at $499/month for small restaurants. Would you like a custom quote for your kitchen?',
        emergency: 'We offer 24/7 emergency service with 2-hour response time! Call (323) 555-1234 now for immediate assistance.',
        schedule: 'Great! What day and time works best for you? Our team is available 7 days a week.'
    };

    const chatMessages = document.querySelector('.chat-messages');
    const botMsg = document.createElement('div');
    botMsg.className = 'chat-message bot-message';
    botMsg.innerHTML = `
        <p>${responses[type]}</p>
        <span class="message-time">Just now</span>
    `;
    chatMessages.appendChild(botMsg);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Allow Enter key to send message
document.addEventListener('DOMContentLoaded', () => {
    const chatInput = document.getElementById('chat-input');
    if (chatInput) {
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
});

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Add any initialization code here
    console.log('GroundOps website loaded successfully!');

    // Check if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
        // Disable animations for accessibility
        document.querySelectorAll('*').forEach(el => {
            el.style.animation = 'none';
            el.style.transition = 'none';
        });
    }

    // Auto-show chat widget after 5 seconds
    setTimeout(() => {
        const chatBadge = document.querySelector('.chat-badge');
        if (chatBadge) {
            chatBadge.style.animation = 'pulse 2s infinite';
        }
    }, 5000);
});