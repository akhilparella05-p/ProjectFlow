function toggleTheme() {

    document.body.classList.toggle("dark");

    const isDark = document.body.classList.contains("dark");

    localStorage.setItem(
        "projectflow-theme",
        isDark ? "dark" : "light"
    );

    updateThemeButton();
}


function updateThemeButton() {

    const button = document.getElementById("themeToggle");

    if (!button) {
        return;
    }

    if (document.body.classList.contains("dark")) {
        button.innerHTML = "☀️";
        button.title = "Switch to light mode";
    } else {
        button.innerHTML = "🌙";
        button.title = "Switch to dark mode";
    }
}


function loadTheme() {

    const savedTheme =
        localStorage.getItem("projectflow-theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark");
    }

    updateThemeButton();
}


document.addEventListener("DOMContentLoaded", function () {

    loadTheme();

});