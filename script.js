// Mobile Menu Toggle
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (mobileMenuToggle && navLinks) {
  mobileMenuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
}

// FAQ Accordion
document.querySelectorAll('.faq-question').forEach(question => {
  question.addEventListener('click', () => {
    const faqItem = question.parentElement;
    const isActive = faqItem.classList.contains('active');

    document.querySelectorAll('.faq-item').forEach(item => {
      item.classList.remove('active');
      const answer = item.querySelector('.faq-answer');
      if (answer) answer.style.maxHeight = null;
    });

    if (!isActive) {
      faqItem.classList.add('active');
      const answer = faqItem.querySelector('.faq-answer');
      if (answer) answer.style.maxHeight = answer.scrollHeight + 'px';
    }
  });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    if (href === '#request-access') return; // handled by openRequestForm
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      const offset = target.offsetTop - 60;
      window.scrollTo({ top: offset, behavior: 'smooth' });
      if (navLinks) navLinks.classList.remove('active');
    }
  });
});

// Request Access Modal
function openRequestForm(e) {
  if (e) e.preventDefault();
  const modal = document.getElementById('requestModal');
  if (modal) modal.style.display = 'block';
}

function closeRequestForm() {
  const modal = document.getElementById('requestModal');
  if (modal) modal.style.display = 'none';
}

function submitRequestForm(e) {
  e.preventDefault();
  const form = e.target;
  const data = new FormData(form);
  const status = document.getElementById('formStatus');

  // Build mailto fallback with form data
  const subject = encodeURIComponent(`Access Request: ${data.get('company')}`);
  const body = encodeURIComponent(
    `Name: ${data.get('name')}\n` +
    `Company: ${data.get('company')}\n` +
    `Email: ${data.get('email')}\n` +
    `Phone: ${data.get('phone') || 'N/A'}\n` +
    `Locations: ${data.get('locations') || 'N/A'}\n` +
    `Message: ${data.get('message') || 'N/A'}`
  );

  window.location.href = `mailto:info@groundops.com?subject=${subject}&body=${body}`;

  if (status) status.textContent = 'Opening email client...';
  setTimeout(() => {
    form.reset();
    closeRequestForm();
    if (status) status.textContent = '';
  }, 2000);
}

// Close modal on outside click
window.addEventListener('click', function(e) {
  const modal = document.getElementById('requestModal');
  if (e.target === modal) closeRequestForm();
});
