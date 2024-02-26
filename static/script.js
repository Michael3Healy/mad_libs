const createStoryInputs = document.querySelectorAll('input.answer');
const createStoryForm = document.querySelector('form');

function hasInput(input) {
	return Boolean(input.value);
}

function isOneWord(phrase) {
	try {
		for (let char of phrase) {
			if (char === ' ') {
				return false;
			}
		}
		return true;
	} catch (err) {}
}

function atLeastThreeChars(word) {
	return word.length >= 3;
}

function checkStoryInput(evt) {
	evt.preventDefault();

	for (let input of createStoryInputs) {
		if (!hasInput(input)) {
			alert('You must fill out every field!');
			return;
		}
		if (!isOneWord(input.value)) {
			alert('You can only have one word per entry!');
			return;
		}
		if (!atLeastThreeChars(input.value)) {
			alert('Your word must have at least three characters!');
			return;
		}
	}

	createStoryForm.submit();
}

createStoryForm.addEventListener('submit', checkStoryInput);
