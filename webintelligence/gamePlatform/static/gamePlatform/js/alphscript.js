const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const letterGrid = document.getElementById('letter-grid');
const targetLetterElement = document.getElementById('target-letter');
const resetButton = document.getElementById('reset-button');
const finishButton = document.getElementById('finish-button');

let foundLetters = new Set();
let targetLetter;

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function createGrid(letters) {
    letterGrid.innerHTML = '';
    letters.forEach(letter => {
        const button = document.createElement('button');
        button.textContent = letter;
        button.addEventListener('click', () => checkLetter(letter, button));
        letterGrid.appendChild(button);
    });
}

function checkLetter(selectedLetter, button) {
    if (selectedLetter === targetLetter) {
        foundLetters.add(selectedLetter);
        // Создаем пустое место вместо кнопки
        const emptySpace = document.createElement('div');
        emptySpace.classList.add('empty-space');
        button.replaceWith(emptySpace);
        if (foundLetters.size === alphabet.length) {
            alert('Поздравляем! Вы нашли все буквы.');
            resetGame();
        } else {
            targetLetter = getRandomLetter();
            targetLetterElement.textContent = targetLetter;
        }
    } else {
        button.classList.add('incorrect');
        setTimeout(() => {
            button.classList.remove('incorrect');
        }, 1000);
    }
}

function getRandomLetter() {
    const availableLetters = alphabet.filter(letter => !foundLetters.has(letter));
    return availableLetters[Math.floor(Math.random() * availableLetters.length)];
}

function resetGame() {
    foundLetters.clear();
    shuffleArray(alphabet);
    targetLetter = getRandomLetter();
    targetLetterElement.textContent = targetLetter;
    createGrid(alphabet);
}

resetButton.addEventListener('click', resetGame);
finishButton.addEventListener('click', () => {
    alert('Игра завершена.');
    resetGame();
});

resetGame();