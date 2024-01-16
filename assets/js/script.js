window.addEventListener('load', () => {
    const menuButton = document.getElementById('hamburger-button');
    const menu = document.getElementById('menu');
    menuButton.addEventListener('click', () => {
        menu.classList.toggle('open');
    });
});