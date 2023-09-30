const imgPetite = document.querySelector(".panier .img-petite .img-petite-child1")
const imgGrande = document.querySelector(".panier .img-grande .img-grande-child1")

imgPetite.addEventListener('click',()=>{
imgGrande.classList.toggle('mobile-menu')
})  