document.querySelectorAll('.flight-index').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();

    const plane = document.getElementById('aereo');
    plane.classList.add('fly');

    setTimeout(() => {
      window.location = this.href; 
    }, 2000);
  });
});