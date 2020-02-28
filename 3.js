

const inputs = document.querySelectorAll('.form-control input');
const labels = document.querySelectorAll('.form-control label');

labels.forEach(label => {
	label.innerHTML = label.innerText
		.split('')
		.map((letter, idx) => `<span style="
				transition-delay: ${idx * 30}ms
			">${letter}</span>`)
		.join('');
});



//SOCIAL PANEL JS
//const floating_btn = document.querySelector('.floating-btn');
//const close_btn = document.querySelector('.close-btn');
//const social_panel_container = document.querySelector('.social-panel-container');
//
//floating_btn.addEventListener('click', () => {
//	social_panel_container.classList.toggle('visible')
//});
//
//close_btn.addEventListener('click', () => {
//	social_panel_container.classList.remove('visible')
//});