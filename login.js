const signUpButtonOverlay = document.getElementById('signUp');
const signInButtonOverlay = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButtonOverlay.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButtonOverlay.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});




