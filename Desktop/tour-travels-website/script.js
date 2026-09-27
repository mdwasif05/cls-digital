// MOBILE MENU
menuBtn.addEventListener('click', () => {
navLinks.classList.toggle('active');
});


// DARK MODE

const darkToggle = document.getElementById('darkToggle');

if(darkToggle){

  darkToggle.addEventListener('click', () => {

    document.body.classList.toggle('dark-mode');

  });

}


// PACKAGE FILTER

function filterPackages(category){

const packages = document.querySelectorAll('.package-card');

packages.forEach(pkg => {

if(category === 'all'){
pkg.style.display = 'block';
}

else if(pkg.classList.contains(category)){
pkg.style.display = 'block';
}

else{
pkg.style.display = 'none';
}

});

}


// CONTACT FORM

const form = document.querySelector('.contact-form');

if(form){

form.addEventListener('submit', (e) => {

  e.preventDefault();

  alert('Thank you! We will contact you soon.');

  form.reset();

});

}


// STICKY NAVBAR SHADOW

window.addEventListener('scroll', () => {

const navbar = document.querySelector('.navbar');

if(window.scrollY > 50){
navbar.style.background = '#0B3D91';
}

else{
navbar.style.background = 'rgba(0,0,0,0.5)';
}

});