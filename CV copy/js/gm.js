const img = document.querySelector(".loisir-section .loisir .box span .box-child img")
const description = document.querySelector(".loisir-section .loisir .box .box-child .box-text")

img.addEventListener('click',()=>{
description.classList.toggle('active')
})

