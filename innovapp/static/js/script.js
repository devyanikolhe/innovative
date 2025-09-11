// FAQ toggle
document.addEventListener("DOMContentLoaded", () => {
  const faqButtons = document.querySelectorAll(".faq-q");
  faqButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const answer = btn.nextElementSibling;
      if(answer.style.display === "block"){
        answer.style.display = "none";
      } else {
        answer.style.display = "block";
      }
    });
  });

  // Learn more alert
  const learnBtns = document.querySelectorAll(".learn-more");
  learnBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      alert(`You clicked on: ${btn.dataset.service}`);
    });
  });
});
