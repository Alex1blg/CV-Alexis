const menuHamburger = document.querySelector(".navbar .menu-hamburger")
const navLinks = document.querySelector(".navbar .nav-links")

menuHamburger.addEventListener('click',()=>{
navLinks.classList.toggle('mobile-menu')
})

