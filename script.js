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

// =========================
// WHATSAPP FORM INTEGRATION
// =========================

const contactForm =
document.getElementById("contactForm");

contactForm.addEventListener("submit", function(e){

  e.preventDefault();

  // USER INPUTS

  const name =
  document.getElementById("name").value;

  const contact =
  document.getElementById("contact").value;

  const service =
  document.getElementById("service").value;

  const message =
  document.getElementById("message").value;

  // YOUR WHATSAPP NUMBER
  // Use country code without +

  const phoneNumber = "918879424534";

  // WHATSAPP MESSAGE

  const whatsappMessage =
`New CSC Service Request

Name: ${name}

Contact : ${contact}

Service: ${service}

Message: ${message}`;

  // ENCODE MESSAGE

  const encodedMessage =
  encodeURIComponent(whatsappMessage);

  // OPEN WHATSAPP

  const whatsappURL =
  `https://wa.me/${phoneNumber}?text=${encodedMessage}`;

  window.open(whatsappURL, "_blank");

});

// =========================
// SERVICE DETAILS MODAL
// =========================

const modal =
document.getElementById("serviceModal");

const modalTitle =
document.getElementById("modalTitle");

const modalBody =
document.getElementById("modalBody");

const closeModal =
document.querySelector(".close-modal");

const serviceButtons =
document.querySelectorAll(".card-btn");

const serviceData = {

  pan: {
    title: "PAN Card Application",
    content: `
      <p><strong>Required Documents:</strong></p>
      <ul>
        <li>Aadhaar Card</li>
        <li>Voter ID/Berth Certificate/Matriculation Certificate</li>
        <li>G-Mail Id</li>
        <li>Mobile Number</li>
        <li>Passport Size Photo</li>
        <li>Applicant Signature</li>
      </ul>

      <p><strong>Processing Time:</strong> 2-7 Days</p>
      <p><strong>Service Charge:</strong> ₹200 </p>
    `
  },

  aadhaar: {
    title: "Aadhaar Update",
    content: `
      <p><strong>Required Documents:</strong></p>
      <ul>
        <li>Aadhaar Card</li>
        <li>Supporting Document</li>
      </ul>

      <p><strong>Processing Time:</strong> Same Day</p>
      <p><strong>Service Charge:</strong> ₹150 </p>
    `
  },

  passport: {
    title: "Passport Service",
    content: `
      <ul>
        <li>Aadhaar Card</li>
        <li>PAN Card/10th Marksheet(Compulsory for Non-ECR Category)</li>
        <li>Address Proof</li>
      </ul>

      <p><strong>Processing Time:</strong> As per Passport Office</p>
      <p><strong>Service Charge:</strong> ₹3000 </p>
    `
  },

  bill: {
    title: "Utility Bill Payment",
    content: `
      <ul>
        <li>Electricity Bills</li>
        <li>Gas Bills</li>
        <li>DTH Recharge</li>
        <li>Mobile Recharge</li>
        <p><strong>Service Charge:</strong> As Per Service Cost </p>
      </ul>
    `
  },

  voter: {
    title: "Voter ID Service",
    content: `
      <ul>
        <li>New Registration</li>
        <li>Name Correction</li>
        <li>Address Update</li>
        <p><strong>Service Charge:</strong> ₹100 </p>
      </ul>
    `
  },

  dl: {
    title: "Driving Licence Service",
    content: `
      <ul>
        <li>New DL</li>
        <li>Renewal</li>
        <li>Duplicate DL</li>
        <p><strong>Processing Time:</strong> As per RTO Office</p>
        <p><strong>Service Charge:</strong> ₹3500 </p>
      </ul>
    `
  },

  scheme: {
    title: "Government Schemes",
    content: `
      <ul>
        <li>PM Kisan</li>
        <li>E-Shram Card</li>
        <li>Ayushman Card</li>
        <li>Pension Schemes</li>
      </ul>
    `
  },

  certificate: {
    title: "Certificates",
    content: `
      <ul>
        <li>Income Certificate</li>
        <li>Domicile Certificate</li>
        <li>Caste Certificate</li>
        <li>EWS Certificate</li>
        <p><strong>Processing Time:</strong> 3-5 Days</p>
        <p><strong>Service Charge:</strong> ₹100 </p>
      </ul>
    `
  }

};

serviceButtons.forEach(button => {

  button.addEventListener("click", function(e){

    e.preventDefault();

    const service =
    this.dataset.service;

    modalTitle.textContent =
    serviceData[service].title;

    modalBody.innerHTML =
    serviceData[service].content;

    modal.style.display = "flex";

  });

});

closeModal.addEventListener("click", () => {

  modal.style.display = "none";

});

window.addEventListener("click", (e) => {

  if(e.target === modal){

    modal.style.display = "none";

  }

});

// =========================
// ANIMATED COUNTERS
// =========================

const counters =
document.querySelectorAll(".counter");

const startCounter = () => {

  counters.forEach(counter => {

    const target =
    +counter.getAttribute("data-target");

    let count = 0;

    const increment =
    target / 100;

    const updateCounter = () => {

      if(count < target){

        count += increment;

        counter.innerText =
        Math.ceil(count);

        setTimeout(updateCounter, 20);

      }

      else{

        counter.innerText = target;

      }

    };

    updateCounter();

  });

};


// RUN WHEN SECTION APPEARS

const statsSection =
document.querySelector(".stats-section");

const observer =
new IntersectionObserver((entries) => {

  entries.forEach(entry => {

    if(entry.isIntersecting){

      startCounter();

      observer.unobserve(statsSection);

    }

  });

});

observer.observe(statsSection);