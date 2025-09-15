

  // Learn more alert
  const learnBtns = document.querySelectorAll(".learn-more");
  learnBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      alert(`You clicked on: ${btn.dataset.service}`);
    });
  });

// document.addEventListener("DOMContentLoaded", () => {

// });

//   function toggleMenu() {
//     document.querySelector("nav ul").classList.toggle("show");
//   }
  
//   // Dropdown open/close on mobile
//   document.querySelectorAll(".dropdown > a").forEach(link => {
//     link.addEventListener("click", e => {
//       if (window.innerWidth <= 768) {
//         e.preventDefault(); // prevent redirect
//         link.parentElement.classList.toggle("open");
//       }
//     });
//   });
