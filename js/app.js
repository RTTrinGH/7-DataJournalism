/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
particlesJS.load('particles-js', 'particles.json', function() {
  console.log('callback - particles.js config loaded');
});

const navIcon = document.getElementById('nav-icon');
const siteMenu = document.getElementById('menu');

navIcon.addEventListener('click', () => {
  const isOpen = navIcon.classList.toggle('open');

  navIcon.setAttribute('aria-expanded', String(isOpen));
  siteMenu.style.display = isOpen ? 'flex' : 'none';
});