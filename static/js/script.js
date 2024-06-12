
let navbar=document.querySelector('.navbar navbar-expand-lg navbar-dark bg-dark fixed-top')
window.onscroll = () =>{
    navbar.classList.remove('fa-times');
    navbar.classList.remove('active')
}

document.querySelector('#search-icon','#search-box').onclick=() =>{
    document.querySelector('#search-form').classList.toggle('active');
}

document.querySelector('#close').onclick=() =>{
    document.querySelector('#search-form').classList.remove('active');
}