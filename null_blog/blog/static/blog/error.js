let error = document.getElementById('error-wrapper')
let btn = document.getElementById('error-close-btn')
let close = document.getElementById('error-close')

btn.onclick = () => error.classList.add('hidden')
close.onclick = () => error.classList.add('hidden')