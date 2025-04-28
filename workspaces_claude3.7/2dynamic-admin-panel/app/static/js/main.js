// This file contains the main JavaScript functionality for the application.

document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const paramView = document.getElementById('parameter-view');

    if (paramView) {
        params.forEach((value, key) => {
            const paramElement = document.createElement('div');
            paramElement.className = 'param-item';
            paramElement.innerHTML = `<strong>${key}:</strong> ${value}`;
            paramView.appendChild(paramElement);
        });
    }

    const customizeButton = document.getElementById('customize-button');
    if (customizeButton) {
        customizeButton.addEventListener('click', function() {
            const customParam = document.getElementById('custom-param').value;
            const customValue = document.getElementById('custom-value').value;
            if (customParam && customValue) {
                const customElement = document.createElement('div');
                customElement.className = 'param-item';
                customElement.innerHTML = `<strong>${customParam}:</strong> ${customValue}`;
                paramView.appendChild(customElement);
            }
        });
    }
});