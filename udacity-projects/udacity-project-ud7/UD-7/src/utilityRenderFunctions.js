// Utility functions for rendering UI components
import { shuffle } from './Shuffle.js';

// Function to render card sets
export function renderCardSets(container, cardSets) {
    container.innerHTML = '';
    
    cardSets.forEach((cardSet, index) => {
        const cardSetElement = document.createElement('div');
        cardSetElement.className = 'card-set';
        cardSetElement.setAttribute('data-cy', `card-set-${index}`);
        
        const title = document.createElement('h3');
        title.textContent = cardSet.name;
        cardSetElement.appendChild(title);
        
        const cardCount = document.createElement('p');
        cardCount.textContent = `Cards: ${cardSet.cards.length}`;
        cardSetElement.appendChild(cardCount);
        
        const shuffleBtn = document.createElement('button');
        shuffleBtn.textContent = 'Shuffle Cards';
        shuffleBtn.setAttribute('data-cy', `shuffle-btn-${index}`);
        shuffleBtn.addEventListener('click', () => {
            cardSet.cards = shuffle(cardSet.cards);
            renderCards(cardSetElement.querySelector('.cards-container'), cardSet.cards);
        });
        cardSetElement.appendChild(shuffleBtn);
        
        const cardsContainer = document.createElement('div');
        cardsContainer.className = 'cards-container';
        renderCards(cardsContainer, cardSet.cards);
        cardSetElement.appendChild(cardsContainer);
        
        const addCardBtn = document.createElement('button');
        addCardBtn.textContent = 'Add Card';
        addCardBtn.setAttribute('data-cy', `add-card-btn-${index}`);
        addCardBtn.addEventListener('click', () => {
            // Function will be available globally from app.js
            if (typeof window.showAddCardModal === 'function') {
                window.showAddCardModal(cardSet);
            }
        });
        cardSetElement.appendChild(addCardBtn);
        
        container.appendChild(cardSetElement);
    });
}

// Function to render individual cards
export function renderCards(container, cards) {
    container.innerHTML = '';
    
    cards.forEach((card, index) => {
        const cardElement = document.createElement('div');
        cardElement.className = 'card';
        cardElement.setAttribute('data-cy', `card-${index}`);
        
        const front = document.createElement('div');
        front.className = 'card-front';
        front.textContent = card.front;
        cardElement.appendChild(front);
        
        const back = document.createElement('div');
        back.className = 'card-back';
        back.textContent = card.back;
        cardElement.appendChild(back);
        
        container.appendChild(cardElement);
    });
}

// Function to show modal (intentional ESLint errors)
export function showModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
    } else {
        console.error('Modal not found:', modalId);
    }
}

// Function to hide modal
export function hideModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
    }
}

// Function to show error message
export function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.style.display = 'block';
        
        // Hide error after 3 seconds
        setTimeout(() => {
            errorElement.style.display = 'none';
        }, 3000);
    }
}

// Import shuffle function (intentional missing import)
// This should trigger an ESLint error
export function shuffleAndRender(cardSet, container) {
    const shuffledCards = shuffle(cardSet.cards);
    cardSet.cards = shuffledCards;
    renderCards(container, shuffledCards);
}
