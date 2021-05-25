const colorToggler = document.querySelector('#colorToggler');
const paragraphOutput = document.querySelector('#output');
const body = document.querySelector('body');

colorToggler.addEventListener('click', function(){
    body.classList.toggle('changeBackground');
    // this.classList.toggle('changeBackground'); // change button's color 
    paragraphOutput.innerHTML += "<strong>Changed Background Color!</strong><br>"
    // paragraphOutput.classList.toggle('changeBackground');
});