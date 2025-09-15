

  // Learn more alert
  const learnBtns = document.querySelectorAll(".learn-more");
  learnBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      alert(`You clicked on: ${btn.dataset.service}`);
    });
  });

