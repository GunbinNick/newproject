const numbers = Array.from({ length: 32 }, (_, i) => {
    const number = (i + 1).toString();
    const word = [
        'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
        'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty',
        'Twenty-One', 'Twenty-Two', 'Twenty-Three', 'Twenty-Four', 'Twenty-Five', 'Twenty-Six', 'Twenty-Seven', 'Twenty-Eight', 'Twenty-Nine', 'Thirty',
        'Thirty-One', 'Thirty-Two'
    ][i];
    return { number, word };
});

const numberGrid = document.getElementById('number-grid');
const resetButton = document.getElementById('reset-button');
const finishButton = document.getElementById('finish-button');
const levelSelect = document.getElementById('level-select');

let foundPairs = new Set();
let firstCard = null;
let secondCard = null;
let lockBoard = false; 

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function createGrid(numbers, level) {
    numberGrid.innerHTML = '';
    const maxNumbers = [10, 15, 22, 32];
    const levelNumbers = numbers.slice(0, maxNumbers[level - 1]);
    shuffleArray(levelNumbers);

    const buttons = levelNumbers.flatMap(num => [
        { text: num.number, type: 'number', word: num.word },
        { text: num.word, type: 'word', word: num.word }
    ]).map(btn => {
        const button = document.createElement('button');
        button.dataset.word = btn.word;
        button.dataset.type = btn.type;
        button.textContent = btn.text;
        button.addEventListener('click', () => checkPair(button));
        return button;
    });

    shuffleArray(buttons);
    buttons.forEach(button => numberGrid.appendChild(button));
}

function checkPair(button) {
    if (lockBoard || button.classList.contains('empty-space') || button.classList.contains('flipped')) return;

    button.classList.add('flipped');
    if (firstCard === null) {
        firstCard = button;
    } else if (secondCard === null) {
        secondCard = button;
        lockBoard = true; 
        const isMatch = firstCard.dataset.word === secondCard.dataset.word;
        setTimeout(() => {
            if (isMatch) {
                foundPairs.add(firstCard.dataset.word);
                [firstCard, secondCard].forEach(card => {
                    card.classList.add('empty-space');
                    card.classList.remove('flipped');
                });
                if (foundPairs.size === numbers.length) {
                    alert('Поздравляем! Вы нашли все пары.');
                    resetGame();
                }
            } else {
                [firstCard, secondCard].forEach(card => card.classList.remove('flipped'));
            }
            [firstCard, secondCard] = [null, null];
            lockBoard = false;
        }, isMatch ? 300 : 1000);
    }
}

function resetGame() {
    foundPairs.clear();
    [firstCard, secondCard] = [null, null];
    lockBoard = false; 
    createGrid(numbers, parseInt(levelSelect.value));
}

resetButton.addEventListener('click', resetGame);
finishButton.addEventListener('click', () => {
    alert('Игра завершена.');
    resetGame();
});

levelSelect.addEventListener('change', resetGame);

resetGame();