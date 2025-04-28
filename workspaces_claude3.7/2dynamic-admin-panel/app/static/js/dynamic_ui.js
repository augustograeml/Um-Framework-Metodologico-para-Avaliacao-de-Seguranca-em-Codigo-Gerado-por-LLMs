// This file contains JavaScript functions to dynamically update the UI based on parameters.

document.addEventListener("DOMContentLoaded", function() {
    const params = new URLSearchParams(window.location.search);
    const paramContainer = document.getElementById("param-container");

    if (paramContainer) {
        params.forEach((value, key) => {
            const paramElement = document.createElement("div");
            paramElement.className = "param-item";
            paramElement.innerHTML = `<strong>${key}:</strong> ${value}`;
            paramContainer.appendChild(paramElement);
        });
    }

    const customizeButton = document.getElementById("customize-button");
    if (customizeButton) {
        customizeButton.addEventListener("click", function() {
            const newColor = document.getElementById("color-input").value;
            document.body.style.backgroundColor = newColor;
        });
    }
});