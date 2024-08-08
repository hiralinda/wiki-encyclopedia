document
  .getElementById("dark-mode-toggle")
  .addEventListener("click", function () {
    document.body.classList.toggle("dark-mode");
    document.querySelector(".sidebar").classList.toggle("dark-mode-sidebar");
    document.querySelector(".search").classList.toggle("dark-mode-search");
    if (document.body.classList.contains("dark-mode")) {
      localStorage.setItem("darkModeEnabled", true);
    } else {
      localStorage.removeItem("darkModeEnabled");
    }
  });

if (localStorage.getItem("darkModeEnabled")) {
  // Apply dark mode classes
  document.body.classList.add("dark-mode");
  document.querySelector(".sidebar").classList.add("dark-mode-sidebar");
  document.querySelector(".search").classList.add("dark-mode-search");
}
