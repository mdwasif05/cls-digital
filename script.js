// FAQ ACCORDION

const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach((item) => {

  const question = item.querySelector(".faq-question");

  question.addEventListener("click", () => {

    item.classList.toggle("active");

  });

});

// =========================
// DARK / LIGHT MODE
// =========================

const themeToggle =
document.getElementById("theme-toggle");

const body = document.body;


// LOAD SAVED THEME

if(localStorage.getItem("theme") === "dark"){

  body.classList.add("dark-mode");

  themeToggle.innerHTML =
  '<i class="fa-solid fa-sun"></i>';

}


// THEME TOGGLE

themeToggle.addEventListener("click", () => {

  // ADD ANIMATION EFFECT

  body.classList.add("theme-animate");

  setTimeout(() => {

    body.classList.remove("theme-animate");

  }, 500);


  // TOGGLE DARK MODE

  body.classList.toggle("dark-mode");


  // SAVE THEME

  if(body.classList.contains("dark-mode")){

    localStorage.setItem("theme", "dark");

    themeToggle.innerHTML =
    '<i class="fa-solid fa-sun"></i>';

  }

  else{

    localStorage.setItem("theme", "light");

    themeToggle.innerHTML =
    '<i class="fa-solid fa-moon"></i>';

  }

});